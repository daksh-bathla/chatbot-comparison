# Chatbot: Rule-Based vs LLM-Powered

Two chatbot implementations showing the evolution from simple keyword matching to conversational AI.

## Files

- **`app.py`** ⭐ — **Interactive Streamlit web app** (both chatbots side-by-side) ← START HERE
- **`faq_chatbot.py`** — Rule-based chatbot using if-else/keyword matching (CLI)
- **`llm_chatbot.py`** — LLM-powered chatbot using Groq API (CLI)
- **`example_conversations.txt`** — Sample conversations showing both in action

## Quick Start

### 🌐 Interactive Web App (Recommended for Presentation)

```bash
pip install streamlit groq
export GROQ_API_KEY="gsk_your-key-here"
streamlit run app.py
```

Opens browser with both chatbots running side-by-side. Ask the same question and compare responses instantly. Perfect for screenshots/demos.

### Rule-Based Chatbot (No Setup - CLI)

```bash
python faq_chatbot.py
```

No dependencies. Just run it. Example prompts:
- "What are your hours?"
- "How much does shipping cost?"
- "Can I return items?"

### LLM-Powered Chatbot (Requires Groq API Key)

**1. Install dependency:**
```bash
pip install groq
```

**2. Get API key:**
- Sign up at [console.groq.com](https://console.groq.com)
- Create API key in settings
- Set environment variable:
```bash
export GROQ_API_KEY="gsk-your-key-here"
```

**3. Check available models:**
- Login to [console.groq.com](https://console.groq.com)
- Go to "Models" section to see what's available on your account
- Note: Models available vary by region and account tier

**4. Update model in code (if needed):**
Edit `llm_chatbot.py` and change `GROQ_MODEL` at top of file:
```python
GROQ_MODEL = "deepseek-r1-distill-llama-70b"  # Change to match your available model
```

**5. Run it:**
```bash
python llm_chatbot.py
```

Try the same questions — notice more natural, flexible responses. Try follow-ups too.

## For Your Presentation

### Use the Streamlit App (Live Demo)

```bash
streamlit run app.py
```

This is perfect for live presentations:
- Both chatbots side-by-side in one interface
- Real-time comparison of responses
- Easy to screenshot or screen-record
- Shows conversation history and context handling
- Clean UI with built-in explanations

### Or Capture Manual Screenshots

Run both chatbots in separate terminals and ask them the same questions:

**Test Prompt 1 (Simple):**
```
What are your hours?
```
→ Both answer correctly, but LLM more conversational

**Test Prompt 2 (Variation):**
```
What time do you close on weekdays?
```
→ Rule-based fails, LLM succeeds

**Test Prompt 3 (Follow-up):**
```
How much is shipping?
[wait for answer]
What about overnight?
```
→ Rule-based fails on follow-up, LLM understands context

**Test Prompt 4 (Related but not in FAQ):**
```
Is there a warranty?
```
→ Rule-based doesn't match, LLM infers from return policy

## Code Structure

### Rule-Based Chatbot

```python
FAQS = {
    "hours": {
        "keywords": ["hour", "open", "close", ...],
        "response": "..."
    },
    ...
}

# Matches user input to FAQ using keyword count
# No conversation history
# Fast, predictable, limited
```

### LLM-Powered Chatbot

```python
SYSTEM_PROMPT = "You are a helpful customer support chatbot..."

conversation_history = []  # Maintains context across turns

# Sends full conversation to LLM API
# LLM generates natural, contextual responses
# Flexible, conversational, costs money per query
```

## Key Insights for Presentation

| Aspect | Rule-Based | LLM-Powered |
|--------|-----------|------------|
| **Setup** | None | API key required |
| **Cost** | $0 | ~$0.0005-0.001 per message |
| **Flexibility** | Rigid | Highly flexible |
| **Context** | No | Full conversation history |
| **Response Speed** | Instant | 1-2 seconds (API) |
| **Scaling** | Manual FAQ updates | Add to system prompt |
| **Quality** | Feels automated | Feels human |

## Customization

### Add More FAQs to Rule-Based:
```python
FAQS["warranty"] = {
    "keywords": ["warranty", "guarantee", "broken"],
    "response": "2-year warranty on hardware..."
}
```

### Change LLM Model:
In `llm_chatbot.py`, change `GROQ_MODEL` at the top:
```python
GROQ_MODEL = "deepseek-r1-distill-llama-70b"  # Change to any model on your account
```
See available models: [console.groq.com/docs/models](https://console.groq.com/docs/models)

## Troubleshooting

**LLM Chatbot: "Error connecting to API"**
- Check `GROQ_API_KEY` is set: `echo $GROQ_API_KEY`
- Verify API key is valid in Groq console
- Check internet connection

**LLM Chatbot: "module not found: groq"**
- Install: `pip install groq`

**Rule-Based Chatbot: Not matching my question**
- Expected behavior — only matches FAQ keywords
- This is the limitation being demonstrated
