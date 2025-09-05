from flask import Flask, request
import os

app = Flask(__name__)


@app.route("/", methods=['GET'])
def hello_world():
    return f"Hello World!!!"


@app.route("/addition", methods=['GET'])
def addition_operation():
    a, b = request.args
    return a + b


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
