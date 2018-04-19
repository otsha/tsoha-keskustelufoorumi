from flask_wtf import FlaskForm
from wtforms import TextAreaField, validators

# Define the new reply form
class ReplyForm(FlaskForm):
    content = TextAreaField("Reply content", [validators.Length(min=3)])

    class Meta:
        csrf = False

# Define the reply editing form
class ReplyEditForm(FlaskForm):
    content = TextAreaField("Reply content", [validators.Length(min=3)])

    class Meta:
        csrf = False