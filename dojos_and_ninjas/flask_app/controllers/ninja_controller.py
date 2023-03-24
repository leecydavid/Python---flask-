from flask_app import app

from flask import render_template, redirect, request

from flask_app.models.dojo_model import Dojo
from flask_app.models.ninja_model import Ninja

@app.route('/ninjas')
def ninjas():
    return render_template('ninja.html', dojos = Dojo.get_all())


@app.route('/new_ninjas', methods = ['POST'])
def new_create():
    Ninja.new_create(request.form)
    return redirect ('/dojos')







