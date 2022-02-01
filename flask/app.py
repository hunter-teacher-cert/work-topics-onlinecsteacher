from flask import Flask
from flask import render_template
import random

app = Flask(__name__)

@app.route("/rand")
def randomnumber():
  i = random.randrange(100)
  s = "<h1>Your lucky number is: "
  s = s + str(i)
  s = s + "</h1>"
  return s

@app.route("/")
def index():
  return "<h1>Hello World!</h1>"

@app.route("/about")
def about():
  return render_template("about.html")

@app.route("/lucky")
def lucky():
  return render_template("lucky.html")

app.run(host="0.0.0.0", port=5000, debug=True)
