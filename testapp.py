import pyrebase

config={'apiKey': "AIzaSyCXBR_0_UQhRsq9_Z75rKY9Z8gO7f-FYh0",
  'authDomain': "test-fcfc1.firebaseapp.com",
  'databaseURL': "",
  'projectId': "test-fcfc1",
  'storageBucket': "test-fcfc1.appspot.com",
  'messagingSenderId': "475633284013",
  'appId': "1:475633284013:web:412f26593b6b38ceffe724"}

firebase = pyrebase.initialize_app(config)
auth=firebase.auth()
storage=firebase.storage()

def sign_in():
    email=input("enter your email: ")
    password=input("enter your password: ")

    auth.sign_in_with_email_and_password(email,password)
    print(db.collection(peulot).where('ownerId', '=', auth.current_user['localId']).get())
    print("signed in")

    
    
def sign_up():
    email=input("enter your email: ")
    password=input("enter your password: ")
    confirmpass=input("confirm your password: ")
    if password==confirmpass:
        try:
            auth.create_user_with_email_and_password(email, password)
            print("signed up succesfully!")
        except:
            print("user already exists")
    else:
        print("passwords don't match!")
        
        
sign_in()