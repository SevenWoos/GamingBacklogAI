# Generates a personalized weekly gaming plan using a local LLM (via Ollama) based on user input.

# Generates a personalized weekly gaming plan using a local LLM (via Ollama) based on user input.

# Pokemon red(20 hours), 
# uncharted 2(30 hours), 
# gta 5 (50 hours)

import ollama

def generate_plan_from_prompt(prompt: str) -> str:
    response = ollama.chat(
        model='llama3',
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response['message']['content']
