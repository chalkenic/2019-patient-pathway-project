import os
from flask import Flask, redirect, request,render_template, jsonify
import sys

# sys.path.append(os.path.join(os.path.dirname(__file__), '..'))




serv = Flask(__name__)

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'css'])

@serv.route("/test", methods = ['GET'])
def main_header():
    if request.method == 'GET':

        # os.chdir('..')
        return render_template('01_homepage.html')

if __name__ == "__main__":
    serv.run(debug=True)
