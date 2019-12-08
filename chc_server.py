import os
from flask import Flask, redirect, request,render_template, make_response, escape, jsonify, session
import sys
import sqlite3
import json

# Login Imports
import sqlite3 as sql
import models as dbHandler
import models

# sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

DATABASE = 'survey_project.db'

serv = Flask(__name__)
serv.secret_key = 'alanr?jn312653'

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'css'])

# Login System
# class LoginForm(FlaskForm):
#     username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
#     password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=25)])

#
# def insertUser(email_addr,password):
#     con = sql.connect("survey_project.db")
#     cur = con.cursor()
#     cur.execute("INSERT INTO accounts (email_addr,password) VALUES (?,?)", (email_addr,password))
#     con.commit()
#     con.close()
#
# def retrieveUsers():
# 	con = sql.connect("survey_project.db")
# 	cur = con.cursor()
# 	cur.execute("SELECT email_addr, password FROM accounts")
# 	users = cur.fetchall()
# 	con.close()
# 	return users

# #
# @serv.route('/register', methods=['POST', 'GET'])
# def home():
#     if request.method=='POST':
#         email_addr = request.form['email_addr']
#         password = request.form['password']
#         dbHandler.insertUser(email_addr, password)
#         users = dbHandler.retrieveUsers()
#         return render_template('register.html', users=users)
#     else:
#         return render_template('register.html')
#
# @serv.route('/register', methods=['POST', 'GET'])
# def home():
#     if request.method=='POST':
#         return render_template('register.html', users=users)
#     else:
#         return render_template('register.html')

#
# @serv.route('/register/addRecord', methods=['GET'])
# def newUser():
#     try:
#         conn = sqlite3.connect(DATABASE)
#         cur = conn.cursor()
#         cur.execute("INSERT INTO accounts ('email_addr', 'name', 'password', access) VALUES (?,?,?,?)", ("nik@nik.com", "Nikrad", "Nikniknik.1", "User"))
#         conn.commit()
#         msg = "Record Successfuly added"
#     except:
#         conn.rollback()
#         msg = "error in insert operation"
#     finally:
#         return msg
#         conn.close()


@serv.route("/register", methods = ['POST', 'GET'])
def newUser():
    if request.method == 'GET':
        return render_template('register.html')
    if request.method == 'POST':
        regEmail = request.form.get('email1', default = 'error')
        regPass1 = request.form.get ('pass1', default = 'error')
        regPass2 = request.form.get ('pass2', default = 'error')
        try:
            request.form.get('')
            conn = sqlite3.connect(DATABASE)
            cur = conn.cursor ()
            cur.execute("INSERT INTO main.accounts('email_addr','name','password','access') VALUES (?,?,?,?)", (regEmail, regPass1, regPass, "User"))

            conn.commit()
            msg ="Survey Data successfully recorded"
        except:
            conn.rollback()
            msg ="Error"
        finally:
            return msg
            conn.close()







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




# @serv.route("/register", methods = ['POST','GET'])
# def register():
#     if request.method == 'GET':
#         username = request.cookies.get('username')
#
#         if username is not None:
#             return render_template('register.html', username = username, section_name = str(f'{username}\'s '), welcome = str(f'Welcome {username}!'))
#         else:
#             return render_template('register.html', username = "", section_name = str(""))
#
#     if request.method == 'POST':
#         if 'login1' in request.form:
#             return user_login()
#
#         else:
#             username = ''
#             if 'username' in session:
#                 username = escape(session['username'])
#             return render_template('00-1-empty_homepage.html', login_message ='', username = '')


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
                get_all_users()

                return render_template('01-2-admin_section.html', username = username, section_name = str(f'{username}\'s '), welcome = str(f'Welcome {username}!'))
            else:
                return render_template('01-2-admin_section.html', username = "", section_name = str(""))

        elif Access == "User":
            if username is not None:
                return graph_data(username)
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

@serv.route("/allAccounts", methods = ['GET', 'POST'])
def allAccounts():

    if request.method == 'GET':
        username = request.cookies.get('username')
        # get_all_users()

        db = sqlite3.connect(DATABASE)
        query = "SELECT userID, email_addr, name, access from accounts"
        cursor = db.cursor()

        cursor.execute(query)

        data = cursor.fetchall()


        # all_accounts = json.dumps(data)
        #
        # items = [dict(zip([key[0] for key in cursor.description],row))for row in data]

        db.commit()
        db.close()

        return render_template('01-2-allAccounts.html', data = data, username = username, section_name = str(f'{username}\'s '), welcome = str(f'Welcome {username}!'))

    if request.method == 'POST':
            return user_login()

@serv.route("/survey", methods = ['POST','GET'])
def survey():
    if request.method == 'GET':
        username = request.cookies.get('username')

        if username is not None:
            return render_template('03-daily_survey.html', username = username, section_name = str(f'{username}\'s '), welcome = str(f'Welcome {username}!'))
        else:
            return render_template('03-daily_survey.html', username = "", section_name = str(""))

    elif 'survey' in request.form:
        
        Date = request.form.get('Date', default = 'error')
        Health = request.form.get ('Health', default = 'error')
        SocialCare = request.form.get ('SocialCare', default = 'error')
        LocalAuthority = request.form.get('LocalAuthority', default = 'error')
        ThirdSector = request.form.get('ThirdSector', default = 'error')
        OwnActivities = request.form.get('OwnActivities', default = 'error')

        try:
            request.form.get('')
            conn = sqlite3.connect(DATABASE)
            cur = conn.cursor ()
            cur.execute("INSERT INTO Survey('Date','Health','SocialCare','LocalAuthority','ThirdSector','OwnActivities') VALUES (?,?,?,?,?,?)",(Date, Health, SocialCare, LocalAuthority, ThirdSector, OwnActivities));

            conn.commit()
            msg ="Survey Data successfully recorded. See You Tomorrow!"
        except Exception as e:
            conn.rollback()
            print(e)
            msg ="Something's gone wrong :("
        finally:
            conn.close()

    return render_template('03-daily_survey.html', msg = msg)
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

