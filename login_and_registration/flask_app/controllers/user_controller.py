# controller is everything happening in the front end 
# anything we want to get done in flask and browser, we will maniuplate from this file
from flask_app import app

from flask import render_template, redirect, request, session
from flask_app.models.user_model import User


@app.route('/')          
def index():
    return render_template('index.html')
# just to be safe, always set this to redirect to home page(next route)

@app.route('/login', methods=['POST'])
def login():
    log_in_user = User.validate_login(request.form)

    if log_in_user:
        session['uid'] = log_in_user.id
        return redirect('/dashboard')
    else:
        return redirect('/')

@app.route('/register', methods=['POST'])
def register():
    if not User.validate_register(request.form):
        return redirect('/')
    
    User.create(request.form)
    return redirect('/')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/dashboard')
def dashboard():
    if "uid" not in session:
        return redirect('/')
    
    return render_template('/dashboard.html')
    

