import streamlit as st
import urllib.parse
import textwrap

st.set_page_config(page_title="UTF-8 Decoder", layout="centered")

# --- Title ---
st.markdown("<h2 style='text-align: center;'>UTF-8 URL Decoder</h2>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align: center; font-size: 0.9rem; color: grey;'>Paste a UTF-8 encoded URL below to decode it. This app uses Streamlit’s built-in copy button for convenience.</p>",
    unsafe_allow_html=True
)

# --- Input ---
st.markdown("#### Input")

with st.form("decode_form"):
    utf8_input = st.text_area(
        "Encoded URL:",
        placeholder="Example: https%3A%2F%2Fexample.com%2Fsearch%3Fq%3Dtest",
        height=100
    )
    decode_clicked = st.form_submit_button("Decode", use_container_width=True)

# --- Output ---
if decode_clicked:
    if utf8_input.strip():
        try:
            decoded_text = urllib.parse.unquote(utf8_input)

            # Manually wrap the decoded text to 80 characters per line
            wrapped = "\n".join(textwrap.wrap(decoded_text, width=80))

            st.success("Decoded URL")
            st.code(wrapped, language="text")

        except Exception:
            st.error("Invalid UTF-8 encoded string. Please check your input.")
    else:
        st.warning("Please enter a UTF-8 encoded string.")
