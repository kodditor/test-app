from flask import Flask
from decouple import config
from waitress import serve

app = Flask(__name__)
port = config("PORT", default=5000)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=port)