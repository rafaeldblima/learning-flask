## Flask App

`export FLASK_APP=api.py`

#### Running tests
- flask test

#### Flask-migrate commands
##### Iniciar migrate
- flask db init
##### Criar migration
- flask db migrate -m "initial migration"
##### Aplicar migration
- flask db upgrade
##### Remover migration (última)
- flask db downgrade