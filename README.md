# Django Rest Framework - Project Starter (+ jwt auth)

![django-logo](https://abstract-technology.fr/media/technology/django-logo-negative.png/@@images/image.png)
![rest-logo](https://camo.githubusercontent.com/1cdabf8bfacdd06847a820f6572b3c9f2d17c0ff3d33719d10dc058749f22870/68747470733a2f2f6d69726f2e6d656469756d2e636f6d2f6d61782f3732322f312a4d512d4c6638746d7466612d70756d4e3253683063772e706e67)

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