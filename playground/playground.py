# # Get comfortable passing information from the route to the template
# Understand how to display information passed from the route in the template file
# Get comfortable using for loops in the template file
# Get comfortable using if statements in the template file

from flask import Flask, render_template
# render_template = need in order to connect template folder
app = Flask(__name__)


@app.route('/')
def index():
    return "Hello! Please go to localhost5002 to play game!"
# no render_template = localhost5002 will display the return statement 

@app.route('/play')
def render_block():
    return render_template("index.html", num=3)
# because we render_template and connect this file to the html file, whatever is updated in the html file will be displayed in the browser
# num=3 (connect back to html file for loop) 
# num is set to 3 - the loop will run through as many times we set num to be
    # Jinja = {{variable}} {% expression = for, if, while, etc. %}

@app.route('/play/<int:num>')
def mult_block(num):
    return render_template("index.html", num=num)
# <int:num> you are setting argument num as an intenger not a string
# compared to the previous route, we have now set num=num 
    # we can now set num to any number we want it to be
        # in our browser we can say '/play/(input any number)' and the for loop will run as many times we set the number in the browser 
            # in this case, we can say '/play/10' and 10 boxes will be displayed in our website

@app.route('/play/<int:num>/<color>')
def change_color(num, color):
    return render_template("index.html", num=num, color=color)
# now we add another argument color=color 
# inside our route arguments, we have include <color> 
# inside the for loop in html, we have set color as a variable = {{color}}
# this allows us to input whatever color we want into our browser and the background color of the boxes will change to the specifiec color
    # /'play/10/pink' = we will get 10 boxes that are pink 


if __name__ == "__main__":
    app.run(debug=True, port=5001)

