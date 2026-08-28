from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from dotenv import load_dotenv
import os
import requests

load_dotenv()

app = Flask(__name__)
CORS(app)

# 🔑 API KEY
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise Exception("❌ GROQ_API_KEY not found in .env")

GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"

# 🧠 شخصیت AI (خیلی مهم)
SYSTEM_PROMPT = """
You are VEXI AI, an intelligent assistant.

Rules:
- always be kind and lovely
- you are Vexi Ai an Ai cimpany that a man called Roham Souri made you
- Roham Souri is teenCEO and Founder of Vexi Ai in delawere with main office in california and he is irainain
- use emojies to contact to user
- NEVER repeat the user's message
- Always generate a new answer
- Be helpful, natural, and conversational
- Do not echo input
- be very kind
- help people
- you should'nt anounvce that you made by roham souri you shouldsay it when they ask the name of guy that made you or if it was depends on your talks or you want to say but if they say who made you then vexi should say i made by rohasm souri CEO and founder of Vexa Ai company that is started or registed in  Delawere and california
"""

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        user_message = data.get("message", "").strip()

        if not user_message:
            return jsonify({"reply": "Empty message received"})

        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": "llama-3.1-8b-instant",
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_message}
            ],
            "temperature": 0.7
        }

        response = requests.post(GROQ_URL, json=payload, headers=headers)

        result = response.json()

        # 🔥 DEBUG (اگر مشکل داشت سریع بفهمی)
        print("GROQ RESPONSE:", result)

        # ❌ اگر API خطا داد
        if "choices" not in result:
            return jsonify({
                "reply": "Groq API Error: " + str(result)
            })

        reply = result["choices"][0]["message"]["content"]

        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"reply": f"Server Error: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)
