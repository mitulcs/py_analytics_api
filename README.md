# Django project create steps

## Create Virtual Environment

```sh
python3 -m venv {environmentname}
```

## Activate Virtual Environment

```sh
source {environmentname}/bin/activate
```

## Create Django project

```sh
django-admin startproject mysite
```

## Create django App

```sh
python manage.py startapp polls
```

## Migarte Command

```sh
python manage.py migrate
```

## RunProject

```sh
python manage.py runserver
```

## Create Super User Command

```sh
python manage.py createsuperuser
```

## Generate Requirements txt

```sh
pip3 freeze > requirements.txt
```

## Install Requirements Txt File

```sh
pip install -r requirements.txt
```
