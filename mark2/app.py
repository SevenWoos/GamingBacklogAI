import streamlit as st
from planner import generate_plan

st.title('🎮 Backlog Planner Lite')

st.markdown('Enter your gaming backlog and get a weekly gaming plan!')

games_input = st.text_area(
    "📝 Your backlog (one game per line with optional estimated hours):",
    placeholder="Example:\nPokemon Red (6 hrs)\nUncharted: A Thief's End (25 hrs)"
)

time = st.slider("⏱️ Hours available this week:", min_value=1, max_value=40, value=5)

priority = st.selectbox(
    "🎯 Planning strategy:",
    ["Shortest games first", "Most fun games first", "Random mix"]
)