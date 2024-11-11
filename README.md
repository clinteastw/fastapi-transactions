# Transactions processing app
Fastapi app that emulates the processing of a webhook from a third-party payment system.

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

Run app
```python
cd src
py main.py
```

