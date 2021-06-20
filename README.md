# neon-starter-template-flask-service

A starter template for building a flask application ready to be deployed to google cloud.

This is a minimal flask application for building microservices.

## Tech Stack
The backend server uses flask to implement logic in python for flexibility.

The frontend server uses Bootstrap and flask's jinja engine.

Static assets (css, js, and images) in the `public` directory are deployed separately from the flask web app in the `server` directory.

## Getting started

### Installations
- python
- virtualenv
- pip

### Setting up a virtual environment
Run the following to set up a virutal environment using `virtualenv`
```
pwd # ensure you are at repo root directory
--> starter-template-flask-service
virtualenv template-env # create a virtual environment called "template-env"
source template-env/bin/activate # activate the virtual environment
pip install -r requirements.txt # install python packages
```

### See `server/README.md` for running Locally

### Deploying
```
firebase deploy
cd server

gcloud builds submit --tag gcr.io/go-neon-312006/neon-starter-template-flask-service
gcloud beta run deploy neon-starter-template-flask-service --image gcr.io/go-neon-312006/neon-starter-template-flask-service --platform=managed --region=us-west1 --ingress=all
```

https://neon-starter-template-flask-service-wjrnu3p4ya-uw.a.run.app/
