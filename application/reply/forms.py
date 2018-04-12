from flask_wtf import FlaskForm
from wtforms import TextAreaField, validators

# Define the new message form
class ReplyForm(FlaskForm):
    content = TextAreaField("Reply content", [validators.Length(min=3)])

    class Meta:
        csrf = False