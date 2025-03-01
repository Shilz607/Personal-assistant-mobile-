from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import requests

app = Flask(__name__)
CORS(app)

# API Keys (Replace with your actual keys)
OPENAI_API_KEY = "your_openai_key"
ELEVENLABS_API_KEY = "your_elevenlabs_key"

openai.api_key = OPENAI_API_KEY

@app.route('/assistant', methods=['POST'])
def assistant():
    data = request.json
    user_input = data.get("query")

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": user_input}]
    )

    reply = response["choices"][0]["message"]["content"]
    return jsonify({"response": reply})

if __name__ == '__main__':
    app.run(debug=True)
