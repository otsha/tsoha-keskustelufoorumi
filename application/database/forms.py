from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators

# Define the new message form
class MessageForm(FlaskForm):
    name = StringField("Post title", [validators.Length(min=2)])
    content = TextAreaField("Post content", [validators.Length(min=3)])

    class Meta:
        csrf = False