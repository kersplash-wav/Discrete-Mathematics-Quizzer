#region Imports
import sys
import streamlit as st
import database as db
#endregion
# Setup #
st.set_page_config(
    layout="wide"
)
# Checks #
if "questions" not in st.session_state:
    st.session_state["questions"] = {}
    db.refresh_questions()
# Make Page #
pg = st.navigation(['pages/Home.py', 'pages/Credits.py'], position='top')
pg.run()

# Images used for logo
st.logo("images/discretemathiconwithtext.png", size='large', icon_image="images/discreteiconexpanded.png") # Sets the logo for the sidebar when opened or closed.