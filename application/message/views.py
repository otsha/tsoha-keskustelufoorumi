from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db
from application.message.models import Message
from application.message.forms import MessageForm, MessageEditForm
from application.auth.models import User
from application.reply.models import Reply
from application.reply.forms import ReplyForm, ReplyEditForm
from application.readmessage.models import ReadMessage
from application.category.models import Category

from sqlalchemy import desc, asc

# GET the dashboard page / POST update sorting
@app.route("/messages/", methods=["GET", "POST"])
def messages_index():

    # Which way are the messages sorted?
    if request.method == "POST":
        if request.form.get("selected_sorting") == "age_asc":
            return render_template("messages/list.html", messages = Message.query.order_by(asc(Message.date_created)).all())
        elif request.form.get("selected_sorting") == "title_desc":
            return render_template("messages/list.html", messages = Message.query.order_by(desc(Message.name)).all())
        elif request.form.get("selected_sorting") == "title_asc":
            return render_template("messages/list.html", messages = Message.query.order_by(asc(Message.name)).all())
        else:
            return render_template("messages/list.html", messages = Message.query.order_by(desc(Message.date_created)).all())

    # Return the default order (newest first)
    return render_template("messages/list.html", messages = Message.query.order_by(desc(Message.date_created)).all())

# HANDLE creating new messages
@app.route("/messages/new/", methods=["GET", "POST"])
@login_required
def messages_form():
    if request.method == "GET":
        return render_template("messages/new.html", form = MessageForm(), categories = Category.query.all())
    
    form = MessageForm(request.form)

    # Validate the form
    if not form.validate():
        return render_template("messages/new.html", form = form, categories = Category.query.all())

    # Check if the dropdown menu selection is valid
    if request.form.get('category_select') == 'null':
        return render_template("messages/new.html", form = form, categories = Category.query.all(), error = "Please select a category")

    # Create a message object and add it to the database
    m = Message(form.name.data)
    m.content = form.content.data
    m.account_id = current_user.id
    m.category_id = request.form.get('category_select')

    db.session().add(m)
    db.session().commit()

    return redirect(url_for("messages_index"))

# POST set message to read
@app.route("/messages/<message_id>/read/", methods = ["POST"])
@login_required
def messages_set_read(message_id):
    m = Message.query.get(message_id)
    u = current_user
    
    # Check if user has already marked the thread as 'read'
    if ReadMessage.hasUserReadMessage(u.id, m.id) == False:
        rm = ReadMessage(u.id, m.id)

        db.session().add(rm)
        db.session().commit()

    return redirect(url_for("message_view", message_id = m.id))

# GET message page (a specific post)
@app.route("/messages/<message_id>/")
def message_view(message_id):
    m = Message.query.get(message_id)
    u = User.query.get(m.account_id)
    c = Category.query.get(m.category_id)

    # Get a list of the users who have read this message
    readers = ReadMessage.findAllUsersWhoRead(m.id)

    return render_template("messages/message.html", message = m, user = u, category = c, readers = readers, replies = m.findAllReplies(m.id))

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
    
    # Delete all the replies to this post
    m.deleteAllReplies(m.id)
    m.deleteReadMessage(m.id)

    # Delete the message from the database
    db.session().delete(m)
    db.session().commit()

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

# POST Search from messages
@app.route("/search", methods = ["POST"])
def messages_search():
    term = request.form.get("search")

    # If the search terms are empty, show the Dashboard
    if term == "":
        return redirect(url_for("messages_index"))

    return redirect(url_for("messages_search_results", search_term = term))

# GET search results
@app.route("/search/results/<search_term>", methods = ["GET", "POST"])
def messages_search_results(search_term):

    # Which way are the messages sorted?
    if request.method == "POST":
        if request.form.get("selected_sorting") == "age_asc":
            messages = Message.query.filter(Message.name.like('%'+search_term+'%')).order_by(asc(Message.date_created)).all()
            return render_template("messages/search.html", messages = messages, search_term = search_term)
        elif request.form.get("selected_sorting") == "title_desc":
            messages = Message.query.filter(Message.name.like('%'+search_term+'%')).order_by(desc(Message.name)).all()
            return render_template("messages/search.html", messages = messages, search_term = search_term)
        elif request.form.get("selected_sorting") == "title_asc":
            messages = Message.query.filter(Message.name.like('%'+search_term+'%')).order_by(asc(Message.name)).all()
            return render_template("messages/search.html", messages = messages, search_term = search_term)
        else:
            messages = Message.query.filter(Message.name.like('%'+search_term+'%')).order_by(desc(Message.date_created)).all()
            return render_template("messages/search.html", messages = messages, search_term = search_term)

    # If GET, return the default order (newest first)
    messages = Message.query.filter(Message.name.like('%'+search_term+'%')).order_by(desc(Message.date_created)).all()
    return render_template("messages/search.html", messages = messages, search_term = search_term)

# GET new reply page
@app.route("/messages/<message_id>/reply", methods = ["GET"])
@login_required
def message_new_reply(message_id):
    m = Message.query.get(message_id)

    # Get the original poster of the message
    op = User.query.get(m.account_id)  

    return render_template("reply/new.html", message = m, user = op, form = ReplyForm())

# POST new reply
@app.route("/messages/<message_id>/reply", methods = ["POST"])
@login_required
def message_post_reply(message_id):
    form = ReplyForm(request.form)
    m = Message.query.get(message_id)

    if not form.validate():
        return url_for("message_new_reply", message_id = m.id)
    
    # Create a new reply object and add it to the database
    r = Reply(form.content.data)
    r.content = form.content.data
    r.account_id = current_user.id
    r.message_id = m.id

    db.session().add(r)
    db.session().commit()

    return redirect(url_for("message_view", message_id = m.id))

# POST delete a reply
@app.route("/messages/<message_id>/replies/<reply_id>/delete", methods = ["POST"])
@login_required
def reply_delete(message_id, reply_id):
    r = Reply.query.get(reply_id)

    # Check if the user is a Super or the original poster (this is already checked in the html, but JUST IN CASE)
    if r.account_id != current_user.id:
        if current_user.isSuper == False:
            return redirect(url_for("message_view", message_id=message_id))
        else:
            pass
    
    # Delete the message from the database
    db.session().delete(r)
    db.session().commit()

    return redirect(url_for("message_view", message_id=message_id))

# HANDLE editing a reply
@app.route("/messages/<message_id>/replies/<reply_id>/edit/", methods = ["GET", "POST"])
@login_required
def reply_edit(message_id, reply_id):
    m = Message.query.get(message_id)
    r = Reply.query.get(reply_id)
    form = ReplyEditForm(request.form)

    # Check if the user is a Super or the original poster (this is already checked in the html, but JUST IN CASE)
    if m.account_id != current_user.id:
        if current_user.isSuper == False:
            return redirect(url_for("message_view", message_id=m.id))
        else:
            pass

    # Return the edit view
    if request.method == "GET":
        return render_template("reply/edit.html", message = m, reply = r, form = form)

    # Update the database
    if not form.validate():
        return render_template("reply/edit.html", message = m, reply = r, form = form)

    # Update the title and contents of the message to the database
    r.content = form.content.data

    db.session().add(r)
    db.session().commit()

    return redirect(url_for("message_view", message_id=m.id))