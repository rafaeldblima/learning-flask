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

#### Httpie
##### Testar requests com auth (instalar dependências de dev antes)
```virtualenv
http --json --auth <email>:<password> GET http://127.0.0.1:5000/api/v1/posts/
```
```virtualenv
http --auth <email>:<password> --json POST http://127.0.0.1:5000/api/v1/posts/ \
"body=I'm adding a post from the *command line*."
```
```virtualenv
http --auth <email>:<password> --json POST http://127.0.0.1:5000/api/v1/tokens/
```
```virtualenv
http --json --auth eyJpYXQ...: GET http://127.0.0.1:5000/api/v1/posts/ 
```