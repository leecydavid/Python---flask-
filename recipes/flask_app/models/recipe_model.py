# model is everything happening in the backend -
# anything we want to get done in sql we will manipulate it from this file

# import the function that will connect mysqlconnection.py to connectToMySQL
# this function allows us to connect mysql to the front end(flask)
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import bcrypt, DATABASE
from flask import flash, session
from flask_app.models.user_model import User
# import re
# EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.under_thirty = data['under_thirty']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']


    @classmethod
    def create_recipe(cls, form):
        data = {
            **form,
            'user_id': session['uid']
        }
        query = """
            INSERT INTO recipes
            (name, description, instructions, created_at, under_thirty, user_id)
            VALUES (%(name)s, %(description)s, %(instructions)s, %(created_at)s, %(under_thirty)s, %(user_id)s)
        """

        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes JOIN users ON recipes.user_id = users.id;"
        results = connectToMySQL(DATABASE).query_db(query)

        recipes = []

        if results:
            for row in results:
                recipe = cls(row)

                user_data = {
                    **row,
                    'id': row['users.id'],
                    'created_at': row['users.created_at'],
                    'updated_at': row['users.updated_at']
                }

                user = User(user_data)
                recipe.creator = user
                recipes.append(recipe)

        return recipes

    @classmethod
    def get_one(cls, id):
        data = {
            "id": id
        }
                
        query = "SELECT * FROM recipes WHERE id = %(id)s"

        results = connectToMySQL(DATABASE).query_db(query, data)

        result = results[0]
        users = cls(result)

        return users
    
    @classmethod
    def update_recipe(cls, data):
        query = "UPDATE recipes SET name=%(name)s, description=%(description)s, instructions=%(instructions)s, created_at=%(created_at)s, under_thirty=%(under_thirty)s WHERE id=%(id)s;"

        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def delete_recipe(cls, id):
        data = {
            "id":id
        }

        query = "DELETE FROM recipes WHERE id=%(id)s"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def show_recipe(cls, id):
        data={
            "id":id
        }
        query = "SELECT * FROM recipes WHERE id=%(id)s"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @staticmethod
    def validate(form):
        is_valid = True
        if len(form['name']) < 3:
            flash("Recipe name must be longer than 3 letters!")
            is_valid = False
        if len(form['description']) < 3:
            flash("Recipe description is too short!")
            is_valid = False
        if len(form['instructions']) < 3:
            flash("Recipe instructions are too short!")
            is_valid = False
        if len(form['created_at']) < 1:
            flash("You must fill in the date")
            is_valid = False
        # if len(form['under_thirty']) >3:
        #     flash("Please select Yes or No")
        #     is_valid = False

        return is_valid

        
