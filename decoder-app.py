import streamlit as st
import urllib.parse

st.set_page_config(page_title="UTF-8 Decoder", layout="centered")

# --- Title ---
st.markdown("<h2 style='text-align: center;'>UTF-8 URL Decoder</h2>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align: center; font-size: 0.9rem; color: grey;'>Paste a UTF-8 encoded URL below to decode it. Then click 'Prepare Copy' to copy the result manually.</p>",
    unsafe_allow_html=True
)

# --- Step 1: Decode Form ---
st.markdown("#### Step 1: Decode")

with st.form("decode_form"):
    utf8_input = st.text_area(
        "Encoded URL:",
        placeholder="https%3A%2F%2Fexample.com%2Fsearch%3Fq%3Dtest",
        height=100
    )
    decode_clicked = st.form_submit_button("Decode", use_container_width=True)

# --- Step 1 Result ---
if decode_clicked:
    if utf8_input.strip():
        try:
            decoded = urllib.parse.unquote(utf8_input)
            st.session_state["decoded_text"] = decoded
            st.success("✅ Decoded successfully! Proceed to Step 2.")
        except Exception:
            st.error("❌ Invalid UTF-8 encoded string. Please check your input.")
    else:
        st.warning("Please enter a UTF-8 encoded string.")

# --- Step 2: Copy Section ---
if "decoded_text" in st.session_state:
    st.markdown("#### Step 2: Copy Decoded URL")

    if st.button("Prepare Copy", use_container_width=True):
        # You could do formatting or re-processing here
        st.session_state["ready_to_copy"] = st.session_state["decoded_text"]

    if "ready_to_copy" in st.session_state:
        st.text_area(
            "Decoded Output (ready to copy):",
            value=st.session_state["ready_to_copy"],
            height=150,
            disabled=True
        )
        st.caption("📋 Click inside the box and press Ctrl+C (or Cmd+C on Mac) to copy.")
