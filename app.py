import streamlit as st

st.title("Personality Snapshot")

sleep = st.selectbox("Average sleep per night", ["< 6 hours", "6–7 hours", "> 7 hours"])
risk = st.selectbox("Risk preference", ["Low", "Medium", "High"])
social = st.selectbox("Social energy", ["Low", "Medium", "High"])

if sleep and risk and social:
    if sleep == "< 6 hours" and risk == "High":
        st.write("You are an impulsive optimizer: fast-moving, high-energy, low patience.")
    elif sleep == "> 7 hours" and social == "Low":
        st.write("You are a deliberate thinker: calm, analytical, and self-directed.")
    elif risk == "Low" and social == "High":
        st.write("You are a cooperative stabilizer: reliable, people-oriented, risk-aware.")
    else:
        st.write("You are a balanced generalist: adaptable, situational, and pragmatic.")
