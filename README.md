# Transactions processing app
FastAPI app that emulates the processing of a webhook from a third-party payment system.

### Features

- Auth via JWT;
- Entities;
  + User;
  + Account with balance;
  + Payment with transaction_id and amount of transaction;
 
# Quick start

Create .env file with following content
```python
DB_HOST=localhost
DB_PORT=5432
DB_NAME=yourdbname
DB_USER=postgres
DB_PASS=yourdbpass

SECRET_KEY=SECRET
```
- ## Docker

Build container
```python
docker-compose up --build -d
```
```python
docker-compose exec app alembic upgrade head
```
Go to `<link>` : <http://localhost:8000/docs>


- ## Virtualenv

Create virtualenv
```python
virtualenv venv
```

Install dependencies
```python
venv/scripts/activate
pip install -r -requirements.txt
```

Run migration
```python
alembic upgrade head
```

Run app
```python
cd src
py main.py
```

