import streamlit as st
import urllib.parse
import hashlib
from urllib.parse import urlparse

# Version: v1.0.0

st.set_page_config(page_title="UTF-8 Decoder & URL Shortener", layout="centered")

# --- Title ---
st.markdown("<h2 style='text-align: center;'>UTF-8 Decoder & URL Shortener</h2>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align: center; font-size: 0.9rem; color: grey;'>Paste a UTF-8 encoded URL to decode it, or shorten a long URL using a simple hash-based shortener. Works entirely in-browser — nothing is stored permanently.</p>",
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
utf8_input = st.text_input("Encoded URL:", placeholder="Example: https%3A%2F%2Fexample.com%2Fsearch%3Fq%3Dtest")

if utf8_input:
    try:
        decoded_text = urllib.parse.unquote(utf8_input)
        st.success("Decoded Output")
        st.code(decoded_text, language="text")
    except Exception:
        st.error("Invalid UTF-8 encoded string. Please check your input.")

# --- Section: URL Shortener ---
st.markdown("#### URL Shortener")
url_input = st.text_input("Long URL to shorten:", placeholder="https://your-website.com/page")

if url_input:
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

# --- Footer ---
st.markdown(
    "<hr style='margin-top: 2rem;'>"
    "<p style='text-align: center; font-size: 0.75rem; color: grey;'>v1.0.0 · Developed by You · Built with Streamlit</p>",
    unsafe_allow_html=True
)
