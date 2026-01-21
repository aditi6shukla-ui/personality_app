import streamlit as st

st.set_page_config(page_title="Mood Machine", layout="centered")

energy = st.slider("Energy level", 0, 100, 50)
logic = st.slider("Logic vs intuition", 0, 100, 50)
chaos = st.slider("Chaos tolerance", 0, 100, 50)

score = energy + logic - chaos

if score > 150:
    st.markdown("## Cognitive State: Strategic Overdrive")
    st.write("High output, high clarity, low noise. Dangerous when unchecked.")
elif score > 80:
    st.markdown("## Cognitive State: Focused Operator")
    st.write("Balanced execution mode. Reliable and controlled.")
elif score > 20:
    st.markdown("## Cognitive State: Adaptive Wanderer")
    st.write("Exploratory, flexible, context-sensitive.")
else:
    st.markdown("## Cognitive State: Entropic Drift")
    st.write("Low structure, high randomness. Creative but unstable.")

st.write("Raw Signal Value:", score)
