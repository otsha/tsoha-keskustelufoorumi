from flask import render_template
from application import app

# Rendering the index page
@app.route("/")
def index():
    return render_template("index.html")
    