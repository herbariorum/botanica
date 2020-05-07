from app.pages import pages
from flask import render_template, redirect, url_for

@pages.route('/')
@pages.route('/index')
def index():
    return redirect(url_for('pages.home'))

@pages.route('/', methods=['GET','POST'])
@pages.route('/home', methods=['GET','POST'])
def home():
    return render_template('pages/home.html', title='Início')
