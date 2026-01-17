import google.generativeai as genai
import json
import os
from dotenv import load_dotenv

load_dotenv()

# Configure API
API_KEY = os.getenv("GEMINI_API_KEY")

# Fallback for Streamlit Cloud Secrets if local .env fails
if not API_KEY:
    try:
        import streamlit as st
        API_KEY = st.secrets["GEMINI_API_KEY"]
    except:
        pass

if API_KEY:
    genai.configure(api_key=API_KEY)

def analyze_waste(image):
    if not API_KEY:
        return {"error": "API Key missing"}

    model = genai.GenerativeModel('gemini-1.5-flash')

    prompt = """
    Act as an environmental expert. Analyze the waste item in this image.
    Return ONLY a raw JSON object (no markdown, no ```json tags).
    Follow this exact schema:
    {
        "item_name": "Short Name",
        "category": "Recyclable | Organic | Hazardous | E-Waste | Residual",
        "confidence": "80-100%",
        "material_breakdown": "e.g., 90% Plastic, 10% Paper",
        "bin_color": "Blue (for Paper) | Green (for Organic) | Yellow (for Plastic/Metal) | Red (Hazardous) | Black (General)",
        "disposal_steps": ["Step 1", "Step 2", "Step 3"],
        "environmental_impact": "1 sentence on impact if not disposed correctly",
        "sustainability_tips": {
            "reduce": "Advice to reduce this waste",
            "reuse": "Advice to reuse this item",
            "recycle": "Specific recycling advice"
        },
        "upcycling_ideas": ["Creative Idea 1", "Creative Idea 2"]
    }
    """

    try:
        response = model.generate_content([prompt, image])
        # Clean response if LLM adds markdown wrappers
        clean_json = response.text.replace('```json', '').replace('```', '').strip()
        return json.loads(clean_json)
    except Exception as e:
        return {"error": str(e)}