from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chatbot', methods=['POST'])
def chatbot_response():
    user_message = request.json.get('message')
    # Basic response logic for demonstration
    if user_message.lower() == 'hi':
        response = "Hello! How can I assist you today?"
    elif user_message.lower() == 'bye':
        response = "Goodbye! Have a great day!"
    else:
        response = f"You said: {user_message}. I’m still learning to respond to that."

    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
