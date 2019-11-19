import os
from flask import Flask, redirect, request,render_template, jsonify
import sys

# sys.path.append(os.path.join(os.path.dirname(__file__), '..'))




serv = Flask(__name__)

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'css'])

@serv.route("/home", methods = ['POST','GET'])
def frontPage():
    if request.method == 'GET':

        return render_template('01_homepage.html')
    if request.method == 'POST':
        return None

@serv.route("/contact", methods = ['GET'])
def contactUs():
    if request.method == 'GET':

        return render_template('02-contact_us.html')

@serv.route("/survey", methods = ['GET'])
def survey():
    if request.method == 'GET':

        return render_template('03-survey.html')




if __name__ == "__main__":
    serv.run(debug=True)
