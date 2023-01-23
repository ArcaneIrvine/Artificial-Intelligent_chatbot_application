from website import db
from website.models import User
from flask import Blueprint
from flask import render_template, request, url_for, flash, redirect
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)


@auth.route("/signup", methods=["POST", "GET"])
def signup():
    if request.method == "POST":
        usrn = request.form["username"]
        psw1 = request.form["password1"]
        psw2 = request.form["password2"]

        # check if passwords match, if not flash message
        if psw1 != psw2:
            flash('Passwords do not match', category='error')
        elif len(psw1) < 4:
            flash('Password must be at least 4 characters', category='error')
        elif len(usrn) < 2:
            flash('username must be more than 2 characters', category='error')
        # otherwise add user to the database
        else:
            # store password with a hash for security reasons
            new_user = User(username=usrn, password=generate_password_hash(psw1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('signed up successfully!', category='success')
            return render_template("chat.html")
    return render_template("signup.html")


@auth.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        usrn = request.form["username"]
        psw = request.form["password"]
        return render_template("chat.html")
    else:
        return render_template("login.html")