# controller is everything happening in the front end 
# anything we want to get done in flask and browser, we will maniuplate from this file

import dataclasses

from flask_app import app

from flask import render_template, redirect, request
from flask_app.models.ninja_model import Ninja
from flask_app.models.dojo_model import Dojo

@app.route('/')          
def index():
    return redirect('/dojos')
# just to be safe, always set this to redirect to home page(next route)

@app.route('/dojos')
# dojos is browser name (home page) this is the extension that a lot of routes will redirect to
def dojo():
    return render_template('index.html', dojos = Dojo.get_all())
    # get_all is linked to 
# this route is retrieving the data linked to class Dojo in dojo_model so we can start manipulating the data 
# linked to our Dojo class in dojo_model

@app.route('/create', methods=['POST'])
def create():
# def create is linked to classmethod create in dojo_model 
# we will display the results we get in classmethod def create 
    Dojo.create(request.form)
    # targeting class Dojo from dojo_model and printing the data onto our browser by using request.form
    return redirect('/dojos')
    # the data will be displayed in our '/dojos' homepage 
        # redirecting extension creae back to our homepage 

@app.route('/dojo_show/<int:id>')
def show(id):
    return render_template('new_ninja.html', dojos = Dojo.show(id))