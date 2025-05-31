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

            # Display decoded URL and setup clean copy logic
            st.markdown(
                f"""
                <div onclick="copyDecoded()" style="
                    cursor: pointer;
                    font-family: monospace;
                    background-color: #ffffff;
                    color: #000000;
                    padding: 1rem;
                    border-radius: 6px;
                    border: 2px solid #2563eb;
                    text-align: left;
                    transition: background-color 0.2s;
                    word-wrap: break-word;
                    white-space: pre-wrap;
                " title="Click to copy">
                    <pre style="margin: 0; white-space: pre-wrap;">{decoded_text}</pre>
                </div>

                <textarea id="hidden-copy-target" style="position: absolute; left: -9999px;">{decoded_text}</textarea>

                <div id="copied-msg" style="text-align: center; display: none; margin-top: 10px;">
                    <span style="color: green; font-weight: 500;">✅ Copied to clipboard!</span>
                </div>

                <script>
                function copyDecoded() {{
                    var copyTarget = document.getElementById("hidden-copy-target");
                    copyTarget.select();
                    document.execCommand("copy");

                    var msg = document.getElementById("copied-msg");
                    msg.style.display = "block";
                    setTimeout(function() {{
                        msg.style.display = "none";
                    }}, 2000);
                }}
                </script>
                """,
                unsafe_allow_html=True
            )

        except Exception:
            st.error("Invalid UTF-8 encoded string. Please check your input.")
    else:
        st.warning("Please enter a UTF-8 encoded string.")
