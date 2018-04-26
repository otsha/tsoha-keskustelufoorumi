from application import db
from application.models import Base

# Define the database model for a category
class Category(Base):
    
    name = db.Column(db.String(140), nullable = False)

    def __init__(self, name):
        self.name = name
