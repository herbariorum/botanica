# Botânico

# Requerimentos
 - flask
 - python-dotenv
 - flask-migrate

# Criação
```python
$mkdir botanico
$cd botanico
$python -m venv venv
$pip install flask
$pip install python-dotenv
```

# Flaskenv
```python
$touch .flaskenv
$nano .flaskenv
    FLASK_APP=app
    FLASK_ENV=development
    FLASK_RUN_EXTRA_FILES=README.md
```

# Rodando o aplicativo
$flask run
