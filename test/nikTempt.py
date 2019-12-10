@serv.route("/register", methods = ['POST', 'GET'])
def newUser():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        regEmail = request.form.get('registerEmail', default = 'error')
        regPass1 = request.form.get ('registerPassword', default = 'error')

        userID = "15"
        userName = "Nikrad"
        userAccess = "User"
        volunteerID = "132"

        print (regEmail)
        print (regPass1)
        try:
            # request.form.get('')
            conn = sqlite3.connect(DATABASE)
            cur = conn.cursor()
            # cur.execute(("INSERT INTO accounts('email_addr','password') VALUES ('','');"),(regEmail, regPass1))
            # cur.execute("INSERT INTO 'accounts' ('email_addr','password') VALUES ('152', ?, '', ?, 'User','1512');"),(regEmail, regPass1)

            cur.execute(("INSERT INTO accounts('userID', 'email_addr', 'name', 'password', 'access', 'volunteerID') VALUES (?,?,?,?,?,?);"),(userID, regEmail, userName, regPass1, userAccess, volunteerID))


            conn.commit()
            msg ="Survey Data successfully recorded"
            conn.close()
        except:
            conn.rollback()
            msg ="Error in appending data "
        finally:
            return msg + regEmail
            conn.close()

















<form action="/register" method="get">
<div class="container">
<h1>Register</h1>
<p>Please enter your registration details in the form provided below.</p>
<div class="vertical-form"><hr>

<label for="email" name="email" id="email"><b>Email</b></label>
<input type="email"
class="form-control"
placeholder="Email" required>

<label for="psw" name="psw" id="psw"><b>Password</b></label>
<input type="password"
class="form-control" required id="passwordInput" pattern="(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}" title="Must contain at least one number and one uppercase and lowercase letter, and at least 8 or more characters"
placeholder="Password" required>

<label for="psw-repeat" name="pass2" id="pass2"><b>Repeat Password</b></label>
<input type="password"
class="form-control" required id="passwordInput" pattern="(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}" title="Must contain at least one number and one uppercase and lowercase letter, and at least 8 or more characters"
placeholder="Password" required>
<hr></div>
<p>By creating an account you agree to our <a href="#">Terms & Privacy</a>.</p>

<button
class="btn btn-default" class="register-button"><a href = "/register">Register new account</a>
</button>
</div>

<div class="container signin">
<p>Already have an account? <a href="#">Sign in</a>.</p>
</div>
</form>



























<main>


{%block title %}

<title> Cancer Patient Pathways - Contact </title>
<!-- <div class="sub_text"> <h2>Generic Questions Only</h2> </div> -->
{%endblock %}


{%block content%}
<form method = 'post' class = "admin_form">
<div class="container">
<h1>Register</h1>
<p>Please enter your registration details in the form provided below.</p>
<div class="vertical-form"><hr>

<label  for = "email_register"></label>
Email:  <input class="form-control" type = "email" name = "registerEmail"><br>
<input type="email"
   class="form-control"
   placeholder="Email" required>

<label for="psw" name="psw" id="psw"><b>Password</b></label>
<input type="password"
class="form-control" required id="passwordInput" pattern="(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}" title="Must contain at least one number and one uppercase and lowercase letter, and at least 8 or more characters"
placeholder="Password" required>

<label for="psw-repeat" name="pass2" id="pass2"><b>Repeat Password</b></label>
<input type="password"
   class="form-control" required id="passwordInput" pattern="(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}" title="Must contain at least one number and one uppercase and lowercase letter, and at least 8 or more characters"
   placeholder="Password" required>
<hr></div>
<p>By creating an account you agree to our <a href="#">Terms & Privacy</a>.</p>

<button
  class="btn btn-default" class="register-button"><a href = "/register">Register new account</a>
</button>
</div>

<div class="container signin">
<p>Already have an account? <a href="#">Sign in</a>.</p>
</div>
</form>


<form method = 'post' class = "admin_form">
<label  for = "email_register"></label>
Email:  <input class="form-control" type = "email" name = "registerEmail"><br>

