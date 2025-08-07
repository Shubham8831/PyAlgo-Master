import streamlit as st
from team.dsa_team import create_dsa_team

st.title("</> PyAlgo Master - Our DSA Problem Solver")
st.write("Welcome to PyAlgo Master, your personal DSA problem solver! here you can ask sollution for variour data structures and algorithms problems")

task = st.text_input("Enter your DSA Problem or Question : ")
if st.button("Run"):
    st.write("Running the task...")

    team , local_exec = create_dsa_team()
