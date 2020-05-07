import os
from flask import Flask
from flask import redirect, url_for
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from .models import configure as config_db
from .serializer import configure as config_ma

def create_app():
    app = Flask(__name__, static_url_path='',static_folder='static' ,template_folder='templates')
    app.config.from_pyfile('../config.py')

    # configura o db e o serialize
    config_db(app)
    config_ma(app)
    
    migrate = Migrate(app, app.db)

    with app.app_context():
        # from app.auth import auth as auth_blueprint
        # app.register_blueprint(auth_blueprint, url_prefix='/auth')
        @app.route('/')
        @app.route('/index')
        def index():
            return redirect(url_for('pages.home'))

        from app.pages import pages as pages_blueprint
        app.register_blueprint(pages_blueprint, url_prefix='/pages')

        return app
