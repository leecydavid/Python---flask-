from flask import Flask  # Import Flask to allow us to create our app
#1 localhost:5000/ - have it say "Hello World!"
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

#2 localhost:5000/dojo - have it say "Dojo!"
@app.route('/dojo')
def success():
    return "Dojo!"

#3 Create one url pattern and function that can handle the following examples:
# localhost:5000/say/flask - have it say "Hi Flask!"
# localhost:5000/say/michael - have it say "Hi Michael!"
# localhost:5000/say/john - have it say "Hi John!"
@app.route('/say/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hello(name):
    print(name)
    return "Hi, " + name

#4 Create one url pattern and function that can handle the following examples (HINT: path variables are by default passed as strings. How might you handle a number?):
# localhost:5000/repeat/35/hello - have it say "hello" 35 times
# localhost:5000/repeat/80/bye - have it say "bye" 80 times
# localhost:5000/repeat/99/dogs - have it say "dogs" 99 times
@app.route('/repeat/<int:number>/<word>')
def repeat(number, word):
    print(number, word)
    return number * word 

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True, port=5001)    # Run the app in debug mode.python



