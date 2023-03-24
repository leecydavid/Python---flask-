# In the root route, save a random number between 1 and 100 and display a form for the user to guess the number
from flask import Flask, render_template, session, redirect,request
import random

app = Flask(__name__)

app.secret_key="Benny bob wuz heer."

@app.route('/')
def index():
    if "num" not in session:
        session['num'] = random.randint(1,100)

    return render_template("index.html")

@app.route('/guess',methods=['POST'])
def guess():
    session['guess'] = int(request.form['guess'])
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')




if __name__=="__main__":   
    app.run(debug=True, port=5001)    