<label  for = "password_register"></label>
Password:  <input class="form-control" type = "text" name = "registerPassword" required id="passwordInput" pattern="(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}" title="Must contain at least one number and one uppercase and lowercase letter, and at least 8 or more characters"
placeholder="Password"><br>
<label  for = "password_register"></label>
Password:  <input class="form-control" type = "text" name = "registerPassword2" required id="passwordInput" pattern="(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}" title="Must contain at least one number and one uppercase and lowercase letter, and at least 8 or more characters"
placeholder="Password"><br>
<button class = "admin_button" name = 'patient_search' type = "submit"> search </button>
</form>


</main>























@serv.route("/register", methods = ['POST', 'GET'])
def newUser():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        regEmail = request.form.get('registerEmail', default = 'error')
        regPass1 = request.form.get ('registerPassword', default = 'error')

        userName = "Nikrad"
        userAccess = "User"
        volunteerID = "132223"

        print (regEmail)
        print (regPass1)
        try:
            # request.form.get('')
            conn = sqlite3.connect(DATABASE)
            cur = conn.cursor()
            # cur.execute(("INSERT INTO accounts('email_addr','password') VALUES ('','');"),(regEmail, regPass1))
            # cur.execute("INSERT INTO 'accounts' ('email_addr','password') VALUES ('152', ?, '', ?, 'User','1512');"),(regEmail, regPass1)

            cur.execute(("INSERT INTO accounts('email_addr', 'name', 'password', 'access', 'volunteerID') VALUES (?,?,?,?,?);"),(regEmail, userName, regPass1, userAccess, volunteerID))


            conn.commit()
            msg ="Survey Data successfully recorded"
            conn.close()
        except:
            conn.rollback()
            msg ="Error in appending data "
        finally:
            return msg + regEmail
            conn.close()





@serv.route("/register", methods = ['POST', 'GET'])
def newUser():
    if request.method == 'GET':
        return render_template('register.html')

    elif request.method == 'POST':
        regName = request.form.get('registerName', default = 'error')
        regEmail = request.form.get('registerEmail', default = 'error')
        regPass1 = request.form.get ('registerPassword', default = 'error')
        regPass2 = request.form.get ('registerPassword2', default = 'error')
        if regPass1 == regPass2:
            userAccess = "User"
            volunteerID = "9925"

            print (regEmail)
            print (regPass1)
            try:
                conn = sqlite3.connect(DATABASE)
                cur = conn.cursor()
                cur.execute(("INSERT INTO accounts('email_addr', 'name', 'password', 'access', 'volunteerID') VALUES (?,?,?,?,?);"),(regEmail, regName, regPass1, userAccess, volunteerID))
                conn.commit()
                msg ="Survey Data successfully recorded"
                conn.close()
            except:
                conn.rollback()
                msg ="Error in appending data "
            finally:
                return msg + regEmail
                conn.close()
        else:
            return "didnt match"




























@serv.route("/register", methods = ['POST', 'GET'])
def newUser():
    if request.method == 'GET':
        return render_template('register.html')

    elif request.method == 'POST':
        regName = request.form.get('registerName', default = 'error')
        regEmail = request.form.get('registerEmail', default = 'error')
        regPass1 = request.form.get ('registerPassword', default = 'error')
        regPass2 = request.form.get ('registerPassword2', default = 'error')
        if regPass1 == regPass2:
            userAccess = "User"
            volunteerID = "9925"

            print (regEmail)
            print (regPass1)
            try:
                conn = sqlite3.connect(DATABASE)
                cur = conn.cursor()
                cur.execute(("INSERT INTO accounts('email_addr', 'name', 'password', 'access', 'volunteerID') VALUES (?,?,?,?,?);"),(regEmail, regName, regPass1, userAccess, volunteerID))
                conn.commit()
                msg ="Survey Data successfully recorded"
                conn.close()
            except:
                conn.rollback()
                msg ="Error in appending data "
            finally:
                return msg + regEmail
                conn.close()
        else:
            return "didnt match"
