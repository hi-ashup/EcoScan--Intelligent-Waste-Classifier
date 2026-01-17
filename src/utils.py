import streamlit as st

def text_to_speech(text):
    """
    Injects JavaScript to use the browser's native SpeechSynthesis API.
    This avoids installing heavy audio libraries on the server.
    """
    js_code = f"""
        <script>
            var msg = new SpeechSynthesisUtterance("{text}");
            window.speechSynthesis.cancel(); // Stop any previous
            window.speechSynthesis.speak(msg);
        </script>
    """
    st.components.v1.html(js_code, height=0)

def display_glass_metric(label, value, icon=""):
    st.markdown(f"""
    <div class="glass-card">
        <h4 style="margin:0; color: #94a3b8; font-size: 0.8rem; text-transform: uppercase;">{label}</h4>
        <h2 style="margin:0; color: #10b981; font-size: 1.8rem;">{icon} {value}</h2>
    </div>
    """, unsafe_allow_html=True)