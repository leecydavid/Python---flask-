from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key = 'nomames'
# remember, when using session, we always need an app.secret_key = ''


@app.route('/')
def index():
    session.clear()
    # .clear() because when the user presses the Go Back button
    return render_template('index.html')

@app.route('/displayinfo', methods = ['POST'])
def displaypy():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']

    return redirect('/result')

@app.route('/result')
def result():
    return render_template('displayinfo.html')



if __name__ == "__main__":
    app.run(debug=True, port=5001)


# The POST method is used to send data mostly through a form to the server for creating or updating data in the server.