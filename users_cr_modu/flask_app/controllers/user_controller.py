from flask_app import app

from flask import render_template, redirect, request

from flask_app.models.user_table import User

@app.route('/')          
def index():
    return redirect('/user')  

@app.route('/user')
def user():
    return render_template('user.html', users = User.get_all())

@app.route('/user_new')
def user_new():
    return render_template('create_user.html')

@app.route('/create', methods=['POST'])
def create():
    print(request.form)
    User.save(request.form)
    return redirect('/user')

@app.route('/edit/<int:id>')
def edit(id):
    data = {
        "id":id
    }
    return render_template('edit_user.html', user=User.get_one(data))

@app.route('/show/<int:id>')
def show(id):
    data = {
        "id":id
    }
    return render_template('show_user.html', user=User.get_one(data))

@app.route('/new_update', methods=['POST'])
def new():
    User.new(request.form)
    return redirect('/user')

@app.route('/delete/<int:id>')
def delete(id):
    User.delete(id)
    return redirect('/user')