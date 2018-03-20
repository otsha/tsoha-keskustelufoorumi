from application import app, db
from flask import render_template, request, redirect, url_for
from application.database.models import Message

# GET messages page
@app.route("/messages/", methods=["GET"])
def messages_index():
    return render_template("messages/list.html", messages = Message.query.all())

# GET new message page
@app.route("/messages/new/", methods=["GET"])
def messages_form():
    return render_template("messages/new.html")

# POST set message to read
@app.route("/messages/<message_id>/read/", methods = ["POST"])
def messages_set_read(message_id):
    m = Message.query.get(message_id)

    m.read = True
    db.session().commit()

    return redirect(url_for("messages_index"))

# POST create new message
@app.route("/messages/", methods = ["POST"])
def messages_create():
    m = Message(request.form.get("content"))

    db.session().add(m)
    db.session().commit()

    return redirect(url_for("messages_index"))

