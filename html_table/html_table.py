from flask import Flask, render_template 
# render_template = need in order to connect template folder 
app = Flask(__name__)    

@app.route('/')          
def index():
    return "Welcome to HTML Table Assignment"

@app.route('/data')
def table ():
    users = [
    {'first_name' : 'Michael', 'last_name' : 'Choi'},
    {'first_name' : 'John', 'last_name' : 'Supsupin'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
    return render_template("index.html", users=users)

# the dictionary above will be displayed in our data browser 
    # we are able to pass this into our html = look at the for loop in html
        # first in our for loop we say 'for name in users' (we are connecting users in python so that it can be displayed in the html)
            # we have set first_name , last_name, full_name into variables using {{}}
                # next, we target specific names with [] = this targets the values that are set in our python into our html
                    # for example: ['first_name'] will transfer the first_name value in python into the html so that it can be displayed in our website


if __name__=="__main__":       
    app.run(debug=True, port=5001)   