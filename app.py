import streamlit as st
import random
import time

st.set_page_config(page_title="Color Memory Game", layout="centered")

colors = ["red", "green", "blue", "yellow"]

if "sequence" not in st.session_state:
    st.session_state.sequence = []
    st.session_state.user_input = []
    st.session_state.round = 0
    st.session_state.show = False

st.title("Color Memory Game")

if st.button("Start / Next Round"):
    st.session_state.user_input
