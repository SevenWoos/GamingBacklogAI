# Generates a personalized weekly gaming plan using a local LLM (via Ollama) based on user input.

# Generates a personalized weekly gaming plan using a local LLM (via Ollama) based on user input.

# Pokemon Red(20 hours), 
# Uncharted: Among Thieves (30 hours), 
# GTA 5 (50 hours)

import ollama

def generate_plan_from_prompt(prompt: str):
    response = ollama.chat(
        model='llama3', 
        messages=[
            {'role': 'user', 'content': prompt}
        ]
    )
    return response['message']['content']