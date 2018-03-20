from application import db

class Message(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    date_created = db.Column(db.DateTime, default = db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default = db.func.current_timestamp())
    onupdate = db.func.current_timestamp()

    content = db.Column(db.String(140), nullable = False)
    read = db.Column(db.Boolean, nullable = False)

    def __init__(self, content):
        self.content = content
        self.read = False