from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)

app.secret_key = '01189998819991197253'

@app.route('/')
def index():
  session['key'] = random.randrange(0,101);
  return render_template("index.html")

@app.route('/guessing', methods=['POST'])
def guessing():
  guess = request.form['guess']
  print session['key']
  if(guess == ""):
    return render_template("index.html")
  
  if int(guess) == int(session['key']):
    return render_template("index.html", result="right", value=guess)
  elif int(guess) > int(session['key']):
    return render_template("index.html", result="high")
  else:
    return render_template("index.html", result="low")

@app.route('/playagain', methods=['POST'])
def playagain():
  session.pop('key')
  return redirect('/')


app.run(debug=True)