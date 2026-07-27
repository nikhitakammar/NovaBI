import streamlit as st
from dotenv import load_dotenv

from modules.chat import show_chat
from modules.dashboard import show_dashboard
from modules.leadership import show_leadership

# -------------------------------
# Load Environment Variables
# -------------------------------
load_dotenv()

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="NovaBI",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------------
# Load Custom CSS
# -------------------------------
def load_css():
    with open("static/styles.css") as css:
        st.markdown(
            f"<style>{css.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

# -------------------------------
# Session State
# -------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -------------------------------
# Header
# -------------------------------
st.title("🚀 NovaBI")
st.caption("AI Business Intelligence Assistant")

# -------------------------------
# Sidebar
# -------------------------------
st.sidebar.title("🚀 NovaBI")
st.sidebar.markdown("---")

option = st.sidebar.radio(
    "Navigation",
    [
        "💬 Chat",
        "📊 Dashboard",
        "📈 Leadership Update"
    ]
)

st.sidebar.markdown("---")
st.sidebar.caption("Version 1.0")

# -------------------------------
# Navigation
# -------------------------------
if option == "💬 Chat":
    show_chat()

elif option == "📊 Dashboard":
    show_dashboard()

elif option == "📈 Leadership Update":
    show_leadership()