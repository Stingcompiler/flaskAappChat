from flask import Flask, request, jsonify,render_template

from chat import get_response

app = Flask(__name__)

#
# @app.route('/predict', methods=['POST'])
# def predict():
#     try:
#         # Get the JSON data from the request
#         data = request.get_json()
#
#         if not data or 'message' not in data:
#             # Return a 400 Bad Request error if the message is missing
#             return jsonify({"error": "Message is required"}), 400
#
#         message = data['message']
#
#         # Example logic for prediction (replace with your actual logic)
#         if not message:
#             return jsonify({"error": "Empty message"}), 400
#
#         answer = f"Received message: {message}"  # Placeholder for prediction logic
#
#         return jsonify({"answer": answer})
#
#     except Exception as e:
#         # Catch any errors and return a JSON response with the error message
#         print(f"Error occurred: {e}")
#         return jsonify({"error": "Internal Server Error"}), 500
#
#
# if __name__ == '__main__':
#     app.run(debug=True)


app = Flask(__name__)

@app.get("/")
def index_get():
    return render_template("index.html")


@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    response = get_response(text)
    message = {"answer":response}
    return  jsonify(message)



if __name__ == "__main__":
    app.run(debug=True)
