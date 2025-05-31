import streamlit as st
import urllib.parse
import textwrap

# --- Page Config ---
st.set_page_config(page_title="UTF-8 URL Decoder", layout="centered")

# --- Title and Description ---
st.markdown("<h2 style='text-align: center;'>UTF-8 URL Decoder</h2>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align: center; font-size: 0.9rem; color: grey;'>"
    "Paste a UTF-8 encoded URL below to decode it into human-readable format. "
    "This tool works entirely in-browser and does not store any data."
    "</p>",
    unsafe_allow_html=True
)

# --- Step 1: Input ---
st.markdown("#### Step 1: Paste Encoded URL")

with st.form("decode_form"):
    utf8_input = st.text_area(
        "Encoded URL:",
        placeholder="Example: https%3A%2F%2Fexample.com%2Fsearch%3Fq%3Dtest",
        height=100
    )
    decode_clicked = st.form_submit_button("Decode", use_container_width=True)

# --- Step 2: Output ---
if decode_clicked:
    if utf8_input.strip():
        try:
            decoded_text = urllib.parse.unquote(utf8_input)

            # Optional line wrapping to improve readability in `st.code()`
            wrapped = "\n".join(textwrap.wrap(decoded_text, width=80))

            st.success("✅ Decoded successfully!")

            st.markdown("#### Step 2: Decoded URL")
            st.code(wrapped, language="text")  # ✅ Built-in copy icon

            st.caption("📋 Click the copy icon in the top-right of the box to copy the decoded URL.")

        except Exception:
            st.error("❌ Invalid UTF-8 encoded string. Please check your input.")
    else:
        st.warning("⚠️ Please enter a UTF-8 encoded string.")
