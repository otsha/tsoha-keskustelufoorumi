from application import db
from application.models import Base
from application.message.models import Message

from sqlalchemy import text

# Define the database model for a category
class Category(Base):
    
    name = db.Column(db.String(140), nullable = False)

    def __init__(self, name):
        self.name = name

    @staticmethod
    def deleteAllMessages(category_id):
        messages = Message.query.filter_by(category_id=category_id).all()
        for message in messages:
            Message.deleteReadMessage(message.id)
            Message.deleteAllReplies(message.id)

        stmt = text("DELETE FROM Message"
                        " WHERE Message.category_id = :category_id").params(category_id = category_id)
        db.engine.execute(stmt)
        db.engine.execute(stmt)
