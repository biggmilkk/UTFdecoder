import streamlit as st
import urllib.parse
import textwrap

st.set_page_config(page_title="UTF-8 URL Decoder", layout="centered")

# --- Title ---
st.markdown("<h2 style='text-align: center;'>UTF-8 URL Decoder</h2>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align: center; font-size: 0.9rem; color: grey;'>"
    "Paste a UTF-8 encoded URL below to decode it. No data is stored.</p>",
    unsafe_allow_html=True
)

# --- Input ---
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

            # --- Wrap decoded text to improve visual height in st.code ---
            wrapped = "\n".join(textwrap.wrap(decoded, width=200))

            st.markdown("#### Decoded URL")
            st.code(wrapped, language="text")  # ✅ Copy icon works

        except Exception:
            st.error("Invalid UTF-8 encoded string. Please check your input.")
    else:
        st.warning("Please enter a UTF-8 encoded string.")
