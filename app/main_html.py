from flask import Blueprint, render_template

main_html = Blueprint('main_html', __name__, template_folder='templates')

@main_html.route('/')
def index():
    return render_template('index.html')

@main_html.route('/games')
def games():
    return render_template('games.html')
