from flask import Flask, request, jsonify
import groq
from flask_cors import CORS  # To allow frontend requests

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes (or customize the origin as needed)

# Replace with your actual Groq API key
client = groq.Client(api_key="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")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        # Get the user message from the incoming request
        data = request.json
        user_message = data.get("message", "")

        # If no message is received, return an error response
        if not user_message:
            return jsonify({"response": "No message received."}), 400

        # Make the API call to Groq
        response = client.chat.completions.create(
            model="llama3-8b-8192",  # Specify the model (adjust as needed)
            messages=[ 
                {"role": "system", "content": "You are a helpful AI chatbot."},
                {"role": "user", "content": user_message}
            ]
        )

        # Return the response from Groq as a JSON response
        return jsonify({"response": response.choices[0].message.content})

    except Exception as e:
        # Catch any errors and send a generic error message
        print(f"Error: {e}")
        return jsonify({"response": "Sorry, something went wrong. Please try again later."}), 500

if __name__ == "__main__":
    app.run(debug=True)  # Enable debug mode for easier development and testing
