# app.py
import sys
import os
from flask import Flask, render_template, request, jsonify

# Ensure current folder is in Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import your chatbot class
from it_chatbot_pro import ITChatBot

# Initialize Flask app and chatbot
app = Flask(__name__)
bot = ITChatBot("TechBot")

# Home page route
@app.route("/")
def home():
    return render_template("index.html")  # HTML chatbox

# API route for chatbot responses
@app.route("/get_response", methods=["POST"])
def get_response():
    user_input = request.json.get("message")  # Get user message from frontend
    response, end = bot.get_response(user_input)  # Get chatbot response
    return jsonify({"response": response, "end": end})  # Return JSON

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
