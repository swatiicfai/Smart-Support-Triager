<div align="center">
  <img src="https://img.shields.io/badge/UiPath-AgentHack-blue?style=for-the-badge&logo=uipath" alt="UiPath AgentHack" />
  <h1>🤖 Smart Support Triager</h1>
  <p><strong>Track 2: UiPath Maestro BPMN</strong></p>
  <p>An intelligent agentic workflow that uses AI to classify customer support emails and UiPath Maestro BPMN to automatically resolve simple requests or route complex exceptions to human agents.</p>
  <br/>
  
  [![Live Demo](https://img.shields.io/badge/Live-Demo-success?style=for-the-badge)](https://swatiicfai.github.io/Smart-Support-Triager/)
  [![Demo Video](https://img.shields.io/badge/Demo-Video-red?style=for-the-badge&logo=youtube)](https://www.youtube.com/watch?v=WiQBYqf0Wh8)
</div>

---

## 📖 Inspiration

Customer support teams spend countless hours manually reading and triaging emails. Simple requests (like "Where is my order?") take time away from complex issues (like angry customers demanding refunds). We wanted to build an agentic solution that acts as a highly intelligent "first line of defense," utilizing AI to understand customer intent and UiPath Maestro to orchestrate the downstream actions.

## 🚀 What it does

The Smart Support Triager sits between the customer's inbox and the support team. When an email arrives, it triggers our workflow:

1. **AI Classification:** An AI agent reads the email to determine the underlying intent (e.g., `order_status`, `refund_request`) and the customer's sentiment (e.g., `neutral`, `angry`).
2. **BPMN Logic Gateway:** The UiPath Maestro flow evaluates the AI's classification against our business rules.
3. **Automated Resolution (Happy Path):** If the email is a simple status check, Maestro triggers an RPA task to look up the order in the database and automatically drafts a reply to the customer.
4. **Human Escalation (Exception Path):** If the customer is angry or requesting a refund, Maestro automatically routes the ticket to the UiPath Action Center, creating a High-Priority case for immediate human review.

## 💻 How we built it

Since we had a strict timeline, we rapidly prototyped the agentic logic using Python and created an interactive frontend to demonstrate the flow.

*   **The Brain (`agent.py`):** We designed the AI classification schema to reliably output structured JSON containing `intent`, `sentiment`, and `urgency`.
*   **The Orchestration (`bpmn_simulator.py`):** We mapped out the Maestro BPMN logic to handle conditional routing based on the AI's structured output. 
*   **The UI (`index.html`, `styles.css`, `script.js`):** To demonstrate the flow clearly to the judges, we built a custom, interactive web interface using HTML, CSS (Glassmorphism), and Vanilla JavaScript to visually simulate the exact steps Maestro takes as it processes different types of emails.

## ⚙️ Running the Project

You can experience the interactive visualizer locally by opening the frontend file in your browser:

1. Clone this repository:
   ```bash
   git clone https://github.com/swatiicfai/Smart-Support-Triager.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Smart-Support-Triager
   ```
3. Open `index.html` in any modern web browser.
4. Click **Run Agentic Workflow** to see the simulated Maestro BPMN flow in action!

## 🚧 Challenges we ran into

The biggest challenge was designing a system that doesn't just "answer" questions, but actually knows *when* to hand off to a human. Determining the exact routing logic for the BPMN gateway required careful thought about which sentiments and intents require human empathy versus which can be fully automated. 

## 🏆 Accomplishments that we're proud of

We are incredibly proud of completing a fully functional, visually stunning prototype of a complex enterprise workflow in under 2 hours. The custom UI clearly demonstrates the power of combining AI Agents with structured BPMN orchestration.

## 🔮 What's next for Smart Support Triager

In the future, we plan to connect this directly to a live email inbox using UiPath Integration Service, integrate it with a real CRM (like Salesforce or Zendesk), and expand the AI Agent to handle dozens of different intent classifications.