@serv.route("/Diary", methods = ['POST', 'GET'])
def Diary():
    if request.method == 'GET':
        return render_template('05- Diary.html')

# FAQ LINKING
@serv.route("/FAQ", methods = ['POST', 'GET'])
def FAQ():
    if request.method == 'GET':
        return render_template('FAQ.html')

#CONTACT US USERS LINK
@serv.route("/contact_us_users", methods = ['POST', 'GET'])
def contact_us_users_link():
    if request.method == 'GET':
        return render_template('02-contact_us_users.html')

# ADMIN CONTACT US LINK
@serv.route("/admin_contact", methods = ['POST', 'GET'])
def admin_contact_link():
    if request.method == 'GET':
        return render_template('admin_contact.html')

@serv.route("/contact", methods = ['POST','GET'])
def contactUs():
    if request.method == 'GET':
        return render_template('02-contact_us.html', username = "", section_name = str(""))

    if request.method == 'POST':
        if 'login1' in request.form:
            return user_login()

        else:
            username = ''
            if 'username' in session:
                username = escape(session['username'])
            return render_template('00_homepage.html', login_message ='', username = '')

# Adapted from stackoverflow "ThiefMaster" question Flask: How to remove cookies?. Available at: https://stackoverflow.com/questions/14386304/flask-how-to-remove-cookies



@serv.route("/contact_us", methods = ['POST', 'GET'])
def contactFormdata():
    if request.method =='GET':

        username = request.cookies.get('username')

        if username is not None:
            return render_template('02-contact_us_users.html', username = username, section_name = str(f'{username}\'s '), welcome = str(f'Welcome {username}!'))
        else:
            return render_template('02-contact_us.html')

    if request.method =='POST':

        if 'login1' in request.form:
            return user_login()

        elif 'form_submission_guest' in request.form:
            add_firstName = request.form.get('firstName', default="Error")
            add_lastName = request.form.get('lastName', default="Error")
            add_email = request.form.get('email', default="Error")
            add_query = request.form.get('query', default="Error")
            print("inserting contact result "+ add_firstName)
            print(add_lastName)
            # try:
            conn = sqlite3.connect(DATABASE)
            cur = conn.cursor()
            # cur.execute("INSERT INTO contactForm ('firstName', 'surname', 'email', 'query')\
			# 		VALUES (?,?,?,?)",(add_firstName, add_lastName, add_email, add_query) )
            cur.execute("INSERT INTO contactForm ('firstName', 'lastName', 'email', 'query') VALUES (?,?,?,?)", (add_firstName, add_lastName, add_email, add_query))
            # cur.fetchall()
            conn.commit()
            msg = "Thanks, we'll respond as soon as possible."
        # # except:
        #     conn.rollback()
        #     msg = "error in insert operation"
        # # finally:
        #     conn.close()
            return render_template('02-contact_us.html', msg = msg)


        # session['user_email'] = request.form['user_email']
        # session['Password'] = request.form['user_password']
        # print("Password checks out, hello " + user + "!")

@serv.route("/logout", methods = ['GET', 'POST'])
def logout():

    if request.method == 'GET':
        logout = make_response(render_template('00-1-empty_homepage.html', login_message ="Logged out successfully", username = None))
        logout.set_cookie('username', expires = 0)
        logout.set_cookie('email_addr', expires = 0 )
        logout.set_cookie('Access', expires = 0)
        return logout

    if request.method == 'POST':
        return user_login()

# FUNCTIONS
# FUNCTIONS
# FUNCTIONS

def graph_data(username):

    email = request.cookies.get('email_addr')
    print(email)

    try:
        db = sqlite3.connect(DATABASE)
        cursor = db.cursor()
        print("Working 0")

        cursor.execute('''SELECT surveyID, email_addr, happiness_q,contact_q, date FROM surveyData\
        INNER JOIN accounts\
        ON surveyData.accountID=accounts.userID\
        WHERE email_addr =?;''', [email])

        data = cursor.fetchall()
        print(data)

        js_data = json.dumps(data)
        print("Working 1")
        print(js_data)

    except:
        print("Unfortunately an error has occurred", data)
        db.close()

    finally:
        db.close()

        username = request.cookies.get('username')

        return render_template('01-1-user_section.html', username = username, section_name = str(f'{username}\'s '), welcome = str(f'Welcome {username}!'), lineg_data = json.loads(js_data))

def get_all_users():

    db = sqlite3.connect(DATABASE)
    query = "SELECT * from accounts"
    cursor = db.cursor()

    cursor.execute(query)

    data = cursor.fetchall()

    all_accounts = json.dumps(data)
    #
    # items = [dict(zip([key[0] for key in cursor.description],row))for row in data]

    print()
    rows = cursor.fetchall()

    db.commit()
    db.close()

    return data

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

    else:
        response = make_response(render_template('00_homepage.html', login_message ='Incorrect login, please try again', username=""))
    return response

if __name__ == "__main__":
    serv.run(debug=True)
