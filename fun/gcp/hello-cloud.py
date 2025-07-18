from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def hello():
    return jsonify(message="Hello from Cloud Run!")

@app.route("/square/<int:number>")
def square(number):
    result = number * number
    return jsonify(number=number, square=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
