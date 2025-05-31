import streamlit as st
import urllib.parse
import hashlib
from urllib.parse import urlparse

# Initialize session state for URL mapping
if 'url_mapping' not in st.session_state:
    st.session_state.url_mapping = {}

# Function to validate URLs
def is_valid_url(url):
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

# Streamlit UI
st.set_page_config(page_title="UTF-8 Decoder & URL Shortener", layout="centered")
st.title("🌐 UTF-8 Decoder & URL Shortener")

# --- UTF-8 Decoding Section ---
st.header("🔓 UTF-8 URL Decoder")
utf8_input = st.text_input("Enter UTF-8 encoded string to decode:")

if utf8_input:
    try:
        decoded_text = urllib.parse.unquote(utf8_input)
        st.success("Decoded Result:")
        st.code(decoded_text)
    except Exception:
        st.error("⚠️ Invalid UTF-8 encoded string. Please check your input.")

# --- URL Shortening Section ---
st.header("🔗 URL Shortener")
url_to_shorten = st.text_input("Enter a full URL to shorten (include http:// or https://):")

if url_to_shorten:
    if is_valid_url(url_to_shorten):
        short_hash = hashlib.md5(url_to_shorten.encode()).hexdigest()[:6]
        short_url = f"https://{st.runtime.scriptrunner.get_script_run_ctx().host}/?code={short_hash}"
        st.session_state.url_mapping[short_hash] = url_to_shorten
        st.success("Here is your shortened URL:")
        st.code(short_url)
    else:
        st.error("❌ Invalid URL. Please include http:// or https://")

# --- URL Redirect Simulation ---
st.header("🚀 Visit a Shortened URL")
code_input = st.text_input("Enter short code to retrieve original URL (e.g., abc123):")

if code_input:
    original_url = st.session_state.url_mapping.get(code_input)
    if original_url:
        st.info(f"✅ Original URL found:")
        st.markdown(f"[Click here to visit]({original_url})")
    else:
        st.error("❌ No URL found for this code.")
