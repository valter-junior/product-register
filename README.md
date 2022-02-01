# product-register

Existem duas branches uma possue o backend a outra o frontend

# Rodando o backend

## Clone o repositório
Para rodar o projeto será necessário:
- Você ter o python 3 instalado na sua máquina
- Você deve instalar o Django (python -m pip install Django)
- Você deve instalar psycopg2 (pip install django djangorestframework psycopg2)
- Você deve criar um banco de dados local postgreSQL com o nome product.

git clone https://github.com/valter-junior/product-register.git

cd /backend

git checkout Feat/backend

- Você deve fazer as migrations para o seu banco de dados
- python manage.py makemigrations e python manage.py migrate

Depois você coloca o seguinte comando:
python manage.py runserver

# Rodando o front-end

## Clone o repositório
Para rodar o projeto será necessário:
- Você instalar Angular CLI na sua maquina

git clone https://github.com/valter-junior/product-register.git

cd /frontend

git checkout Feat/frontend

npm install

npm install - g @angular/cli

ng serve
