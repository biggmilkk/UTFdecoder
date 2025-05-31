import streamlit as st
import urllib.parse
import hashlib
from urllib.parse import urlparse

st.set_page_config(page_title="UTF-8 Decoder & URL Shortener", layout="centered")

# --- Title ---
st.markdown("<h2 style='text-align: center;'>UTF-8 Decoder & URL Shortener</h2>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align: center; font-size: 0.9rem; color: grey;'>Paste a UTF-8 encoded URL to decode it, or shorten a long URL using a hash-based code. Nothing is saved — all processing happens in the browser session.</p>",
    unsafe_allow_html=True
)

# --- In-Memory Store ---
if "url_mapping" not in st.session_state:
    st.session_state.url_mapping = {}

# --- Helpers ---
def is_valid_url(url):
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

# --- Section: UTF-8 Decoder ---
st.markdown("#### UTF-8 URL Decoder")

with st.form(key="decode_form"):
    utf8_input = st.text_area(
        "Encoded URL:",
        placeholder="Example: https%3A%2F%2Fexample.com%2Fsearch%3Fq%3Dtest",
        height=100
    )
    decode_clicked = st.form_submit_button("Decode", use_container_width=True)

if decode_clicked:
    if utf8_input.strip():
        try:
            decoded_text = urllib.parse.unquote(utf8_input)
            st.success("Decoded Output")
            st.code(decoded_text, language="text")
        except Exception:
            st.error("Invalid UTF-8 encoded string. Please check your input.")
    else:
        st.warning("Please enter a UTF-8 encoded string.")

# --- Divider ---
st.markdown("<hr style='margin: 2rem 0;'>", unsafe_allow_html=True)

# --- Section: URL Shortener ---
st.markdown("#### URL Shortener")

with st.form(key="shorten_form"):
    url_input = st.text_input("Long URL to shorten:", placeholder="https://your-website.com/page")
    shorten_clicked = st.form_submit_button("Generate Code", use_container_width=True)

if shorten_clicked:
    if url_input.strip():
        if is_valid_url(url_input):
            short_hash = hashlib.md5(url_input.encode()).hexdigest()[:6]
            short_code = f"?code={short_hash}"
            st.session_state.url_mapping[short_hash] = url_input
            st.success("Shortened Code")
            st.code(short_code, language="text")
            st.markdown(
                "<p style='font-size: 0.85rem; color: grey;'>Append this code to your app's URL to simulate redirection.</p>",
                unsafe_allow_html=True
            )
        else:
            st.error("Invalid URL format. Please include http:// or https://")
    else:
        st.warning("Please enter a URL.")

# --- Divider ---
st.markdown("<hr style='margin: 2rem 0;'>", unsafe_allow_html=True)

# --- Section: Simulate Redirect ---
st.markdown("#### Simulate Short URL Access")
code_input = st.text_input("Enter short code (e.g. abc123):")

if code_input:
    original_url = st.session_state.url_mapping.get(code_input)
    if original_url:
        st.info("Match Found")
        st.markdown(f"[Click here to visit]({original_url})", unsafe_allow_html=True)
    else:
        st.error("No matching URL found for this code.")
