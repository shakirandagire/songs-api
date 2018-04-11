from api import db

class Songs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(225))
    artist = db.Column(db.String(225))

    def __repr__(self):
        "Returns the representstion of the object"
        return "Songs: {}". format(self.title)

    def save(self):
        "Save method for the songs"
        db.session.add(self)
        db.session.commit()

    def delete(self):
        "Delete method for the songs"
        db.session.delete(self)
        db.session.commit()



