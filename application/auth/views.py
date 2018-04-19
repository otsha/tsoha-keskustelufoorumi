from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm, RegisterForm

# Handle the login page


@app.route("/auth/login", methods=["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form=LoginForm())

    form = LoginForm(request.form)

    user = User.query.filter_by(
        username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form=form, error="Incorrect username or password")

    # Return to the dashboard
    login_user(user)
    print("User " + user.username + " authenticated")
    return redirect(url_for("messages_index"))

# Handle the register page


@app.route("/auth/register", methods=["GET", "POST"])
def auth_register():
    if request.method == "GET":
        return render_template("auth/registerform.html", form=RegisterForm())

    form = RegisterForm(request.form)

    if not form.validate():
        return render_template("auth/registerform.html", form=form)

    # Check if username already in use
    user = User.query.filter_by(username=form.username.data).first()
    if user:
        return render_template("auth/registerform.html", form=form, error="Username already in use")

    # Add new account to database
    a = User(form.username.data, form.password.data)

    db.session().add(a)
    db.session().commit()

    # Return the login page
    return redirect(url_for("auth_login"))

# Handle logging out


@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))

# GET User page


@app.route("/users/<user_id>", methods=["GET"])
def view_user(user_id):
    u = User.query.get(user_id)
    return render_template("auth/user.html", user=u)

# POST Promote user to admin


@app.route("/users/<user_id>/promote", methods=["POST"])
@login_required
def promote_user(user_id):
    u = User.query.get(user_id)

    # Make sure that the current user is allowed to do this
    if not current_user.isSuper:
        return redirect(url_for("view_user", user_id=u.id))

    u.isSuper = True
    db.session().add(u)
    db.session().commit()

    return redirect(url_for("view_user", user_id=u.id))


# POST Demote user from admin
@app.route("/users/<user_id>/demote", methods=["POST"])
@login_required
def demote_user(user_id):
    u = User.query.get(user_id)

    u.isSuper = False
    db.session().add(u)
    db.session().commit()

    # Make sure that the current user is allowed to do this

    if not current_user.isSuper:
        return redirect(url_for("view_user", user_id=u.id))

    return redirect(url_for("view_user", user_id=u.id))
