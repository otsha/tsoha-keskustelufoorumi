from application import db
from application.models import Base
from application.auth.models import User
from application.reply.models import Reply
from sqlalchemy.sql import text

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

    @staticmethod
    def findAllReplies(message_id):
        stmt = text("SELECT Reply.id, Reply.account_id from Reply"
                        " WHERE Reply.message_id = :message_id").params(message_id = message_id)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            r = Reply.query.get(row[0])
            u = User.query.get(row[1])
            response.append({"reply":r, "user":u})

        return response