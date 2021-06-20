## Setting Flask Web Server Locally

### Set up
```
sqlite3 ## have sqlite3 running

export SQLALCHEMY_DATABASE_URI=sqlite://     \
       APP_SETTINGS=config.DevelopmentConfig \
       FLASK_ENV=development

flask run
```
