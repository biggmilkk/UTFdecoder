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

            # Display decoded text with copy button
            st.markdown(
                f"""
                <div style='word-wrap: break-word; white-space: pre-wrap; font-family: monospace; background-color: #f0f2f6; padding: 1rem; border-radius: 6px; text-align: left;'>{decoded_text}</div>
                <textarea id="decodedText" style="position: absolute; left: -9999px;">{decoded_text}</textarea>
                <div style='text-align: center; margin-top: 10px;'>
                    <button onclick="copyDecoded()" style='padding: 0.5rem 1.25rem; font-size: 0.85rem; border: none; background-color: #2563eb; color: white; border-radius: 6px; cursor: pointer;'>Copy to Clipboard</button>
                </div>
                <script>
                    function copyDecoded() {{
                        var text = document.getElementById("decodedText");
                        text.select();
                        document.execCommand("copy");
                    }}
                </script>
                """,
                unsafe_allow_html=True
            )

        except Exception:
            st.error("Invalid UTF-8 encoded string. Please check your input.")
    else:
        st.warning("Please enter a UTF-8 encoded string.")
