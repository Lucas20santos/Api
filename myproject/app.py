from flask import Flask, url_for # type: ignore
from flask import render_template # type: ignore

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.hmtl')


@app.route("/login", methods=["GET", "POST"])
def hello_world():
    return "<p>Page Login</p>"

# url_for('static', filename='style.css')
