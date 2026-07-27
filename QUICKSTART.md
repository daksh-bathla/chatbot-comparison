# Quick Start Guide

## 1️⃣ Setup (One-time)

```bash
# Install dependencies
pip install streamlit groq

# Set Groq API key (get from https://console.groq.com)
export GROQ_API_KEY="gsk_YOUR_KEY_HERE"
```

## 2️⃣ Run Streamlit App (Recommended)

```bash
streamlit run app.py
```

Browser opens at `http://localhost:8501` with both chatbots side-by-side.

### Try these questions to see the difference:

**Simple FAQ:**
- "What are your hours?"

**Variation (rule-based fails, LLM succeeds):**
- "What time do you close on weekdays?"

**Follow-up (tests context):**
- Ask "How much does shipping cost?"
- Then ask "What about overnight?"

**Related Q not in FAQ:**
- "Is there a warranty?"

**Out of scope:**
- "What's the meaning of life?"

## 3️⃣ CLI Versions (Optional)

Rule-based only (no setup):
```bash
python3 faq_chatbot.py
```

LLM-powered (requires GROQ_API_KEY):
```bash
python3 llm_chatbot.py
```

## For Presentations

**Option A: Live Demo**
- Run `streamlit run app.py`
- Ask questions live on projector
- Shows instant difference between chatbots

**Option B: Screenshots**
- Use the web app to capture side-by-side responses
- Use the pre-written transcripts in `example_conversations.txt`

## Troubleshooting

**"GROQ_API_KEY not set"**
```bash
export GROQ_API_KEY="gsk_..."
```

**"Module not found: groq"**
```bash
pip install groq
```

**"Module not found: streamlit"**
```bash
pip install streamlit
```

**"Model decommissioned"**
- Check available models: https://console.groq.com/docs/models
- Update `GROQ_MODEL` in `app.py` or `llm_chatbot.py`

## File Reference

- `app.py` — Streamlit web UI (best for demos)
- `faq_chatbot.py` — Rule-based CLI version
- `llm_chatbot.py` — LLM CLI version
- `example_conversations.txt` — Pre-written transcripts
- `README.md` — Full documentation
