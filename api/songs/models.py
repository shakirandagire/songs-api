from api import db
from sqlalchemy.orm import relationship

class Songs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(225))
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'))
    
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
    
    def update(self):
        db.session.commit()

class Artist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(225))
    songs = db.relationship('Songs', backref='artist', lazy=True)
    
    def __repr__(self):
        "Returns the representstion of the object"
        return "Artist: {}". format(self.name)

    def save(self):
        "Save method for the songs"
        db.session.add(self)
        db.session.commit()

    def delete(self):
        "Delete method for the songs"
        db.session.delete(self)
        db.session.commit()


