from flask import Blueprint, jsonify, request
from .models import db, Igra, Igrac, Trener
from .services import save_player

main = Blueprint('main', __name__)

@main.route('/igre', methods=['GET'])
def get_igre():
    igre = Igra.query.all()
    return jsonify([{'id': igra.id, 'naziv': igra.naziv} for igra in igre])

@main.route('/registracija', methods=['POST'])
def registracija():
    try:
        data = request.json
        ime = data['ime']
        prezime = data['prezime']
        korisnicko_ime = data['korisnickoIme']
        igra_id = data['igraId']
        trener_id = data['trenerId']

        save_player(ime, prezime, korisnicko_ime, igra_id, trener_id)

        return jsonify({'message': 'Uspješno ste se registrirali za igru.'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400
