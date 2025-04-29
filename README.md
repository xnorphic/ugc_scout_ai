
# UGC Scout AI (GPT-4 Vision)

A Streamlit app that uses GPT-4 Vision to score user-generated content (UGC) against your brand tone. It also classifies each image as "ad-worthy", "testimonial", "flatlay", "lifestyle", or "uncategorized".

## Setup

1. Clone this repo
2. Run `pip install -r requirements.txt`
3. Add your OpenAI API key to `.streamlit/secrets.toml`
4. Run locally with:
   ```bash
   streamlit run app.py
   ```

## Deploy on Streamlit Cloud

1. Push this repo to GitHub
2. Go to [streamlit.io/cloud](https://streamlit.io/cloud) → New App
3. Connect your GitHub account
4. Select this repo and `app.py`
5. Add your OpenAI API key in Settings → Secrets:

```
OPENAI_API_KEY = "sk-proj-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

6. Click **Deploy**
