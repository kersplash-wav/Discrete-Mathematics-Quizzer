import streamlit as st
import database as db
import random
import sys;
# Main #
def main(argv: list[str]):
    st.title("Discrete Mathematics Quizzer")
    filter_options()
    display_question()

def filter_options():
    left, right = st.columns(2)
    st.session_state["difficulty_filter"] = [difficulty.lower() for difficulty in left.multiselect("Difficulty", ['Easy', 'Medium', 'Hard'])]
    st.session_state["topic_filter"] = [topic.lower() for topic in right.multiselect("Topic", ['Set Theory', 'Logic', 'Probability', 'Trees', "Coloring", "Planar Graphs"])]
    pass

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
    # Buttons #
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
    
main(sys.argv)