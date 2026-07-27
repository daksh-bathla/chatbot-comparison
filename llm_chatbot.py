#!/usr/bin/env python3
"""
LLM-Powered FAQ Chatbot
Uses Groq API to handle open-ended questions beyond fixed FAQs.
Shows advantages: flexible, conversational, handles variations & follow-ups.

Setup:
  1. Install: pip install groq
  2. Set API key: export GROQ_API_KEY="gsk_..."
  3. Run: python llm_chatbot.py
"""

import os
from groq import Groq

# Initialize Groq client (reads GROQ_API_KEY from environment)
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Model selection - change based on what's available in your account
# Check https://console.groq.com/docs/models for available models
GROQ_MODEL = "deepseek-r1-distill-llama-70b"

# System prompt defines chatbot personality and role
SYSTEM_PROMPT = """You are a helpful customer support chatbot for an e-commerce company.
You have knowledge about:
- Hours: Open Mon-Fri 9am-6pm EST, Sat 10am-4pm EST. Closed Sundays.
- Pricing: Basic plan $9.99/mo, Pro plan $29.99/mo, Enterprise custom pricing.
- Shipping: Standard (5-7 days) free over $50, Express (2-3 days) $9.99, International available.
- Returns: 30-day money-back guarantee, no questions asked.
- Password reset: Click 'Forgot Password' on login, check email for link.

Answer questions helpfully and naturally. If asked something outside your knowledge, say you don't know.
Keep responses concise (1-2 sentences, 3 max for complex topics)."""

def chat_with_llm(conversation_history: list) -> str:
    """
    Send conversation to Groq API and get response.
    conversation_history: list of {"role": "user"/"assistant", "content": "..."} dicts
    """
    try:
        response = client.chat.completions.create(
            model=GROQ_MODEL,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                *conversation_history  # Include full conversation context
            ],
            temperature=0.7,  # Balanced creativity vs consistency
            max_tokens=150
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error connecting to API: {str(e)}"

def run_chatbot():
    """Run the LLM-powered chatbot CLI."""
    print("=" * 60)
    print("FAQ CHATBOT (LLM-Powered)")
    print("=" * 60)
    print("Type 'quit' to exit.\n")

    # Maintain conversation history for context awareness
    conversation_history = []

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() == "quit":
            print("Goodbye!")
            break

        if not user_input:
            continue

        # Add user message to history
        conversation_history.append({"role": "user", "content": user_input})

        # Get LLM response
        response = chat_with_llm(conversation_history)

        # Add bot response to history (for context in next turn)
        conversation_history.append({"role": "assistant", "content": response})

        print(f"Bot: {response}\n")

if __name__ == "__main__":
    if not os.getenv("GROQ_API_KEY"):
        print("❌ Error: GROQ_API_KEY not set.")
        print("Set it with: export GROQ_API_KEY='gsk_...'")
        exit(1)

    run_chatbot()
