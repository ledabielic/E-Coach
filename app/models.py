from app import db

class Trener(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ime = db.Column(db.String(50), nullable=False)
    prezime = db.Column(db.String(50), nullable=False)

class Igra(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    naziv = db.Column(db.String(50), nullable=False)
    slika = db.Column(db.String(50), nullable=False)
    trener_id = db.Column(db.Integer, db.ForeignKey('trener.id'), nullable=False)
    trener = db.relationship('Trener', backref=db.backref('igre', lazy=True))
