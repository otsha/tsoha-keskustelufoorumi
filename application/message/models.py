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
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable = False)

    def __init__(self, name):
        self.name = name
        self.content = ""
        self.read = False

    # Find all replies to a message
    @staticmethod
    def findAllReplies(message_id):
        stmt = text("SELECT Reply.id, Reply.account_id from Reply"
                        " WHERE Reply.message_id = :message_id"
                        " ORDER BY Reply.date_created").params(message_id = message_id)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            r = Reply.query.get(row[0])
            u = User.query.get(row[1])
            response.append({"reply":r, "user":u})

        return response

    # Delete all replies to a message (this is executed when a thread is deleted)
    @staticmethod
    def deleteAllReplies(message_id):
        stmt = text("DELETE FROM Reply"
                        " WHERE Reply.message_id = :message_id").params(message_id = message_id)
        db.engine.execute(stmt)

    # Delete all ReadMessage data for the specified message (this is executed when a thread is deleted)
    @staticmethod
    def deleteReadMessage(message_id):
        stmt = text("DELETE FROM read_message"
                        " WHERE read_message.message_id = :message_id").params(message_id = message_id)
        
        db.engine.execute(stmt)

    # Find all messages (threads) posted by an user
    @staticmethod
    def findAllThreadsPostedBy(user_id):
        stmt = text("SELECT Message.id from Message"
                        " WHERE Message.account_id = :user_id"
                        " ORDER BY Message.date_created").params(user_id = user_id)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            m = Message.query.get(row[0])
            response.append(m)
        
        return response