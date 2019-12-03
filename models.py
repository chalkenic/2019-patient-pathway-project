import sqlite3 as sql

def insertUser(email_addr,password):
    con = sql.connect("survey_project.db")
    cur = con.cursor()
    cur.execute("INSERT INTO accounts (email_addr,password) VALUES (?,?)", (email_addr,password))
    con.commit()
    con.close()

def retrieveUsers():
	con = sql.connect("survey_project.db")
	cur = con.cursor()
	cur.execute("SELECT email_addr, password FROM accounts")
	users = cur.fetchall()
	con.close()
	return users
