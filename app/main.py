from flask import Blueprint, jsonify, request
import os

main = Blueprint('main', __name__)

@main.route('/registracija', methods=['POST'])
def registracija():
    data = request.json
    ime = data['ime']
    prezime = data['prezime']
    korisnicko_ime = data['korisnicko_ime']
    igra = data['igra']
    trener = data['trener']

    # Spremanje podataka u tekstualni fajl
    try:
        file_path = os.path.join(os.getcwd(), 'registracije.txt')
        with open(file_path, 'a') as f:
            f.write(f"Ime: {ime}, Prezime: {prezime}, Korisnicko ime: {korisnicko_ime}, Igra: {igra}, Trener: {trener}\n")
        return jsonify({'message': 'Uspješno ste se registrirali za igru.'}), 201
    except Exception as e:
        return jsonify({'message': 'Došlo je do greške prilikom spremanja u tekstualni fajl.', 'error': str(e)}), 500
