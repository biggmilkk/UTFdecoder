import streamlit as st
import urllib.parse

st.set_page_config(page_title="UTF-8 Decoder", layout="centered")

# --- Title ---
st.markdown("<h2 style='text-align: center;'>UTF-8 URL Decoder</h2>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align: center; font-size: 0.9rem; color: grey;'>Paste a UTF-8 encoded URL below to decode it. This app works entirely in-browser and stores no data.</p>",
    unsafe_allow_html=True
)

# --- Decode Form ---
st.markdown("#### Input")

with st.form(key="decode_form"):
    utf8_input = st.text_area(
        "Encoded URL:",
        placeholder="Example: https%3A%2F%2Fexample.com%2Fsearch%3Fq%3Dtest",
        height=100
    )
    decode_clicked = st.form_submit_button("Decode", use_container_width=True)

# --- Result ---
if decode_clicked:
    if utf8_input.strip():
        try:
            decoded_text = urllib.parse.unquote(utf8_input)
            st.success("Decoded URL")

            # Show wrapped decoded URL in readable area
            st.text_area("Decoded (wrapped):", value=decoded_text, height=100, disabled=True)

            # Inject the code block and fully hide its contents, but keep the copy icon
            st.markdown(
                f"""
                <style>
                .hidden-code-block pre,
                .hidden-code-block code {{
                    visibility: hidden;
                    max-height: 0;
                    padding: 0;
                    margin: 0;
                }}
                </style>
                <div class="hidden-code-block">
                """,
                unsafe_allow_html=True
            )
            st.code(decoded_text, language="text")
            st.markdown("</div>", unsafe_allow_html=True)

            st.caption("✅ Click the copy icon above to copy the decoded URL.")
        except Exception:
            st.error("Invalid UTF-8 encoded string. Please check your input.")
    else:
        st.warning("Please enter a UTF-8 encoded string.")
