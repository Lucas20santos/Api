from flask import Flask, url_for, render_template # type: ignore


app = Flask(__name__, template_folder='templates')

@app.route("/")
def index_page():
    return render_template('index.html')

@app.route("/login", methods=["POST", "GET"])
def login():
    return render_template('pages/login.html')
