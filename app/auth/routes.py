from app.auth import auth
from flask import render_template, redirect, url_for

@auth.route('/')
@auth.route('/index')
def index():
    return redirect(url_for('auth.login'))

@auth.route('/', methods=['GET','POST'])
@auth.route('/login', methods=['GET','POST'])
def login():
    return render_template('auth/login.html', title='Login')
