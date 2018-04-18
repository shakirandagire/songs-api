from api import db

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(225))
    username = db.Column(db.String(225))
    password = db.Column(db.String(225))

    def __repr__(self):
        "Returns the representstion of the object"
        return "User: {}". format(self.username)

    def save(self):
        "Save method for the users"
        db.session.add(self)
        db.session.commit()
