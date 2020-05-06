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

#### Faker
##### Adicionar usuários fake (instalar dependências de dev antes)
- flask shell
```shell
from app import fake
fake.users(100)
```
##### Adicionar posts fake (instalar dependências de dev antes)
- flask shell
```shell
from app import fake
fake.posts(100)
```