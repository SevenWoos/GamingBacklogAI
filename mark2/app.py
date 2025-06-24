import streamlit as st
from planner import generate_plan_from_prompt

st.title('🎮 Backlog Planner Lite')

st.markdown('Enter your gaming backlog and get a weekly gaming plan!')

games_input = st.text_area(
    "📝 Your backlog (one game per line with optional estimated hours):",
    placeholder="Example:\nCall of Duty Black Ops (15 hrs)\nPokemon Red (6 hrs)\nUncharted: A Thief's End (25 hrs)"
)

time = st.slider("⏱️ Hours available this week:", min_value=1, max_value=40, value=5)

priority = st.selectbox(
    "🎯 Planning strategy:",
    ["Shortest games first", "Most fun games first", "Random mix"]
)

# Want recommendations?
want_recs = st.checkbox('Would you like game recommendations based on your interests')

# New input: Only show if user wants recommendations
interests = ''
if want_recs:
    interests = st.text_input('What kind of games do you like to play? (Adventure, FPS, RPG, multiplayer?): ')

if st.button('🧠 Generate Plan'):
    game_list = [line.strip() for line in games_input.split('\n') if line.strip()]

    if not game_list:
        st.warning("⚠️ Please enter at least one game. You can also ask for game recommendations if you currently don't have any!")
    else:
        with st.spinner("Generating your personalized gaming plan..."):
            