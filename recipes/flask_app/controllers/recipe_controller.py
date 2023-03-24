# controller is everything happening in the front end
# anything we want to get done in flask and browser, we will maniuplate from this file
from flask_app import app

from flask import render_template, redirect, request, session
from flask_app.models.user_model import User
from flask_app.models.recipe_model import Recipe


@app.route('/recipes')
def recipes():
    if "uid" not in session:
        return redirect('/')
    
    user = User.get_one(session['uid'])
    recipes = Recipe.get_all()
    return render_template('recipes.html', recipes=recipes, user=user)

@app.route('/add_recipe')
def add_recipe():
    if "uid" not in session:
        return redirect('/')

    return render_template('recipes_new.html')

@app.route('/create_recipe', methods=['POST'])
def create_recipe():
    # print(request.form)

    if Recipe.validate(request.form):
        Recipe.create_recipe(request.form)
        return redirect('/recipes')
    else:
        return redirect('add_recipe')
    
@app.route('/edit_recipe/<int:id>')
def edit_recipe(id):
    if 'uid' not in session:
        return redirect('/')
    
    user = User.get_one(session['uid'])
    recipe = Recipe.get_one(id)
    return render_template('recipes_edit.html', user=user, recipe=recipe)

@app.route('/update_recipe', methods=['POST'])
def update_recipe():
    if not Recipe.validate(request.form):
        return redirect(f'/edit_recipe/{request.form["id"]}')
    
    Recipe.update_recipe(request.form)

    return redirect('/recipes')

@app.route('/delete_recipe/<int:id>')
def delete_recipe(id):
    Recipe.delete_recipe(id)

    return redirect('/recipes')

@app.route('/show_recipe/<int:id>')
def show_recipe(id):
    if 'uid' not in session:
        return redirect('/')

    user = User.get_one(session['uid'])
    recipe = Recipe.get_one(id)
    return render_template('recipes_show.html', recipe=recipe, user=user)










