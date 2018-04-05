from application import db

class Message(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    date_created = db.Column(db.DateTime, default = db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default = db.func.current_timestamp(), onupdate = db.func.current_timestamp())

    name = db.Column(db.String(140), nullable = False)
    content = db.Column(db.String(1000), nullable = False)
    read = db.Column(db.Boolean, nullable = False)

    def __init__(self, name):
        self.name = name
        self.content = ""
        self.read = False