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


| Rotas | Descrição | Parametros | Output |
|-------|-------------|------------|-----------------|
| `POST /signin`| login de usuário | body: `{ email: string, password: string}` | `{ token: string, refresh_token: string }` |
| `POST /signup` | registro de usuário | body `{ nome: string, email: string, password: string}` | `criado com sucesso`|
| `POST /product/create` | criar um produto | body `{ name: string}` | `{ id: number, name: string, }` |
| `POST /product/ordem` | criar uma ordem | body `{ product: foreignkey(id), qtd: number, price: number, pOrS: ((P, compra), (S, venda))}` | `{ id: number, product: foreignkey(id), qtd: number, price: number, pOrS: ((P, compra), (S, venda))}`|
| `GET /product/ordem-list` | lista todas as ordens | | `{ id: number, product: foreignkey(id), qtd: number, price: number, pOrS: ((P, compra), (S, venda))}`|
| `GET /product/list` | Lista todos os produtos |  | `{id: id, name: string}` |
| `GET /product/movement` | Movimento do estoque | | `{name: string, purchase: number, sales: number, qtdStock: number, cost: number, revenues: number, profit: number, }` |
| `PUT /pruduct/update/{id}` | Edita um produto | body `{name: string}` | `{name: string}` |
| `DELETE /product/delete/{id}` | Deleta um produto |  | `{name: null` |

# Rodando o front-end

## Clone o repositório
Para rodar o projeto será necessário:
- 

git clone https://github.com/valter-junior/product-register.git

cd /frontend

git checkout Feat/frontend

yarn install
yarn start
