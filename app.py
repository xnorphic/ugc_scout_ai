
import streamlit as st
import base64
import requests
from PIL import Image
from io import BytesIO

# --------------------------
# CONFIGURATION
# --------------------------
st.set_page_config(page_title="UGC Scout with GPT-4 Vision", layout="centered")
st.title("📸 UGC Scout (AI-powered)")

st.markdown("Upload user-generated content (UGC) images and evaluate how well they match your brand aesthetic using GPT-4 Vision.")

# API Key check
if "OPENAI_API_KEY" not in st.secrets:
    st.error("🚨 OPENAI_API_KEY not found in Streamlit secrets. Please set it in your Streamlit Cloud settings.")
    st.stop()

API_KEY = st.secrets["OPENAI_API_KEY"]
API_URL = "https://api.openai.com/v1/chat/completions"

# --------------------------
# HELPER FUNCTION
# --------------------------
def analyze_image_with_project_key(image: Image.Image, brand_prompt: str) -> str:
    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    img_b64 = base64.b64encode(buffered.getvalue()).decode()

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "gpt-4-vision-preview",
        "messages": [
            {
                "role": "system",
                "content": "You are a creative brand stylist helping a D2C skincare brand evaluate user-generated content."
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": f"""Please evaluate the attached image. 
Does it match this brand tone: '{brand_prompt}'?
Give a score out of 10 and a brief reason. Mention what works, what doesn’t, and what can be improved.
Also classify the image as one of the following types: 'ad-worthy', 'testimonial', 'flatlay', 'lifestyle', or 'uncategorized'."""
                    },
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64,{img_b64}"}
                    }
                ]
            }
        ],
        "max_tokens": 500
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()['choices'][0]['message']['content']
    except requests.exceptions.RequestException as e:
        return f"❌ Error analyzing image: {str(e)}"

# --------------------------
# USER INPUT
# --------------------------
brand_prompt = st.text_input("🧬 Describe your brand aesthetic (e.g. 'minimal, clean, luxury skincare')", "")

uploaded_files = st.file_uploader("📤 Upload UGC Images (JPG/PNG)", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

# --------------------------
# PROCESS FILES
# --------------------------
if uploaded_files and brand_prompt:
    for file in uploaded_files:
        image = Image.open(file).convert("RGB")
        st.image(image.resize((300, 300)), caption=file.name, use_column_width="always")
        with st.spinner("Analyzing image..."):
            analysis = analyze_image_with_project_key(image, brand_prompt)
        st.markdown(f"🧠 **GPT-4 Vision Feedback:**\n\n{analysis}")
        st.divider()
