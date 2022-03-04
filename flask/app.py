from flask import Flask, request, session
from flask import render_template
import random

app = Flask(__name__)
app.secret_key = "mysecretkey"

@app.route("/")
def index():
  print(session)
  if 'count' not in session:
    session['count'] = 1
  else:
    session['count'] = session['count'] + 1
  return render_template("index.html",count = session['count'])
  # return render_template('index.html')

@app.route("/blog")
def blog():
  return render_template("blog.html") 

@app.route("/rand")
def randomnumber():
  i = random.randrange(100)
  s = "<h1>Your lucky number is: "
  s = s + str(i)
  s = s + "</h1>"
  return s

@app.route("/lucky")
def lucky():
  return render_template("lucky.html", number=random.randrange(100), number2 = random.randrange(10))

@app.route("/list")
def list():
  return render_template("list.html")

# example of static content
# like an image or including css
@app.route("/image_css")
def image_css():
  return render_template("image_css.html")

@app.route("/about", methods=['GET','POST'])
def about():
  if request.method=="GET":
    return render_template("about.html")
  else:
    user = request.form['username']
    return render_template('about.html',user=user)

@app.route("/login_form",methods=['GET','POST'])
def login_form():
  # GET is when we just load the page in our browser
  # POST is when we click the button 
  if request.method=="GET":
    return render_template("login_form.html")
  else:
    # here we clicked the button
    # so we can check the form data
    name = request.form['username']
    pw = request.form['password']
    print(name,pw)
    if name != "Emma":
      error = "Username not recognized"
      name=""
      pw = ""
    elif pw != "12345":
      error = "Incorrect password"
      name=""
    else: 
      error = ""
    return render_template("login_form.html",error=error, name=name)



app.run(host="0.0.0.0", port=5000, debug=True)
