# Deployment Guide

## GitHub Setup

### 1. Create GitHub repo

```bash
# Create new repo at https://github.com/new
# Name it: chatbot-comparison (or whatever you prefer)
# Do NOT initialize with README/license (we have those)
```

### 2. Add GitHub remote & push

```bash
git remote add origin https://github.com/YOUR_USERNAME/chatbot-comparison.git
git branch -M main
git push -u origin main
```

Verify at: `https://github.com/YOUR_USERNAME/chatbot-comparison`

---

## Deploy to Streamlit Cloud (Free)

### 1. Connect Streamlit account to GitHub

- Go to [share.streamlit.io](https://share.streamlit.io)
- Sign up with GitHub (authorizes Streamlit to access your repos)

### 2. Deploy app

- Click "New app"
- Select your GitHub repo
- Set:
  - **Repository:** `YOUR_USERNAME/chatbot-comparison`
  - **Branch:** `main`
  - **Main file path:** `app.py`

### 3. Add API key (Streamlit Secrets)

In Streamlit Cloud dashboard:
1. Click your deployed app
2. Settings → Secrets
3. Paste (replace with your key from https://console.groq.com):
```toml
GROQ_API_KEY = "gsk_YOUR_KEY_HERE"
```
4. Save & app auto-redeploys

**⚠️ Important:** Never commit `.env` or API keys to GitHub. Streamlit Secrets keeps them private.

### 4. View live app

Your app is now live at:
```
https://chatbot-comparison.streamlit.app
```
(URL changes based on repo name)

---

## Alternative: Deploy to Heroku / Railway / Render

If you want more control, use these platforms:

### Heroku
```bash
heroku login
heroku create chatbot-comparison
git push heroku main
heroku config:set GROQ_API_KEY="gsk_..."
```

### Railway
- Connect GitHub repo
- Auto-deploys on push
- Set env vars in dashboard

### Render
- Similar to Railway
- Free tier available
- Connect GitHub

---

## Local Development

After pushing to GitHub, team members can clone & run:

```bash
git clone https://github.com/YOUR_USERNAME/chatbot-comparison.git
cd chatbot-comparison

pip install -r requirements.txt
export GROQ_API_KEY="gsk_..."
streamlit run app.py
```

---

## Updating Deployed App

After making changes locally:

```bash
git add .
git commit -m "Your changes"
git push origin main
```

Streamlit Cloud auto-redeploys in ~30 seconds.

---

## Troubleshooting

**"API key not found"**
- Check Streamlit Secrets are set in dashboard
- Secrets don't sync from local `.env`, must be set in cloud

**"Module not found"**
- Check `requirements.txt` has all dependencies
- Commit `requirements.txt` changes
- Push to GitHub

**Slow response time**
- Free Streamlit tier has limited resources
- LLM API calls add latency (normal)
- Upgrade to Streamlit Pro for better performance
