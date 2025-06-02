from prompt_template import PROMPT_TEMPLATE

def create_prompt(backlog, hours, priority, game_details_db):
    # Convert your game_details_db dict to a nicely formatted string if needed
    game_details_str = "\n".join(
        f"{game}: {details}" for game, details in game_details_db.items()
    )
    
    prompt = PROMPT_TEMPLATE.format(
        backlog=backlog,
        hours=hours,
        priority=priority,
        game_details=game_details_str
    )
    return prompt

def build_prompt(user_input, hours, priority, game_details_db, want_recommendations=False, interests=None):
    """
    Build a prompt string with optional game recommendations.

    Parameters:
        user_input (str): User's game backlog input.
        hours (int): Available gaming hours this week.
        priority (str): User's play priority.
        game_details_db (dict): Game details for each game.
        want_recommendations (bool): Whether to include game recommendations.
        interests (str): Interests to base recommendations on.

    Returns:
        str: The constructed prompt string.
    """
    games_text = user_input.strip()

    prompt = f"""
You are a friendly gaming assistant. A user has {hours} hours to play games this week.
Here’s their backlog:
{games_text}

Game details:
"""
    for game in [line.strip() for line in games_text.split('\n') if line.strip()]:
        details = game_details_db.get(game, "No additional info available.")
        prompt += f"{game}: {details}\n"

    prompt += f"\nThey want to prioritize: {priority}.\n\n"

    if want_recommendations and interests:
        prompt += f"""Also, the user asked for game recommendations based on these interests: {interests}.
Please provide a few concise game recommendations that align with their interests.
"""

    prompt += """
Create a weekly plan using ONLY the games provided in the backlog (unless asked for recommendations).
Make sure you provide a schedule for ALL days inputted by user.
Do NOT mention any games outside the backlog unless recommending as requested.

For each game, suggest how many hours to play it this week.
Include one fun fact or gameplay tip per game if available, but only if accurate.

Be concise and friendly.
"""

    return prompt
