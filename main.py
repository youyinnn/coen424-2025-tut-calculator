from flask import Flask, request, jsonify
import os

app = Flask(__name__)


@app.route("/", methods=['GET'])
def hello_world():
    return f"Hello World!!!"


@app.route("/addition", methods=['POST'])
def add():
    a = request.form.get('a', 0)
    b = request.form.get('b', 0)
    try:
        result = float(a) + float(b)
    except (TypeError, ValueError):
        return jsonify({'error': 'Invalid input'}), 400
    return jsonify({'result': result})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
