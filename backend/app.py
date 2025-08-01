import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import google.generativeai as genai
from pathlib import Path

load_dotenv(dotenv_path=Path(__file__).resolve().parent / ".env")

app = Flask(__name__)
CORS(app)

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    print("WARNING: GEMINI_API_KEY not found in environment variables!")

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('models/gemini-1.5-pro-latest')


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    print("Received data:", data)  # DEBUG: print the incoming JSON

    user_message = data.get("message") if data else None
    if not user_message:
        print("No message provided in request")  # DEBUG
        return jsonify({"error": "Message is empty"}), 400

    try:
        print("Sending message to Gemini API:", user_message)  # DEBUG
        response = model.generate_content(user_message)
        print("Received response from Gemini API:", response.text)  # DEBUG
        return jsonify({"response": response.text})
    except Exception as e:
        print("Error from Gemini API:", e)  # DEBUG
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
