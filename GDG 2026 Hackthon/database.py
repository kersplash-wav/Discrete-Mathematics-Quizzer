
import json
import random
import streamlit as st
from typing import Any

def request_question():
    questions = st.session_state["questions"]
    question_index = st.session_state["question_index"]

    question = questions[question_index]
    return (question_index, question)

def refresh_questions():
    st.session_state["questions"] = [
        {
            "topic": "Sets",
            "set": [random.randint(1, 9) for _ in range(random.randint(1, 10))],
            "question": lambda index: 
                f"\\text{{Let S be a set. What is the cardinality of S}} \\equiv {st.session_state["questions"][index]["set"]}",
            "answer": lambda index:
                str(len(set(st.session_state["questions"][index]["set"]))),
            "difficulty": "Easy"
        },
        {
            "topic": "Sets",
            "question": lambda index:
                f"\\text{{True or False: The empty set has no elements.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Sets",
            "question": lambda index:
                f"\\text{{True or False: The empty set has one element.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Easy"
        },
        {
            "topic": "Sets",
            "set": [random.randint(-3, 9) for _ in range(random.randint(1, 9))],
            "question": lambda index: 
                f"\\text{{Let S be a set. True or False: Is S finite? S}} \\equiv {st.session_state["questions"][index]["set"]}",
            "answer": lambda index:
               "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Sets",
            "set": [random.randint(-3, 9) for _ in range(random.randint(1, 9))],
            "question": lambda index: 
                f"\\text{{Let S be a set. True or False: Is S infinite? S}} \\equiv {st.session_state["questions"][index]["set"]}",
            "answer": lambda index:
               "False",
            "difficulty": "Easy"
        },
        {
            "topic": "Sets",
            "question": lambda index: 
                f"\\text{{Let S be a set of all whole numbers. True or False: Is S infinite?}}",
            "answer": lambda index:
               "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Sets",
            "question": lambda index: 
                f"\\text{{Let S be a set of all rational numbers. True or False: Is S infinite?}}",
            "answer": lambda index:
               "True",
            "difficulty": "Easy"
        },        
        {
            "topic": "Sets",
            "question": lambda index: 
                f"\\text{{Let S be a set of all irrational numbers. True or False: Is S infinite?}}",
            "answer": lambda index:
               "True",
            "difficulty": "Medium"
        },          
        {
            "topic": "Sets",
            "question": lambda index: 
                f"\\text{{Let S be a set of all integers. True or False: Is S infinite?}}",
            "answer": lambda index:
               "True",
            "difficulty": "Easy"
        },          
        {
            "topic": "Sets",
            "question": lambda index: 
                f"\\text{{Let S be a set of all real numbers. True or False: Is S infinite?}}",
            "answer": lambda index:
               "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Sets",
            "question": lambda index: 
                f"\\text{{Let S be a set of all natural numbers. True or False: Is S infinite?}}",
            "answer": lambda index:
               "True",
            "difficulty": "Easy"
        },       
        {
            "topic": "Sets",
            "question": lambda index: 
                f"\\text{{True or False: The cardinality of the empty set is zero.}}",
            "answer": lambda index:
               "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Sets",
            "question": lambda index: 
                f"\\text{{True or False: The cardinality of the empty set is one.}}",
            "answer": lambda index:
               "False",
            "difficulty": "Medium"
        },          
        {
            "topic": "Sets",
            "question": lambda index: 
                f"\\text{{True or False: The cardinality of the empty set is one.}}",
            "answer": lambda index:
               "False",
            "difficulty": "Medium"
        },                          
    ]

    question_amount = len(st.session_state["questions"])
    st.session_state['question_index'] = random.randint(1, question_amount)


if "questions" not in st.session_state:
    refresh_questions()