# /mnt/data/services.py
from .models import db, Igra, Trener, Igrac

def save_player(ime, prezime, korisnicko_ime, igra_id, trener_id):
    if not ime or not prezime or not korisnicko_ime or not igra_id or not trener_id:
        return {'message': 'Svi podaci moraju biti pruženi.'}, 400

    novi_igrac = Igrac(
        ime=ime,
        prezime=prezime,
        korisnicko_ime=korisnicko_ime,
        igra_id=igra_id,
        trener_id=trener_id
    )

    try:
        db.session.add(novi_igrac)
        db.session.commit()
        return {'message': 'Uspješno ste se registrirali za igru.'}, 201
    except Exception as e:
        db.session.rollback()
        return {'message': 'Došlo je do greške prilikom spremanja u bazu podataka.', 'error': str(e)}, 500
