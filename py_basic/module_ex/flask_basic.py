from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>헬로 월드<h1>"