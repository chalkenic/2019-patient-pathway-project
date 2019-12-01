import os
from flask import Flask, redirect, request,render_template, make_response, escape, jsonify, session
import sys
import sqlite3
import json

# sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

DATABASE = 'survey_project.db'

serv = Flask(__name__)
serv.secret_key = 'alanr?jn312653'

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'css'])

# Login System
class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=25)])



@serv.route("/home", methods = ['POST','GET'])
def frontPage():
    if request.method == 'GET':
        username = request.cookies.get('username')
        access = request.cookies.get('Access')

        if access == "Admin":

            if username is not None:
                return render_template('00-2-admin_homepage.html', username = username, section_name = str(f'{username}\'s '), welcome = str(f'Welcome {username}!'))
            else:
                return render_template('00-1-empty_homepage.html', username = "", section_name = str(""))

        elif access == "User":
                if username is not None:
                    return render_template('00-3-user_homepage.html', username = username, section_name = str(f'{username}\'s '), welcome = str(f'Welcome {username}!'))
                else:
                    return render_template('00-1-empty_homepage.html', username = "", section_name = str(""))
        else:
            return render_template('00-1-empty_homepage.html', username = "", section_name = str(""))
    if request.method == 'POST':

        if 'login1' in request.form:
            return user_login()

        elif 'regLink' in request.form:
            return render_template('register.html')

        else:
            username = ''
            if 'username' in session:
                username = escape(session['username'])
            return render_template('00_homepage.html', login_message ='', username = '')




@serv.route("/register", methods = ['POST','GET'])
def register():
    if request.method == 'GET':
        username = request.cookies.get('username')

        if username is not None:
            return render_template('register.html', username = username, section_name = str(f'{username}\'s '), welcome = str(f'Welcome {username}!'))
        else:
            return render_template('register.html', username = "", section_name = str(""))

    if request.method == 'POST':
        if 'login1' in request.form:
            return user_login()

        else:
            username = ''
            if 'username' in session:
                username = escape(session['username'])
            return render_template('00_homepage.html', login_message ='', username = '')


@serv.route("/section", methods = ['POST','GET'])
def section():
    if request.method == 'GET':
        username = request.cookies.get('username')
        Access = "empty"
        #TBC content:
        # if 'Access' in session:
        #     Access = escape(session['Access'])

        #Temp:
        Access = request.cookies.get('Access')

        if Access == "Admin":
            if username is not None:
                get_all_users(json_str = True)

                return render_template('01-2-admin_section.html', username = username, section_name = str(f'{username}\'s '), welcome = str(f'Welcome {username}!'))
            else:
                return render_template('01-2-admin_section.html', username = "", section_name = str(""))

        elif Access == "User":
            if username is not None:
                return experience_graph(username)
                # return render_template('01-1-user_section.html', username = username, section_name = str(f'{username}\'s '), welcome = str(f'Welcome {username}!'))
            else:
                return render_template('01-1-user_section.html', username = "", section_name = str(""))

    if request.method == 'POST':

        if 'login1' in request.form:
            return user_login()

        elif 'patient_search' in request.form:
            try:
                email_search = request.form.get('email_search', default ='Error')

                db = sqlite3.connect(DATABASE)
                cursor = db.cursor()
                cursor.execute("SELECT * FROM accounts WHERE email_addr=? AND Access = 'User' ;", [email_search])
                data = cursor.fetchall()
                print(data)

            except:
                print("Unfortunately an error has occurred", data)
                db.close()

            finally:
                db.close()

                username = request.cookies.get('username')
                return render_template('01-3-patient_target_list.html', data = data, username = username, section_name = str(f'{username}\'s '), welcome = str(f'Welcome {username}!'))

@serv.route("/survey", methods = ['POST','GET'])
def survey():
    if request.method == 'GET':
        username = request.cookies.get('username')

        if username is not None:
            return render_template('03-daily_survey.html', username = username, section_name = str(f'{username}\'s '), welcome = str(f'Welcome {username}!'))
        else:
            return render_template('03-daily_survey.html', username = "", section_name = str(""))

    elif 'initial_survey' in request.form:

        Date = request.form.get('Date', default = 'error')
        Health = request.form.get ('Health', default = 'error')
        Social_Care = request.form.get ('Q2', default = 'error')
        Local_Authority = request.form.get('Q3', default = 'error')
        Third_Sector = request.form.get('Q4', default = 'error')
        Own_Activities = request.form.get('Q5', default = 'error')

        try:
            request.form.get('')
            conn = sqlite3.connect(DATABASE)
            cur = conn.cursor ()
            cur.execute("INSERT INTO main.Survey('Date','Health','Social_Care','Local_Authority','3rd_Sector', 'Own_Activities') VALUES (?,?,?,?,?,?)", (Date, Health, Social_Care, Local_Authority, Third_Sector, Own_Activities) )

            conn.commit()
            msg ="Survey Data successfully recorded"
        except:
            conn.rollback()
            msg ="Error"
        finally:
            return msg
            conn.close()


    if request.method == 'POST':

        if 'login1' in request.form:
            return user_login()

        else:
            username = ''
            if 'username' in session:
                username = escape(session['username'])
            return render_template('00_homepage.html', login_message ='', username = '')



    if request.method == 'POST':
        if 'login1' in request.form:
            return user_login()

        else:
            username = ''
            if 'username' in session:
                username = escape(session['username'])
            return render_template('00_homepage.html', login_message ='', username = '')


