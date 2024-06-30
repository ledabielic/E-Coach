from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import db, Igra, Trener

main_html = Blueprint('main_html', __name__)

@main_html.route('/')
def index():
    return render_template('index.html')

@main_html.route('/games')
def games():
    igre = Igra.query.all()
    treneri = Trener.query.all()
    return render_template('games.html', igre=igre, treneri=treneri)

@main_html.route('/create_game', methods=['GET', 'POST'])
def create_game():
    if request.method == 'POST':
        naziv = request.form['naziv']
        slika = request.form['slika']
        trener_id = request.form['trener_id']
        nova_igra = Igra(naziv=naziv, slika=slika, trener_id=trener_id)
        db.session.add(nova_igra)
        db.session.commit()
        return redirect(url_for('main_html.games'))
    treneri = Trener.query.all()
    return render_template('create_game.html', treneri=treneri)

@main_html.route('/update_game/<int:id>', methods=['GET', 'POST'])
def update_game(id):
    igra = Igra.query.get_or_404(id)
    if request.method == 'POST':
        igra.naziv = request.form['naziv']
        igra.slika = request.form['slika']
        igra.trener_id = request.form['trener_id']
        db.session.commit()
        return redirect(url_for('main_html.games'))
    treneri = Trener.query.all()
    return render_template('update_game.html', igra=igra, treneri=treneri)

@main_html.route('/delete_game/<int:id>')
def delete_game(id):
    igra = Igra.query.get_or_404(id)
    db.session.delete(igra)
    db.session.commit()
    return redirect(url_for('main_html.games'))
