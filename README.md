
# FirstGit


## Start application

### Install deps
```
pip install psycopg2
pip install django-environ
```

### Start docker containers
```
docker-compose up -d
```
### Run application
```
python3 manage.py migrate 
python3 manage.py runserver ${PORT}
```