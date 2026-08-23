"""
Home page for Streamlit authentication interface.
"""

import logging

import streamlit as st

import uuid

# Hide sidebar for cleaner look
hide_sidebar_style = """
    <style>
        [data-testid="stSidebarNav"] {
            display: none;
        }
    </style>
"""
st.markdown(hide_sidebar_style, unsafe_allow_html=True)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="app.log",
    filemode="a",
)
logger = logging.getLogger(__name__)

st.set_page_config(page_title="LangGraph Chat - Login")

st.title("🔐 Welcome to LangGraph Assistant")

token = ""

# Step 1: Fetch API token only once per session
token = ""

# Step 1: Fetch API token only once per session
# Step 1: Initialize local session ID
if "session_id" not in st.session_state:
    st.session_state["session_id"] = str(uuid.uuid4())

# Step 2: Render login/signup form
with st.form("auth_form"):
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    submit = st.form_submit_button("Login")

# Step 3: Handle login/account creation
if submit:
    if not username or not password:
        st.error("Username and password required.")
    else:
        st.session_state["username"] = username
        st.session_state["jwt_token"] = st.session_state["session_id"]
        st.switch_page("pages/chat.py")
        
# Debug logs section
with st.expander("📜 Debug Logs"):
    try:
        with open("app.log", "r") as log_file:
            st.text(log_file.read())
    except FileNotFoundError:
        st.warning("Log file not found yet.")
