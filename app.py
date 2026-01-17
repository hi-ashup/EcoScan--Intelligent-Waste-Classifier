import streamlit as st
from PIL import Image
from src.styles import load_css
from src.ai_engine import analyze_waste
from src.utils import text_to_speech, display_glass_metric

# 1. Page Config
st.set_page_config(
    page_title="EcoScan AI",
    page_icon="♻️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. Load Styles
load_css()

# 3. Session State Management
if 'analysis' not in st.session_state:
    st.session_state.analysis = None
if 'scanned_img' not in st.session_state:
    st.session_state.scanned_img = None

# 4. Header
st.markdown("<h1 style='text-align: center; color: #fff;'>Eco<span style='color: #10b981'>Scan</span></h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #94a3b8; margin-bottom: 30px;'>INTELLIGENT WASTE CLASSIFICATION SYSTEM</p>", unsafe_allow_html=True)

# 5. Input Section (Homepage)
if st.session_state.analysis is None:
    # Custom Tabs for Input Method
    tab_cam, tab_up = st.tabs(["📸 Camera Scan", "📂 File Upload"])
    
    img_input = None
    
    with tab_cam:
        cam_img = st.camera_input("Point camera at waste item")
        if cam_img: img_input = cam_img

    with tab_up:
        up_img = st.file_uploader("Upload waste image", type=['jpg', 'png', 'jpeg'])
        if up_img: img_input = up_img

    # Processing Logic
    if img_input:
        st.session_state.scanned_img = Image.open(img_input)
        
        # Display Scanning Animation
        if img_input:
        st.session_state.scanned_img = Image.open(img_input)

        # Creates a unified glass card for the preview
        st.markdown('<div class="glass-container">', unsafe_allow_html=True)
        st.image(st.session_state.scanned_img, use_container_width=True)
        # We simulate the scanner overlay just below visually (limit of Python UI)
        st.markdown('<div class="scan-bar"></div></div>', unsafe_allow_html=True)
        
        if st.button("CLASSIFY OBJECT"):
            with st.spinner("Accessing Neural Database..."):
                result = analyze_waste(st.session_state.scanned_img)
                if "error" in result:
                    st.error("Identification Failed. Please try again.")
                else:
                    st.session_state.analysis = result
                    st.rerun()

# 6. Results Dashboard
else:
    data = st.session_state.analysis
    
    # Show Thumbnail of scanned item
    col_l, col_r = st.columns([1, 3])
    with col_l:
        st.image(st.session_state.scanned_img, width=100, use_column_width=True)
    with col_r:
        st.markdown(f"### Identified: {data['item_name']}")
        st.caption(f"Confidence: {data.get('confidence', 'N/A')}")

    # Tabs for detailed info
    tab1, tab2, tab3, tab4 = st.tabs(["🔍 ID & Bin", "📝 Instructions", "🌿 Sustainability", "💡 Upcycling"])

    # --- TAB 1: Identification ---
    with tab1:
        c1, c2 = st.columns(2)
        with c1:
            display_glass_metric("Category", data['category'], "📦")
        with c2:
            # Dynamic color for bin text
            bin_color = data['bin_color'].split()[0].lower()
            color_map = {'green': '#4ade80', 'blue': '#60a5fa', 'red': '#f87171', 'yellow': '#facc15', 'black': '#94a3b8'}
            txt_color = color_map.get(bin_color, '#fff')
            
            st.markdown(f"""
            <div class="glass-card" style="border: 1px solid {txt_color};">
                <h4 style="margin:0; color: #94a3b8; font-size: 0.8rem;">DISPOSAL BIN</h4>
                <h2 style="margin:0; color: {txt_color}; font-size: 1.8rem;">{data['bin_color']}</h2>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("**Material Profile:**")
        st.info(data['material_breakdown'])

    # --- TAB 2: Instructions ---
    with tab2:
        st.subheader("Disposal Protocol")
        
        # Audio Button
        if st.button("🔊 Read Instructions"):
            full_text = f"To dispose of {data['item_name']}. " + ". ".join(data['disposal_steps'])
            text_to_speech(full_text)

        for i, step in enumerate(data['disposal_steps']):
            st.markdown(f"""
            <div style="display:flex; align-items:center; gap:15px; margin-bottom:10px; background:rgba(255,255,255,0.03); padding:10px; border-radius:10px;">
                <div style="background:#10b981; color:black; width:25px; height:25px; border-radius:50%; display:flex; align-items:center; justify-content:center; font-weight:bold;">{i+1}</div>
                <div>{step}</div>
            </div>
            """, unsafe_allow_html=True)

    # --- TAB 3: Sustainability (3Rs) ---
    with tab3:
        st.markdown("<h3 style='color:#10b981'>The 3Rs Strategy</h3>", unsafe_allow_html=True)
        
        tips = data['sustainability_tips']
        
        st.markdown("**📉 Reduce**")
        st.success(tips.get('reduce', 'N/A'))
        
        st.markdown("**🔄 Reuse**")
        st.warning(tips.get('reuse', 'N/A'))
        
        st.markdown("**♻️ Recycle**")
        st.info(tips.get('recycle', 'N/A'))

        st.markdown("---")
        st.caption(f"**Eco Impact:** {data['environmental_impact']}")

    # --- TAB 4: Upcycling ---
    with tab4:
        st.subheader("Creative Lab")
        for idea in data['upcyclingIdeas']:
            st.markdown(f"""
            <div class="glass-card">
                <h4 style="color: #facc15; margin:0;">💡 Idea</h4>
                <p style="margin-top:5px;">{idea}</p>
            </div>
            """, unsafe_allow_html=True)

    # Reset Button
    st.markdown("---")
    if st.button("Scan New Item"):
        st.session_state.analysis = None
        st.session_state.scanned_img = None
        st.rerun()