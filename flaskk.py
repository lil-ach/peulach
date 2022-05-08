import pyrebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from flask import Flask, render_template, request
app = Flask(__name__)

config={'apiKey': "AIzaSyCXBR_0_UQhRsq9_Z75rKY9Z8gO7f-FYh0",
  'authDomain': "test-fcfc1.firebaseapp.com",
  'databaseURL': "",
  'projectId': "test-fcfc1",
  'storageBucket': "test-fcfc1.appspot.com",
  'messagingSenderId': "475633284013",
  'appId': "1:475633284013:web:412f26593b6b38ceffe724"}
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
firebase = pyrebase.initialize_app(config)
auth=firebase.auth()
db = firestore.client()
def sign_in_form(email, password):
    try:
        auth.sign_in_with_email_and_password(email,password)
        return auth.current_user['localId']
    except:
        return "invalid email or password"

def sign_up_form(email, password, confirmpass):
    if password==confirmpass:
        try:
            auth.create_user_with_email_and_password(email, password)
            return "signed up succesfully!"
        except:
            return "invalid email"
    else:
        return "passwords don't match!"
        
        
@app.route('/handle_data', methods=['POST'])
def handle_data():
    email = request.form['email']
    password = request.form['password']
    return sign_in_form(email, password)
    
@app.route('/handle_newacc_data', methods=['POST'])
def handle_newacc_data():
    email = request.form['email']
    password = request.form['password']
    confpass = request.form['confpass']

    return sign_up_form(email, password, confpass)
    
@app.route('/sign_in')
def sign_in():
    return render_template("sign_in.html")
    
@app.route('/sign_up')
def sign_up():
    return render_template("sign_up.html")
    
@app.route('/')
def index():
    return render_template("index.html")

if __name__ == '__main__':
   app.run()