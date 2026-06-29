import json
import time
from agent import classify_email

# Simulate loading the mock database
def load_db():
    with open('mock_db.json', 'r') as f:
        return json.load(f)

# The simulated BPMN Workflow
def process_incoming_email(email_text: str, email_address: str):
    print("\n" + "="*60)
    print(f"[BPMN START] New email received from {email_address}")
    print(f"   Content: '{email_text}'")
    print("="*60)
    
    print("\n[BPMN STEP 1] Calling AI Agent for Classification...")
    time.sleep(1) # Simulate network delay
    classification = classify_email(email_text)
    print(f"   Agent Output: {json.dumps(classification, indent=2)}")
    
    intent = classification.get('intent', '').lower()
    sentiment = classification.get('sentiment', '').lower()
    
    print("\n[BPMN GATEWAY] Evaluating routing rules...")
    
    # Routing Logic (This is what you would model in UiPath Studio/Maestro)
    if intent == 'order_status' and sentiment not in ['angry', 'frustrated', 'complaint']:
        print("   -> Route: Automated Response (Happy Path)")
        handle_automated_order_status(email_text)
    elif intent == 'refund_request' or sentiment in ['angry', 'frustrated', 'complaint']:
        print("   -> Route: Escalate to Human Agent (Exception Path)")
        handle_escalation(email_text, classification)
    else:
        print("   -> Route: Default Support Queue")
        print("   Action: Ticket created in standard queue.")
        
    print("="*60)
    print("[BPMN END] Workflow completed.\n")

def handle_automated_order_status(email_text):
    print("\n[BPMN STEP 2A] Executing RPA task: Checking Database...")
    db = load_db()
    # Simple mock logic to find order ID in text (very basic for hackathon demo)
    found_order = None
    for record in db:
        if record['order_id'] in email_text:
            found_order = record
            break
            
    time.sleep(1)
    if found_order:
        print(f"   RPA Result: Found order {found_order['order_id']} with status '{found_order['status']}'")
        print("\n[BPMN STEP 3A] Sending automated reply...")
        print(f"   Draft: 'Hello, your order {found_order['order_id']} is currently {found_order['status']}. Expected delivery is {found_order['expected_delivery']}.'")
    else:
        print("   RPA Result: Order ID not found in text.")
        print("   Action: Escalating to human to ask for Order ID.")

def handle_escalation(email_text, classification):
    print("\n[BPMN STEP 2B] Executing Action Center Handoff...")
    time.sleep(1)
    print(f"   Action: Creating a High-Priority Case in UiPath Action Center.")
    print(f"   Case Details: Intent='{classification['intent']}', Sentiment='{classification['sentiment']}'")
    print("   Status: Waiting for Human Review.")

if __name__ == "__main__":
    # Test Case 1: Simple Order Status (Automated)
    process_incoming_email("Hi, can you tell me the status of ORD-1234? Thanks!", "john.doe@example.com")
    
    # Test Case 2: Angry Customer (Escalation)
    process_incoming_email("This is ridiculous! I've been waiting forever for ORD-9999. I want a refund now!", "angry.customer@example.com")
