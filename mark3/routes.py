from flask import render_template, request, redirect, url_for, session, jsonify,Blueprint
from flask_login import login_required, current_user
import requests
import os

chat_bp = Blueprint('chat', __name__)

@chat_bp.route('/chat', methods=['GET', 'POST'])
@login_required
def chat():
    if request.method == 'POST':
        user_input = request.json['message']

        # Loading prompt template
        prompt_path = os.path.join(os.path.dirname(__file__), 'prompts', 'scheduler_prompt.txt')
        
        with open(prompt_path, 'r', encoding='utf-8') as f:
            prompt_template = f.read()
        
        # Insert user input into prompt
        full_prompt = prompt_template.replace('{{USER_INPUT_HERE}}', user_input)


        response = requests.post(
            'http://localhost:11434/api/generate',
            json={
                "model": "llama3",  # change based on whatever model i use
                "prompt": user_input,
                "stream": False
            }
        )
        data = response.json()
        return jsonify({"response": data.get("response", "")})

    return render_template('chat.html', user=current_user)