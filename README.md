
# UGC Scout AI (GPT-4 Vision with sk-proj- Key)

This version of the UGC Scout app uses GPT-4 Vision via direct HTTP requests to support project-specific API keys (sk-proj-...).

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
