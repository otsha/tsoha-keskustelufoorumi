from application import db
from application.models import Base
from application.auth.models import User
from application.message.models import Message
from sqlalchemy.sql import text

# Define the database model for a message
class ReadMessage(Base):

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable = False)
    message_id = db.Column(db.Integer, db.ForeignKey('message.id'), nullable = False)

    def __init__(self, account_id, message_id):
        self.account_id = account_id
        self.message_id = message_id

    @staticmethod
    def findAllUsersWhoRead(message_id):
        stmt = text("SELECT account_id FROM read_message"
                        " WHERE read_message.message_id = :message_id").params(message_id = message_id)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            u = User.query.get(row[0])
            response.append({"user":u})

        return response

    @staticmethod
    def hasUserReadMessage(user_id, message_id):
        stmt = text("SELECT DISTINCT account_id FROM read_message"
                        " WHERE read_message.message_id = :message_id"
                        " AND read_message.account_id = :user_id").params(message_id = message_id, user_id = user_id)
        res = db.engine.execute(stmt)

        response = []

        for row in res:
            response.append(1)

        if not response.__contains__(1):
            return False
        else:
            return True