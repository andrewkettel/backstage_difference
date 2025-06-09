# Notes from Andrew Kettel

# Get the code
Clone repo from git:<br/>
`git clone git@github.com:andrewkettel/backstage_difference.git`<br />

# To setup local environment
Inside `backstage_difference` folder: <br/>
`python3 -m venv .venv`<br/>
`source .venv/bin/activate`<br/>
`pip install -r requirements.txt`<br/>
## Initial DB setup
`python manage.py migrate`
## To run the test server
`python manage.py runserver`
## To run the unit tests
`python manage.py test`

# To setup docker environment
Inside `backstage_difference` folder: <br/>
`docker compose up`

## To run the unit tests
`docker compose exec api python manage.py test`

# API Example Usage
[http://localhost:8000/difference?number=10](http://localhost:8000/difference?number=10)

# API Documentation
[http://localhost:8000/docs](http://localhost:8000/docs)
