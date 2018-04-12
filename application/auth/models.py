from application import db
from application.models import Base

# Define User/account model for SQLAlchemy
class User(Base):
    
    __tablename__ = "account"

    username = db.Column(db.String(30), nullable = False)
    password = db.Column(db.String(144), nullable = False)
    isSuper = db.Column(db.Boolean, nullable = False)

    tasks = db.relationship("Message", backref = 'account', lazy = True)

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.isSuper = False

    def get_id(self):
        return self.id

    def is_active(self):
        return True
    
    def is_anonyous(self):
        return False
    
    def is_authenticated(self):
        return True
    
