import streamlit as st
import urllib.parse

st.set_page_config(page_title="UTF-8 URL Decoder", layout="centered")

# --- Title ---
st.markdown("<h2 style='text-align: center;'>UTF-8 URL Decoder</h2>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align: center; font-size: 0.9rem; color: grey;'>"
    "Paste a UTF-8 encoded URL below to decode it. No data is stored.</p>",
    unsafe_allow_html=True
)

# --- Custom style to change code block to dark gray with white text ---
st.markdown("""
    <style>
    pre {
        background-color: #2e2e2e !important;  /* Dark gray background */
        color: #ffffff !important;             /* White text */
        border-radius: 6px;
        padding: 1rem;
        font-size: 0.95rem;
    }
    </style>
""", unsafe_allow_html=True)

# --- Input Form ---
with st.form("decode_form"):
    utf8_input = st.text_area(
        "Encoded URL:",
        placeholder="https%3A%2F%2Fexample.com%2Fsearch%3Fq%3Dtest",
        height=100
    )
    decode_clicked = st.form_submit_button("Decode", use_container_width=True)

# --- Output ---
if decode_clicked:
    if utf8_input.strip():
        try:
            decoded = urllib.parse.unquote(utf8_input)
            st.markdown("#### Decoded URL")
            st.code(decoded, language="text")
        except Exception:
            st.error("Invalid UTF-8 encoded string. Please check your input.")
    else:
        st.warning("Please enter a UTF-8 encoded string.")
