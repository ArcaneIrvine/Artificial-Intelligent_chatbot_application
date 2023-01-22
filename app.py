import os
from flask import Flask, render_template, request, url_for, flash
from ChatBot import chat

# application
app = Flask(__name__)
app.secret_key = os.urandom(12).hex()


@app.route("/", methods=["POST", "GET"])
def welcome():
    return render_template("signup.html")


@app.route("/signup", methods=["POST", "GET"])
def signup():
    if request.method == "POST":
        usrn = request.form["username"]
        psw1 = request.form["password1"]
        psw2 = request.form["password2"]

        # check if passwords match
        if psw1 != psw2:
            flash('Passwords do not match', category='error')
        elif len(psw1) < 4:
            flash('Password must be at least 4 characters', category='error')
        elif len(usrn) < 2:
            flash('username must be more than 2 characters', category='error')
        else:
            flash('signed up successfully!', category='success')
            # add user to database
            pass

        return render_template("signup.html")
    else:
        return render_template("signup.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        usrn = request.form["username"]
        psw = request.form["password"]
        return render_template("chat.html")
    else:
        return render_template("login.html")


@app.route("/chat")
def chat():
    return render_template("chat.html")


if __name__ == "__main__":
    app.run()