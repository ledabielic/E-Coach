from .models import db, Igrac

def save_player(ime, prezime, korisnicko_ime, igra_id, trener_id):
    novi_igrac = Igrac(ime=ime, prezime=prezime, korisnicko_ime=korisnicko_ime, igra_id=igra_id, trener_id=trener_id)
    db.session.add(novi_igrac)
    db.session.commit()
