import streamlit as st
import urllib.parse
import json  # to safely escape text for JavaScript

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

            # Show wrapped decoded text
            st.text_area("Decoded (wrapped):", value=decoded_text, height=100, disabled=True)

            # Safely inject decoded text into JS using json.dumps to escape
            escaped_text = json.dumps(decoded_text)

            st.markdown(
                f"""
                <div style="text-align: center; margin-top: 10px;">
                    <button onclick='copyToClipboard()' style="
                        padding: 0.5rem 1.25rem;
                        font-size: 0.85rem;
                        border: none;
                        background-color: #2563eb;
                        color: white;
                        border-radius: 6px;
                        cursor: pointer;
                    ">Copy to Clipboard</button>
                </div>
                <p id="copied-msg" style="text-align: center; color: green; font-size: 0.85rem; display: none; margin-top: 5px;">
                    ✅ Copied!
                </p>
                <script>
                    function copyToClipboard() {{
                        const text = {escaped_text};
                        navigator.clipboard.writeText(text).then(function() {{
                            const msg = document.getElementById("copied-msg");
                            msg.style.display = "block";
                            setTimeout(() => {{
                                msg.style.display = "none";
                            }}, 2000);
                        }});
                    }}
                </script>
                """,
                unsafe_allow_html=True
            )

        except Exception:
            st.error("Invalid UTF-8 encoded string. Please check your input.")
    else:
        st.warning("Please enter a UTF-8 encoded string.")
