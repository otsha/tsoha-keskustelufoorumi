from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db
from application.database.models import Message
from application.database.forms import MessageForm, MessageEditForm
from application.auth.models import User

# GET all messages (dashboard) page
@app.route("/messages/", methods=["GET"])
def messages_index():
    return render_template("messages/list.html", messages = Message.query.all())

# GET new message page
@app.route("/messages/new/", methods=["GET"])
@login_required
def messages_form():
    return render_template("messages/new.html", form = MessageForm())

# POST set message to read
@app.route("/messages/<message_id>/read/", methods = ["POST"])
@login_required
def messages_set_read(message_id):
    m = Message.query.get(message_id)

    m.read = True
    db.session().commit()

    return redirect(url_for("messages_index"))

# POST create new message
@app.route("/messages/", methods = ["POST"])
@login_required
def messages_create():
    form = MessageForm(request.form)

    if not form.validate():
        return render_template("messages/new.html", form = form)

    # Create a message object and add it to the database
    m = Message(form.name.data)
    m.content = form.content.data
    m.account_id = current_user.id

    db.session().add(m)
    db.session().commit()

    return redirect(url_for("messages_index"))

# GET message page (a specific post)
@app.route("/messages/<message_id>/")
def message_view(message_id):
    m = Message.query.get(message_id)
    u = User.query.get(m.account_id)

    return render_template("messages/message.html", message = m, user = u)

# POST delete message
@app.route("/messages/<message_id>/delete/", methods = ["POST"])
@login_required
def message_delete(message_id):
    m = Message.query.get(message_id)

    # Check if the user is a Super or the original poster (this is already checked in the html, but JUST IN CASE)
    if m.account_id != current_user.id:
        if current_user.isSuper == False:
            return redirect(url_for("message_view", message_id=m.id))
        else:
            pass
    
    # Delete the message from the database
    db.session().delete(m)
    db.session().commit()

    # < Deleting all the replies to this message goes here at a later date >

    return redirect(url_for("messages_index"))

# HANDLE message editing
@app.route("/messages/<message_id>/edit/", methods = ["GET", "POST"])
@login_required
def message_edit(message_id):
    m = Message.query.get(message_id)
    form = MessageEditForm(request.form)

    # Check if the user is a Super or the original poster (this is already checked in the html, but JUST IN CASE)
    if m.account_id != current_user.id:
        if current_user.isSuper == False:
            return redirect(url_for("message_view", message_id=m.id))
        else:
            pass

    # Return the edit view
    if request.method == "GET":
        return render_template("messages/edit.html", message = m, form = form)

    # Update the database
    if not form.validate():
        return render_template("messages/edit.html", form = form)

    # Update the title and contents of the message to the database
    m.name = form.name.data
    m.content = form.content.data

    db.session().add(m)
    db.session().commit()

    return redirect(url_for("message_view", message_id=m.id))