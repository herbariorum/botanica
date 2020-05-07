from app.pages import pages
from flask import render_template, redirect, url_for

@pages.route('/')
@pages.route('/index')
def index():
    return redirect(url_for('pages.home'))

@pages.route('/', methods=['GET','POST'])
@pages.route('/home', methods=['GET','POST'])
def home():

    posts = [
        {
         'id': 1,
         'author': {'username': 'Elias Gomes'},
         'title': 'Anoitecer em Augustinópolis',
         'body': 'Augustinópolis é bonita ao anoitecer. Porém ainda fica muito quente',
         'thumb': 'anoitecer_augustinopolis.png',
         'post_date': '01/10/2019'
        },
        {
         'id': 2,
         'author': {'username': 'Elias Gomes'},
         'title': 'Anoitecer em Axixá',
         'body': 'Axixá tem serras muito altas. Não tenho coragem de subir até lá',
         'thumb': 'serras_axixa.png',
         'post_date': '10/12/2019'
        },
        {
         'id': 3,
         'author': {'username': 'Elias Gomes'},
         'title': 'Anoitecer em Sampaio',
         'body': 'Sampaio tem ótimas. Sempre vou lá aos finais de semana',
         'thumb': 'praia_sampaio.png',
         'post_date': '05/06/2020'
        },
        {
         'id': 4,
         'author': {'username': 'Elias Gomes'},
         'title': 'Peixaria de Praia Norte',
         'body': 'Sempre estou visitando as peixarias de Prais Norte. Tem ótimos peixes',
         'thumb': 'peixarias_praia_norte.png',
         'post_date': '20/04/2020'
        }
    ]

    return render_template('pages/home.html', title='Início', posts=posts)
