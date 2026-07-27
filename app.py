#!/usr/bin/env python3
"""
Streamlit app comparing rule-based vs LLM-powered chatbots.
Run: streamlit run app.py
"""

import streamlit as st
import os
from groq import Groq

# Page config
st.set_page_config(page_title="Chatbot Comparison", layout="wide", initial_sidebar_state="collapsed")
st.title("📊 Chatbot Comparison: Rule-Based vs LLM-Powered")

# ============================================================================
# RULE-BASED CHATBOT
# ============================================================================

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

def get_faq_response(user_input: str) -> str:
    """Rule-based chatbot using keyword matching."""
    user_input_lower = user_input.lower()
    best_match = None
    best_count = 0

    for faq_key, faq_data in FAQS.items():
        match_count = sum(1 for keyword in faq_data["keywords"]
                         if keyword in user_input_lower)
        if match_count > best_count:
            best_count = match_count
            best_match = faq_data

    if best_match:
        return best_match["response"]
    else:
        return "I'm not sure about that. Try asking about: hours, pricing, shipping, returns, or password reset."


# ============================================================================
# LLM-POWERED CHATBOT
# ============================================================================

GROQ_MODEL = "deepseek-r1-distill-llama-70b"

SYSTEM_PROMPT = """You are a helpful customer support chatbot for an e-commerce company.
You have knowledge about:
- Hours: Open Mon-Fri 9am-6pm EST, Sat 10am-4pm EST. Closed Sundays.
- Pricing: Basic plan $9.99/mo, Pro plan $29.99/mo, Enterprise custom pricing.
- Shipping: Standard (5-7 days) free over $50, Express (2-3 days) $9.99, International available.
- Returns: 30-day money-back guarantee, no questions asked.
- Password reset: Click 'Forgot Password' on login, check email for link.

Answer questions helpfully and naturally. If asked something outside your knowledge, say you don't know.
Keep responses concise (1-2 sentences, 3 max for complex topics)."""

def get_llm_response(conversation_history: list) -> str:
    """LLM chatbot using Groq API."""
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        return "❌ Error: GROQ_API_KEY not set. Set it with: export GROQ_API_KEY='gsk_...'"

    try:
        client = Groq(api_key=api_key)
        response = client.chat.completions.create(
            model=GROQ_MODEL,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                *conversation_history
            ],
            temperature=0.7,
            max_tokens=150
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ API Error: {str(e)}"


# ============================================================================
# STREAMLIT UI
# ============================================================================

st.markdown("""
**Test the same question on both chatbots to see the difference:**
- **Left (Rule-Based)**: Rigid keyword matching, limited responses
- **Right (LLM-Powered)**: Flexible, conversational, contextual understanding
""")

# User input
user_question = st.text_input("Ask a question:", placeholder="e.g., What are your hours?", key="user_question")

if user_question:
    col1, col2 = st.columns(2)

    # RULE-BASED RESPONSE
    with col1:
        st.subheader("🤖 Rule-Based Chatbot")
        st.info("Uses keyword matching (if-else logic)")
        rule_response = get_faq_response(user_question)
        st.write(f"**Bot:** {rule_response}")

    # LLM RESPONSE
    with col2:
        st.subheader("🧠 LLM-Powered Chatbot")
        st.info("Uses Groq API (AI-generated)")
        llm_response = get_llm_response([{"role": "user", "content": user_question}])
        st.write(f"**Bot:** {llm_response}")

    # Comparison insight
    st.divider()
    st.markdown("""
    **💡 What to notice:**
    - Rule-based chatbot can fail on slight wording variations
    - LLM chatbot understands natural language better
    - Try follow-ups or questions outside the FAQ to see bigger differences
    """)

# ============================================================================
# CONVERSATION HISTORY TAB
# ============================================================================

st.divider()
st.subheader("💬 Full Conversation Mode")

if "rule_history" not in st.session_state:
    st.session_state.rule_history = []
if "llm_history" not in st.session_state:
    st.session_state.llm_history = []

col1, col2 = st.columns(2)

with col1:
    st.write("**Rule-Based Chat:**")
    chat_container_rule = st.container(height=300, border=True)
    with chat_container_rule:
        for msg in st.session_state.rule_history:
            if msg["role"] == "user":
                st.write(f"👤 **You:** {msg['content']}")
            else:
                st.write(f"🤖 **Bot:** {msg['content']}")

with col2:
    st.write("**LLM-Powered Chat:**")
    chat_container_llm = st.container(height=300, border=True)
    with chat_container_llm:
        for msg in st.session_state.llm_history:
            if msg["role"] == "user":
                st.write(f"👤 **You:** {msg['content']}")
            else:
                st.write(f"🧠 **Bot:** {msg['content']}")

# Input for full conversation
convo_input = st.text_input("Continue conversation:", placeholder="Ask another question...", key="convo_input")

if convo_input:
    # Rule-based response
    rule_resp = get_faq_response(convo_input)
    st.session_state.rule_history.append({"role": "user", "content": convo_input})
    st.session_state.rule_history.append({"role": "assistant", "content": rule_resp})

    # LLM response
    llm_history_for_api = [
        {"role": msg["role"], "content": msg["content"]}
        for msg in st.session_state.llm_history
    ]
    llm_history_for_api.append({"role": "user", "content": convo_input})
    llm_resp = get_llm_response(llm_history_for_api)
    st.session_state.llm_history.append({"role": "user", "content": convo_input})
    st.session_state.llm_history.append({"role": "assistant", "content": llm_resp})

    st.rerun()

# Clear button
if st.button("Clear Conversation History"):
    st.session_state.rule_history = []
    st.session_state.llm_history = []
    st.rerun()

# ============================================================================
# INFO & SETUP
# ============================================================================

with st.sidebar:
    st.markdown("### ℹ️ Setup Instructions")
    st.code("""
pip install streamlit groq

export GROQ_API_KEY="gsk_..."

streamlit run app.py
    """, language="bash")

    st.markdown("### 📋 Test Prompts")
    st.markdown("""
    **Simple FAQ:**
    - What are your hours?

    **Variation (tests flexibility):**
    - What time do you close on weekdays?

    **Follow-up (tests context):**
    - How much is shipping?
    - What about overnight?

    **Out of scope (tests graceful failure):**
    - What's the meaning of life?
    """)

    st.markdown("### 📊 Key Differences")
    st.markdown("""
    | Aspect | Rule-Based | LLM |
    |--------|-----------|-----|
    | **Setup** | None | API key |
    | **Speed** | Instant | 1-2s |
    | **Flexibility** | Low | High |
    | **Context** | No | Yes |
    | **Cost** | $0 | ~$0.001/msg |
    """)