@serv.route("/contact", methods = ['POST','GET'])
def contactUs():
    if request.method == 'GET':
        username = request.cookies.get('username')

        if username is not None:
            return render_template('02-contact_us.html', username = username, section_name = str(f'{username}\'s '), welcome = str(f'Welcome {username}!'))
        else:
            return render_template('02-contact_us.html', username = "", section_name = str(""))

    if request.method == 'POST':
        if 'login1' in request.form:
            return user_login()

        else:
            username = ''
            if 'username' in session:
                username = escape(session['username'])
            return render_template('00_homepage.html', login_message ='', username = '')


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
    email_addr = request.form.get('user_email', default="Error")
    tmp = username.split('@')
    user = tmp[0]
    password = request.form.get('user_password', default="Error")
    # if login_credentials(username, password) == True:
    if user == "Nick":

        response = make_response(render_template('00-2-admin_homepage.html',
        username = user,
        welcome = 'Welcome ' + user + "!",
        email = email_addr,
        section_name = str(f'{user}\'s ')))

        response.set_cookie('username', user )
        response.set_cookie('email_addr', email_addr )
        response.set_cookie('Access', 'Admin')

    elif user != "Nick":
        response = make_response(render_template('00-3-user_homepage.html',
        username = user,
        welcome = 'Welcome ' + user + "!",
        email = email_addr,
        section_name = str(f'{user}\'s ')))

        response.set_cookie('username', user )
        response.set_cookie('email_addr', email_addr )
        response.set_cookie('Access','User')

        # session['user_email'] = request.form['user_email']
        # session['Password'] = request.form['user_password']
        # print("Password checks out, hello " + user + "!")

    else:
        response = make_response(render_template('00_homepage.html', login_message ='Incorrect login, please try again', username=""))
    return response


@serv.route("/contact_us", methods = ['POST', 'GET'])
def contactFormdata():
    if request.method =='GET':

        username = request.cookies.get('username')

        if username is not None:
            return render_template('02-contact_us_users.html')
        else:
            return render_template('02-contact_us.html')

    if request.method =='POST':
        firstName = request.form.get('firstName', default="Error")
        lastName = request.form.get('lastName', default="Error")
        email = request.form.get('email', default="Error")
        query = request.form.get('query', default="Error")
        print("inserting contact form"+firstName)
        try:
            conn = sqlite3.connect(DATABASE)
            cur = conn.cursor()
            cur.execute("INSERT INTO contactForm ('firstName', 'lastName', 'email', 'query')\
                VALUES (?,?,?,?,?)", (firstName, lastName, email, query, "True") )

            conn.commit()
            msg = "Query successfully added"
        except:
            conn.rollback()
            msg = "Error adding Query"
        finally:
            conn.close()
            return msg

def get_all_users(json_str = False):

    db = sqlite3.connect(DATABASE)
    query = "SELECT * from accounts"
    cursor = db.cursor()

    data = cursor.execute(query)

    items = [dict(zip([key[0] for key in cursor.description],row))for row in data]

    print()
    rows = cursor.fetchall()

    db.commit()
    db.close()

    if json_str:
        with open('accounts_data.json', 'w') as json_file:
            json.dump(rows, json_file)

def experience_graph(username):

    email = request.cookies.get('email_addr')
    print(email)

    try:
        db = sqlite3.connect(DATABASE)
        cursor = db.cursor()
        print("Working 0")
        cursor.execute("SELECT userID from accounts WHERE email_addr=?", [email])

        print("Working 1")
        id = cursor.fetchall()

        cursor.execute('''SELECT surveyID, email_addr, happiness_q, date FROM surveyData\
        INNER JOIN accounts\
        ON surveyData.accountID=accounts.userID\
        WHERE email_addr =?;''', [email])

        data = cursor.fetchall()

        js_data = json.dumps(data)
        print("Working 6")

    except:
        print("Unfortunately an error has occurred", data)
        db.close()

    finally:
        db.close()

        username = request.cookies.get('username')

        return render_template('01-1-user_section.html', username = username, section_name = str(f'{username}\'s '), welcome = str(f'Welcome {username}!'), data = json.loads(js_data))

if __name__ == "__main__":
    serv.run(debug=True)
