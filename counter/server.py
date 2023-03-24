from flask import Flask, render_template, session, redirect
app = Flask(__name__)
app.secret_key = 'nomames'  
# when using session, we always need a app.secret_key
    # set it whatever string you want - the more complicated the better for privacy reasons 

@app.route('/')
def index():
    if 'count' not in session:
    # 'count' is set to session key when we set name=count {{session['count']}} (html line 14)
        session['count'] = 1
    else: 
        session['count'] += 1
    return render_template('index.html') 
# if statement is used to increment count everytime the user visits the default browser 
    # so everytime the user visits the home page, count goes up by one 
        # if count is not in session(so if user is not in the page), we just leave count at 1 but if count is in session(user is in the browser) than count increment by 1
# 1) first connect 'count' with html by setting name='count' in the html --> this allows us to update the display of count in our default page
# 2) in html, we create variable {{session}} and target 'count' by placing it in [] --> refer to playground notes 

@app.route('/play')
def play():
    session['count'] += 1
    return redirect('/')
# 3) we create '/play' route to display the actual increment of 'count' in the html side of our website (frontend)
    # we connect '/play/ by using anchor tag and href='/play/ (html line 15)
        # everytime we click the 'click' button (html line 15), it will direct the user to '/play' browser and increment count by 1
            # return redirect('/') = everytime the user clicks the 'click' button, count will increment but the page will be redirected to the homepage 
                

@app.route('/clear')
def counter():
    session.clear()
    return redirect('/')
# 4) we create '/clear' route to reset the information / or when someone logs out, we want to delete all our their private infromation 
    # we connect '/clear' by referencing it back into our html (html line 16)
    # we use session.clear() which will clear all the session information 
        # return redirect('/') = everytime the user clicks 'reset', the session information will display 1 and it will displayed on the homepage 



if __name__=="__main__":     
    app.run(debug=True, port=5001) 


# session: used to pass around information that we dont want to be public, we want it to be hidden
    # session is used to pass information within the browser but when user leaves the page, session will also disappear (hence the name 'session')
        # the user visting a page is a session for that user 
    # sessions are temporary and are stored in the browser, not on the clients side
