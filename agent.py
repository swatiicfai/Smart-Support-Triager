import json
from openai import OpenAI
import os

# Note: Set your OPENAI_API_KEY environment variable before running
api_key = os.environ.get("OPENAI_API_KEY")
client = OpenAI(api_key=api_key) if api_key else None

def classify_email(email_text: str) -> dict:
    """
    Uses an LLM to classify the intent, sentiment, and urgency of an email.
    """
    # Fallback mock logic for hackathon demo if no API key is provided
    if not client:
        print("   [!] No OPENAI_API_KEY found. Using mock AI response for demo purposes.")
        if "ORD-1234" in email_text:
            return {"intent": "order_status", "sentiment": "neutral", "urgency": "low"}
        elif "refund" in email_text.lower() or "ridiculous" in email_text.lower():
            return {"intent": "refund_request", "sentiment": "angry", "urgency": "high"}
        else:
            return {"intent": "unknown", "sentiment": "neutral", "urgency": "low"}

    prompt = f"""
    You are an AI assistant for a customer support team. 
    Analyze the following customer email and extract the intent, sentiment, and urgency.
    
    Return ONLY a JSON object with the following keys:
    - "intent": (e.g., "order_status", "refund_request", "technical_issue", "complaint")
    - "sentiment": (e.g., "positive", "neutral", "angry", "frustrated")
    - "urgency": ("high" or "low")
    
    Email:
    "{email_text}"
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini", # Fast and cheap for hackathons
            messages=[
                {"role": "system", "content": "You are a helpful assistant that outputs strict JSON."},
                {"role": "user", "content": prompt}
            ],
            response_format={ "type": "json_object" }
        )
        
        result = json.loads(response.choices[0].message.content)
        return result
    except Exception as e:
        print(f"Error parsing JSON: {e}")
        return {"intent": "unknown", "sentiment": "neutral", "urgency": "low"}

if __name__ == "__main__":
    # Test the agent directly
    test_email = "Where is my order? I ordered it 2 weeks ago and it's still not here! ORD-9999"
    print("Testing Agent Output:")
    print(json.dumps(classify_email(test_email), indent=2))
