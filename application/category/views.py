from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db
from application.category.models import Category
from application.category.forms import CategoryForm
from application.message.models import Message
from application.readmessage.models import ReadMessage

from sqlalchemy import desc, asc

# GET the category listing page
@app.route("/categories/", methods=["GET"])
def categories_index():
    return render_template("categories/list.html", categories = Category.query.order_by('name').all())

# GET new category page
@app.route("/categories/new", methods=["GET", "POST"])
@login_required
def new_category():
    if request.method == "GET":
        # Check if the current user is a super user
        if current_user.isSuper == True:
            return render_template("categories/new.html", form = CategoryForm())
        else:
            return redirect(url_for("categories_index"))
    
    # Validate the name data of the form
    form = CategoryForm(request.form)
    if not form.validate():
        return render_template("categories/new.html", form = CategoryForm())

    # Check if a category with an identical name already exists in the database
    category = Category.query.filter_by(name=form.name.data).first()
    if category:
        return render_template("categories/new.html", form = CategoryForm(), error = "Category already exists!")

    # Add the category to the database
    c = Category(form.name.data)
    db.session().add(c)
    db.session().commit()

    return redirect(url_for("categories_index"))

# POST delete category
@app.route("/categories/<category_id>/delete", methods=["POST"])
@login_required
def delete_category(category_id):
    # Check if the current user is a super user
    if (current_user.isSuper == False):
        return redirect(url_for("categories_index"))
    
    # Delete the category from the database
    Category.deleteAllMessages(category_id)
    c = Category.query.get(category_id)
    db.session().delete(c)
    db.session().commit()

    return redirect(url_for("categories_index"))

# GET the message listing for a specific category
@app.route("/categories/<category_id>/", methods=["GET", "POST"])
def view_category(category_id):
    c = Category.query.get(category_id)

    # Which way are the messages sorted?
    if request.method == "POST":
        messages = []

        # Get all messages based on the sorting method
        if request.form.get("selected_sorting") == "age_asc":
            messages = Message.query.filter_by(category_id = c.id).order_by(asc(Message.date_created)).all()
        elif request.form.get("selected_sorting") == "title_desc":
            messages = Message.query.filter_by(category_id = c.id).order_by(desc(Message.name)).all()
        elif request.form.get("selected_sorting") == "title_asc":
            messages = Message.query.filter_by(category_id = c.id).order_by(asc(Message.name)).all()
        else:
            messages = Message.query.filter_by(category_id = c.id).order_by(desc(Message.date_created)).all()
        
        # Limit the message listing based on the selected limiting method
        if request.form.get("selected_limiting") == "limit_20":
            messages = messages[0:20]
        elif request.form.get("selected_limiting") == "limit_50":
            messages = messages[0:50]
        elif request.form.get("selected_limiting") == "limit_none":
            pass
        else:
            messages = messages[0:10]

        # Finally return the listing as requested to be sorted and limited by the user
        return render_template("categories/category.html", category = c, messages = messages)

    # Return the default listing (newest first, limited to 10)
    return render_template("categories/category.html", category = c, messages = Message.query.filter_by(category_id = c.id).order_by(desc(Message.date_created)).all()[0:10])
