import os
from flask import Flask
from flask_migrate import Migrate


def create_app():
    app = Flask(__name__, static_url_path='',static_folder='static' ,template_folder='templates')
    app.config.from_pyfile('../config.py')

    migrate = Migrate(app)

    with app.app_context():
        # from app.auth import auth as auth_blueprint
        # app.register_blueprint(auth_blueprint, url_prefix='/auth')

        from app.pages import pages as pages_blueprint
        app.register_blueprint(pages_blueprint, url_prefix='/pages')

        return app
