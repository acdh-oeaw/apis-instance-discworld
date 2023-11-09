Discworld APIS example instance
===============================


Initialize your database
```
poetry run ./manage.py migrate
```

Load data from fixtures
```
poetry run ./manage.py loaddata data/dump.json
```

Create user
```
poetry run ./manage.py createsuperuser
```

Run server
```
poetry run ./manage.py runserver
```
