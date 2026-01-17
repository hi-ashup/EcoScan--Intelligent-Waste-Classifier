import streamlit as st

def load_css():
    st.markdown("""
    <style>
        /* Import Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;500;700&family=Inter:wght@300;400;600&display=swap');

        /* Base App Styles */
        .stApp {
            background-color: #05080d;
            background-image: radial-gradient(circle at 50% 50%, rgba(16, 185, 129, 0.05) 0%, transparent 50%);
        }

        /* Typography - FIX: Added missing colons here */
        h1, h2, h3 { 
            font-family: 'Outfit', sans-serif; 
            letter-spacing: -0.5px; 
        }
        
        p, div, span { 
            font-family: 'Inter', sans-serif; 
        }

        /* Custom Glass Card */
        .glass-card {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 24px;
            padding: 24px;
            backdrop-filter: blur(12px);
            margin-bottom: 20px;
            box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease;
        }
        .glass-card:hover {
            border-color: rgba(16, 185, 129, 0.3);
            box-shadow: 0 0 20px rgba(16, 185, 129, 0.1);
        }

        /* Scanner Animation */
        .scan-container {
            position: relative;
            border-radius: 20px;
            overflow: hidden;
            border: 1px solid #10b981;
        }
        .scan-line {
            width: 100%;
            height: 4px;
            background: #10b981;
            box-shadow: 0 0 15px #10b981;
            position: absolute;
            z-index: 10;
            animation: scan 3s infinite linear;
        }
        @keyframes scan {
            0% { top: 0%; opacity: 0; }
            10% { opacity: 1; }
            90% { opacity: 1; }
            100% { top: 100%; opacity: 0; }
        }

        /* Buttons */
        .stButton>button {
            background: rgba(16, 185, 129, 0.1);
            border: 1px solid #10b981;
            color: #10b981;
            border-radius: 12px;
            font-family: 'Outfit', sans-serif;
            font-weight: 700;
            letter-spacing: 1px;
            width: 100%;
        }
        .stButton>button:hover {
            background: #10b981;
            color: white;
            box-shadow: 0 0 20px rgba(16, 185, 129, 0.4);
        }
    </style>
    """, unsafe_allow_html=True)