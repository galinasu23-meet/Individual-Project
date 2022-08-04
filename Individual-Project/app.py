from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

config = {

    "apiKey": "AIzaSyDcgqV0-59KrI5kZ4yL30t73FVfTeXnZ1w",

    "authDomain": "galicake-45eee.firebaseapp.com",

    "projectId": "galicake-45eee",

    "storageBucket": "galicake-45eee.appspot.com",

    "messagingSenderId": "1096490776579",

    "appId": "1:1096490776579:web:8f608908c5c0a1a1f8f636",

    "measurementId": "G-L75SJLBRGF",

    "databaseURL": "https://galicake-45eee-default-rtdb.europe-west1.firebasedatabase.app/"

}




firebase= pyrebase.initialize_app(config)
auth = firebase.auth()
db= firebase.database()

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'

#Code goes below here


# cakes ={'dinoCake':[}

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/home')
def home1():
    return render_template("home.html")

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = auth.sign_in_with_email_and_password(email, password)
            return redirect(url_for("home1"))
        except:
            error = "fail"
    return render_template("signin.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        try:
            login_session['user'] = auth.create_user_with_email_and_password(email, password)
            user = {"email":email, "password": password}
            db.child("Users").child(login_session['user']['localId']).set(user)
            return redirect (url_for("home1"))
        except:
            error = "Authentication failed"
    return render_template("signup.html")

@app.route('/cakes')
def cakes():
    return render_template("cakes.html")


@app.route('/csd.cakes')
def cakes2():
    return render_template("coursed_cakes.html")




# gali_says = "shutup" to Tom







#Code goes above here

if __name__ == '__main__':
    app.run(debug=True)