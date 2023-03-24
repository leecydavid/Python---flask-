# model is everything happening in the backend - 
# anything we want to get done in sql we will manipulate it from this file

from flask_app.config.mysqlconnection import connectToMySQL\
# import the function that will connect mysqlconnection.py to connectToMySQL 
    # this function allows us to connect mysql to the front end(flask)

class Ninja:
    # always set this class to Upper case to whatever the name is of one of your table names but singular
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.dojo_id = data['dojo_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
# this class is getting all the column-names in the ninjas table
        # take in self and data(with data you can transfer the table variables and target them in different ways when we refer back to data, you'll see)

    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
    # the get_all is retrieving all info from the dojos table so we can start manipulating sql 
        query = "SELECT * FROM ninjas;"
        # query -> the way we pull information from our tables database(s) / giving it commands 
        # refer back to wrlds assignment on how to write sql queries!!!!
        results = connectToMySQL('dojos_ninjas_schema').query_db(query)
        # make sure to call the connectToMySQL function with the schema you are targeting.
        ninjas = []
        # this should be set to whatever the name is of the table you are targeting 
        # Create an empty list to append our instances

        # Iterate over the database results and create instances of friends with cls.
        if results:
            for u in results:
                new_ninja= cls(u)
                # change new_ninja
                ninjas.append(new_ninja)
            return ninjas
        # you can copy and paste this whole thing BUT change the names after results
        
    @classmethod
    def new_create(cls, data):
        query = "INSERT INTO ninjas(first_name, last_name, age, dojo_id) VALUES(%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);"
        # this sql is adding into the table(select columns you want to add info to) 
            # VALUES(%(actually writing down the information we want to include into the columns we selected)s)    
        result = connectToMySQL('dojos_ninjas_schema').query_db(query, data)
        # retrieving the outcome of sqlquery in workbench so we can display it in the front end 
        return result


    
    @classmethod
    def save(cls, data):
        query = "SELECT * FROM ninjas WHERE name = %(name)s"
        # selecting all columns from ninjas table --> selecting (name) specifically 
        result = connectToMySQL('dojos_ninjas_schema').query_db(query, data)
        # result = retrieivng the query we set above from our schema (workbench) 
        return result
        # displaying the information we retrieved from our schema when we used query  

        

