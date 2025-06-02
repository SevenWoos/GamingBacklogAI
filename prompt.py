def build_prompt(games_text, hours, priority, game_details_db):
    user_games = [line.strip() for line in games_text.split('\n') if line.strip()]

    game_details = ""
    for game in user_games:
        if game in game_details_db:
            game_details += f"{game}: {game_details_db[game]}\n"
        else:
            game_details += f"{game}: No additional info available.\n"

    prompt = f"""
You are a helpful gaming assistant. A user has {hours} hours to play games this week.
Here’s their backlog:\n{games_text}\n
Game details:\n{game_details}\n
They want to prioritize: {priority}.

Create a weekly plan using ONLY the games provided in the backlog. Make sure you provide a schedule for ALL days inputted by user.
Do NOT recommend or mention any other games unless user asks for it.

For each game, suggest how many hours to play it this week.
Also include one fun fact, one gameplay tip, or a recommended level to focus on — 
but only if that information is 100% accurate and verified from numerous sources.

Be concise and friendly. If you don't have details for a game, just plan time for it without adding extras.

IMPORTANT: Only include facts and tips that are verified and accurate. Avoid any unconfirmed trivia or rumors.
Be concise and friendly.
"""
    return prompt