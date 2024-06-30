from app import create_app, db
from app.models import Trener, Igra

def dodaj_igre_i_trenere():
    treneri = [
        Trener(ime='Neo', prezime='Čikić'),
        Trener(ime='Josip', prezime='Džinić'),
        Trener(ime='Lina', prezime='Bilić')
    ]

    igre = [
        Igra(naziv='Counter Strike 2', slika='game1.jpg', trener_id=1),
        Igra(naziv='League of Legends', slika='game2.jpg', trener_id=1),
        Igra(naziv='Apex Legends', slika='game3.jpg', trener_id=2),
        Igra(naziv='Valorant', slika='game4.jpg', trener_id=2),
        Igra(naziv='Tekken', slika='game5.jpg', trener_id=3),
        Igra(naziv='Overwatch 2', slika='game6.jpg', trener_id=3)
    ]

    db.session.bulk_save_objects(treneri)
    db.session.bulk_save_objects(igre)
    db.session.commit()

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        db.create_all()
        dodaj_igre_i_trenere()
