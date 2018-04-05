from application import db

class User(db.Model):
    
    __tablename__ = "account"

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

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
    
