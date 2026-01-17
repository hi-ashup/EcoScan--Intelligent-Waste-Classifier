import streamlit as st
from PIL import Image
from src.styles import load_css
from src.ai_engine import analyze_waste
from src.utils import text_to_speech, display_glass_metric

# 1. Page Config (Must be the first command)
st.set_page_config(
    page_title="EcoScan AI",
    page_icon="♻️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. Load the High-Fidelity Styles
load_css()

# 3. Session State Init
if 'analysis' not in st.session_state:
    st.session_state.analysis = None
if 'scanned_img' not in st.session_state:
    st.session_state.scanned_img = None

# 4. Top Header
st.markdown("""
<div style="text-align:center; padding: 20px 0;">
    <h1 style="margin:0;">Eco<span style="color:#10b981;">Scan</span></h1>
    <p style="color:#64748b; font-size: 0.9rem; letter-spacing: 2px;">NEURAL WASTE CLASSIFICATION PROTOCOL</p>
</div>
""", unsafe_allow_html=True)

# 5. INPUT VIEW
if st.session_state.analysis is None:
    
    # Custom Styled Tabs
    tab_cam, tab_up = st.tabs([" 📸 LIVE SENSOR ", " 📂 DATA UPLOAD "])
    
    img_input = None

    with tab_cam:
        cam_img = st.camera_input("Optical Feed Active", label_visibility="collapsed")
        if cam_img: img_input = cam_img

    with tab_up:
        up_img = st.file_uploader("Drop Biological/Synthetic Data", type=['jpg', 'png', 'jpeg'], label_visibility="collapsed")
        if up_img: img_input = up_img

    # Processing Logic (FIXED Indentation)
    if img_input:
        st.session_state.scanned_img = Image.open(img_input)

        # Scanning Preview Card
        st.markdown('<div class="glass-container">', unsafe_allow_html=True)
        st.image(st.session_state.scanned_img, use_container_width=True)
        # Visual FX
        st.markdown("""
            <div class="scan-bar"></div>
        </div>
        """, unsafe_allow_html=True)
        
        col_c, _ = st.columns([1, 0.1]) 
        with col_c:
            if st.button("RUN CLASSIFICATION ALGORITHM"):
                with st.spinner("QUANTUM CORE PROCESSING..."):
                    result = analyze_waste(st.session_state.scanned_img)
                    if "error" in result:
                        st.error("SYSTEM ERROR: Neural Link Failure. Retrying recommended.")
                    else:
                        st.session_state.analysis = result
                        st.rerun()

# 6. ANALYSIS VIEW
else:
    data = st.session_state.analysis
    
    # Hero Result Card
    st.markdown('<div class="glass-container" style="display: flex; gap: 20px; align-items: center;">', unsafe_allow_html=True)
    c1, c2 = st.columns([1, 2])
    with c1:
        st.image(st.session_state.scanned_img, use_container_width=True)
    with c2:
        st.markdown(f"<h2 style='color:#10b981; margin:0;'>{data.get('item_name', 'Unknown Item').upper()}</h2>", unsafe_allow_html=True)
        st.caption(f"DETECTED CATEGORY: {data.get('category', 'General').upper()}")
        st.caption(f"CONFIDENCE LEVEL: {data.get('confidence', '95%')}")
    st.markdown('</div>', unsafe_allow_html=True)

    # Detailed Module Tabs
    t1, t2, t3, t4 = st.tabs(["📦 CLASSIFY", "📜 PROTOCOL", "🌍 ECOLOGY", "💡 INNOVATE"])

    # --- CLASSIFY TAB ---
    with t1:
        st.markdown("### DISPOSAL DIRECTIVE")
        col_bin, col_mat = st.columns(2)
        
        with col_bin:
            bin_type = data.get('bin_color', 'Black')
            
            # Logic for color coding the bin result
            b_color = "#333"
            if "green" in bin_type.lower(): b_color = "#10b981"
            elif "blue" in bin_type.lower(): b_color = "#3b82f6"
            elif "yellow" in bin_type.lower(): b_color = "#facc15"
            elif "red" in bin_type.lower(): b_color = "#ef4444"

            st.markdown(f"""
            <div class="glass-container" style="text-align:center; border: 1px solid {b_color};">
                <p style="color: #94a3b8; font-size: 10px; font-weight: bold; letter-spacing: 1px;">RECOMMENDED BIN</p>
                <h1 style="color: {b_color}; font-size: 32px; margin: 0;">{bin_type}</h1>
            </div>
            """, unsafe_allow_html=True)

        with col_mat:
            st.markdown("""
            <div class="glass-container">
                 <p style="color: #94a3b8; font-size: 10px; font-weight: bold; letter-spacing: 1px;">MATERIAL COMPOSITION</p>
            </div>
            """, unsafe_allow_html=True)
            st.info(data.get('material_breakdown', 'N/A'))

    # --- INSTRUCTION TAB ---
    with t2:
        st.markdown("### OPERATIONAL STEPS")
        steps = data.get('disposal_steps', [])
        
        # Audio
        if st.button("▶ INITIALIZE AUDIO BRIEFING"):
            full_audio = f"System identified {data.get('item_name')}. To dispose correctly: " + " ".join(steps)
            text_to_speech(full_audio)

        for i, step in enumerate(steps):
             st.markdown(f"""
             <div style="margin-bottom: 12px; background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.05); padding: 16px; border-radius: 12px; display: flex; align-items: start; gap: 12px;">
                <span style="color: #10b981; font-weight: bold;">0{i+1}</span>
                <span style="color: #cbd5e1;">{step}</span>
             </div>
             """, unsafe_allow_html=True)

    # --- ECO TAB ---
    with t3:
        tips = data.get('sustainability_tips', {})
        st.markdown(f"""
        <div class="glass-container" style="border-left: 4px solid #f59e0b;">
            <h4 style="color: #f59e0b; margin: 0 0 10px 0;">ECO IMPACT</h4>
            <p style="font-size: 0.9rem; color: #cbd5e1;">{data.get('environmental_impact', 'Unknown impact.')}</p>
        </div>
        """, unsafe_allow_html=True)
        
        c_red, c_reuse = st.columns(2)
        with c_red:
             st.markdown("**REDUCE**")
             st.caption(tips.get('reduce', 'N/A'))
        with c_reuse:
             st.markdown("**REUSE**")
             st.caption(tips.get('reuse', 'N/A'))

    # --- INNOVATION TAB ---
    with t4:
        ideas = data.get('upcycling_ideas', [])
        for idea in ideas:
            st.markdown(f"""
             <div class="glass-container" style="padding: 20px;">
                <span style="color: #10b981;">✦ CONCEPT:</span> 
                <span style="color: #e2e8f0;">{idea}</span>
             </div>
             """, unsafe_allow_html=True)

    st.markdown("<div style='height: 40px;'></div>", unsafe_allow_html=True)
    if st.button("RESET SYSTEM / NEW SCAN"):
        st.session_state.analysis = None
        st.rerun()