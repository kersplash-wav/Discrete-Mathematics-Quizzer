
import json
import random
import streamlit as st

def request_question():
    questions = st.session_state["questions"]
    question_index = st.session_state["question_index"]
    question = questions[question_index]

    return question_index, question

def refresh_questions():
    questions = [
        #region Set Theory
        {
            "topic": "Set Theory",
            "set": [random.randint(1, 9) for _ in range(random.randint(1, 10))],
            "question": lambda index: 
                f"\\text{{Let S be a set. What is the cardinality of S}} \\equiv {st.session_state["questions"][index]["set"]}",
            "answer": lambda index:
                str(len(set(st.session_state["questions"][index]["set"]))),
            "difficulty": "Easy"
        },
        {
            "topic": "Set Theory",
            "question": lambda index:
                f"\\text{{True or False: The empty set has no elements.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Set Theory",
            "question": lambda index:
                f"\\text{{True or False: The empty set has one element.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Easy"
        },
        {
            "topic": "Set Theory",
            "set": [random.randint(-3, 9) for _ in range(random.randint(1, 9))],
            "question": lambda index: 
                f"\\text{{Let S be a set. True or False: Is S finite? S}} \\equiv {st.session_state["questions"][index]["set"]}",
            "answer": lambda index:
               "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Set Theory",
            "set": [random.randint(-3, 9) for _ in range(random.randint(1, 9))],
            "question": lambda index: 
                f"\\text{{Let S be a set. True or False: Is S infinite? S}} \\equiv {st.session_state["questions"][index]["set"]}",
            "answer": lambda index:
               "False",
            "difficulty": "Easy"
        },
        {
            "topic": "Set Theory",
            "question": lambda index: 
                f"\\text{{Let S be a set of all whole numbers. True or False: Is S infinite?}}",
            "answer": lambda index:
               "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Set Theory",
            "question": lambda index: 
                f"\\text{{Let S be a set of all rational numbers. True or False: Is S infinite?}}",
            "answer": lambda index:
               "True",
            "difficulty": "Easy"
        },        
        {
            "topic": "Set Theory",
            "question": lambda index: 
                f"\\text{{Let S be a set of all irrational numbers. True or False: Is S infinite?}}",
            "answer": lambda index:
               "True",
            "difficulty": "Medium"
        },          
        {
            "topic": "Set Theory",
            "question": lambda index: 
                f"\\text{{Let S be a set of all integers. True or False: Is S infinite?}}",
            "answer": lambda index:
               "True",
            "difficulty": "Easy"
        },          
        {
            "topic": "Set Theory",
            "question": lambda index: 
                f"\\text{{Let S be a set of all real numbers. True or False: Is S infinite?}}",
            "answer": lambda index:
               "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Set Theory",
            "question": lambda index: 
                f"\\text{{Let S be a set of all natural numbers. True or False: Is S infinite?}}",
            "answer": lambda index:
               "True",
            "difficulty": "Easy"
        },       
        {
            "topic": "Set Theory",
            "question": lambda index: 
                f"\\text{{True or False: The cardinality of the empty set is zero.}}",
            "answer": lambda index:
               "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Set Theory",
            "question": lambda index: 
                f"\\text{{True or False: The cardinality of the empty set is one.}}",
            "answer": lambda index:
               "False",
            "difficulty": "Medium"
        },          
        {
            "topic": "Set Theory",
            "question": lambda index: 
                f"\\text{{True or False: The cardinality of the empty set is one.}}",
            "answer": lambda index:
               "False",
            "difficulty": "Medium"
        },

        {
            "topic": "Set Theory",
            "question": lambda index: 
                "\\text{Let set S} \\equiv \\{1,\\{1\\},\\{1,\\{1\\}\\}\\}. \\text{ What is the cardinality of set S?}",
            "answer": lambda index:
               "3",
            "difficulty": "Medium"
        },
        #endregion
        #region Logic
        {
            "topic": "Logic",
            "set": [random.randint(0, 1) == 1 for _ in range(3)],
            "question": lambda index:
                f"""\\text{{Let the set S}} \\equiv 
                {st.session_state["questions"][index]["set"][0]} \\cup {st.session_state["questions"][index]["set"][1]} \\cap {st.session_state["questions"][index]["set"][2]}.
                \\space\\text{{Is the set S equivalent to True or False?}}""",
            "answer": lambda index:
                str(st.session_state["questions"][index]["set"][0] or st.session_state["questions"][index]["set"][1] and st.session_state["questions"][index]["set"][2]),
            "difficulty": "Easy"
        },
        #endregion
        #region Probability
        {
           "topic": "Probability",
            "question": lambda index: 
                f"\\text{{True or False: An experiment is a procedure that yields one of given set of possible outcomes.}}",
            "answer": lambda index:
               "True",
            "difficulty": "Medium"
        },
        {
           "topic": "Probability",
            "question": lambda index: 
                f"\\text{{True or False: An experiment is the set of all possible outcomes.}}",
            "answer": lambda index:
               "False",
            "difficulty": "Medium"
        },  
        {
           "topic": "Probability",
            "question": lambda index: 
                f"\\text{{True or False: A sample space is a procedure that yields one of given set of possible outcomes.}}",
            "answer": lambda index:
               "False",
            "difficulty": "Medium"
        },
        {
           "topic": "Probability",
            "question": lambda index: 
                f"\\text{{True or False: A sample space is the set of all possible outcomes.}}",
            "answer": lambda index:
               "True",
            "difficulty": "Medium"
        }, 
        {
           "topic": "Probability",
            "question": lambda index: 
                f"\\text{{True or False: An event is a subset of the sample space.}}",
            "answer": lambda index:
               "True",
            "difficulty": "Medium"
        },
        {
        "topic": "Probability",
            "question": lambda index: 
                f"\\text{{True or False: A sample space is a subset of an event.}}",
            "answer": lambda index:
               "False",
            "difficulty": "Medium"
        },
        {
        "topic": "Probability",
            "question": lambda index: 
                f"\\text{{True or False: Equal chance probability is determined by the formula |E|/|S|.}}",
            "answer": lambda index:
               "True",
            "difficulty": "Easy"
        },
        {
        "topic": "Probability",
            "question": lambda index: 
                f"\\text{{True or False: Equal chance probability is determined by the formula |S|/|E|.}}",
            "answer": lambda index:
               "False",
            "difficulty": "Easy"
        },
        {
        "topic": "Probability",
            "question": lambda index: 
                f"\\text{{True or False: Complement probability is equal to 1 - p(E).}}",
            "answer": lambda index:
               "True",
            "difficulty": "Easy"
        },
        {
         "topic": "Probability",
            "question": lambda index: 
                f"\\text{{True or False: Complement probability is not equal to 1 - p(E).}}",
            "answer": lambda index:
               "False",
            "difficulty": "Easy"
        },
        {
         "topic": "Probability",
            "question": lambda index: 
                f"\\text{{True or False: Uniform distribution is when each element has a 1/n chance of occurring.}}",
            "answer": lambda index:
               "True",
            "difficulty": "Easy"
        },
        {
         "topic": "Probability",
            "question": lambda index: 
                f"\\text{{True or False: Uniform distribution is when each element has a 1/2^n chance of occurring.}}",
            "answer": lambda index:
               "False",
            "difficulty": "Easy"
        },
        {
            "topic": "Probability",
            "question": lambda index:
                f"\\text{{True or False: The probability of any event E must satisfy 0 ≤ p(E) ≤ 1.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Probability",
            "question": lambda index:
                f"\\text{{True or False: The probability of the sample space S is equal to 0.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Easy"
        },
        {
            "topic": "Probability",
            "question": lambda index:
                f"\\text{{True or False: The probability of the empty set ∅ is equal to 0.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Probability",
            "question": lambda index:
                f"\\text{{True or False: Two events are mutually exclusive if they can both occur at the same time.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },
        {
            "topic": "Probability",
            "question": lambda index:
                f"\\text{{True or False: Two events are mutually exclusive if their intersection is the empty set.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Probability",
            "question": lambda index:
                f"\\text{{True or False: If E and F are mutually exclusive, then p(E ∪ F) = p(E) + p(F).}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Probability",
            "question": lambda index:
                f"\\text{{True or False: For any two events E and F, p(E ∪ F) = p(E) + p(F) - p(E ∩ F).}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Probability",
            "question": lambda index:
                f"\\text{{True or False: For any two events E and F, p(E ∪ F) = p(E) + p(F) + p(E ∩ F).}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },

        # --- Conditional Probability ---
        {
            "topic": "Probability",
            "question": lambda index:
                f"\\text{{True or False: The conditional probability of E given F is defined as p(E|F) = p(E ∩ F) / p(F).}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Probability",
            "question": lambda index:
                f"\\text{{True or False: The conditional probability of E given F is defined as p(E|F) = p(E ∩ F) / p(E).}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },
        {
            "topic": "Probability",
            "question": lambda index:
                f"\\text{{True or False: p(E|F) is only defined when p(F) > 0.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Probability",
            "question": lambda index:
                f"\\text{{True or False: In general, p(E|F) = p(F|E).}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },
        {
            "topic": "Probability",
            "question": lambda index:
                f"\\text{{True or False: Bayes' theorem states that p(F|E) = p(E|F) · p(F) / p(E).}}",
            "answer": lambda index:
                "True",
            "difficulty": "Hard"
        },
        {
            "topic": "Probability",
            "question": lambda index:
                f"\\text{{True or False: Bayes' theorem states that p(F|E) = p(E|F) · p(E) / p(F).}}",
            "answer": lambda index:
                "False",
            "difficulty": "Hard"
        },

        # --- Independence ---
        {
            "topic": "Probability",
            "question": lambda index:
                f"\\text{{True or False: Two events E and F are independent if p(E ∩ F) = p(E) · p(F).}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Probability",
            "question": lambda index:
                f"\\text{{True or False: Two events E and F are independent if p(E ∩ F) = p(E) + p(F).}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },
        {
            "topic": "Probability",
            "question": lambda index:
                f"\\text{{True or False: If E and F are independent, then p(E|F) = p(E).}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Probability",
            "question": lambda index:
                f"\\text{{True or False: If E and F are independent, then p(E|F) = p(F).}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },
        {
            "topic": "Probability",
            "question": lambda index:
                f"\\text{{True or False: Mutually exclusive events with nonzero probability are always independent.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Hard"
        },
        {
            "topic": "Probability",
            "question": lambda index:
                f"\\text{{True or False: If E and F are independent, then their complements E' and F' are also independent.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Hard"
        },
        {
            "topic": "Probability",
            "question": lambda index:
                f"\\text{{True or False: Events E₁, E₂, ..., Eₙ are pairwise independent if every pair of events is independent.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Hard"
        },
        {
            "topic": "Probability",
            "question": lambda index:
                f"\\text{{True or False: Pairwise independence of events implies mutual independence.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Hard"
        },

        # --- Bernoulli Trials ---
        {
            "topic": "Probability",
            "question": lambda index:
                f"\\text{{True or False: A Bernoulli trial is an experiment with exactly two possible outcomes: success and failure.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Probability",
            "question": lambda index:
                f"\\text{{True or False: A Bernoulli trial is an experiment with any number of possible outcomes.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Easy"
        },
        {
            "topic": "Probability",
            "question": lambda index:
                f"\\text{{True or False: In a sequence of Bernoulli trials, each trial is independent of the others.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Probability",
            "question": lambda index:
                f"\\text{{True or False: In a sequence of Bernoulli trials, the probability of success can change between trials.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Easy"
        },
        {
            "topic": "Probability",
            "question": lambda index:
                f"\\text{{True or False: The probability of exactly k successes in n Bernoulli trials is C(n,k) · pᵏ · (1-p)ⁿ⁻ᵏ.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Probability",
            "question": lambda index:
                f"\\text{{True or False: The probability of exactly k successes in n Bernoulli trials is C(n,k) · pⁿ⁻ᵏ · (1-p)ᵏ.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },
        {
            "topic": "Probability",
            "question": lambda index:
                f"\\text{{True or False: If p is the probability of success in a Bernoulli trial, then the probability of failure is 1 - p.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Probability",
            "question": lambda index:
                f"\\text{{True or False: The binomial distribution gives the probability of k successes in n independent Bernoulli trials.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Probability",
            "question": lambda index:
                f"\\text{{True or False: The binomial distribution gives the probability of k successes in n dependent Bernoulli trials.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },

        #endregion
        #region Trees

        # --- Definitions & Forest ---
        {
            "topic": "Trees",
            "question": lambda index:
                f"\\text{{True or False: A tree is a connected undirected graph with no simple circuits.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Trees",
            "question": lambda index:
                f"\\text{{True or False: A tree is a connected undirected graph that may contain simple circuits.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Easy"
        },
        {
            "topic": "Trees",
            "question": lambda index:
                f"\\text{{True or False: A forest is an undirected graph with no simple circuits that may be disconnected.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Trees",
            "question": lambda index:
                f"\\text{{True or False: Every tree is a forest.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Trees",
            "question": lambda index:
                f"\\text{{True or False: Every forest is a tree.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Easy"
        },
        {
            "topic": "Trees",
            "question": lambda index:
                f"\\text{{True or False: Each connected component of a forest is a tree.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Trees",
            "question": lambda index:
                f"\\text{{True or False: A tree with n vertices has exactly n - 1 edges.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Trees",
            "question": lambda index:
                f"\\text{{True or False: A tree with n vertices has exactly n + 1 edges.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },
        {
            "topic": "Trees",
            "question": lambda index:
                f"\\text{{True or False: Adding any edge to a tree creates a simple circuit.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Trees",
            "question": lambda index:
                f"\\text{{True or False: There is a unique simple path between every pair of vertices in a tree.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Trees",
            "question": lambda index:
                f"\\text{{True or False: There may be multiple simple paths between two vertices in a tree.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },

        # --- Rooted vs Free Trees ---
        {
            "topic": "Trees",
            "question": lambda index:
                f"\\text{{True or False: A rooted tree is a tree in which one vertex is designated as the root.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Trees",
            "question": lambda index:
                f"\\text{{True or False: A free tree has a designated root vertex.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Easy"
        },
        {
            "topic": "Trees",
            "question": lambda index:
                f"\\text{{True or False: In a rooted tree, every edge is directed away from the root.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Trees",
            "question": lambda index:
                f"\\text{{True or False: A free tree and a rooted tree are structurally identical concepts.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Easy"
        },

        # --- Parent, Child, Siblings ---
        {
            "topic": "Trees",
            "question": lambda index:
                f"\\text{{True or False: In a rooted tree, the parent of a vertex v is the first vertex on the path from v to the root.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Trees",
            "question": lambda index:
                f"\\text{{True or False: The root of a tree has a parent vertex.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Easy"
        },
        {
            "topic": "Trees",
            "question": lambda index:
                f"\\text{{True or False: Vertices that share the same parent are called siblings.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Trees",
            "question": lambda index:
                f"\\text{{True or False: A child of vertex v is any vertex for which v is the parent.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Trees",
            "question": lambda index:
                f"\\text{{True or False: A vertex can have at most one parent in a rooted tree.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Trees",
            "question": lambda index:
                f"\\text{{True or False: A vertex can have multiple parents in a rooted tree.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Easy"
        },

        # --- Ancestors & Descendants ---
        {
            "topic": "Trees",
            "question": lambda index:
                f"\\text{{True or False: The ancestors of a vertex v are all vertices on the path from v to the root, excluding v itself.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Trees",
            "question": lambda index:
                f"\\text{{True or False: The descendants of a vertex v are all vertices for which v is an ancestor.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Trees",
            "question": lambda index:
                f"\\text{{True or False: The root has no ancestors.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Trees",
            "question": lambda index:
                f"\\text{{True or False: A vertex can be its own ancestor.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },

        # --- Leaves & Internal Vertices ---
        {
            "topic": "Trees",
            "question": lambda index:
                f"\\text{{True or False: A leaf is a vertex with no children.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Trees",
            "question": lambda index:
                f"\\text{{True or False: A leaf is a vertex with no parent.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Easy"
        },
        {
            "topic": "Trees",
            "question": lambda index:
                f"\\text{{True or False: An internal vertex is a vertex that has at least one child.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Trees",
            "question": lambda index:
                f"\\text{{True or False: The root is always a leaf.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Easy"
        },
        {
            "topic": "Trees",
            "question": lambda index:
                f"\\text{{True or False: The root is always an internal vertex.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },

        # --- Subtrees ---
        {
            "topic": "Trees",
            "question": lambda index:
                f"\\text{{True or False: A subtree rooted at vertex v consists of v and all of its descendants.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Trees",
            "question": lambda index:
                f"\\text{{True or False: A subtree rooted at vertex v consists of v and all of its ancestors.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },
        {
            "topic": "Trees",
            "question": lambda index:
                f"\\text{{True or False: The entire tree is a subtree of itself.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },

        # --- m-ary Trees ---
        {
            "topic": "Trees",
            "question": lambda index:
                f"\\text{{True or False: A rooted tree is called an m-ary tree if every internal vertex has at most m children.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Trees",
            "question": lambda index:
                f"\\text{{True or False: A rooted tree is called an m-ary tree if every internal vertex has exactly m children.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },
        {
            "topic": "Trees",
            "question": lambda index:
                f"\\text{{True or False: A full m-ary tree is one where every internal vertex has exactly m children.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Trees",
            "question": lambda index:
                f"\\text{{True or False: A binary tree is a special case of an m-ary tree where m = 2.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Trees",
            "question": lambda index:
                f"\\text{{True or False: A binary tree is a special case of an m-ary tree where m = 3.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Easy"
        },
        {
            "topic": "Trees",
            "question": lambda index:
                f"\\text{{True or False: A full binary tree with i internal vertices has exactly i + 1 leaves.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Hard"
        },
        {
            "topic": "Trees",
            "question": lambda index:
                f"\\text{{True or False: A full m-ary tree with i internal vertices has m · i + 1 total vertices.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Hard"
        },
        {
            "topic": "Trees",
            "question": lambda index:
                f"\\text{{True or False: A full m-ary tree with i internal vertices has m · i - 1 total vertices.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Hard"
        },

        # --- Ordered Rooted Trees ---
        {
            "topic": "Trees",
            "question": lambda index:
                f"\\text{{True or False: An ordered rooted tree is one where the children of each vertex are ordered from left to right.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Trees",
            "question": lambda index:
                f"\\text{{True or False: Two ordered rooted trees are the same if they have the same structure but their children are in a different order.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },
        {
            "topic": "Trees",
            "question": lambda index:
                f"\\text{{True or False: In an ordered binary tree, every internal vertex has a designated left and right child.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },

        # --- Levels & Height ---
        {
            "topic": "Trees",
            "question": lambda index:
                f"\\text{{True or False: The level of the root in a rooted tree is 0.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Trees",
            "question": lambda index:
                f"\\text{{True or False: The level of the root in a rooted tree is 1.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Easy"
        },
        {
            "topic": "Trees",
            "question": lambda index:
                f"\\text{{True or False: The level of a vertex v is the length of the path from the root to v.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Trees",
            "question": lambda index:
                f"\\text{{True or False: The height of a rooted tree is the maximum level of any vertex in the tree.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Trees",
            "question": lambda index:
                f"\\text{{True or False: The height of a rooted tree is the minimum level of any leaf.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Easy"
        },
        {
            "topic": "Trees",
            "question": lambda index:
                f"\\text{{True or False: A tree consisting of only the root has a height of 0.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },

        # --- Balanced Trees ---
        {
            "topic": "Trees",
            "question": lambda index:
                f"\\text{{True or False: A rooted m-ary tree of height h is balanced if all leaves are at levels h or h - 1.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Trees",
            "question": lambda index:
                f"\\text{{True or False: A balanced tree requires all leaves to be at the same level.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },
        {
            "topic": "Trees",
            "question": lambda index:
                f"\\text{{True or False: A full m-ary tree of height h can have at most mʰ leaves.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Hard"
        },
        {
            "topic": "Trees",
            "question": lambda index:
                f"\\text{{True or False: If a binary tree has more than 2ʰ leaves, its height must be greater than h.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Hard"
        },

        # --- Spanning Trees ---
        {
            "topic": "Trees",
            "question": lambda index:
                f"\\text{{True or False: A spanning tree of a connected graph G is a subgraph of G that is a tree containing every vertex of G.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Trees",
            "question": lambda index:
                f"\\text{{True or False: A spanning tree of G contains every edge of G.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },
        {
            "topic": "Trees",
            "question": lambda index:
                f"\\text{{True or False: Every connected graph has at least one spanning tree.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Trees",
            "question": lambda index:
                f"\\text{{True or False: A disconnected graph has a spanning tree.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },
        {
            "topic": "Trees",
            "question": lambda index:
                f"\\text{{True or False: A minimum spanning tree is a spanning tree with the smallest possible total edge weight.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Trees",
            "question": lambda index:
                f"\\text{{True or False: A minimum spanning tree of a graph is always unique.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Hard"
        },

        # --- Kruskal's Algorithm ---
        {
            "topic": "Trees",
            "question": lambda index:
                f"\\text{{True or False: Kruskal's algorithm builds a minimum spanning tree by repeatedly adding the lowest-weight edge that does not form a circuit.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Trees",
            "question": lambda index:
                f"\\text{{True or False: Kruskal's algorithm builds a minimum spanning tree by repeatedly adding the lowest-weight edge regardless of whether it forms a circuit.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },
        {
            "topic": "Trees",
            "question": lambda index:
                f"\\text{{True or False: Kruskal's algorithm is a greedy algorithm.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Trees",
            "question": lambda index:
                f"\\text{{True or False: Kruskal's algorithm begins by selecting the vertex with the lowest degree.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },
        {
            "topic": "Trees",
            "question": lambda index:
                f"\\text{{True or False: Kruskal's algorithm considers edges in non-decreasing order of weight.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Trees",
            "question": lambda index:
                f"\\text{{True or False: Kruskal's algorithm considers edges in non-increasing order of weight.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },
        {
            "topic": "Trees",
            "question": lambda index:
                f"\\text{{True or False: Kruskal's algorithm always produces a minimum spanning tree for any connected weighted graph.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Hard"
        },

        # --- Prim's Algorithm ---
        {
            "topic": "Trees",
            "question": lambda index:
                f"\\text{{True or False: Prim's algorithm builds a minimum spanning tree by growing a single tree one edge at a time from a starting vertex.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Trees",
            "question": lambda index:
                f"\\text{{True or False: Prim's algorithm builds a minimum spanning tree by growing multiple disconnected trees simultaneously.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },
        {
            "topic": "Trees",
            "question": lambda index:
                f"\\text{{True or False: At each step, Prim's algorithm adds the minimum-weight edge connecting a vertex in the tree to a vertex outside the tree.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Trees",
            "question": lambda index:
                f"\\text{{True or False: At each step, Prim's algorithm adds the minimum-weight edge connecting any two vertices outside the current tree.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },
        {
            "topic": "Trees",
            "question": lambda index:
                f"\\text{{True or False: Prim's algorithm is a greedy algorithm.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Trees",
            "question": lambda index:
                f"\\text{{True or False: Prim's algorithm and Kruskal's algorithm always produce the same spanning tree.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Hard"
        },
        {
            "topic": "Trees",
            "question": lambda index:
                f"\\text{{True or False: Both Prim's and Kruskal's algorithms always produce a minimum spanning tree.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Trees",
            "question": lambda index:
                f"\\text{{True or False: Prim's algorithm maintains a connected subtree throughout its execution.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Hard"
        },
        {
            "topic": "Trees",
            "question": lambda index:
                f"\\text{{True or False: Kruskal's algorithm maintains a connected subtree throughout its execution.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Hard"
        },
        #endregion
        #region Coloring

        # --- Definitions ---
        {
            "topic": "Coloring",
            "question": lambda index:
                f"\\text{{True or False: A proper coloring of a graph assigns colors to vertices so that no two adjacent vertices share the same color.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Coloring",
            "question": lambda index:
                f"\\text{{True or False: A proper coloring of a graph assigns colors to vertices so that no two vertices share the same color.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Easy"
        },
        {
            "topic": "Coloring",
            "question": lambda index:
                f"\\text{{True or False: An edge coloring assigns colors to edges so that no two edges sharing an endpoint have the same color.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },

        # --- Chromatic Number ---
        {
            "topic": "Coloring",
            "question": lambda index:
                f"\\text{{True or False: The chromatic number χ(G) is the minimum number of colors needed to properly color G.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Coloring",
            "question": lambda index:
                f"\\text{{True or False: The chromatic number χ(G) is the maximum number of colors needed to properly color G.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Easy"
        },
        {
            "topic": "Coloring",
            "question": lambda index:
                f"\\text{{True or False: The chromatic number of a bipartite graph is at most 2.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Coloring",
            "question": lambda index:
                f"\\text{{True or False: The chromatic number of any tree is at most 2.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Coloring",
            "question": lambda index:
                f"\\text{{True or False: The chromatic number of the complete graph Kₙ is n.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Coloring",
            "question": lambda index:
                f"\\text{{True or False: A graph G has chromatic number 1 if and only if it has no edges.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Coloring",
            "question": lambda index:
                f"\\text{{True or False: A graph G has χ(G) = 2 if and only if it is bipartite and has at least one edge.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Hard"
        },
        {
            "topic": "Coloring",
            "question": lambda index:
                f"\\text{{True or False: A graph containing an odd cycle must have chromatic number at least 3.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Hard"
        },
        {
            "topic": "Coloring",
            "question": lambda index:
                f"\\text{{True or False: A graph containing only even cycles can have chromatic number 3.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Hard"
        },

        # --- Four Color Theorem ---
        {
            "topic": "Coloring",
            "question": lambda index:
                f"\\text{{True or False: The Four Color Theorem states that every planar graph has chromatic number at most 4.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Coloring",
            "question": lambda index:
                f"\\text{{True or False: The Four Color Theorem states that every graph has chromatic number at most 4.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Easy"
        },
        {
            "topic": "Coloring",
            "question": lambda index:
                f"\\text{{True or False: The Four Color Theorem was proved with the aid of a computer.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Coloring",
            "question": lambda index:
                f"\\text{{True or False: Every planar graph requires exactly 4 colors to be properly colored.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },

        # --- Petersen Graph ---
        {
            "topic": "Coloring",
            "question": lambda index:
                f"\\text{{True or False: The Petersen graph has chromatic number 3.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Hard"
        },
        {
            "topic": "Coloring",
            "question": lambda index:
                f"\\text{{True or False: The Petersen graph is bipartite.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },
        {
            "topic": "Coloring",
            "question": lambda index:
                f"\\text{{True or False: The Petersen graph is planar.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },
        {
            "topic": "Coloring",
            "question": lambda index:
                f"\\text{{True or False: The Petersen graph is a 3-regular graph on 10 vertices.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Coloring",
            "question": lambda index:
                f"\\text{{True or False: The Petersen graph has 15 edges.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Hard"
        },

#endregion
        #region Planar Graphs

        # --- Definitions ---
        {
            "topic": "Planar Graphs",
            "question": lambda index:
                f"\\text{{True or False: A planar graph is one that can be drawn in the plane with no edges crossing.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Planar Graphs",
            "question": lambda index:
                f"\\text{{True or False: A graph is planar only if it is currently drawn without crossings.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Easy"
        },
        {
            "topic": "Planar Graphs",
            "question": lambda index:
                f"\\text{{True or False: A planar representation of a graph divides the plane into regions called faces.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Planar Graphs",
            "question": lambda index:
                f"\\text{{True or False: Every planar representation of a connected graph has an unbounded outer face.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Planar Graphs",
            "question": lambda index:
                f"\\text{{True or False: Every complete graph is planar.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Easy"
        },

        # --- Euler's Formula ---
        {
            "topic": "Planar Graphs",
            "question": lambda index:
                f"\\text{{True or False: Euler's formula for connected planar graphs states that v - e + f = 2.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Planar Graphs",
            "question": lambda index:
                f"\\text{{True or False: Euler's formula for connected planar graphs states that v + e - f = 2.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },
        {
            "topic": "Planar Graphs",
            "question": lambda index:
                f"\\text{{True or False: In Euler's formula v - e + f = 2, the variable f includes the unbounded outer face.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Planar Graphs",
            "question": lambda index:
                f"\\text{{True or False: Euler's formula v - e + f = 2 holds for all planar graphs, whether connected or not.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Hard"
        },
        {
            "topic": "Planar Graphs",
            "question": lambda index:
                f"\\text{{True or False: For a connected planar graph with v vertices, e edges, and f faces: v - e + f = 2 regardless of how it is drawn.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Hard"
        },

        # --- Degree of a Region ---
        {
            "topic": "Planar Graphs",
            "question": lambda index:
                f"\\text{{True or False: The degree of a face in a planar graph is the number of edges on its boundary.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Planar Graphs",
            "question": lambda index:
                f"\\text{{True or False: An edge shared between two faces contributes 1 to the total degree sum of all faces.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Hard"
        },
        {
            "topic": "Planar Graphs",
            "question": lambda index:
                f"\\text{{True or False: The sum of the degrees of all faces in a planar graph equals 2e.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Hard"
        },
        {
            "topic": "Planar Graphs",
            "question": lambda index:
                f"\\text{{True or False: Every face in a simple connected planar graph has degree at least 3.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Hard"
        },

        # --- Edge Inequality (m <= 3n - 6) ---
        {
            "topic": "Planar Graphs",
            "question": lambda index:
                f"\\text{{True or False: If G is a connected planar simple graph with n ≥ 3 vertices and m edges, then m ≤ 3n - 6.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Hard"
        },
        {
            "topic": "Planar Graphs",
            "question": lambda index:
                f"\\text{{True or False: If G is a connected planar simple graph with n ≥ 3 vertices and m edges, then m ≤ 2n - 6.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Hard"
        },
        {
            "topic": "Planar Graphs",
            "question": lambda index:
                f"\\text{{True or False: The inequality m ≤ 3n - 6 can be used to prove that K₅ is not planar.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Hard"
        },
        {
            "topic": "Planar Graphs",
            "question": lambda index:
                f"\\text{{True or False: If G is a connected planar simple bipartite graph with n ≥ 3 vertices and m edges, then m ≤ 2n - 4.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Hard"
        },
        {
            "topic": "Planar Graphs",
            "question": lambda index:
                f"\\text{{True or False: If G is a connected planar simple bipartite graph with n ≥ 3 vertices and m edges, then m ≤ 3n - 6.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Hard"
        },
        {
            "topic": "Planar Graphs",
            "question": lambda index:
                f"\\text{{True or False: The tighter bound m ≤ 2n - 4 for bipartite planar graphs arises because bipartite graphs contain no odd cycles, so every face has degree at least 4.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Hard"
        },
        {
            "topic": "Planar Graphs",
            "question": lambda index:
                f"\\text{{True or False: The inequality m ≤ 2n - 4 can be used to prove that K₃,₃ is not planar.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Hard"
        },

        # --- Smallest Non-Planar Graphs ---
        {
            "topic": "Planar Graphs",
            "question": lambda index:
                f"\\text{{True or False: K₅ is a non-planar graph.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Planar Graphs",
            "question": lambda index:
                f"\\text{{True or False: K₄ is a non-planar graph.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },
        {
            "topic": "Planar Graphs",
            "question": lambda index:
                f"\\text{{True or False: K₃,₃ is a non-planar graph.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Planar Graphs",
            "question": lambda index:
                f"\\text{{True or False: K₂,₃ is a non-planar graph.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },
        {
            "topic": "Planar Graphs",
            "question": lambda index:
                f"\\text{{True or False: K₅ and K₃,₃ are the two smallest non-planar graphs up to subdivision.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Hard"
        },

        # --- Subdivisions & Homeomorphism ---
        {
            "topic": "Planar Graphs",
            "question": lambda index:
                f"\\text{{True or False: A subdivision of a graph is obtained by inserting new vertices of degree 2 into edges.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Planar Graphs",
            "question": lambda index:
                f"\\text{{True or False: A subdivision of a planar graph may be non-planar.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },
        {
            "topic": "Planar Graphs",
            "question": lambda index:
                f"\\text{{True or False: Two graphs are homeomorphic if they can both be obtained from the same graph by a sequence of subdivisions.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Hard"
        },
        {
            "topic": "Planar Graphs",
            "question": lambda index:
                f"\\text{{True or False: Homeomorphic graphs always have the same number of vertices.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Hard"
        },
        {
            "topic": "Planar Graphs",
            "question": lambda index:
                f"\\text{{True or False: If G is planar, then every subdivision of G is also planar.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },

        # --- Kuratowski's Theorem ---
        {
            "topic": "Planar Graphs",
            "question": lambda index:
                f"\\text{{True or False: Kuratowski's theorem states that a graph is planar if and only if it contains no subgraph homeomorphic to K₅ or K₃,₃.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Hard"
        },
        {
            "topic": "Planar Graphs",
            "question": lambda index:
                f"\\text{{True or False: Kuratowski's theorem states that a graph is planar if and only if it contains no subgraph homeomorphic to K₄ or K₂,₃.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Hard"
        },
        {
            "topic": "Planar Graphs",
            "question": lambda index:
                f"\\text{{True or False: According to Kuratowski's theorem, a graph is non-planar if it contains a subdivision of K₅ as a subgraph.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Hard"
        },
        {
            "topic": "Planar Graphs",
            "question": lambda index:
                f"\\text{{True or False: Kuratowski's theorem provides a necessary but not sufficient condition for planarity.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Hard"
        },

#endregion
    ]

    # Filter #
    if 'difficulty_filter' not in st.session_state or len(st.session_state['difficulty_filter']) == 0:
        st.session_state["questions"] = questions
    else:
        st.session_state["questions"] = list(filter(
            lambda question: st.session_state['difficulty_filter'].__contains__(question['difficulty'].lower()), 
            questions
        ))

    questions = st.session_state["questions"]

    if 'topic_filter' in st.session_state and len(st.session_state['topic_filter']) > 0:
        st.session_state["questions"] = list(filter(
            lambda question: st.session_state['topic_filter'].__contains__(question['topic'].lower()), 
            questions
        ))
        
    # Pick Random Question #
    question_amount = len(st.session_state["questions"])
    st.session_state['question_index'] = random.randint(0, question_amount - 1)