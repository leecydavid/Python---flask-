# model is everything happening in the backend - 
# anything we want to get done in sql we will manipulate it from this file

# import the function that will connect mysqlconnection.py to connectToMySQL 
    # this function allows us to connect mysql to the front end(flask)
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import bcrypt, DATABASE
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 


class User:
    def __init__( self , data ):
        # always set this class to Upper case to whatever the name is of one of your table names but singular
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at'] 

    @classmethod
    def create(cls, form):
        data = {
        **form,
        'password' : bcrypt.generate_password_hash(form['password']) 
        }

        query = "INSERT INTO users(first_name, last_name, email, password) VALUES(%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        return connectToMySQL(DATABASE).query_db(query, data) 
    
    @classmethod
    def get_one_by_email(cls, email):
        data = {
        'email' : email
        }
        query = "SELECT * FROM users WHERE email = (%(email)s)"
        results = connectToMySQL(DATABASE).query_db(query, data) 

        if results:
            return cls(results[0])
        else:
            return False
        
    @classmethod
    def validate_login(cls, form):
        found_user = cls.get_one_by_email(form['email'])

        if found_user:
            if bcrypt.check_password_hash(found_user.password, form['password']):
                return found_user
            else:
                flash("Invalid Login!")
                return False
        else:
            flash("Invalid Login!")
            return False
        
    @classmethod
    def validate_register(cls, form):
        is_valid = True

        if len(form['first_name']) < 1:
            is_valid = False
            flash("First name is too short!")
        if len(form['last_name']) < 1:
            is_valid = False
            flash("Last name is too short!")
        if not EMAIL_REGEX.match(form['email']):
            is_valid = False
            flash("Invalid email address!")
        if len(form['password']) < 8:
            is_valid = False
            flash("Password must be 8 characters!")
        if form['password'] != form['confirm_password']:
            is_valid = False
            flash("Password does not match!")
        
        return is_valid
        



