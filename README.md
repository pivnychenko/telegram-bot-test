## Local run 

### Create .env file from .env-example and set all data

```sh

$ docker-compose build --no-cache
$ docker-compose up
$ docker-compose run botserver python app/manage.py migrate
$ docker-compose run botserver python app/manage.py makemigrations
$ docker-compose run botserver python app/manage.py createsuperuser


$ ssh -R 80:localhost:8000 nokey@localhost.run and use url https
```

### Required SET hook for telebot http://localhost:8000/set-hook/

### SET Question for bot http://localhost:8000/admin/botstarter/question/