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


