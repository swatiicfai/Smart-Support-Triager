import streamlit as st
import json
import time
from agent import classify_email

# Simulate loading the mock database
def load_db():
    with open('mock_db.json', 'r') as f:
        return json.load(f)

st.set_page_config(page_title="Smart Support Triager", page_icon="🤖")

st.title("🤖 Smart Support Triager")
st.markdown("**UiPath AgentHack: Track 2 (Maestro BPMN)**")
st.write("This app simulates a UiPath Maestro flow. It uses an AI Agent to classify incoming support emails and automatically routes them to either an RPA automation or a human escalation queue.")

st.divider()

st.subheader("📥 Incoming Email Simulation")
email_address = st.text_input("Customer Email", value="customer@example.com")
email_text = st.text_area("Email Content", value="Hi, can you tell me the status of ORD-1234? Thanks!", height=100)

if st.button("Run Maestro BPMN Flow", type="primary"):
    st.divider()
    
    # STEP 1: Classification
    with st.status("🤖 Calling AI Agent for Classification...", expanded=True) as status:
        st.write("Analyzing intent and sentiment...")
        classification = classify_email(email_text)
        time.sleep(1)
        st.json(classification)
        status.update(label="✅ AI Classification Complete", state="complete")
        
    intent = classification.get('intent', '').lower()
    sentiment = classification.get('sentiment', '').lower()
    
    # STEP 2: Routing
    st.subheader("🛤️ BPMN Gateway Routing")
    
    if intent == 'order_status' and sentiment not in ['angry', 'frustrated', 'complaint']:
        st.success("Route: Automated Response (Happy Path)")
        
        with st.status("⚙️ Executing RPA Task: Database Lookup...", expanded=True) as status:
            db = load_db()
            st.write("Searching database for Order ID...")
            time.sleep(1)
            
            found_order = None
            for record in db:
                if record['order_id'] in email_text:
                    found_order = record
                    break
                    
            if found_order:
                st.write(f"**Found Order:** {found_order['order_id']} | **Status:** {found_order['status']}")
                status.update(label="✅ RPA Task Complete", state="complete")
                
                st.info(f"**✉️ Automated Reply Drafted:**\n\n'Hello, your order {found_order['order_id']} is currently {found_order['status']}. Expected delivery is {found_order['expected_delivery']}.'")
            else:
                st.warning("Order ID not found in text.")
                status.update(label="⚠️ RPA Task Failed: No ID", state="error")
                
    elif intent == 'refund_request' or sentiment in ['angry', 'frustrated', 'complaint']:
        st.error("Route: Escalate to Human Agent (Exception Path)")
        
        with st.status("⚠️ Executing Action Center Handoff...", expanded=True) as status:
            time.sleep(1)
            st.write("Creating High-Priority Case in UiPath Action Center...")
            st.write(f"**Case Details:** Intent='{intent}', Sentiment='{sentiment}'")
            status.update(label="✅ Case Escalated to Human", state="complete")
            
    else:
        st.warning("Route: Default Support Queue")
        st.write("Action: Ticket created in standard queue.")
