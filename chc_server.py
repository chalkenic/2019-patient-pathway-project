import os
from flask import Flask, redirect, request,render_template, make_response, escape, jsonify, session
import sys
import sqlite3

# sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

DATABASE = 'survey_project.db'

serv = Flask(__name__)
serv.secret_key = 'alanr?jn312653'

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'css'])

@serv.route("/home", methods = ['POST','GET'])
def frontPage():
    if request.method == 'GET':
        username = request.cookies.get('username')

        if username is not None:
            return render_template('00_homepage.html', username = username, section_name = str(f'{username}\'s '), welcome = str(f'Welcome {username}!'))
        else:
            return render_template('00_homepage.html', username = "", section_name = str(""))
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
                return render_template('01-2-admin_section.html', username = username, section_name = str(f'{username}\'s '), welcome = str(f'Welcome {username}!'))
            else:
                return render_template('01-2-admin_section.html', username = "", section_name = str(""))

        elif Access == "User":
            if username is not None:
                return user_graph()
                # return render_template('01-1-user_section.html', username = username, section_name = str(f'{username}\'s '), welcome = str(f'Welcome {username}!'))
            else:
                return render_template('01-1-user_section.html', username = "", section_name = str(""))

        else:

            return render_template('00_homepage.html', login_message = 'Please login to access your section', username = '', section_name = str(""))

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
        else:
            username = ''
            if 'username' in session:
                username = escape(session['username'])
            return render_template('00_homepage.html', login_message ='', username = '')

@serv.route("/survey", methods = ['POST','GET'])
def survey():
    if request.method == 'GET':
        username = request.cookies.get('username')

        if username is not None:
            return render_template('03-survey.html', username = username, section_name = str(f'{username}\'s '), welcome = str(f'Welcome {username}!'))
        else:
            return render_template('03-survey.html', username = "", section_name = str(""))

    elif 'initial_survey' in request.form:

        Date = request.form.get('Date', default = 'error')
        Q1 = request.form.get ('Q1', default = 'error')
        Q2 = request.form.get ('Q2', default = 'error')
        Q3 = request.form.get('Q3', default = 'error')
        Q4 = request.form.get('Q4', default = 'error')
        Q5 = request.form.get('Q5', default = 'error')

        try:
            request.form.get('')
            conn = sqlite3.connect(DATABASE)
            cur = conn.cursor ()
            cur.execute("INSERT INTO Survey('ACCOUNT ID', 'Date', 'Q1', 'Q2', 'Q3', 'Q4', 'Q5') VALUES (1,'','','','','','');"
            )
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

@serv.route("/LTS-surv", methods = ['POST','GET'])
def LTS_surv():
    if request.method == 'GET':
        username = request.cookies.get('username')

        if username is not None:
            return render_template('04-Local&ThirdSector.html', username = username, section_name = str(f'{username}\'s '), welcome = str(f'Welcome {username}!'))
        else:
            return render_template('04-Local&ThirdSector.html', username = "", section_name = str(""))

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
    tmp = username.split('@')
    user = tmp[0]
    password = request.form.get('user_password', default="Error")
    if login_credentials(username, password) == True:
        response = make_response(render_template('00_homepage.html',
        username = user,
        login_message = 'hello ' + user,
        section_name = str(f'{user}\'s ', welcome = str(f'Welcome {username}!'))))

        response.set_cookie('username', user )

        if user == 'Nick':
            response.set_cookie('Access', 'Admin')

        else:
            response.set_cookie('Access','User')

        # session['user_email'] = request.form['user_email']
        # session['Password'] = request.form['user_password']
        # print("Password checks out, hello " + user + "!")

    else:
        response = make_response(render_template('00_homepage.html', login_message ='Incorrect login, please try again', username=""))
    return response


# @serv.route("/contact_us", methods=['POST', 'GET'])
# def addform():
# 	if request.method =='GET':
# 		return render_template('contactus.html')
# 	if request.method =='POST':
# 		forename = request.form.get('name', default="Error")#rem: args for get form for post
# 		surname = request.form.get('lname', default="Error")
# 		emailaddress = request.form.get('email', default="Error")
# 		query = request.form.get('query', default="Error")
# 		print("inserting query into database")
#     try:
#         request.form.get('')
#         conn = sqlite3.connect(DATABASE)
#         cur = conn.cursor ()
#         cur.execute("INSERT INTO Contact('queryID', 'firstName', 'lastName', 'emailAddress', 'query')"
#         )
#         conn.commit()
#         msg ="Contact us form successfully recorded"
#     except:
#         conn.rollback()
#         msg ="Error"
#     finally:
#         return msg
#         conn.close()

# /* TEST STUFF!!! */
# /* TEST STUFF!!! */
# /* TEST STUFF!!! */
# /* TEST STUFF!!! */
# /* TEST STUFF!!! */
# /* TEST STUFF!!! */
# /* TEST STUFF!!! */

def user_graph():

    username = request.cookies.get('username')

    try:
        db = sqlite3.connect(DATABASE)
        cursor = db.cursor()
        cursor.execute('''SELECT surveyData.date, surveyData.happiness_q
        FROM surveyData
        INNER JOIN accounts
        ON surveyData.accountID = accounts.userID
        WHERE accounts.userID = 1''')


        data = cursor.fetchall()
        print(data)

    except:
        print("Unfortunately an error has occurred", data)
        db.close()

    finally:
        db.close()

        username = request.cookies.get('username')

        return render_template('01-1-user_section.html', data = data, username = username, section_name = str(f'{username}\'s '), welcome = str(f'Welcome {username}!'))

if __name__ == "__main__":
    serv.run(debug=True)
