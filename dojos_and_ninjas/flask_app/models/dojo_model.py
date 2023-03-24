# model is everything happening in the backend - 
# anything we want to get done in sql we will manipulate it from this file

# import the function that will connect mysqlconnection.py to connectToMySQL 
    # this function allows us to connect mysql to the front end(flask)
from flask_app.config.mysqlconnection import connectToMySQL

from flask_app.models import ninja_model

class Dojo:
    def __init__( self , data ):
        # always set this class to Upper case to whatever the name is of one of your table names but singular
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # this class is getting all the column-names in the ninjas table
        # whatever the names are of variables in the table you are targeting 

    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
    # the get_all is retrieving all info from the dojos table so we can start manipulating sql 
        query = "SELECT * FROM dojos;"
        # query -> the way we pull information from our tables database(s) giving it commands 
        results = connectToMySQL('dojos_ninjas_schema').query_db(query)
        # make sure to call the connectToMySQL function with the schema you are targeting.
        dojos = []
        # Create an empty list to append our instances
        # name this whatever the name is of one of your tables 

    # Iterate over the database results and create instances of friends with cls.
        if results:
            for u in results:
                new_dojo = cls(u)
                # change new_dojo
                dojos.append(new_dojo)
            return dojos
        # you can copy and paste this whole thing BUT change the names after results

    # Now we use class methods to query our database
    @classmethod
    def create (cls, data):
    # the create is linked to route create in dojo_controller 
        query = "INSERT into dojos(name) VALUES(%(name)s);"
        # query -> the way we pull information from our tables database(s) / giving it commands 
        # this sql is inserting into dojos(name) value of (%(writing down different names into the column)s)
        results = connectToMySQL('dojos_ninjas_schema').query_db(query, data)
        # retrieving the outcome of sqlquery in workbench so we can display it in the front end 
        return results
        # displaying the information we retrieved from our schema when we used query  

    
    @classmethod
    def display (cls, data):
        query = "SELECT * FROM dojos WHERE name= %(name)s"
        results = connectToMySQL('dojos_ninjas_schema').query_db(query, data)
        return results
    
    @classmethod
    def show(cls, id):
        data = {
        "id": id
        }

        query = "SELECT * FROM dojos JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;"

        results = connectToMySQL('dojos_ninjas_schema').query_db(query, data)

        if results:
            dojo = cls(results[0])

            ninjas = []
            for row in results: 
                ninjas_data = {
                    **row,
                    'id': row['ninjas.id'],
                    'created_at': row['ninjas.created_at'],
                    'updated_at': row['ninjas.updated_at']
                }

                new_ninja = ninja_model.Ninja(ninjas_data)
                ninjas.append(new_ninja)

            dojo.ninjas = ninjas 

        return dojo


# query = "SELECT first_name, last_name, age FROM ninjas JOIN dojos ON dojo_id = dojos.id WHERE dojos.id = %(dojos.id)s;"


        # if result: 
        #     dojo = cls(result[0])
        #     ninjas = []
        #     for row in result:
        #         ninjas_data = {
        #             **row
        #             'id': row['ninjas.id'],
        #             'created_at': row['created_at'],
        #             'updated_at': row['updated_at']
        #         }
        
        #     new_ninja = ninja_model.Ninja(ninjas_data)

        #     ninjas.append(new_ninja)

        #     dojo.ninjas = ninjas


    
