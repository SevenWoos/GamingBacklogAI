import streamlit as st
from game_details import load_or_fetch_game_details
from prompt_builder import create_prompt  # Function that builds the prompt string
from planner import generate_plan_from_prompt  # Function that takes the prompt and returns a plan

# Streamlit app setup
st.set_page_config(page_title="Backlog Planner Lite", page_icon="🎮")
st.title("🎮 Backlog Planner Lite")
st.markdown("Enter your backlog and get a personalized weekly gaming plan!")

# User inputs
games_input = st.text_area(
    "📝 Your backlog (one game per line with optional estimated hours):",
    placeholder="Example:\nPokemon Red (6 hrs)\nUncharted: A Thief's End (25 hrs)"
)

time = st.slider("⏱️ Hours available this week:", min_value=1, max_value=40, value=5)

priority = st.selectbox(
    "🎯 Planning strategy:",
    ["Shortest games first", "Most fun games first", "Random mix"]
)

# Generate button logic
if st.button("🧠 Generate Plan"):
    game_list = [line.strip() for line in games_input.split('\n') if line.strip()]
    
    if not game_list:
        st.warning("⚠️ Please enter at least one game.")
    else:
        with st.spinner("Generating your personalized gaming plan..."):
            # 1. Load game details (cached or fetched)
            game_details_db = load_or_fetch_game_details(game_list)

            # 2. Build prompt using new helper
            prompt = create_prompt(games_input, time, priority, game_details_db)

            # 3. Generate plan from prompt using local model
            plan = generate_plan_from_prompt(prompt)

        st.success("Here's your weekly plan:")
        st.markdown(plan, unsafe_allow_html=True)
