from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Igra(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    naziv = db.Column(db.String(100), nullable=False)
    trener_id = db.Column(db.Integer, db.ForeignKey('trener.id'), nullable=False)

class Trener(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ime = db.Column(db.String(100), nullable=False)
    prezime = db.Column(db.String(100), nullable=False)
    igre = db.relationship('Igra', backref='trener', lazy=True)

class Igrac(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ime = db.Column(db.String(100), nullable=False)
    prezime = db.Column(db.String(100), nullable=False)
    korisnicko_ime = db.Column(db.String(100), nullable=False)
    igra_id = db.Column(db.Integer, db.ForeignKey('igra.id'), nullable=False)
    trener_id = db.Column(db.Integer, db.ForeignKey('trener.id'), nullable=False)
