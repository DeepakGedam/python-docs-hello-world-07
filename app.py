from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World! I am Deepak...(-_-)"
