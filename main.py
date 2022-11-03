import os

from flask import Flask, request

app = Flask(__name__)


@app.errorhandler(404)
def invalid_route(e):
    return "Invalid route."


@app.route('/', methods=["POST"])
def index():
    operation = request.json["operation_type"]
    x = request.json["x"]
    y = request.json["y"]

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

    return response
    

if __name__ == "__main__":
    app.run(port=os.getenv("PORT", default=5000))