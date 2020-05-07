import os
database_dir = os.path.join(os.path.dirname(__file__), 'database/')

SECRET_KEY = os.environ.get('SECRET_KEY') or '\xfd{H\xe5<\x95\xf9\xe3\x96.5\xd1\x01O<!\xd5\xa2\xa0\x9fR"\xa1\xa8'

FLASKY_MAIL_SUBJECT_PREFIX = '[Gomes]'
FLASKY_MAIL_SENDER = 'GOMES ADMIN <eliaspbareia@gmail.com>'
FLASKY_ADMIN = os.environ.get('ADMIN')
CSRF_ENABLED = True

# Configurações do BD
SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                              'sqlite:///' + os.path.join(database_dir, 'botanico.sqlite3')
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
SQLALCHEMY_TRACK_MODIFICATIONS = False
