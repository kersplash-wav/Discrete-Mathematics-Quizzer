
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

        # --- Set Definition & Elements ---
        {
            "topic": "Set Theory",
            "question": lambda index:
                f"\\text{{True or False: A set is an unordered collection of distinct objects.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Set Theory",
            "question": lambda index:
                f"\\text{{True or False: A set is an ordered collection of objects.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Easy"
        },
        {
            "topic": "Set Theory",
            "question": lambda index:
                f"\\text{{True or False: The notation x}} \\space \\isin \\space \\text{{A means x is an element of set A.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Set Theory",
            "question": lambda index:
                f"\\text{{True or False: The notation x}} \\space \\notin \\space \\text{{A means x is an element of set A.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Easy"
        },
        {
            "topic": "Set Theory",
            "question": lambda index:
                f"\\text{{True or False: A set can contain duplicate elements.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Easy"
        },
        {
            "topic": "Set Theory",
            "question": lambda index:
                f"\\text{{True or False: Two sets are equal if and only if they have exactly the same elements.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Set Theory",
            "question": lambda index:
                f"\\text{{True or False: The sets \\{{1, 2, 3\\}} and \\{{3, 1, 2\\}} are equal.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Set Theory",
            "question": lambda index:
                f"\\text{{True or False: The sets \\{{1, 2, 3\\}} and \\{{1, 2, 3, 3\\}} are equal.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },

        # --- Subsets & Proper Subsets ---
        {
            "topic": "Set Theory",
            "question": lambda index:
                f"\\text{{True or False: A is a subset of B if every element of A is also an element of B.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Set Theory",
            "question": lambda index:
                f"\\text{{True or False: Every set is a subset of itself.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Set Theory",
            "question": lambda index:
                f"\\text{{True or False: A proper subset of B must satisfy A ⊆ B and A ≠ B.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Set Theory",
            "question": lambda index:
                f"\\text{{True or False: A set is a proper subset of itself.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Easy"
        },
        {
            "topic": "Set Theory",
            "question": lambda index:
                f"\\text{{True or False: The empty set is a subset of every set.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Set Theory",
            "question": lambda index:
                f"\\text{{True or False: The empty set is a proper subset of every set.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },
        {
            "topic": "Set Theory",
            "question": lambda index:
                f"\\text{{True or False: The empty set is a proper subset of every nonempty set.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Set Theory",
            "question": lambda index:
                f"\\text{{True or False: If A ⊆ B and B ⊆ A, then A = B.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },

        # --- Finite vs. Infinite & Cardinality ---
        {
            "topic": "Set Theory",
            "question": lambda index:
                f"\\text{{True or False: A finite set has a cardinality equal to the number of elements it contains.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Set Theory",
            "question": lambda index:
                f"\\text{{True or False: The set of natural numbers ℕ is a finite set.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Easy"
        },
        {
            "topic": "Set Theory",
            "question": lambda index:
                f"\\text{{True or False: The cardinality of the empty set is 0.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Set Theory",
            "question": lambda index:
                f"\\text{{True or False: The cardinality of the empty set is 1.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Easy"
        },
        {
            "topic": "Set Theory",
            "question": lambda index:
                f"\\text{{True or False: The cardinality of \\{{∅\\}} is 1.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Set Theory",
            "question": lambda index:
                f"\\text{{True or False: The cardinality of \\{{∅\\}} is 0.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },

        # --- Power Sets ---
        {
            "topic": "Set Theory",
            "question": lambda index:
                f"\\text{{True or False: The power set of A is the set of all subsets of A.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Set Theory",
            "question": lambda index:
                f"\\text{{True or False: If |A| = n, then |𝒫(A)| = 2ⁿ.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Set Theory",
            "question": lambda index:
                f"\\text{{True or False: If |A| = n, then |𝒫(A)| = n².}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },
        {
            "topic": "Set Theory",
            "question": lambda index:
                f"\\text{{True or False: The power set of the empty set is the empty set.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },
        {
            "topic": "Set Theory",
            "question": lambda index:
                f"\\text{{True or False: The power set of the empty set is \\{{∅\\}}.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Set Theory",
            "question": lambda index:
                f"\\text{{True or False: The cardinality of the power set of \\{{∅\\}} is 1.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Set Theory",
            "question": lambda index:
                f"\\text{{True or False: The power set of \\{{∅\\}} contains the empty set as an element.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Hard"
        },

        # --- Ordered Tuples & Cartesian Product ---
        {
            "topic": "Set Theory",
            "question": lambda index:
                f"\\text{{True or False: An ordered n-tuple is a sequence of n elements in which order matters.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Set Theory",
            "question": lambda index:
                f"\\text{{True or False: The ordered pairs (1,2) and (2,1) are equal.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Easy"
        },
        {
            "topic": "Set Theory",
            "question": lambda index:
                f"\\text{{True or False: The Cartesian product A × B is the set of all ordered pairs (a,b) where a ∈ A and b ∈ B.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Set Theory",
            "question": lambda index:
                f"\\text{{True or False: If |A| = m and |B| = n, then |A × B| = m + n.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Easy"
        },
        {
            "topic": "Set Theory",
            "question": lambda index:
                f"\\text{{True or False: If |A| = m and |B| = n, then |A × B| = m · n.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Set Theory",
            "question": lambda index:
                f"\\text{{True or False: A × B = B × A for all sets A and B.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },

        # --- Unions, Intersections, Disjoint ---
        {
            "topic": "Set Theory",
            "question": lambda index:
                f"\\text{{True or False: The union A ∪ B is the set of all elements in A or B (or both).}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Set Theory",
            "question": lambda index:
                f"\\text{{True or False: The intersection A ∩ B is the set of all elements in both A and B.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Set Theory",
            "question": lambda index:
                f"\\text{{True or False: Two sets are disjoint if their union is the empty set.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },
        {
            "topic": "Set Theory",
            "question": lambda index:
                f"\\text{{True or False: Two sets are disjoint if their intersection is the empty set.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Set Theory",
            "question": lambda index:
                f"\\text{{True or False: A ∪ B = B ∪ A for all sets A and B.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Set Theory",
            "question": lambda index:
                f"\\text{{True or False: A ∩ B = B ∩ A for all sets A and B.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },

        # --- Difference ---
        {
            "topic": "Set Theory",
            "question": lambda index:
                f"\\text{{True or False: The set difference A - B is the set of elements in A that are not in B.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Set Theory",
            "question": lambda index:
                f"\\text{{True or False: A - B = B - A for all sets A and B.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },
        {
            "topic": "Set Theory",
            "question": lambda index:
                f"\\text{{True or False: The complement of A contains all elements in the universal set that are not in A.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Set Theory",
            "question": lambda index:
                f"\\text{{True or False: The symmetric difference A ⊕ B contains elements in A or B but not both.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Set Theory",
            "question": lambda index:
                f"\\text{{True or False: A ⊕ B = (A ∪ B) - (A ∩ B).}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },

        # --- Principle of Inclusion-Exclusion ---
        {
            "topic": "Set Theory",
            "question": lambda index:
                f"\\text{{True or False: The principle of inclusion-exclusion states |A ∪ B| = |A| + |B| - |A ∩ B|.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Set Theory",
            "question": lambda index:
                f"\\text{{True or False: The principle of inclusion-exclusion states |A ∪ B| = |A| + |B| + |A ∩ B|.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },
        {
            "topic": "Set Theory",
            "question": lambda index:
                f"\\text{{True or False: For three sets, |A ∪ B ∪ C| = |A| + |B| + |C| - |A ∩ B| - |A ∩ C| - |B ∩ C| + |A ∩ B ∩ C|.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Hard"
        },
        {
            "topic": "Set Theory",
            "question": lambda index:
                f"\\text{{True or False: If A and B are disjoint, then |A ∪ B| = |A| + |B|.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },

        # --- Russell's Paradox ---
        {
            "topic": "Set Theory",
            "question": lambda index:
                f"\\text{{True or False: Russell's paradox concerns the set of all sets that do not contain themselves.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Hard"
        },
        {
            "topic": "Set Theory",
            "question": lambda index:
                f"\\text{{True or False: Russell's paradox shows that naive set theory leads to a contradiction.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Hard"
        },
        {
            "topic": "Set Theory",
            "question": lambda index:
                f"\\text{{True or False: Russell's paradox is resolved in naive set theory without modification.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Hard"
        },

        # --- Partitions ---
        {
            "topic": "Set Theory",
            "question": lambda index:
                f"\\text{{True or False: A partition of a set S is a collection of nonempty, pairwise disjoint subsets whose union is S.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Set Theory",
            "question": lambda index:
                f"\\text{{True or False: The empty set can be a part (block) of a partition.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },
        {
            "topic": "Set Theory",
            "question": lambda index:
                f"\\text{{True or False: Every element of S must belong to exactly one block of a partition.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Set Theory",
            "question": lambda index:
                f"\\text{{True or False: A partition of S can have blocks whose union is a proper subset of S.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },

        # --- Increasing/Decreasing/Nondecreasing/Nonincreasing ---
        {
            "topic": "Set Theory",
            "question": lambda index:
                f"\\text{{True or False: A sequence is nondecreasing if each term is greater than or equal to the previous term.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Set Theory",
            "question": lambda index:
                f"\\text{{True or False: A strictly increasing sequence allows consecutive equal terms.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Easy"
        },
        {
            "topic": "Set Theory",
            "question": lambda index:
                f"\\text{{True or False: A nonincreasing sequence allows consecutive equal terms.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Set Theory",
            "question": lambda index:
                f"\\text{{True or False: Every strictly increasing sequence is also nondecreasing.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Set Theory",
            "question": lambda index:
                f"\\text{{True or False: Every nondecreasing sequence is also strictly increasing.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Easy"
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

        # --- Operators & Precedence ---
        {
            "topic": "Logic",
            "question": lambda index:
                f"\\text{{True or False: Negation (¬) has the highest precedence among logical operators.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Logic",
            "question": lambda index:
                f"\\text{{True or False: The precedence order from highest to lowest is: ¬, ∧, ∨, ⊕, →, ↔.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Logic",
            "question": lambda index:
                f"\\text{{True or False: The conditional (→) has higher precedence than conjunction (∧).}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },
        {
            "topic": "Logic",
            "question": lambda index:
                f"\\text{{True or False: The biconditional (↔) has the lowest precedence among logical operators.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },

        # --- Tautology, Contradiction, Equivalence ---
        {
            "topic": "Logic",
            "question": lambda index:
                f"\\text{{True or False: A tautology is a compound proposition that is always true.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Logic",
            "question": lambda index:
                f"\\text{{True or False: A contradiction is a compound proposition that is always false.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Logic",
            "question": lambda index:
                f"\\text{{True or False: p ∨ ¬p is a tautology.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Logic",
            "question": lambda index:
                f"\\text{{True or False: p ∧ ¬p is a tautology.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Easy"
        },
        {
            "topic": "Logic",
            "question": lambda index:
                f"\\text{{True or False: Two propositions are logically equivalent if they have the same truth value in all cases.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Logic",
            "question": lambda index:
                f"\\text{{True or False: p → q is logically equivalent to ¬p ∨ q.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Logic",
            "question": lambda index:
                f"\\text{{True or False: p → q is logically equivalent to ¬q → ¬p (contrapositive).}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Logic",
            "question": lambda index:
                f"\\text{{True or False: p → q is logically equivalent to q → p (converse).}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },

        # --- De Morgan's, Absorption, Identity, Domination ---
        {
            "topic": "Logic",
            "question": lambda index:
                f"\\text{{True or False: De Morgan's law states ¬(p ∧ q) ≡ ¬p ∨ ¬q.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Logic",
            "question": lambda index:
                f"\\text{{True or False: De Morgan's law states ¬(p ∨ q) ≡ ¬p ∧ ¬q.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Logic",
            "question": lambda index:
                f"\\text{{True or False: De Morgan's law states ¬(p ∧ q) ≡ ¬p ∧ ¬q.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Easy"
        },
        {
            "topic": "Logic",
            "question": lambda index:
                f"\\text{{True or False: The absorption law states p ∨ (p ∧ q) ≡ p.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Logic",
            "question": lambda index:
                f"\\text{{True or False: The identity law states p ∧ T ≡ p.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Logic",
            "question": lambda index:
                f"\\text{{True or False: The domination law states p ∨ T ≡ p.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Easy"
        },
        {
            "topic": "Logic",
            "question": lambda index:
                f"\\text{{True or False: The domination law states p ∨ T ≡ T.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Logic",
            "question": lambda index:
                f"\\text{{True or False: The double negation law states ¬(¬p) ≡ p.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Logic",
            "question": lambda index:
                f"\\text{{True or False: The idempotent law states p ∧ p ≡ p.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },

        # --- Rules of Inference ---
        {
            "topic": "Logic",
            "question": lambda index:
                f"\\text{{True or False: Modus ponens states: if p → q and p are true, then q is true.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Logic",
            "question": lambda index:
                f"\\text{{True or False: Modus tollens states: if p → q and ¬q are true, then ¬p is true.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Logic",
            "question": lambda index:
                f"\\text{{True or False: Affirming the consequent is a valid rule of inference.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },
        {
            "topic": "Logic",
            "question": lambda index:
                f"\\text{{True or False: Affirming the consequent concludes p from p → q and q, which is a fallacy.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Logic",
            "question": lambda index:
                f"\\text{{True or False: Denying the antecedent concludes ¬q from p → q and ¬p, which is a fallacy.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Logic",
            "question": lambda index:
                f"\\text{{True or False: Hypothetical syllogism states: if p → q and q → r, then p → r.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Logic",
            "question": lambda index:
                f"\\text{{True or False: Disjunctive syllogism states: if p ∨ q and ¬p, then q.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Logic",
            "question": lambda index:
                f"\\text{{True or False: The addition rule states: p implies p ∨ q.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Logic",
            "question": lambda index:
                f"\\text{{True or False: The simplification rule states: p ∧ q implies p.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Logic",
            "question": lambda index:
                f"\\text{{True or False: Resolution states: from p ∨ q and ¬p ∨ r, we can conclude q ∨ r.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Hard"
        },

        # --- Predicates, Quantifiers, Variables ---
        {
            "topic": "Logic",
            "question": lambda index:
                f"\\text{{True or False: A predicate is a statement that contains variables and becomes a proposition when variables are assigned values.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Logic",
            "question": lambda index:
                f"\\text{{True or False: A free variable in a formula is one that is not bound by any quantifier.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Logic",
            "question": lambda index:
                f"\\text{{True or False: A bound variable is one that is not within the scope of any quantifier.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },
        {
            "topic": "Logic",
            "question": lambda index:
                f"\\text{{True or False: Universal instantiation allows concluding P(c) for a specific c from ∀x P(x).}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Logic",
            "question": lambda index:
                f"\\text{{True or False: Existential generalization allows concluding ∃x P(x) from P(c) for a specific c.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Logic",
            "question": lambda index:
                f"\\text{{True or False: Universal generalization requires that c be an arbitrary element, not a particular one.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Hard"
        },
        {
            "topic": "Logic",
            "question": lambda index:
                f"\\text{{True or False: A nested quantifier ∀x ∃y P(x,y) means for every x there exists some y (possibly depending on x) such that P(x,y).}}",
            "answer": lambda index:
                "True",
            "difficulty": "Hard"
        },
        {
            "topic": "Logic",
            "question": lambda index:
                f"\\text{{True or False: ∀x ∃y P(x,y) is logically equivalent to ∃y ∀x P(x,y).}}",
            "answer": lambda index:
                "False",
            "difficulty": "Hard"
        },

        # --- Theorems, Lemmas, Corollaries ---
        {
            "topic": "Logic",
            "question": lambda index:
                f"\\text{{True or False: A theorem is a statement that has been proved to be true.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Logic",
            "question": lambda index:
                f"\\text{{True or False: A lemma is a minor result proved to assist in proving a larger theorem.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Logic",
            "question": lambda index:
                f"\\text{{True or False: A corollary is a result that follows directly from a theorem with little additional proof.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Logic",
            "question": lambda index:
                f"\\text{{True or False: A conjecture is a statement believed to be true but not yet proved.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },

        # --- Logic Gates ---
        {
            "topic": "Logic",
            "question": lambda index:
                f"\\text{{True or False: An AND gate outputs 1 if and only if both inputs are 1.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Logic",
            "question": lambda index:
                f"\\text{{True or False: An OR gate outputs 1 if at least one input is 1.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Logic",
            "question": lambda index:
                f"\\text{{True or False: A NAND gate is equivalent to an AND gate followed by a NOT gate.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Logic",
            "question": lambda index:
                f"\\text{{True or False: A XOR gate outputs 1 when both inputs are 1.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },
        {
            "topic": "Logic",
            "question": lambda index:
                f"\\text{{True or False: A XOR gate outputs 1 when exactly one input is 1.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Logic",
            "question": lambda index:
                f"\\text{{True or False: NAND gates alone are functionally complete (can implement any Boolean function).}}",
            "answer": lambda index:
                "True",
            "difficulty": "Hard"
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
                f"\\text{{True or False: Uniform distribution is when each element has a}} \\space 1/2^n \\space \\text{{chance of occurring.}}",
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

    #region Euler and Hamilton

        # --- Euler Trails & Circuits ---
        {
            "topic": "Euler and Hamilton",
            "question": lambda index:
                f"\\text{{True or False: An Euler trail is a trail that visits every edge of a graph exactly once.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Euler and Hamilton",
            "question": lambda index:
                f"\\text{{True or False: An Euler trail is a trail that visits every vertex of a graph exactly once.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Easy"
        },
        {
            "topic": "Euler and Hamilton",
            "question": lambda index:
                f"\\text{{True or False: An Euler circuit is a closed trail that visits every edge exactly once.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Euler and Hamilton",
            "question": lambda index:
                f"\\text{{True or False: A connected graph has an Euler circuit if and only if every vertex has even degree.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Euler and Hamilton",
            "question": lambda index:
                f"\\text{{True or False: A connected graph has an Euler circuit if and only if every vertex has odd degree.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },
        {
            "topic": "Euler and Hamilton",
            "question": lambda index:
                f"\\text{{True or False: A connected graph has an Euler trail (but not circuit) if and only if it has exactly two vertices of odd degree.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Euler and Hamilton",
            "question": lambda index:
                f"\\text{{True or False: A connected graph has an Euler trail (but not circuit) if and only if it has exactly one vertex of odd degree.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },
        {
            "topic": "Euler and Hamilton",
            "question": lambda index:
                f"\\text{{True or False: An Euler trail in a graph must begin and end at the two vertices of odd degree.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Euler and Hamilton",
            "question": lambda index:
                f"\\text{{True or False: Every Euler circuit is also an Euler trail.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Euler and Hamilton",
            "question": lambda index:
                f"\\text{{True or False: Every Euler trail is also an Euler circuit.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },

        # --- Fleury vs. Hierholzer ---
        {
            "topic": "Euler and Hamilton",
            "question": lambda index:
                f"\\text{{True or False: Fleury's algorithm constructs an Euler circuit by avoiding bridges unless no other edge is available.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Euler and Hamilton",
            "question": lambda index:
                f"\\text{{True or False: Fleury's algorithm constructs an Euler circuit by preferring bridge edges at each step.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },
        {
            "topic": "Euler and Hamilton",
            "question": lambda index:
                f"\\text{{True or False: Hierholzer's algorithm constructs an Euler circuit by repeatedly splicing in sub-circuits.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Hard"
        },
        {
            "topic": "Euler and Hamilton",
            "question": lambda index:
                f"\\text{{True or False: Hierholzer's algorithm requires checking for bridges at every step.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Hard"
        },
        {
            "topic": "Euler and Hamilton",
            "question": lambda index:
                f"\\text{{True or False: Hierholzer's algorithm is generally more efficient than Fleury's algorithm.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Hard"
        },

        # --- Hamilton Paths & Cycles ---
        {
            "topic": "Euler and Hamilton",
            "question": lambda index:
                f"\\text{{True or False: A Hamilton path visits every vertex of a graph exactly once.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Euler and Hamilton",
            "question": lambda index:
                f"\\text{{True or False: A Hamilton path visits every edge of a graph exactly once.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Easy"
        },
        {
            "topic": "Euler and Hamilton",
            "question": lambda index:
                f"\\text{{True or False: A Hamilton cycle is a closed Hamilton path.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Euler and Hamilton",
            "question": lambda index:
                f"\\text{{True or False: A graph is Hamiltonian if it contains a Hamilton cycle.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Euler and Hamilton",
            "question": lambda index:
                f"\\text{{True or False: There is a known efficient algorithm for determining whether any graph is Hamiltonian.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Hard"
        },
        {
            "topic": "Euler and Hamilton",
            "question": lambda index:
                f"\\text{{True or False: Every Eulerian graph is also Hamiltonian.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Hard"
        },
        {
            "topic": "Euler and Hamilton",
            "question": lambda index:
                f"\\text{{True or False: Every Hamiltonian graph is also Eulerian.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Hard"
        },

        # --- Dirac's Theorem ---
        {
            "topic": "Euler and Hamilton",
            "question": lambda index:
                f"\\text{{True or False: Dirac's theorem states that if every vertex of a simple graph G with n ≥ 3 vertices has degree at least n/2, then G is Hamiltonian.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Hard"
        },
        {
            "topic": "Euler and Hamilton",
            "question": lambda index:
                f"\\text{{True or False: Dirac's theorem states that if every vertex of a simple graph G with n ≥ 3 vertices has degree at least n/3, then G is Hamiltonian.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Hard"
        },
        {
            "topic": "Euler and Hamilton",
            "question": lambda index:
                f"\\text{{True or False: Dirac's theorem provides a sufficient but not necessary condition for a graph to be Hamiltonian.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Hard"
        },
        {
            "topic": "Euler and Hamilton",
            "question": lambda index:
                f"\\text{{True or False: Dirac's theorem provides a necessary and sufficient condition for a graph to be Hamiltonian.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Hard"
        },

        # --- Ore's Theorem ---
        {
            "topic": "Euler and Hamilton",
            "question": lambda index:
                f"\\text{{True or False: Ore's theorem states that if deg(u) + deg(v) ≥ n for every pair of non-adjacent vertices u, v in a simple graph with n ≥ 3 vertices, then G is Hamiltonian.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Hard"
        },
        {
            "topic": "Euler and Hamilton",
            "question": lambda index:
                f"\\text{{True or False: Ore's theorem states that if deg(u) + deg(v) ≥ n for every pair of adjacent vertices u, v, then G is Hamiltonian.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Hard"
        },
        {
            "topic": "Euler and Hamilton",
            "question": lambda index:
                f"\\text{{True or False: Dirac's theorem is a special case of Ore's theorem.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Hard"
        },
        {
            "topic": "Euler and Hamilton",
            "question": lambda index:
                f"\\text{{True or False: Ore's theorem is a special case of Dirac's theorem.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Hard"
        },

        # --- De Bruijn Sequences ---
        {
            "topic": "Euler and Hamilton",
            "question": lambda index:
                f"\\text{{True or False: A de Bruijn sequence of order n over a binary alphabet contains every binary string of length n as a substring exactly once.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Hard"
        },
        {
            "topic": "Euler and Hamilton",
            "question": lambda index:
                f"\\text{{True or False: De Bruijn sequences can be constructed by finding an Euler circuit in a de Bruijn graph.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Hard"
        },
        {
            "topic": "Euler and Hamilton",
            "question": lambda index:
                f"\\text{{True or False: De Bruijn sequences can be constructed by finding a Hamilton path in a de Bruijn graph.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Hard"
        },
        {
            "topic": "Euler and Hamilton",
            "question": lambda index:
                f"\\text{{True or False: The number of de Bruijn sequences of order n over a binary alphabet equals the number of spanning in-trees of the de Bruijn graph.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Hard"
        },
        {
            "topic": "Euler and Hamilton",
            "question": lambda index:
                f"\\text{{True or False: The number of binary de Bruijn sequences of order n is}} \\space 2^(2^(n-1)) / 2^n.",
            "answer": lambda index:
                "True",
            "difficulty": "Hard"
        },
        {
            "topic": "Euler and Hamilton",
            "question": lambda index:
                f"\\text{{True or False: The number of binary de Bruijn sequences of order n is}} \\space 2^(2\\^n) / 2^n.",
            "answer": lambda index:
                "False",
            "difficulty": "Hard"
        },
        {
            "topic": "Euler and Hamilton",
            "question": lambda index:
                f"\\text{{True or False: The number of spanning in-trees of the de Bruijn graph of order n equals the number of binary de Bruijn sequences of order n.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Hard"
        },

#endregion

#region Connectivity

        # --- Walks, Trails, Paths ---
        {
            "topic": "Connectivity",
            "question": lambda index:
                f"\\text{{True or False: A walk in a graph is a sequence of vertices connected by edges where edges and vertices may repeat.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Connectivity",
            "question": lambda index:
                f"\\text{{True or False: A trail is a walk in which no edge is repeated.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Connectivity",
            "question": lambda index:
                f"\\text{{True or False: A trail is a walk in which no vertex is repeated.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Easy"
        },
        {
            "topic": "Connectivity",
            "question": lambda index:
                f"\\text{{True or False: A path is a walk in which no vertex is repeated.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Connectivity",
            "question": lambda index:
                f"\\text{{True or False: Every path is a trail.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Connectivity",
            "question": lambda index:
                f"\\text{{True or False: Every trail is a path.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Easy"
        },
        {
            "topic": "Connectivity",
            "question": lambda index:
                f"\\text{{True or False: Every trail is a walk.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },

        # --- Circuits & Cycles ---
        {
            "topic": "Connectivity",
            "question": lambda index:
                f"\\text{{True or False: A circuit is a closed trail (same start and end vertex, no repeated edges).}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Connectivity",
            "question": lambda index:
                f"\\text{{True or False: A cycle is a closed path (same start and end vertex, no other repeated vertices).}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Connectivity",
            "question": lambda index:
                f"\\text{{True or False: Every cycle is a circuit.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Connectivity",
            "question": lambda index:
                f"\\text{{True or False: Every circuit is a cycle.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },

        # --- Open vs. Closed, Length ---
        {
            "topic": "Connectivity",
            "question": lambda index:
                f"\\text{{True or False: A walk is closed if its first and last vertices are the same.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Connectivity",
            "question": lambda index:
                f"\\text{{True or False: A walk is open if its first and last vertices are the same.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Easy"
        },
        {
            "topic": "Connectivity",
            "question": lambda index:
                f"\\text{{True or False: The length of a walk is the number of edges in the walk.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Connectivity",
            "question": lambda index:
                f"\\text{{True or False: The length of a walk is the number of vertices in the walk.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Easy"
        },

        # --- Connected vs. Disconnected ---
        {
            "topic": "Connectivity",
            "question": lambda index:
                f"\\text{{True or False: An undirected graph is connected if there is a path between every pair of vertices.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Connectivity",
            "question": lambda index:
                f"\\text{{True or False: A disconnected graph has at least one pair of vertices with no path between them.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Connectivity",
            "question": lambda index:
                f"\\text{{True or False: A graph with a single vertex is considered disconnected.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },

        # --- Cut Vertices & Vertex Cuts ---
        {
            "topic": "Connectivity",
            "question": lambda index:
                f"\\text{{True or False: A cut vertex is a vertex whose removal increases the number of connected components.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Connectivity",
            "question": lambda index:
                f"\\text{{True or False: A cut vertex is a vertex whose removal decreases the number of connected components.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },
        {
            "topic": "Connectivity",
            "question": lambda index:
                f"\\text{{True or False: A vertex cut (separating set) is a set of vertices whose removal disconnects the graph.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Connectivity",
            "question": lambda index:
                f"\\text{{True or False: A single cut vertex forms a vertex cut of size 1.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Connectivity",
            "question": lambda index:
                f"\\text{{True or False: Every connected graph has at least one cut vertex.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Hard"
        },

        # --- Strongly vs. Weakly Connected ---
        {
            "topic": "Connectivity",
            "question": lambda index:
                f"\\text{{True or False: A directed graph is strongly connected if there is a directed path between every ordered pair of vertices.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Connectivity",
            "question": lambda index:
                f"\\text{{True or False: A directed graph is weakly connected if its underlying undirected graph is connected.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Connectivity",
            "question": lambda index:
                f"\\text{{True or False: Every strongly connected graph is also weakly connected.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Connectivity",
            "question": lambda index:
                f"\\text{{True or False: Every weakly connected directed graph is also strongly connected.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },
        {
            "topic": "Connectivity",
            "question": lambda index:
                f"\\text{{True or False: A directed graph can be weakly connected but not strongly connected.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },

#endregion

#region Graph Theory

        # --- Adjacency Lists vs. Matrices ---
        {
            "topic": "Graph Theory",
            "question": lambda index:
                f"\\text{{True or False: An adjacency matrix for a graph with n vertices requires O(n²) space.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Graph Theory",
            "question": lambda index:
                f"\\text{{True or False: An adjacency list representation requires O(n²) space for a sparse graph.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },
        {
            "topic": "Graph Theory",
            "question": lambda index:
                f"\\text{{True or False: Adjacency matrices allow O(1) edge-existence queries.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Graph Theory",
            "question": lambda index:
                f"\\text{{True or False: Adjacency lists are more space-efficient than adjacency matrices for sparse graphs.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Graph Theory",
            "question": lambda index:
                f"\\text{{True or False: Adjacency matrices are more space-efficient than adjacency lists for sparse graphs.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },
        {
            "topic": "Graph Theory",
            "question": lambda index:
                f"\\text{{True or False: Adjacency lists are more efficient than adjacency matrices for iterating over all neighbors of a vertex.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Graph Theory",
            "question": lambda index:
                f"\\text{{True or False: Adjacency matrices are more efficient than adjacency lists for iterating over all neighbors of a vertex.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },
        {
            "topic": "Graph Theory",
            "question": lambda index:
                f"\\text{{True or False: The adjacency matrix of an undirected graph is always symmetric.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Graph Theory",
            "question": lambda index:
                f"\\text{{True or False: The adjacency matrix of a directed graph is always symmetric.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Easy"
        },

        # --- Undirected & Directed Graphs ---
        {
            "topic": "Graph Theory",
            "question": lambda index:
                f"\\text{{True or False: In an undirected graph, edges have no orientation.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Graph Theory",
            "question": lambda index:
                f"\\text{{True or False: In a directed graph (digraph), each edge has a direction from one vertex to another.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Graph Theory",
            "question": lambda index:
                f"\\text{{True or False: A multigraph allows multiple edges between the same pair of vertices.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Graph Theory",
            "question": lambda index:
                f"\\text{{True or False: A simple graph allows multiple edges between the same pair of vertices.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Easy"
        },
        {
            "topic": "Graph Theory",
            "question": lambda index:
                f"\\text{{True or False: A pseudograph allows loops (edges from a vertex to itself).}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Graph Theory",
            "question": lambda index:
                f"\\text{{True or False: A simple graph allows loops.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Easy"
        },

        # --- Order & Size ---
        {
            "topic": "Graph Theory",
            "question": lambda index:
                f"\\text{{True or False: The order of a graph is the number of vertices.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Graph Theory",
            "question": lambda index:
                f"\\text{{True or False: The size of a graph is the number of edges.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Graph Theory",
            "question": lambda index:
                f"\\text{{True or False: The order of a graph is the number of edges.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Easy"
        },
        {
            "topic": "Graph Theory",
            "question": lambda index:
                f"\\text{{True or False: The maximum size of a simple undirected graph with n vertices is n(n-1)/2.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Graph Theory",
            "question": lambda index:
                f"\\text{{True or False: The maximum size of a simple directed graph with n vertices is n(n-1).}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Graph Theory",
            "question": lambda index:
                f"\\text{{True or False: The maximum size of a simple undirected graph with n vertices is n(n-1).}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },
        {
            "topic": "Graph Theory",
            "question": lambda index:
                f"\\text{{True or False: The maximum size of a simple directed graph with n vertices is n(n-1)/2.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },

        # --- Degree, Pendant, Isolated ---
        {
            "topic": "Graph Theory",
            "question": lambda index:
                f"\\text{{True or False: The degree of a vertex is the number of edges incident to it.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Graph Theory",
            "question": lambda index:
                f"\\text{{True or False: A pendant vertex is a vertex of degree 1.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Graph Theory",
            "question": lambda index:
                f"\\text{{True or False: An isolated vertex is a vertex of degree 0.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Graph Theory",
            "question": lambda index:
                f"\\text{{True or False: A pendant vertex is a vertex of degree 0.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Easy"
        },
        {
            "topic": "Graph Theory",
            "question": lambda index:
                f"\\text{{True or False: An isolated vertex is a vertex of degree 1.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Easy"
        },

        # --- In-degree, Out-degree ---
        {
            "topic": "Graph Theory",
            "question": lambda index:
                f"\\text{{True or False: The in-degree of a vertex in a directed graph is the number of edges directed toward it.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Graph Theory",
            "question": lambda index:
                f"\\text{{True or False: The out-degree of a vertex in a directed graph is the number of edges directed away from it.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Graph Theory",
            "question": lambda index:
                f"\\text{{True or False: The sum of all in-degrees equals the sum of all out-degrees in a directed graph.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Graph Theory",
            "question": lambda index:
                f"\\text{{True or False: The sum of all in-degrees in a directed graph equals the number of edges.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Graph Theory",
            "question": lambda index:
                f"\\text{{True or False: The sum of all out-degrees in a directed graph equals the number of edges.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Graph Theory",
            "question": lambda index:
                f"\\text{{True or False: The sum of all in-degrees in a directed graph equals twice the number of edges.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },

        # --- Handshaking Theorem ---
        {
            "topic": "Graph Theory",
            "question": lambda index:
                f"\\text{{True or False: The handshaking theorem states that the sum of all vertex degrees equals twice the number of edges.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Graph Theory",
            "question": lambda index:
                f"\\text{{True or False: The handshaking theorem states that the sum of all vertex degrees equals the number of edges.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Easy"
        },
        {
            "topic": "Graph Theory",
            "question": lambda index:
                f"\\text{{True or False: The handshaking theorem implies that the number of vertices with odd degree must be even.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Graph Theory",
            "question": lambda index:
                f"\\text{{True or False: A graph can have an odd number of vertices with odd degree.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },

        # --- Special Graph Families ---
        {
            "topic": "Graph Theory",
            "question": lambda index:
                f"\\text{{True or False: The complete graph Kₙ has an edge between every pair of distinct vertices.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Graph Theory",
            "question": lambda index:
                f"\\text{{True or False: The cycle graph Cₙ is a graph where every vertex has degree exactly 2.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Graph Theory",
            "question": lambda index:
                f"\\text{{True or False: The wheel graph Wₙ is formed by connecting a single hub vertex to every vertex of a cycle graph Cₙ.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Graph Theory",
            "question": lambda index:
                f"\\text{{True or False: The hub vertex of a wheel graph Wₙ has degree n.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Graph Theory",
            "question": lambda index:
                f"\\text{{True or False: The hub vertex of a wheel graph Wₙ has degree 2.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },

        # --- Bipartite Graphs ---
        {
            "topic": "Graph Theory",
            "question": lambda index:
                f"\\text{{True or False: A bipartite graph has its vertices partitioned into two disjoint sets with edges only between the sets.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Graph Theory",
            "question": lambda index:
                f"\\text{{True or False: A bipartite graph can have edges within the same partition set.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Easy"
        },
        {
            "topic": "Graph Theory",
            "question": lambda index:
                f"\\text{{True or False: A graph is bipartite if and only if it contains no odd-length cycles.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Hard"
        },
        {
            "topic": "Graph Theory",
            "question": lambda index:
                f"\\text{{True or False: A complete bipartite graph Km,n has m · n edges.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },

        # --- Matching ---
        {
            "topic": "Graph Theory",
            "question": lambda index:
                f"\\text{{True or False: A matching in a graph is a set of edges with no two edges sharing an endpoint.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Graph Theory",
            "question": lambda index:
                f"\\text{{True or False: A maximum matching is a matching with the largest possible number of edges.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Graph Theory",
            "question": lambda index:
                f"\\text{{True or False: A perfect matching is one where every vertex is matched.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Graph Theory",
            "question": lambda index:
                f"\\text{{True or False: Every maximum matching is also a perfect matching.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Hard"
        },

        # --- Subgraphs & Induced Subgraphs ---
        {
            "topic": "Graph Theory",
            "question": lambda index:
                f"\\text{{True or False: A subgraph of G is a graph whose vertices and edges are subsets of those of G.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Graph Theory",
            "question": lambda index:
                f"\\text{{True or False: An induced subgraph on a vertex set S contains all edges of G that have both endpoints in S.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Graph Theory",
            "question": lambda index:
                f"\\text{{True or False: An induced subgraph on a vertex set S may omit edges of G that have both endpoints in S.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },
        {
            "topic": "Graph Theory",
            "question": lambda index:
                f"\\text{{True or False: Every induced subgraph is a subgraph, but not every subgraph is an induced subgraph.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Hard"
        },

#endregion

#region Binomial

        # --- Binomial Expressions ---
        {
            "topic": "Binomial",
            "question": lambda index:
                f"\\text{{True or False: A binomial expression is the sum of exactly two terms.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Binomial",
            "question": lambda index:
                f"\\text{{True or False: A binomial expression is the sum of exactly three terms.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Easy"
        },
        {
            "topic": "Binomial",
            "question": lambda index:
                f"\\text{{True or False: The binomial theorem states that (x+y)ⁿ = Σₖ₌₀ⁿ C(n,k) xⁿ⁻ᵏ yᵏ.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Binomial",
            "question": lambda index:
                f"\\text{{True or False: The binomial theorem states that (x+y)ⁿ = Σₖ₌₀ⁿ C(n,k) xᵏ yᵏ.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },
        {
            "topic": "Binomial",
            "question": lambda index:
                f"\\text{{True or False: The expansion of (x+y)ⁿ has exactly n+1 terms.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Binomial",
            "question": lambda index:
                f"\\text{{True or False: The expansion of (x+y)ⁿ has exactly n terms.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },
        {
            "topic": "Binomial",
            "question": lambda index:
                f"\\text{{True or False: Setting x = y = 1 in the binomial theorem gives Σₖ₌₀ⁿ C(n,k) = 2ⁿ.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },

        # --- Binomial Coefficients ---
        {
            "topic": "Binomial",
            "question": lambda index:
                f"\\text{{True or False: The binomial coefficient C(n,k) equals n! / (k!(n-k)!).}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Binomial",
            "question": lambda index:
                f"\\text{{True or False: The binomial coefficient C(n,k) equals n! / (k! · k!).}}",
            "answer": lambda index:
                "False",
            "difficulty": "Easy"
        },
        {
            "topic": "Binomial",
            "question": lambda index:
                f"\\text{{True or False: C(n,k) = C(n, n-k) for all valid n and k.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Binomial",
            "question": lambda index:
                f"\\text{{True or False: C(n,0) = 1 for all n ≥ 0.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Binomial",
            "question": lambda index:
                f"\\text{{True or False: C(n,n) = n for all n ≥ 1.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Easy"
        },

        # --- Pascal's Identity ---
        {
            "topic": "Binomial",
            "question": lambda index:
                f"\\text{{True or False: Pascal's identity states that C(n+1, k) = C(n, k-1) + C(n, k).}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Binomial",
            "question": lambda index:
                f"\\text{{True or False: Pascal's identity states that C(n+1, k) = C(n, k) · C(n, k-1).}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },
        {
            "topic": "Binomial",
            "question": lambda index:
                f"\\text{{True or False: Pascal's identity is the rule used to construct Pascal's triangle.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Binomial",
            "question": lambda index:
                f"\\text{{True or False: In Pascal's triangle, each entry is the product of the two entries above it.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Easy"
        },
        {
            "topic": "Binomial",
            "question": lambda index:
                f"\\text{{True or False: The n-th row of Pascal's triangle (starting at row 0) gives the coefficients of (x+y)ⁿ.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },

        # --- Vandermonde's Identity ---
        {
            "topic": "Binomial",
            "question": lambda index:
                f"\\text{{True or False: Vandermonde's identity states that C(m+n, r) = Σₖ₌₀ʳ C(m, r-k) · C(n, k).}}",
            "answer": lambda index:
                "True",
            "difficulty": "Hard"
        },
        {
            "topic": "Binomial",
            "question": lambda index:
                f"\\text{{True or False: Vandermonde's identity states that C(m+n, r) = C(m, r) · C(n, r).}}",
            "answer": lambda index:
                "False",
            "difficulty": "Hard"
        },
        {
            "topic": "Binomial",
            "question": lambda index:
                f"\\text{{True or False: Vandermonde's identity can be proved using a combinatorial argument about choosing r items from two groups.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Hard"
        },
        {
            "topic": "Binomial",
            "question": lambda index:
                f"\\text{{True or False: Setting m = n = r in Vandermonde's identity gives C(2n, n) = Σₖ₌₀ⁿ C(n,k)².}}",
            "answer": lambda index:
                "True",
            "difficulty": "Hard"
        },

#endregion

#region Historians

        # --- Euler ---
        {
            "topic": "Historians",
            "question": lambda index:
                f"\\text{{True or False: Leonhard Euler is credited with founding graph theory through his solution to the Königsberg bridge problem.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Historians",
            "question": lambda index:
                f"\\text{{True or False: Euler solved the Königsberg bridge problem by finding a valid route crossing each bridge exactly once.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },
        {
            "topic": "Historians",
            "question": lambda index:
                f"\\text{{True or False: Euler proved that the Königsberg bridge problem has no solution because not all vertices had even degree.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Historians",
            "question": lambda index:
                f"\\text{{True or False: Euler introduced the formula v - e + f = 2 for connected planar graphs.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },

        # --- Hamilton ---
        {
            "topic": "Historians",
            "question": lambda index:
                f"\\text{{True or False: William Rowan Hamilton invented the Icosian game, which involved finding cycles visiting every vertex of a dodecahedron exactly once.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Historians",
            "question": lambda index:
                f"\\text{{True or False: Hamilton cycles are named after William Rowan Hamilton.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Historians",
            "question": lambda index:
                f"\\text{{True or False: William Rowan Hamilton is primarily known for his contributions to graph coloring.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },

        # --- Petersen ---
        {
            "topic": "Historians",
            "question": lambda index:
                f"\\text{{True or False: Julius Petersen is the mathematician after whom the Petersen graph is named.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Historians",
            "question": lambda index:
                f"\\text{{True or False: Julius Petersen made significant contributions to graph theory in the late 19th century.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },

        # --- Pascal ---
        {
            "topic": "Historians",
            "question": lambda index:
                f"\\text{{True or False: Blaise Pascal is associated with Pascal's triangle and Pascal's identity for binomial coefficients.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Historians",
            "question": lambda index:
                f"\\text{{True or False: Pascal's triangle was first discovered by Blaise Pascal.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Hard"
        },
        {
            "topic": "Historians",
            "question": lambda index:
                f"\\text{{True or False: Versions of Pascal's triangle were known in China and Persia centuries before Pascal.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Hard"
        },

        # --- Newton ---
        {
            "topic": "Historians",
            "question": lambda index:
                f"\\text{{True or False: Isaac Newton generalized the binomial theorem to non-integer exponents.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Historians",
            "question": lambda index:
                f"\\text{{True or False: Newton's generalization of the binomial theorem applies only to positive integer exponents.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },

        # --- Fibonacci ---
        {
            "topic": "Historians",
            "question": lambda index:
                f"\\text{{True or False: Fibonacci introduced the Hindu-Arabic numeral system to Europe through his book Liber Abaci.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Historians",
            "question": lambda index:
                f"\\text{{True or False: The Fibonacci sequence was invented by Fibonacci and was previously unknown outside Europe.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Hard"
        },
        {
            "topic": "Historians",
            "question": lambda index:
                f"\\text{{True or False: The Fibonacci sequence had been described in Indian mathematics before Fibonacci's work.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Hard"
        },

        # --- Sloane ---
        {
            "topic": "Historians",
            "question": lambda index:
                f"\\text{{True or False: Neil Sloane is the founder of the On-Line Encyclopedia of Integer Sequences (OEIS).}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Historians",
            "question": lambda index:
                f"\\text{{True or False: The OEIS is a database of integer sequences used extensively in combinatorics and discrete mathematics.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Historians",
            "question": lambda index:
                f"\\text{{True or False: Neil Sloane is primarily known for his contributions to graph coloring theory.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },

        # --- Frank Ruskey ---
        {
            "topic": "Historians",
            "question": lambda index:
                f"\\text{{True or False: Frank Ruskey is a Canadian mathematician known for his work in combinatorial generation and combinatorics.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Historians",
            "question": lambda index:
                f"\\text{{True or False: Frank Ruskey is associated with the Combinatorial Object Server and research into combinatorial algorithms.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Hard"
        },

        # --- Brendan McKay ---
        {
            "topic": "Historians",
            "question": lambda index:
                f"\\text{{True or False: Brendan McKay is known for the nauty software used for graph isomorphism and canonical labelling.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Hard"
        },
        {
            "topic": "Historians",
            "question": lambda index:
                f"\\text{{True or False: Brendan McKay is an Australian mathematician with major contributions to combinatorics and graph theory.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Historians",
            "question": lambda index:
                f"\\text{{True or False: Brendan McKay is primarily known for proving the Four Color Theorem.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },
        #endregion

#region Functions

        # --- Definition, Domain, Codomain ---
        {
            "topic": "Functions",
            "question": lambda index:
                f"\\text{{True or False: A function from A to B assigns exactly one element of B to each element of A.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Functions",
            "question": lambda index:
                f"\\text{{True or False: A function from A to B can assign more than one element of B to a single element of A.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Easy"
        },
        {
            "topic": "Functions",
            "question": lambda index:
                f"\\text{{True or False: The domain of a function f: A → B is the set A.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Functions",
            "question": lambda index:
                f"\\text{{True or False: The codomain of a function f: A → B is the set B.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Functions",
            "question": lambda index:
                f"\\text{{True or False: The range of a function is always equal to its codomain.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },
        {
            "topic": "Functions",
            "question": lambda index:
                f"\\text{{True or False: The range of a function is a subset of its codomain.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },

        # --- Injection, Surjection, Bijection ---
        {
            "topic": "Functions",
            "question": lambda index:
                f"\\text{{True or False: A function is injective (one-to-one) if different inputs always produce different outputs.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Functions",
            "question": lambda index:
                f"\\text{{True or False: A function f is injective if f(a) = f(b) implies a = b.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Functions",
            "question": lambda index:
                f"\\text{{True or False: A function is surjective (onto) if every element of the codomain is the image of at least one element of the domain.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Functions",
            "question": lambda index:
                f"\\text{{True or False: A function is surjective if every element of the domain maps to every element of the codomain.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },
        {
            "topic": "Functions",
            "question": lambda index:
                f"\\text{{True or False: A bijection is a function that is both injective and surjective.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Functions",
            "question": lambda index:
                f"\\text{{True or False: A bijection is also called a one-to-one correspondence.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Functions",
            "question": lambda index:
                f"\\text{{True or False: A bijection from A to B implies |A| = |B|.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Functions",
            "question": lambda index:
                f"\\text{{True or False: If f: A → B is injective and |A| = |B|, then f is bijective.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Hard"
        },

        # --- Identity & Inverses ---
        {
            "topic": "Functions",
            "question": lambda index:
                f"\\text{{True or False: The identity function maps every element to itself.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Functions",
            "question": lambda index:
                f"\\text{{True or False: A function has an inverse if and only if it is a bijection.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Functions",
            "question": lambda index:
                f"\\text{{True or False: A function has an inverse if and only if it is injective.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },
        {
            "topic": "Functions",
            "question": lambda index:
                f"\\text{{True or False: If f is a bijection, then f⁻¹ ∘ f is the identity function.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Functions",
            "question": lambda index:
                f"\\text{{True or False: Function composition is commutative, i.e., f ∘ g = g ∘ f always.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },

        # --- Floor & Ceiling ---
        {
            "topic": "Functions",
            "question": lambda index:
                f"\\text{{True or False: The floor function ⌊x⌋ is the largest integer less than or equal to x.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Functions",
            "question": lambda index:
                f"\\text{{True or False: The ceiling function ⌈x⌉ is the smallest integer greater than or equal to x.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Functions",
            "question": lambda index:
                f"\\text{{True or False: ⌊3.7⌋ = 4.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Easy"
        },
        {
            "topic": "Functions",
            "question": lambda index:
                f"\\text{{True or False: ⌈3.2⌉ = 4.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Functions",
            "question": lambda index:
                f"\\text{{True or False: For any integer n, ⌊n⌋ = ⌈n⌉ = n.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Functions",
            "question": lambda index:
                f"\\text{{True or False: ⌊-2.3⌋ = -2.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },
        {
            "topic": "Functions",
            "question": lambda index:
                f"\\text{{True or False: ⌊-2.3⌋ = -3.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },

        # --- Factorial ---
        {
            "topic": "Functions",
            "question": lambda index:
                f"\\text{{True or False: The factorial function is defined as n! = n · (n-1) · ... · 2 · 1 for positive integers n.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Functions",
            "question": lambda index:
                f"\\text{{True or False: 0! = 0.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Easy"
        },
        {
            "topic": "Functions",
            "question": lambda index:
                f"\\text{{True or False: 0! = 1.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Functions",
            "question": lambda index:
                f"\\text{{True or False: The factorial function grows faster than any exponential function.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Hard"
        },

#endregion

#region Sums and Sequences

        # --- Sequence Definition ---
        {
            "topic": "Sums and Sequences",
            "question": lambda index:
                f"\\text{{True or False: A sequence is an ordered list of elements, often defined by a formula for the nth term.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Sums and Sequences",
            "question": lambda index:
                f"\\text{{True or False: A sequence is an unordered collection of elements.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Easy"
        },
        {
            "topic": "Sums and Sequences",
            "question": lambda index:
                f"\\text{{True or False: A finite sequence has a last term while an infinite sequence does not.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },

        # --- Summation ---
        {
            "topic": "Sums and Sequences",
            "question": lambda index:
                f"\\text{{True or False: The notation Σᵢ₌₁ⁿ aᵢ represents the sum a₁ + a₂ + ... + aₙ.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Sums and Sequences",
            "question": lambda index:
                f"\\text{{True or False: Σᵢ₌₁ⁿ c · aᵢ = c · Σᵢ₌₁ⁿ aᵢ for any constant c.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Sums and Sequences",
            "question": lambda index:
                f"\\text{{True or False: Σᵢ₌₁ⁿ (aᵢ + bᵢ) = (Σᵢ₌₁ⁿ aᵢ) + (Σᵢ₌₁ⁿ bᵢ).}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Sums and Sequences",
            "question": lambda index:
                f"\\text{{True or False: Σᵢ₌₁ⁿ c = c · n for any constant c.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Sums and Sequences",
            "question": lambda index:
                f"\\text{{True or False: Σᵢ₌₁ⁿ c = c for any constant c.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Easy"
        },

        # --- Arithmetic Progression ---
        {
            "topic": "Sums and Sequences",
            "question": lambda index:
                f"\\text{{True or False: An arithmetic progression has a constant difference between consecutive terms.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Sums and Sequences",
            "question": lambda index:
                f"\\text{{True or False: An arithmetic progression has a constant ratio between consecutive terms.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Easy"
        },
        {
            "topic": "Sums and Sequences",
            "question": lambda index:
                f"\\text{{True or False: The sum of the first n terms of an arithmetic progression is n(a₁ + aₙ)/2.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Sums and Sequences",
            "question": lambda index:
                f"\\text{{True or False: The arithmetic series formula Σᵢ₌₁ⁿ i = n(n+1)/2.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Sums and Sequences",
            "question": lambda index:
                f"\\text{{True or False: The arithmetic series formula Σᵢ₌₁ⁿ i = n(n-1)/2.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },

        # --- Geometric Progression ---
        {
            "topic": "Sums and Sequences",
            "question": lambda index:
                f"\\text{{True or False: A geometric progression has a constant ratio between consecutive terms.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Sums and Sequences",
            "question": lambda index:
                f"\\text{{True or False: The geometric series Σᵢ₌₀ⁿ rⁱ = (rⁿ⁺¹ - 1)/(r - 1) for r ≠ 1.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Sums and Sequences",
            "question": lambda index:
                f"\\text{{True or False: The geometric series Σᵢ₌₀ⁿ rⁱ = (rⁿ - 1)/(r - 1) for r ≠ 1.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },
        {
            "topic": "Sums and Sequences",
            "question": lambda index:
                f"\\text{{True or False: The sum of squares formula is Σᵢ₌₁ⁿ i² = n(n+1)(2n+1)/6.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Sums and Sequences",
            "question": lambda index:
                f"\\text{{True or False: The sum of squares formula is Σᵢ₌₁ⁿ i² = n²(n+1)²/4.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },
        {
            "topic": "Sums and Sequences",
            "question": lambda index:
                f"\\text{{True or False: The sum of cubes formula is Σᵢ₌₁ⁿ i³ = (n(n+1)/2)².}}",
            "answer": lambda index:
                "True",
            "difficulty": "Hard"
        },

        # --- Special Sequences ---
        {
            "topic": "Sums and Sequences",
            "question": lambda index:
                f"\\text{{True or False: The Fibonacci sequence is defined by F(n) = F(n-1) + F(n-2), with F(1) = F(2) = 1.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Sums and Sequences",
            "question": lambda index:
                f"\\text{{True or False: The Fibonacci sequence is defined by F(n) = F(n-1) · F(n-2).}}",
            "answer": lambda index:
                "False",
            "difficulty": "Easy"
        },
        {
            "topic": "Sums and Sequences",
            "question": lambda index:
                f"\\text{{True or False: 2 is the only even prime number.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Sums and Sequences",
            "question": lambda index:
                f"\\text{{True or False: The sequence of prime numbers is finite.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Easy"
        },
        {
            "topic": "Sums and Sequences",
            "question": lambda index:
                f"\\text{{True or False: The Ulam numbers begin 1, 2, 3, 4, 6, ... where each term is uniquely the sum of two distinct earlier terms.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Hard"
        },
        {
            "topic": "Sums and Sequences",
            "question": lambda index:
                f"\\text{{True or False: Aronson's sequence is a self-describing sequence about the positions of the letter 't' in its own English description.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Hard"
        },
        {
            "topic": "Sums and Sequences",
            "question": lambda index:
                f"\\text{{True or False: A perfect number equals the sum of its proper divisors.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Sums and Sequences",
            "question": lambda index:
                f"\\text{{True or False: 6 is a perfect number.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Sums and Sequences",
            "question": lambda index:
                f"\\text{{True or False: 12 is a perfect number.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },

        # --- Subsequences & Index Manipulation ---
        {
            "topic": "Sums and Sequences",
            "question": lambda index:
                f"\\text{{True or False: A subsequence is formed by deleting some elements from a sequence without changing the order of the remaining elements.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Sums and Sequences",
            "question": lambda index:
                f"\\text{{True or False: Splitting a sum Σᵢ₌₁ⁿ aᵢ at index k gives Σᵢ₌₁ᵏ aᵢ + Σᵢ₌ₖ₊₁ⁿ aᵢ.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Sums and Sequences",
            "question": lambda index:
                f"\\text{{True or False: The index of summation can always be shifted without changing the value of the sum.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },

#endregion

#region Induction

        # --- Definitions ---
        {
            "topic": "Induction",
            "question": lambda index:
                f"\\text{{True or False: Mathematical induction consists of a basis step and an inductive step.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Induction",
            "question": lambda index:
                f"\\text{{True or False: The basis step of induction proves the statement for all n simultaneously.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Easy"
        },
        {
            "topic": "Induction",
            "question": lambda index:
                f"\\text{{True or False: The basis step of induction proves the statement for the smallest value of n.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Induction",
            "question": lambda index:
                f"\\text{{True or False: The inductive step assumes the statement holds for n = k and proves it for n = k + 1.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Induction",
            "question": lambda index:
                f"\\text{{True or False: The inductive hypothesis is the assumption that the statement holds for n = k.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Induction",
            "question": lambda index:
                f"\\text{{True or False: In weak induction, the inductive step only uses the case n = k to prove n = k + 1.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Induction",
            "question": lambda index:
                f"\\text{{True or False: In strong induction, the inductive step assumes the statement holds for all values from the base case up to k.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Induction",
            "question": lambda index:
                f"\\text{{True or False: Strong induction can prove strictly more theorems than weak induction.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Hard"
        },
        {
            "topic": "Induction",
            "question": lambda index:
                f"\\text{{True or False: Strong induction and weak induction are logically equivalent.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Hard"
        },

        # --- Validity Examples ---
        {
            "topic": "Induction",
            "question": lambda index:
                f"\\text{{True or False: The following induction is valid — Basis: 1 = 1(1+1)/2 = 1 ✓. Inductive step: assume Σᵢ₌₁ᵏ i = k(k+1)/2, then Σᵢ₌₁ᵏ⁺¹ i = k(k+1)/2 + (k+1) = (k+1)(k+2)/2. ✓}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Induction",
            "question": lambda index:
                f"\\text{{True or False: An induction proof is valid if the inductive step is proved but the basis step is omitted.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },
        {
            "topic": "Induction",
            "question": lambda index:
                f"\\text{{True or False: An induction proof is valid if the basis step is proved but the inductive step is omitted.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },
        {
            "topic": "Induction",
            "question": lambda index:
                f"\\text{{True or False: The following induction is INVALID — Basis: P(1) ✓. Inductive step: assume P(k) is true, and claim P(k+1) is true without proof. This is circular reasoning.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Induction",
            "question": lambda index:
                f"\\text{{True or False: Mathematical induction can only prove statements about natural numbers.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Hard"
        },
        {
            "topic": "Induction",
            "question": lambda index:
                f"\\text{{True or False: Structural induction generalizes mathematical induction to recursively defined structures.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Hard"
        },

#endregion

#region Recurrences

        # --- Definition ---
        {
            "topic": "Recurrences",
            "question": lambda index:
                f"\\text{{True or False: A recurrence relation defines each term of a sequence using one or more previous terms.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Recurrences",
            "question": lambda index:
                f"\\text{{True or False: A recurrence relation requires initial conditions to uniquely define a sequence.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Recurrences",
            "question": lambda index:
                f"\\text{{True or False: A recurrence relation uniquely defines a sequence without any initial conditions.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Easy"
        },
        {
            "topic": "Recurrences",
            "question": lambda index:
                f"\\text{{True or False: The Fibonacci sequence satisfies the recurrence F(n) = F(n-1) + F(n-2).}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },

        # --- Evaluating Recurrences ---
        {
            "topic": "Recurrences",
            "question": lambda index:
                f"\\text{{True or False: For T(n) = 2T(n-1) with T(1) = 1, the value T(3) = 4.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Recurrences",
            "question": lambda index:
                f"\\text{{True or False: For T(n) = 2T(n-1) with T(1) = 1, the value T(3) = 6.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },
        {
            "topic": "Recurrences",
            "question": lambda index:
                f"\\text{{True or False: For T(n) = T(n-1) + 3 with T(1) = 1, the value T(3) = 7.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Recurrences",
            "question": lambda index:
                f"\\text{{True or False: For T(n) = T(n-1) + n with T(1) = 1, the value T(3) = 6.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Recurrences",
            "question": lambda index:
                f"\\text{{True or False: For T(n) = T(n-1) + n with T(1) = 1, the value T(3) = 9.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },

        # --- Compound Interest ---
        {
            "topic": "Recurrences",
            "question": lambda index:
                f"\\text{{True or False: Compound interest can be modelled by the recurrence P(n) = P(n-1) · (1 + r), where r is the interest rate.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Recurrences",
            "question": lambda index:
                f"\\text{{True or False: Compound interest can be modelled by the recurrence P(n) = P(n-1) + r, where r is a constant interest amount.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },
        {
            "topic": "Recurrences",
            "question": lambda index:
                f"\\text{{True or False: The closed-form solution to P(n) = P(n-1) · (1+r) with P(0) = P₀ is P(n) = P₀ · (1+r)ⁿ.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Recurrences",
            "question": lambda index:
                f"\\text{{True or False: A linear recurrence relation has each term as a linear combination of previous terms.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Recurrences",
            "question": lambda index:
                f"\\text{{True or False: The characteristic root method applies to linear homogeneous recurrences with constant coefficients.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Hard"
        },
        {
            "topic": "Recurrences",
            "question": lambda index:
                f"\\text{{True or False: A homogeneous recurrence has a nonzero constant term added to the linear combination of previous terms.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Hard"
        },

#endregion

#region Counting

        # --- Product & Sum Rules ---
        {
            "topic": "Counting",
            "question": lambda index:
                f"\\text{{True or False: The product rule states that if a task can be done in n₁ ways and a second task in n₂ ways, the two tasks together can be done in n₁ · n₂ ways.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Counting",
            "question": lambda index:
                f"\\text{{True or False: The product rule states that if a task can be done in n₁ ways and a second task in n₂ ways, the two tasks together can be done in n₁ + n₂ ways.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Easy"
        },
        {
            "topic": "Counting",
            "question": lambda index:
                f"\\text{{True or False: The sum rule states that if a task can be done in n₁ ways or n₂ ways (mutually exclusive), then there are n₁ + n₂ ways to do it.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Counting",
            "question": lambda index:
                f"\\text{{True or False: The sum rule applies only when the two sets of choices overlap.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Easy"
        },

        # --- Pigeonhole Principle ---
        {
            "topic": "Counting",
            "question": lambda index:
                f"\\text{{True or False: The pigeonhole principle states that if n+1 objects are placed in n boxes, at least one box contains more than one object.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Counting",
            "question": lambda index:
                f"\\text{{True or False: The pigeonhole principle states that if n objects are placed in n boxes, at least one box contains more than one object.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Easy"
        },
        {
            "topic": "Counting",
            "question": lambda index:
                f"\\text{{True or False: The generalized pigeonhole principle states that if N objects are placed in k boxes, at least one box contains at least ⌈N/k⌉ objects.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Counting",
            "question": lambda index:
                f"\\text{{True or False: The generalized pigeonhole principle states that if N objects are placed in k boxes, at least one box contains at least ⌊N/k⌋ objects.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },

        # --- Permutations ---
        {
            "topic": "Counting",
            "question": lambda index:
                f"\\text{{True or False: A permutation of n distinct objects is an ordered arrangement of all n objects.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Counting",
            "question": lambda index:
                f"\\text{{True or False: The number of permutations of n distinct objects is n!.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Counting",
            "question": lambda index:
                f"\\text{{True or False: An r-permutation P(n,r) is an ordered selection of r objects from n distinct objects.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Counting",
            "question": lambda index:
                f"\\text{{True or False: P(n,r) = n! / (n-r)!.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Counting",
            "question": lambda index:
                f"\\text{{True or False: P(n,r) = n! / r!.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Easy"
        },
        {
            "topic": "Counting",
            "question": lambda index:
                f"\\text{{True or False: The number of permutations of n objects where n₁ are identical of type 1, n₂ of type 2, ..., is n! / (n₁! · n₂! · ...).}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Counting",
            "question": lambda index:
                f"\\text{{True or False: The number of ways to arrange n objects in a circle is (n-1)!.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Counting",
            "question": lambda index:
                f"\\text{{True or False: The number of ways to arrange n objects in a circle is n!.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },

        # --- Combinations ---
        {
            "topic": "Counting",
            "question": lambda index:
                f"\\text{{True or False: An r-combination C(n,r) is an unordered selection of r objects from n distinct objects.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Counting",
            "question": lambda index:
                f"\\text{{True or False: C(n,r) = P(n,r) / r!.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Counting",
            "question": lambda index:
                f"\\text{{True or False: C(n,r) = C(n, n-r).}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Counting",
            "question": lambda index:
                f"\\text{{True or False: The number of r-combinations with repetition from n types is C(n+r-1, r).}}",
            "answer": lambda index:
                "True",
            "difficulty": "Hard"
        },
        {
            "topic": "Counting",
            "question": lambda index:
                f"\\text{{True or False: The number of r-combinations with repetition from n types is C(n+r, r).}}",
            "answer": lambda index:
                "False",
            "difficulty": "Hard"
        },

        # --- Inclusion-Exclusion ---
        {
            "topic": "Counting",
            "question": lambda index:
                f"\\text{{True or False: The principle of inclusion-exclusion is used to count elements in the union of overlapping sets.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Counting",
            "question": lambda index:
                f"\\text{{True or False: The principle of inclusion-exclusion subtracts overcounted intersections to avoid double-counting.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },

        # --- Combinatorial Proofs ---
        {
            "topic": "Counting",
            "question": lambda index:
                f"\\text{{True or False: A combinatorial proof establishes an identity by showing both sides count the same thing in different ways.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Counting",
            "question": lambda index:
                f"\\text{{True or False: A combinatorial proof uses algebraic manipulation to simplify both sides of an identity.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },
        {
            "topic": "Counting",
            "question": lambda index:
                f"\\text{{True or False: The identity C(n,r) = C(n-1, r-1) + C(n-1, r) has a combinatorial proof using whether a fixed element is included.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Hard"
        },

        # --- Stars and Bars ---
        {
            "topic": "Counting",
            "question": lambda index:
                f"\\text{{True or False: The number of ways to distribute n identical objects into k distinct bins is C(n+k-1, k-1).}}",
            "answer": lambda index:
                "True",
            "difficulty": "Hard"
        },
        {
            "topic": "Counting",
            "question": lambda index:
                f"\\text{{True or False: The number of ways to distribute n identical objects into k distinct bins is C(n+k, k).}}",
            "answer": lambda index:
                "False",
            "difficulty": "Hard"
        },

        # --- Derangements ---
        {
            "topic": "Counting",
            "question": lambda index:
                f"\\text{{True or False: A derangement is a permutation in which no element appears in its original position.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Hard"
        },
        {
            "topic": "Counting",
            "question": lambda index:
                f"\\text{{True or False: The number of derangements of n elements is exactly n!.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Hard"
        },

#endregion

#region Relations

        # --- Definitions ---
        {
            "topic": "Relations",
            "question": lambda index:
                f"\\text{{True or False: A relation R on a set A is a subset of A × A.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Relations",
            "question": lambda index:
                f"\\text{{True or False: A relation R is reflexive if (a, a) ∈ R for all a ∈ A.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Relations",
            "question": lambda index:
                f"\\text{{True or False: A relation R is reflexive if (a, b) ∈ R implies (b, a) ∈ R.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Easy"
        },
        {
            "topic": "Relations",
            "question": lambda index:
                f"\\text{{True or False: A relation R is symmetric if (a, b) ∈ R implies (b, a) ∈ R.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Relations",
            "question": lambda index:
                f"\\text{{True or False: A relation R is antisymmetric if (a, b) ∈ R and (b, a) ∈ R implies a = b.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Relations",
            "question": lambda index:
                f"\\text{{True or False: A relation can be both symmetric and antisymmetric.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Hard"
        },
        {
            "topic": "Relations",
            "question": lambda index:
                f"\\text{{True or False: The equality relation on any set is both symmetric and antisymmetric.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Hard"
        },
        {
            "topic": "Relations",
            "question": lambda index:
                f"\\text{{True or False: A relation R is transitive if (a,b) ∈ R and (b,c) ∈ R implies (a,c) ∈ R.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Relations",
            "question": lambda index:
                f"\\text{{True or False: A relation that is reflexive, symmetric, and transitive is called an equivalence relation.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Relations",
            "question": lambda index:
                f"\\text{{True or False: A relation that is reflexive, antisymmetric, and transitive is called a partial order.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Relations",
            "question": lambda index:
                f"\\text{{True or False: Every equivalence relation partitions its set into equivalence classes.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Relations",
            "question": lambda index:
                f"\\text{{True or False: Two elements in the same equivalence class must be related by R.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },

        # --- Transitive Closure ---
        {
            "topic": "Relations",
            "question": lambda index:
                f"\\text{{True or False: The transitive closure of R is the smallest transitive relation containing R.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Relations",
            "question": lambda index:
                f"\\text{{True or False: The transitive closure of R can be computed by taking the union of R, R², R³, ... up to Rⁿ for a relation on n elements.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Hard"
        },
        {
            "topic": "Relations",
            "question": lambda index:
                f"\\text{{True or False: The transitive closure is always equal to R itself.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },

        # --- Composition ---
        {
            "topic": "Relations",
            "question": lambda index:
                f"\\text{{True or False: The composition S ∘ R contains (a,c) whenever there exists b such that (a,b) ∈ R and (b,c) ∈ S.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Hard"
        },
        {
            "topic": "Relations",
            "question": lambda index:
                f"\\text{{True or False: Relation composition is always commutative.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Hard"
        },

#endregion
#region Proofs

        # --- Proof Types ---
        {
            "topic": "Proofs",
            "question": lambda index:
                f"\\text{{True or False: A direct proof proves p → q by assuming p and deriving q.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Proofs",
            "question": lambda index:
                f"\\text{{True or False: A proof by contrapositive proves p → q by assuming ¬q and deriving ¬p.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Proofs",
            "question": lambda index:
                f"\\text{{True or False: A proof by contrapositive proves p → q by assuming ¬p and deriving ¬q.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Easy"
        },
        {
            "topic": "Proofs",
            "question": lambda index:
                f"\\text{{True or False: A proof by contradiction assumes the negation of the statement and derives a contradiction.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Proofs",
            "question": lambda index:
                f"\\text{{True or False: A proof by cases proves a statement by exhaustively considering all possible cases.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Proofs",
            "question": lambda index:
                f"\\text{{True or False: A proof by cases is valid even if some cases are not covered.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },
        {
            "topic": "Proofs",
            "question": lambda index:
                f"\\text{{True or False: A counterexample disproves a universal statement by exhibiting one instance where it fails.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Proofs",
            "question": lambda index:
                f"\\text{{True or False: A single counterexample is sufficient to disprove a statement of the form 'for all x, P(x)'.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Proofs",
            "question": lambda index:
                f"\\text{{True or False: A counterexample can prove a universal statement to be true.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Easy"
        },

        # --- Well-Ordering ---
        {
            "topic": "Proofs",
            "question": lambda index:
                f"\\text{{True or False: The well-ordering property states that every nonempty set of positive integers has a least element.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Proofs",
            "question": lambda index:
                f"\\text{{True or False: The well-ordering property states that every nonempty set of integers has a least element.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },
        {
            "topic": "Proofs",
            "question": lambda index:
                f"\\text{{True or False: The well-ordering property is used to justify the validity of mathematical induction.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Hard"
        },

        # --- Vacuous & Trivial Proofs ---
        {
            "topic": "Proofs",
            "question": lambda index:
                f"\\text{{True or False: A vacuous proof of p → q shows that p is false, making the conditional true.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Proofs",
            "question": lambda index:
                f"\\text{{True or False: A trivial proof of p → q shows that q is true regardless of p.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },

        # --- Existence Proofs ---
        {
            "topic": "Proofs",
            "question": lambda index:
                f"\\text{{True or False: A constructive existence proof demonstrates an object exists by explicitly constructing it.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Proofs",
            "question": lambda index:
                f"\\text{{True or False: A non-constructive existence proof proves an object exists without explicitly constructing it.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },

#endregion

#region Integer Properties

        # --- Modulo & Divisibility ---
        {
            "topic": "Integer Properties",
            "question": lambda index:
                f"\\text{{True or False: a ≡ b (mod m) means m divides (a - b).}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Integer Properties",
            "question": lambda index:
                f"\\text{{True or False: a ≡ b (mod m) means a divides (b - m).}}",
            "answer": lambda index:
                "False",
            "difficulty": "Easy"
        },
        {
            "topic": "Integer Properties",
            "question": lambda index:
                f"\\text{{True or False: 17 ≡ 2 (mod 5).}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Integer Properties",
            "question": lambda index:
                f"\\text{{True or False: 17 ≡ 3 (mod 5).}}",
            "answer": lambda index:
                "False",
            "difficulty": "Easy"
        },
        {
            "topic": "Integer Properties",
            "question": lambda index:
                f"\\text{{True or False: If a ≡ b (mod m) and c ≡ d (mod m), then a + c ≡ b + d (mod m).}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Integer Properties",
            "question": lambda index:
                f"\\text{{True or False: If a ≡ b (mod m) and c ≡ d (mod m), then a · c ≡ b · d (mod m).}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },

        # --- Hash Functions & Pseudorandom ---
        {
            "topic": "Integer Properties",
            "question": lambda index:
                f"\\text{{True or False: A hash function maps keys to indices in a hash table, often using h(k) = k mod m.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Integer Properties",
            "question": lambda index:
                f"\\text{{True or False: A linear congruential generator produces pseudorandom numbers using xₙ₊₁ = (a·xₙ + c) mod m.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Integer Properties",
            "question": lambda index:
                f"\\text{{True or False: Pseudorandom numbers generated by a linear congruential generator are truly random.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Easy"
        },

        # --- Cryptography ---
        {
            "topic": "Integer Properties",
            "question": lambda index:
                f"\\text{{True or False: Caesar cipher encrypts by shifting each letter by a fixed number of positions in the alphabet.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Integer Properties",
            "question": lambda index:
                f"\\text{{True or False: In a Caesar cipher with shift k, encryption is c = (p + k) mod 26.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Integer Properties",
            "question": lambda index:
                f"\\text{{True or False: RSA encryption relies on the difficulty of factoring large integers.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Integer Properties",
            "question": lambda index:
                f"\\text{{True or False: RSA encryption is a symmetric-key cryptosystem.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },

        # --- Number Bases ---
        {
            "topic": "Integer Properties",
            "question": lambda index:
                f"\\text{{True or False: The binary representation of 10 (decimal) is 1010.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Integer Properties",
            "question": lambda index:
                f"\\text{{True or False: The binary representation of 10 (decimal) is 1100.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Easy"
        },
        {
            "topic": "Integer Properties",
            "question": lambda index:
                f"\\text{{True or False: The hexadecimal digit F represents the decimal value 15.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Integer Properties",
            "question": lambda index:
                f"\\text{{True or False: One hexadecimal digit corresponds to exactly 4 binary digits (bits).}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Integer Properties",
            "question": lambda index:
                f"\\text{{True or False: One hexadecimal digit corresponds to exactly 8 binary digits (bits).}}",
            "answer": lambda index:
                "False",
            "difficulty": "Easy"
        },

        # --- Fundamental Theorem of Arithmetic ---
        {
            "topic": "Integer Properties",
            "question": lambda index:
                f"\\text{{True or False: The fundamental theorem of arithmetic states every integer greater than 1 can be written uniquely as a product of primes.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Integer Properties",
            "question": lambda index:
                f"\\text{{True or False: The prime factorization of an integer greater than 1 is unique up to the order of factors.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Integer Properties",
            "question": lambda index:
                f"\\text{{True or False: 1 is a prime number.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Easy"
        },

        # --- Mersenne Primes ---
        {
            "topic": "Integer Properties",
            "question": lambda index:
                f"\\text{{True or False: A Mersenne prime is a prime of the form 2ⁿ - 1.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Integer Properties",
            "question": lambda index:
                f"\\text{{True or False: Every number of the form 2ⁿ - 1 is a Mersenne prime.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },
        {
            "topic": "Integer Properties",
            "question": lambda index:
                f"\\text{{True or False: 7 is a Mersenne prime.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },

        # --- GCD, LCM, Euclidean Algorithm ---
        {
            "topic": "Integer Properties",
            "question": lambda index:
                f"\\text{{True or False: The GCD of two integers is the largest integer that divides both of them.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Integer Properties",
            "question": lambda index:
                f"\\text{{True or False: The LCM of two integers is the smallest positive integer divisible by both.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Integer Properties",
            "question": lambda index:
                f"\\text{{True or False: gcd(a, b) · lcm(a, b) = a · b for positive integers a and b.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Integer Properties",
            "question": lambda index:
                f"\\text{{True or False: The Euclidean algorithm computes the GCD using repeated division: gcd(a,b) = gcd(b, a mod b).}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Integer Properties",
            "question": lambda index:
                f"\\text{{True or False: The Euclidean algorithm computes the GCD using repeated multiplication.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },
        {
            "topic": "Integer Properties",
            "question": lambda index:
                f"\\text{{True or False: gcd(a, 0) = a for any positive integer a.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Integer Properties",
            "question": lambda index:
                f"\\text{{True or False: Two integers are relatively prime if their GCD is 1.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },

#endregion

#region Boolean Algebra

        # --- Definitions ---
        {
            "topic": "Boolean Algebra",
            "question": lambda index:
                f"\\text{{True or False: Boolean algebra operates on values 0 and 1, corresponding to false and true.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Boolean Algebra",
            "question": lambda index:
                f"\\text{{True or False: The Boolean complement of 0 is 1.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Boolean Algebra",
            "question": lambda index:
                f"\\text{{True or False: The Boolean complement of 1 is 1.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Easy"
        },
        {
            "topic": "Boolean Algebra",
            "question": lambda index:
                f"\\text{{True or False: In Boolean algebra, x + 1 = 1 for any Boolean variable x.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Boolean Algebra",
            "question": lambda index:
                f"\\text{{True or False: In Boolean algebra, x · 0 = x for any Boolean variable x.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Easy"
        },
        {
            "topic": "Boolean Algebra",
            "question": lambda index:
                f"\\text{{True or False: In Boolean algebra, x · 0 = 0 for any Boolean variable x.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Boolean Algebra",
            "question": lambda index:
                f"\\text{{True or False: In Boolean algebra, x + x̄ = 1.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },
        {
            "topic": "Boolean Algebra",
            "question": lambda index:
                f"\\text{{True or False: In Boolean algebra, x · x̄ = 1.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Easy"
        },
        {
            "topic": "Boolean Algebra",
            "question": lambda index:
                f"\\text{{True or False: In Boolean algebra, x · x̄ = 0.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Easy"
        },

        # --- Laws ---
        {
            "topic": "Boolean Algebra",
            "question": lambda index:
                f"\\text{{True or False: The Boolean distributive law states x · (y + z) = (x · y) + (x · z).}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Boolean Algebra",
            "question": lambda index:
                f"\\text{{True or False: The Boolean distributive law states x + (y · z) = (x + y) · (x + z).}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Boolean Algebra",
            "question": lambda index:
                f"\\text{{True or False: De Morgan's law in Boolean algebra states (x · y)' = x' + y'.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Boolean Algebra",
            "question": lambda index:
                f"\\text{{True or False: De Morgan's law in Boolean algebra states (x + y)' = x' · y'.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Medium"
        },
        {
            "topic": "Boolean Algebra",
            "question": lambda index:
                f"\\text{{True or False: De Morgan's law in Boolean algebra states (x + y)' = x' + y'.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Medium"
        },

        # --- Boolean Functions & Normal Forms ---
        {
            "topic": "Boolean Algebra",
            "question": lambda index:
                f"\\text{{True or False: A Boolean function can be represented by a sum of minterms (disjunctive normal form).}}",
            "answer": lambda index:
                "True",
            "difficulty": "Hard"
        },
        {
            "topic": "Boolean Algebra",
            "question": lambda index:
                f"\\text{{True or False: A minterm is a product of all variables in either complemented or uncomplemented form.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Hard"
        },
        {
            "topic": "Boolean Algebra",
            "question": lambda index:
                f"\\text{{True or False: Every Boolean function can be expressed in disjunctive normal form (DNF).}}",
            "answer": lambda index:
                "True",
            "difficulty": "Hard"
        },
        {
            "topic": "Boolean Algebra",
            "question": lambda index:
                f"\\text{{True or False: A conjunctive normal form (CNF) expresses a Boolean function as a product of sums.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Hard"
        },
        {
            "topic": "Boolean Algebra",
            "question": lambda index:
                f"\\text{{True or False: The set \\{{AND, OR\\}} is functionally complete in Boolean algebra.}}",
            "answer": lambda index:
                "False",
            "difficulty": "Hard"
        },
        {
            "topic": "Boolean Algebra",
            "question": lambda index:
                f"\\text{{True or False: The set \\{{AND, OR, NOT\\}} is functionally complete in Boolean algebra.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Hard"
        },
        {
            "topic": "Boolean Algebra",
            "question": lambda index:
                f"\\text{{True or False: NOR gates alone are functionally complete.}}",
            "answer": lambda index:
                "True",
            "difficulty": "Hard"
        },
        {
            "topic": "Boolean Algebra",
            "question": lambda index:
                f"\\text{{True or False: Boolean algebra and propositional logic are structurally identical systems.}}",
            "answer": lambda index:
                "True",
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