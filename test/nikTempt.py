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
