import os

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/', methods=["POST"])
def index():
    operation = request.json["operation_type"]
    x = int(request.json["x"])
    y = int(request.json["y"])

    response = {
        "slackUsername": "mitsuki",
        "operation_type": operation
    }

    if operation == "addition":
        response.update({ "result": x + y })
    elif operation == "subtraction":
        response.update({ "result": x - y })
    elif operation == "multiplication":
        response.update({ "result": x * y })
    else:
        return "Invalid operation."

    return jsonify(response)
    

if __name__ == "__main__":
    app.run(port=os.getenv("PORT", default=5000))