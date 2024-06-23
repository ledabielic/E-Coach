from app import create_app
from app.models import db, Igra, Trener

def dodaj_igre_i_trenere():
    igre = [
        Igra(naziv='Counter Strike 2', trener_id=1),
        Igra(naziv='League of Legends', trener_id=2),
        Igra(naziv='Apex Legends', trener_id=3),
        Igra(naziv='Valorant', trener_id=1),
        Igra(naziv='Tekken', trener_id=2),
        Igra(naziv='Overwatch 2', trener_id=3),
    ]

    treneri = [
        Trener(ime='Neo', prezime='Čikić'),
        Trener(ime='Josip', prezime='Džinić'),
        Trener(ime='Luka', prezime='Brkić'),
    ]

    db.session.bulk_save_objects(treneri)
    db.session.bulk_save_objects(igre)
    db.session.commit()

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        db.create_all()
        dodaj_igre_i_trenere()
