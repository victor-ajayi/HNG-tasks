from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    data = {
        "slackUsername": "mitsuki",
        "backend": True,
        "age": 22,
        "bio": "I love computers and anime"
        }
    return(jsonify(data))


if __name__ == "__main__":
    app.run(port=5000)