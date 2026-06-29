<div align="center">
  <img src="https://img.shields.io/badge/UiPath-AgentHack-blue?style=for-the-badge&logo=uipath" alt="UiPath AgentHack" />
  <h1>🤖 Smart Support Triager</h1>
  <p><strong>Track 2: UiPath Maestro BPMN</strong></p>
  <p>An intelligent agentic workflow that uses AI to classify customer support emails and UiPath Maestro BPMN to automatically resolve simple requests or route complex exceptions to human agents.</p>
  <br/>

  [![Live Demo](https://img.shields.io/badge/Live-Demo-success?style=for-the-badge)](https://swatiicfai.github.io/Smart-Support-Triager/)
  [![Demo Video](https://img.shields.io/badge/Demo-Video-red?style=for-the-badge&logo=youtube)](https://www.youtube.com/watch?v=WiQBYqf0Wh8)
  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)
</div>

---

## 📖 Inspiration

Customer support teams spend countless hours manually reading and triaging emails. Simple requests (like "Where is my order?") take time away from complex issues (like angry customers demanding refunds). We wanted to build an agentic solution that acts as a highly intelligent "first line of defense," utilizing AI to understand customer intent and UiPath Maestro to orchestrate the downstream actions.

---

## 🚀 What it does

The Smart Support Triager sits between the customer's inbox and the support team. When an email arrives, it triggers our workflow:

1. **AI Classification:** A coded AI agent reads the email to determine the underlying intent (e.g., `order_status`, `refund_request`) and the customer's sentiment (e.g., `neutral`, `angry`). The agent outputs structured JSON for deterministic downstream routing.
2. **BPMN Logic Gateway:** The UiPath Maestro BPMN flow evaluates the AI's classification against our business rules using an Exclusive Gateway.
3. **Automated Resolution (Happy Path):** If the email is a simple status check, Maestro triggers an RPA task to look up the order in the database and automatically drafts a reply to the customer.
4. **Human Escalation (Exception Path):** If the customer is angry or requesting a refund, Maestro automatically routes the ticket to the **UiPath Action Center**, creating a High-Priority case for immediate human review.

---

## 🛠️ UiPath Components Used

> **Agent Type: Combination of Coded Agents + Low-Code Maestro BPMN Orchestration**

| Component | Usage |
|---|---|
| **UiPath Maestro** | Core orchestration engine — hosts the BPMN process that routes tickets |
| **UiPath Maestro BPMN** | Exclusive Gateways evaluate AI output variables to route to Happy or Exception path |
| **UiPath Action Center** | Receives high-priority human escalation tasks for agent review |
| **UiPath Orchestrator** | Queue management for incoming support ticket payloads |
| **UiPath Automation Cloud** | Platform hosting for all orchestration and agent logic |
| **Coded AI Agent (Python)** | LLM-powered agent (`agent.py`) that classifies email intent and sentiment |

---

## 🤖 Coding Agents (Bonus Points)

This solution uses **Coded Agents** built with Python and LLM APIs to perform AI classification. The agent was developed using **Gemini CLI** assistance for rapid prototyping, qualifying for the **Coding Agents Bonus Points** under the Platform Usage criterion.

- `agent.py` — Coded AI Agent that sends email content to an LLM and parses structured JSON output
- `bpmn_simulator.py` — Coded logic layer simulating the Maestro BPMN gateway decision engine

---

## 💻 How we built it

*   **The Brain (`agent.py`):** A coded AI agent that sends email content to an LLM API and reliably parses structured JSON containing `intent`, `sentiment`, and `urgency`.
*   **The Orchestration (`bpmn_simulator.py`):** Maestro BPMN logic mapped to handle conditional routing based on the AI's structured output using Exclusive Gateways.
*   **The UI (`index.html`, `styles.css`, `script.js`):** A custom, interactive glassmorphism web interface that visually simulates the exact steps Maestro takes as it processes different types of emails in real-time.

---

## ⚙️ Prerequisites

- A modern web browser (Chrome, Firefox, Edge)
- Python 3.9+ (for running the backend agent locally)
- UiPath Automation Cloud account (for full platform orchestration)
- An LLM API key (e.g., OpenAI, Gemini) for the coded AI agent

---

## 🚀 Setup Instructions

### Option 1 — Live Web Demo (No setup required!)
Simply visit the live demo:
👉 **https://swatiicfai.github.io/Smart-Support-Triager/**

### Option 2 — Run Locally

1. Clone this repository:
   ```bash
   git clone https://github.com/swatiicfai/Smart-Support-Triager.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Smart-Support-Triager
   ```
3. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the AI agent backend:
   ```bash
   python agent.py
   ```
5. Open `index.html` in any modern web browser.
6. Click **Run Agentic Workflow** to see the simulated Maestro BPMN flow in action!

---

## 🚧 Challenges we ran into

The biggest challenge was designing a system that doesn't just "answer" questions, but actually knows *when* to hand off to a human. Determining the exact routing logic for the BPMN Exclusive Gateway required careful thought about which sentiments and intents require human empathy versus which can be fully automated.

---

## 🏆 Accomplishments that we're proud of

We are incredibly proud of completing a fully functional, visually stunning prototype of a complex enterprise workflow. The custom UI clearly demonstrates the power of combining Coded AI Agents with structured UiPath Maestro BPMN orchestration.

---

## 🔮 What's next for Smart Support Triager

- Connect directly to a live email inbox using **UiPath Integration Service**
- Integrate with a real CRM (Salesforce or Zendesk) via UiPath connectors
- Expand the Coded AI Agent to handle dozens of different intent classifications
- Add multilingual support for global customer support teams

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.
