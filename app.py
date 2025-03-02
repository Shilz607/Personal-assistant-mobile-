from flask import Flask, request, jsonify
from flask_cors import CORS
import openai

app = Flask(__name__)
CORS(app)

@app.route('/assistant', methods=['POST'])
def assistant():
    data = request.json
    user_input = data.get("query", "")

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": user_input}]
    )

    reply = response["choices"][0]["message"]["content"]
    return jsonify({"response": reply})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
