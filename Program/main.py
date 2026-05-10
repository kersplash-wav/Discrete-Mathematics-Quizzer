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
st.logo("https://github.com/kersplash-wav/Discrete-Mathematics-Quizzer/blob/main/Program/Images/discretemathiconwithtext.png?raw=true", size='large', icon_image="https://github.com/kersplash-wav/Discrete-Mathematics-Quizzer/blob/main/Program/Images/discreteiconexpanded.png?raw=true") # Sets the logo for the sidebar when opened or closed.
