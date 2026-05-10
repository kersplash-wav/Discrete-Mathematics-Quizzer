#region Imports
import sys
import streamlit as st
import database as db
import random
#endregion
st.set_page_config(

)
# Main #
def main(argv: list[str]):
    
    # Images used for logo
    HORIZONTAL = "images/discretemathiconwithtext.png"
    ICON = "images/discreteiconexpanded.png"

    st.logo(HORIZONTAL, size='large', icon_image=ICON) # Sets the logo for the sidebar when opened or closed.
    
    st.title("Discrete Mathematics Quizzer")

    display_question()

def display_question():
    # Get Question #
    question_index, question = db.request_question()
    # Extract #
    topic = question['topic']
    question_text = question['question'](question_index)
    answer = question['answer'](question_index)
    # Display #
    st.header(topic)
    st.latex(question_text)
    inputted_answer = st.text_input("Answer", placeholder="Enter answer here")
    
    left, middle, right = st.columns(3)

    if left.button("Submit", width='stretch'): # When Submitted #
        if answer.lower() == inputted_answer.lower():
            st.markdown(f"{inputted_answer} is :green[correct!]")
        else:
            st.markdown(f"{inputted_answer} is :red[incorrect!]")

    if middle.button("Next Question", width='stretch'):
        questions = st.session_state["questions"]
        question_amount = len(questions)
        st.session_state['question_index'] = random.randint(1, question_amount)
        db.refresh_questions()
        st.rerun()

    if right.button("Reveal Answer", width='stretch'):
        st.markdown(f":blue[{answer.lower()} is the answer!]")
    # Display Difficulty #
    
    #match question['difficulty'].lower():
    #    case 'easy':
    #        st.badge("Easy", color="green")
    #    case 'medium':
    #        st.badge("Medium", color="yellow")
    #    case 'hard':
    #        st.badge("Hard", color="red")
    
    pass

# Init #
main(sys.argv)