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
    st.session_state.user_input = []
    st.session_state.round += 1
    st.session_state.sequence.append(random.choice(colors))
    st.session_state.show = True

if st.session_state.show:
    st.write("Memorize the sequence")
    for color in st.session_state.sequence:
        st.markdown(
            f"<div style='width:100px;height:100px;background:{color};margin:10px'></div>",
            unsafe_allow_html=True
        )
        time.sleep(0.6)
    st.session_state.show = False
    st.experimental_rerun()

st.write(f"Round: {st.session_state.round}")

cols = st.columns(4)
for i, color in enumerate(colors):
    if cols[i].button(color.capitalize()):
        st.session_state.user_input.append(color)

if len(st.session_state.user_input) == len(st.session_state.sequence):
    if st.session_state.user_input == st.session_state.sequence:
        st.success("Correct sequence")
    else:
        st.error("Wrong sequence. Game reset.")
        st.session_state.sequence = []
        st.session_state.user_input = []
        st.session_state.round = 0

