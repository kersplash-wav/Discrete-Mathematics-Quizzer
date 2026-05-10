# Discrete Mathematics Quizzer
![A promotional banner which says "Discrete Mathematics Quizzer"](https://github.com/kersplash-wav/Discrete-Mathematics-Quizzer/blob/main/Program/Images/discretemathquizzerbanner.png?raw=true)
<p align="center">Developed by Nico Ranin and Robert Rodriguez</p>

## Set-Up Instructions
Access the Program folder of the project. Then, run the command `make run` in the terminal. The local website is then automatically opened in your default browser. If this fails to work, copy and paste the provided local host address in the terminal in any browser of your choice. You will then be able to access the website locally. The website can also be accessed online by using the website https://discrete-mathematics-quizzer.streamlit.app/.

## Inspiration
When we first encountered discrete mathematics in our undergraduate university courses, we felt extremely challenged by its contents. It felt as if many topics were too difficult to understand and that there wasn't enough practice to support our learning. This wasn't a sentiment only just the two of us developers shared: in fact, it was very common between other peers of ours, both at our university and outside of it.

## What our project does
Our project is a Discrete Mathematics Quiz. With a database consisting of thousands of questions, ranging in categories from combinatorics to trees to set theory, we cover all the areas of discrete mathematics an undergraduate university student should be expected to know and learn. Users are provided a question for which they can attempt to answer, skip it, or view its answer to learn from it. By going through the vast database of questions our project offers, a user can expect to become much more knowledgeable in discrete mathematics by using it.

## How we built it
We built this program using Python as our programming language and Streamlit as our framework. Using Python, we programmed the database and the back-end focus of the work, whilst Streamlit focused on the front-end and web application. We built this program to be possible to access through two methods. The first is local access by downloading this repository and following the documentation to have one's own Streamlit site on their local user address. The other is by using the Streamlit website we created, https://discrete-mathematics-quizzer.streamlit.app/.

## Challenges we encountered
There were various challenges that we encountered throughout the development of our project. One major issue for us was how to store our questions into a database. This search led us to rewite the practice problem quizzer numerous times. We first attempted to use SQL through the SQLite3 module in Python, yet this proved to be too complicated. Thus, we decided to switch to JSON, yet it showed to lack capabilities in random generation, which was undesirable. For this reason, we decided to transform the database of questions into a dictionary, as it would allow us to create lambda functions/anonymous functions for randomizing the questions. However, we quickly realized that this storage system could be made to be more efficient as dictionaries required the index to be manually written, whilst this was not a necessary component for an array. Hence, it was the reason for why we ultimately concluded to write our question database using the array format. Other challenges included proper UI/UX formatting (ex. sizing and centring images correctly), and error-checking in questions, both of which found quick fixing.

## Accomplishments we're proud of
We're extremely proud to have made a tool to help people learn discrete mathematics. It's a collection of the questions we wish we could have had when we were studying discrete mathematics, so we truly desire that it helps others just as much as it could have helped us. We're additionally just as proud of the extent of the questions we have, having garnered half a thousand questions in such a short timeframe.

## What we learned
This project was our first time having experience using Streamlit, and we couldn't be happier with it. Its documentation was extremely clear, allowing us to quickly pick up on how to use it. This project was also our first major implementation of Python for a large project, rather than for school or basic programming exercises. It's taught us how to combine the two to create a full project, and we couldn't be more grateful for the experience.

## What's next for the Discrete Mathematics Quizzer

There's numerous next steps to take for this project that we would have liked to explore, but unfortunately were not feasible within the given deadline for this project. This includes...

- More detailed UI/UX (ex. more detailed background that changes depending on light/dark mode)
- AI explanations for answers (using the Gemini API)
- Gamification aspects (leaderboards, completion statistics, a versus mode)
- More accurate difficulty ratings sourced, from data of other users (tracking the percentage of people who correctly guessed a question)
