from flask import render_template
from app.pages import pages


@pages.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html', title='Página não encontrada'), 404


@pages.app_errorhandler(500)
def internal_server_error(e):
    return render_template('500.html', title='Erro interno'), 500
