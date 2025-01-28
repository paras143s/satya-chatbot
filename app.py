from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Define chatbot responses
responses = {
    "hello": "Hi there! How can I help you?",
    "how are you": "I'm just a bot, but I'm doing great! How about you?",
    "who created you": "I was created by Paras Rajput.",
    "what is your name": "I'm Satya, your friendly chatbot.",
    "What’s your favorite place to visit": "I love Bihar, especially Darbhanga!",
    "what is your purpose": "My purpose is to assist you with anything you need!",
    "can you help me": "Of course! Just let me know what you need help with.",
    "how old are you": "I don't have an age, I'm just a bot created to help you!",
    "where are you from": "I'm from the digital world, but I was created by Paras Rajput.  https://parassingh01.github.io/paraskumar.github.io/",
    "how do I contact support": "If you need support, you can contact the team through their official website or support page.",
    "can you play games": "I can't play games, but I can help you find games to play! https://paras143s.github.io/gamewithparas/",
    "what can you do": "I can answer questions, provide information, and assist with various tasks.",
    "tell me a joke": "Why don’t skeletons fight each other? They don’t have the guts!",
    "what is your favorite color": "I don’t have preferences, but I think black is a nice color!",
    "do you like music": "I don't have ears, but I think music is wonderful for humans! but paras sing old songs",
    "what is the weather like": "I can't check the weather, but you can use weather apps for that!https://www.google.com/search?q=weather&rlz=1C1RXQR_enIN1094IN1095&oq=weather&gs_lcrp=EgZjaHJvbWUyEQgAEEUYORhGGIACGLEDGIAEMhYIARAuGMcBGJECGMkDGNEDGIAEGIoFMg0IAhAAGJIDGIAEGIoFMg0IAxAAGJIDGIAEGIoFMgoIBBAAGLEDGIAEMgoIBRAAGLEDGIAEMgoIBhAAGLEDGIAEMgoIBxAAGLEDGIAEMgcICBAAGI8C0gEJNTA1MmowajE1qAIIsAIB&sourceid=chrome&ie=UTF-8 ",
    "tell me a fun fact": "Did you know that honey never spoils? Archaeologists have found pots of honey in ancient tombs that are still edible!",
    "bye": "Goodbye! Have a great day!",
}

# Function to get chatbot response
def get_response(user_input):
    user_input = user_input.lower()
    return responses.get(user_input, "I'm sorry, I can't understand but you find in google https://www.google.co.uk/")

# Routes
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def chat_response():
    user_message = request.json.get("message")
    bot_response = get_response(user_message)
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)
