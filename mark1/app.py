import streamlit as st
from game_details import load_or_fetch_game_details
from prompt_builder import create_prompt, build_prompt  # import both
from planner import generate_plan_from_prompt

st.set_page_config(page_title="Gaming Backlog Planner Lite", page_icon="🎮")
st.title("🎮 Backlog Planner Lite")
st.markdown("Enter your backlog and get a personalized weekly gaming plan!")

games_input = st.text_area(
    "📝 Your backlog (one game per line with optional estimated hours):",
    placeholder="Example:\nPokemon Red (6 hrs)\nUncharted: A Thief's End (25 hrs)"
)

time = st.slider("⏱️ Hours available this week:", min_value=1, max_value=40, value=5)

priority = st.selectbox(
    "🎯 Planning strategy:",
    ["Shortest games first", "Most fun games first", "Random mix"]
)

# New input: Ask if user wants recommendations
want_recs = st.checkbox("Would you like game recommendations based on your interests?")

# New input: Only show if user wants recommendations
interests = ""
if want_recs:
    interests = st.text_input("Please enter your interests (e.g., RPG, adventure, multiplayer):")

if st.button("🧠 Generate Plan"):
    game_list = [line.strip() for line in games_input.split('\n') if line.strip()]

    if not game_list:
        st.warning("⚠️ Please enter at least one game.")
    else:
        with st.spinner("Generating your personalized gaming plan..."):
            game_details_db = load_or_fetch_game_details(game_list)

            if want_recs and interests.strip():
                # Use new build_prompt with recommendations
                prompt = build_prompt(
                    user_input=games_input,
                    hours=time,
                    priority=priority,
                    game_details_db=game_details_db,
                    want_recommendations=True,
                    interests=interests
                )
            else:
                # Use original prompt builder
                prompt = create_prompt(games_input, time, priority, game_details_db)

            plan = generate_plan_from_prompt(prompt)

        st.success("Here's your weekly gaming plan:")
        st.markdown(plan, unsafe_allow_html=True)
