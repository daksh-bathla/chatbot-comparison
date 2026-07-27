#!/usr/bin/env python3
"""
Rule-Based FAQ Chatbot
Simple keyword matching with if-else logic for fixed FAQs.
Shows limitations: rigid responses, can't handle variations.
"""

# Simple FAQ database
FAQS = {
    "hours": {
        "keywords": ["hour", "open", "close", "when", "available"],
        "response": "We're open Mon-Fri 9am-6pm EST, Sat 10am-4pm EST. Closed Sundays."
    },
    "pricing": {
        "keywords": ["price", "cost", "how much", "charge", "expensive"],
        "response": "Basic plan: $9.99/mo. Pro plan: $29.99/mo. Enterprise: custom pricing. See our website for details."
    },
    "shipping": {
        "keywords": ["ship", "delivery", "arrive", "mail", "post"],
        "response": "Standard shipping (5-7 days): free over $50. Express (2-3 days): $9.99. International available."
    },
    "returns": {
        "keywords": ["return", "refund", "exchange", "broken", "wrong"],
        "response": "30-day money-back guarantee on all purchases. No questions asked. Contact support@example.com."
    },
    "password": {
        "keywords": ["password", "reset", "forgot", "login", "account"],
        "response": "Click 'Forgot Password' on login page. Check your email for reset link. Contact support if not received."
    },
}

def find_faq_response(user_input: str) -> str:
    """
    Match user input to FAQ using simple keyword matching.
    Returns best matching FAQ response or default message.
    """
    user_input_lower = user_input.lower()

    # Track which FAQ has most keyword matches
    best_match = None
    best_count = 0

    for faq_key, faq_data in FAQS.items():
        match_count = sum(1 for keyword in faq_data["keywords"]
                         if keyword in user_input_lower)
        if match_count > best_count:
            best_count = match_count
            best_match = faq_data

    # Return matched response or default fallback
    if best_match:
        return best_match["response"]
    else:
        return "I'm not sure about that. Try asking about: hours, pricing, shipping, returns, or password reset."

def run_chatbot():
    """Run the rule-based chatbot CLI."""
    print("=" * 60)
    print("FAQ CHATBOT (Rule-Based)")
    print("=" * 60)
    print("Type 'quit' to exit.\n")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() == "quit":
            print("Goodbye!")
            break

        if not user_input:
            continue

        response = find_faq_response(user_input)
        print(f"Bot: {response}\n")

if __name__ == "__main__":
    run_chatbot()
