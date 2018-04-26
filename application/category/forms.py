from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators

# Define the new category form
class CategoryForm(FlaskForm):
    name = StringField("Category name", [validators.Length(min=2)])

    class Meta:
        csrf = False