from application import db
from application.models import Base

class Reply(Base):
    
    content = db.Column(db.String(1000), nullable = False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable = False)
    message_id = db.Column(db.Integer, db.ForeignKey('message.id'), nullable = False)

    def __init__(self, content):
        self.content = ""
