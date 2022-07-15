# Django Rest Framework - Project Starter (+ jwt auth)

## Create a new Python Virtual Environment
```
python3 -m venv /path/to/new/env
```
Change to the new environment by running the following command:
```
source {/path/to/new/env}/bin/activate
```

___


## Install the necessary libraries
Head into the project folder and run the following command:
```
pip install -r requirements.txt
```

___

## Make and run migrations
```
cd src/
python manage.py makemigrations
python manage.py migrate
```

---
## Create a superuser
```
python manage.py createsuperuser --username admin --email admin@example.com
```
---
## Start the server
```
python manage.py runserver
```