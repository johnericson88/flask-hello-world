from flask import Flask, render_template, session
from flask_session import Session


#Configure Application
app = Flask(__name__)


# app.config["SESSION_PERMANENT"] = False
# app.config["SESSION_TYPE"] = "filesystem"
# Session(app)


@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/')
def hello_world():
    return render_template("hello_world.html")

@app.route('/home')
def home():
    return render_template("home.html")

