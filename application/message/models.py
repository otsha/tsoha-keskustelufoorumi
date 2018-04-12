from application import db
from application.models import Base

# Define the database model for a message
class Message(Base):
    
    name = db.Column(db.String(140), nullable = False)
    content = db.Column(db.String(1000), nullable = False)
    read = db.Column(db.Boolean, nullable = False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable = False)

    def __init__(self, name):
        self.name = name
        self.content = ""
        self.read = False