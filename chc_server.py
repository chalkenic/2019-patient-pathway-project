import os
from flask import Flask, redirect, request,render_template, make_response, escape, jsonify, session
import sys
import sqlite3

# sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# sess = Session()
# sess.init_app(app)



serv = Flask(__name__)
serv.secret_key = 'alanr?jn312653'

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'css'])

@serv.route("/home", methods = ['POST','GET'])
def frontPage():
    if request.method == 'GET':
        username = request.cookies.get('username')
        return render_template('00_homepage.html', username = username)
    if request.method == 'POST':

        if 'login1' in request.form:
            return user_login()

        else:
            username = ''
            if 'username' in session:
                username = escape(session['username'])
            return render_template('00_homepage.html', login_message ='', username = 'None')

def login_credentials(username, password):
        if username != None:
            if password != None:
                return True
            else:
                return False
        else:
            return False

def user_login():
    username = request.form.get('user_email', default="Error")
    tmp = username.split('@')
    user = tmp[0]
    password = request.form.get('user_password', default="Error")
    if login_credentials(username, password) == True:
        response = make_response(render_template('00_homepage.html',username = user, login_message = 'hello ' + user))

        response.set_cookie('username', user )

        session['user_email'] = request.form['user_email']
        session['Password'] = request.form['user_password']
        print("Password checks out, hello " + user + "!")

    else:
        response = make_response(render_template('00_homepage.html', login_message ='Incorrect login, please try again', username=""))
    return response

@serv.route("/section", methods = ['POST','GET'])
def section():
    if request.method == 'GET':
        username = request.cookies.get('username')
        return render_template('01-p_section.html', username = username)

    if request.method == 'POST':

        if 'login1' in request.form:
            return user_login()

        else:
            username = ''
            if 'username' in session:
                username = escape(session['username'])
            return render_template('00_homepage.html', login_message ='', username = 'None')

@serv.route("/survey", methods = ['POST','GET'])
def survey():
    if request.method == 'GET':
        username = request.cookies.get('username')
        return render_template('03-survey.html', username = username)


    if request.method == 'POST':

        if 'login1' in request.form:
            return user_login()

        else:
            username = ''
            if 'username' in session:
                username = escape(session['username'])
            return render_template('00_homepage.html', login_message ='', username = 'None')

@serv.route("/LTS-surv", methods = ['POST','GET'])
def LTS_surv():
    if request.method == 'GET':
        username = request.cookies.get('username')
        return render_template('04-Local&ThirdSector.html', username = username)

    if request.method == 'POST':
        if 'login1' in request.form:
            return user_login()

        else:
            username = ''
            if 'username' in session:
                username = escape(session['username'])
            return render_template('00_homepage.html', login_message ='', username = 'None')


@serv.route("/contact", methods = ['POST','GET'])
def contactUs():
    if request.method == 'GET':
        username = request.cookies.get('username')
        return render_template('02-contact_us.html', username = username)

    if request.method == 'POST':
        if 'login1' in request.form:
            return user_login()

        else:
            username = ''
            if 'username' in session:
                username = escape(session['username'])
            return render_template('00_homepage.html', login_message ='', username = 'None')



# /* TEST STUFF!!! */
# /* TEST STUFF!!! */
# /* TEST STUFF!!! */
# /* TEST STUFF!!! */
# /* TEST STUFF!!! */
# /* TEST STUFF!!! */
# /* TEST STUFF!!! */


if __name__ == "__main__":
    serv.run(debug=True)
