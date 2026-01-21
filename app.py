import streamlit as st
import random

st.set_page_config(page_title="Message Garden", layout="centered")

flowers = ["🌸", "🌼", "🌷", "🌻", "💐", "🌹"]

if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("Message Garden")
st.write("Type a message and watch it bloom.")

msg = st.text_input("Your message", label_visibility="collapsed")

if msg:
    flower = random.choice(flowers)
    st.session_state.messages.append((msg, flower))
    st.session_state.last = msg
    st.session_state.last = None
    st.rerun()

for text, flower in reversed(st.session_state.messages):
    st.markdown(
        f"""
        <div style="
            background: linear-gradient(135deg, #ffe6f0, #e6f7ff);
            padding: 16px;
            margin: 10px 0;
            border-radius: 16px;
            text-align: center;
            font-size: 20px;
        ">
            {flower} {text} {flower}
        </div>
        """,
        unsafe_allow_html=True
    )


