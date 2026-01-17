import streamlit as st

def load_css():
    st.markdown("""
    <style>
        /* IMPORT FONTS */
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&family=Inter:wght@300;400;600&display=swap');

        /* RESET & BASE THEME */
        :root {
            --primary: #10b981;
            --primary-dark: #059669;
            --background-dark: #05080d;
            --glass-bg: rgba(255, 255, 255, 0.03);
            --glass-border: rgba(255, 255, 255, 0.08);
            --glass-blur: blur(20px);
        }

        .stApp {
            background-color: var(--background-dark);
            background-image: 
                radial-gradient(circle at 10% 20%, rgba(16, 185, 129, 0.08) 0%, transparent 40%),
                radial-gradient(circle at 90% 80%, rgba(16, 185, 129, 0.05) 0%, transparent 40%);
            color: #f1f5f9;
        }

        /* HIDE STREAMLIT BRANDING */
        header {visibility: hidden;}
        footer {visibility: hidden;}
        #MainMenu {visibility: hidden;}

        /* TYPOGRAPHY OVERRIDES */
        h1, h2, h3 { 
            font-family: 'Outfit', sans-serif !important; 
            font-weight: 700 !important;
            letter-spacing: -1px;
            color: white !important;
        }
        
        /* THE 'GLASS' CONTAINER COMPONENT */
        .glass-container {
            background: var(--glass-bg);
            backdrop-filter: var(--glass-blur);
            -webkit-backdrop-filter: var(--glass-blur);
            border: 1px solid var(--glass-border);
            border-radius: 24px;
            padding: 2rem;
            margin-bottom: 24px;
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
            position: relative;
            overflow: hidden;
        }

        /* CUSTOM BUTTON STYLING (Primary Action) */
        .stButton button {
            background: linear-gradient(135deg, rgba(16, 185, 129, 0.1), rgba(16, 185, 129, 0.05));
            color: #10b981 !important;
            border: 1px solid rgba(16, 185, 129, 0.4) !important;
            border-radius: 12px;
            padding: 0.6rem 1.2rem;
            font-family: 'Outfit', sans-serif;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 1px;
            transition: all 0.3s ease;
            box-shadow: 0 0 0px transparent;
        }
        
        .stButton button:hover {
            background: #10b981 !important;
            color: #000 !important;
            box-shadow: 0 0 25px rgba(16, 185, 129, 0.5);
            transform: translateY(-2px);
            border-color: #10b981 !important;
        }

        /* FILE UPLOADER & CAMERA RESTYLING */
        [data-testid='stFileUploader'] {
            background: var(--glass-bg);
            border: 2px dashed rgba(255,255,255,0.1);
            border-radius: 16px;
            padding: 20px;
            text-align: center;
        }
        
        [data-testid='stFileUploader']:hover {
            border-color: var(--primary);
            background: rgba(16, 185, 129, 0.05);
        }

        /* SCANNING ANIMATION LAYER */
        @keyframes scannerLine {
            0% { top: 0%; opacity: 0; }
            5% { opacity: 1; }
            95% { opacity: 1; }
            100% { top: 100%; opacity: 0; }
        }

        .scan-overlay {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: 20;
            border-radius: 20px;
            overflow: hidden;
            box-shadow: inset 0 0 50px rgba(0,0,0,0.5);
        }

        .scan-bar {
            width: 100%;
            height: 3px;
            background: #10b981;
            box-shadow: 0 0 15px #10b981, 0 0 30px #10b981;
            position: absolute;
            animation: scannerLine 3s linear infinite;
        }

        /* TABS RESTYLING */
        .stTabs [data-baseweb="tab-list"] {
            gap: 8px;
            background-color: transparent;
            padding: 10px 0;
        }

        .stTabs [data-baseweb="tab"] {
            background-color: rgba(255, 255, 255, 0.03);
            border-radius: 8px;
            color: #94a3b8;
            border: 1px solid transparent;
            padding: 8px 16px;
            transition: all 0.2s;
        }

        .stTabs [data-baseweb="tab"]:hover {
            background-color: rgba(16, 185, 129, 0.1);
            color: #fff;
        }

        .stTabs [aria-selected="true"] {
            background-color: #10b981 !important;
            color: #000 !important;
            font-weight: bold;
            box-shadow: 0 4px 15px rgba(16, 185, 129, 0.3);
        }
    </style>
    """, unsafe_allow_html=True)