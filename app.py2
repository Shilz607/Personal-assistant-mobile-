from flask import Flask, request, jsonify
import openai
import whisper
import requests

app = Flask(__name__)

openai.api_key = "YOUR_OPENAI_API_KEY"
ELEVENLABS_API_KEY = "YOUR_ELEVENLABS_API_KEY"

# Speech-to-Text (Whisper)
def transcribe_audio(file_path):
    model = whisper.load_model("base")
    result = model.transcribe(file_path)
    return result["text"]

# Generate AI Response
def get_ai_response(user_input):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": user_input}]
    )
    return response["choices"][0]["message"]["content"]

# Text-to-Speech (ElevenLabs)
def text_to_speech(text):
    url = "https://api.elevenlabs.io/v1/text-to-speech"
    headers = {"Authorization": f"Bearer {ELEVENLABS_API_KEY}", "Content-Type": "application/json"}
    payload = {"text": text, "voice": "en-US", "model": "eleven_multilingual_v1"}
    response = requests.post(url, json=payload, headers=headers)
    
    # Save speech output
    with open("output.mp3", "wb") as f:
        f.write(response.content)
    return "output.mp3"

@app.route("/assistant", methods=["POST"])
def assistant():
    data = request.json
    user_input = data.get("query", "")

    # Process input
    ai_response = get_ai_response(user_input)
    speech_file = text_to_speech(ai_response)

    return jsonify({"response": ai_response, "audio_file": speech_file})

if __name__ == "__main__":
    app.run(debug=True)
