# Notes from Andrew Kettel
## To setup environment
Clone repo from git:<br/>
`git clone git@github.com:andrewkettel/backstage_difference.git`<br />

Inside `backstage_difference` folder: <br/>
`python3 -m venv .venv`<br/>
`source .venv/bin/activate`<br/>
`pip install -r requirement.txt`<br/>

## To run the test server
`python manage.py runserver`

## API Example Usage
[http://localhost:8000/difference?number=10](http://localhost:8000/difference?number=10)

## API Documentation
[http://localhost:8000/docs](http://localhost:8000/docs)

## To run the unit tests
`python manage.py test`
