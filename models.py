from flask_sqlalchemy import SQLAlchemy


# Set up db connection
db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)


"""Models for Cupcake app."""
class Cupcake(db.Model):
    """Cupcake Model"""

    # Table setup
    __tablename__ = "cupcakes"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    flavor = db.Column(db.String, nullable=False)
    size = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    image = db.Column(db.String, nullable=True, default='https://tinyurl.com/demo-cupcake')
    # End table setup

    # Instance methods
    def serialize(self):
        return {
            'id': self.id,
            'flavor': self.flavor,
            'size': self.size,
            'rating': self.rating,
            'image': self.image
        }

    def __repr__(self):
        return f"id = {self.id}, flavor = {self.flavor}, size = {self.size}"
