import streamlit as st
import urllib.parse
import hashlib
from urllib.parse import urlparse

# --- Page Config ---
st.set_page_config(page_title="UTF-8 Decoder & URL Shortener", layout="centered")

# --- Title & Description ---
st.markdown("<h2 style='text-align: center;'>UTF-8 Decoder & URL Shortener</h2>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align: center; font-size: 0.9rem; color: grey;'>Decode UTF-8 encoded strings and generate short, shareable links using a simple hash-based shortener.</p>",
    unsafe_allow_html=True
)

# --- Initialize URL Mapping ---
if "url_mapping" not in st.session_state:
    st.session_state.url_mapping = {}

# --- URL Validator ---
def is_valid_url(url):
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

# --- UTF-8 Decoder Section ---
st.markdown("### 🔓 UTF-8 URL Decoder")
utf8_input = st.text_input("Enter UTF-8 encoded string:")

if utf8_input:
    try:
        decoded_text = urllib.parse.unquote(utf8_input)
        st.success("Decoded Result")
        st.code(decoded_text, language="text")
    except Exception:
        st.error("⚠️ Invalid UTF-8 encoded string. Please check your input.")

# --- URL Shortener Section ---
st.markdown("### 🔗 URL Shortener")
url_to_shorten = st.text_input("Enter a full URL (include http:// or https://):")

if url_to_shorten:
    if is_valid_url(url_to_shorten):
        short_hash = hashlib.md5(url_to_shorten.encode()).hexdigest()[:6]
        base_url = st.secrets.get("base_url", "https://example.com")  # Optional for production
        short_url = f"?code={short_hash}"
        st.session_state.url_mapping[short_hash] = url_to_shorten
        st.success("Shortened URL")
        st.code(short_url, language="text")
        st.markdown(
            "<p style='font-size: 0.85rem; color: grey;'>Note: Copy and append the code to your app URL to simulate redirection.</p>",
            unsafe_allow_html=True
        )
    else:
        st.error("❌ Invalid URL. Please include http:// or https://")

# --- Redirect Simulation ---
st.markdown("### 🚀 Simulate Short URL Access")
code_input = st.text_input("Enter short code to retrieve original URL (e.g., abc123):")

if code_input:
    original_url = st.session_state.url_mapping.get(code_input)
    if original_url:
        st.info("✅ Original URL Found")
        st.markdown(f"[Click here to visit]({original_url})", unsafe_allow_html=True)
    else:
        st.error("❌ No URL found for this code.")

# --- Footer ---
st.markdown(
    "<hr style='margin-top: 2rem; margin-bottom: 0.5rem;'>"
    "<p style='text-align: center; font-size: 0.75rem; color: grey;'>v1.0.0 · Built with Streamlit · No data is stored permanently</p>",
    unsafe_allow_html=True
)
