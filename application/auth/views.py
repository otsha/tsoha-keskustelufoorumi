from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm, RegisterForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)

    user = User.query.filter_by(username = form.username.data, password = form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form, error = "Incorrect username or password")
    
    login_user(user)
    print("User" + user.username + " authenticated")
    return redirect(url_for("index"))

@app.route("/auth/register", methods = ["GET", "POST"])
def auth_register():
    if request.method == "GET":
        return render_template("auth/registerform.html", form = RegisterForm())
    
    form = RegisterForm(request.form)

    if not form.validate():
        return render_template("auth/registerform.html", form = form)

    # Check if username already in use
    user = User.query.filter_by(username = form.username.data).first()
    if user:
        return render_template("auth/registerform.html", form = form, error = "Username already in use")

    # Add new account to database
    a = User(form.username.data, form.password.data)
    
    db.session().add(a)
    db.session().commit()

    return redirect(url_for("auth_login"))

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))