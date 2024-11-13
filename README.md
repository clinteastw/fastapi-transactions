# Transactions processing app
FastAPI app that emulates the processing of a webhook from a third-party payment system.

### Features

- Auth via JWT;
- Entities;
  + User;
  + Account with balance;
  + Payment with transaction_id and amount of transaction;
 
### Quick start

Create virtualenv
```python
virtualenv venv
```

Install dependencies
```python
venv/scripts/activate
pip install -r -requirements.txt
```
Create .env file with following content
```python
DB_HOST=localhost
DB_PORT=5432
DB_NAME=yourdbname
DB_USER=postgres
DB_PASS=yourdbpass

SECRET_KEY=SECRET
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

