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

# Notes from Andrew Kettel
I started with a basic Django setup and decided to use Django-ninja as I heard about it recently and have used it to make quick APIs.  It seemed like it would fit well here. The math and some validation of the input to the API would be a good place to start. Unit tests are always a good idea so I wrote a few to test the math and the input validation.

Once I was happy with the math and unit tests, I moved on to the occurrence and date tracking. An SQLite database was already connected and I don't think the data would grow very large so I kept it.  If this project was to be expanded or deployed somewhere, I would probably switch to a postgreSQL database. Once I added the model to store the number of occurrences and last_datetime, I realized I could store all the data in the table which would make the endpoint faster on subsequent requests of the same number; there is no need to recalculate since the math doesn't change.  I added some more unit tests to make sure the request occurrence counting worked. 

After that, I spent some time getting the Readme into a good state with accurate setup steps. Also reorganized the folder structure to separate the tests and to be able to use the Django startapp command if new services are ever requested.  I also decided to start using feature branches and pull requests for changes as it's bad form to commit and push to main. I would normally do a squash and merge and delete the feature branch from the remote in the interest of cleanliness but for a coding assessment, I kept a standard merge and left the feature branches intact.

Next step was to add a simple Docker setup and update the readme with steps for both local and docker setups. This would make deployment and setup easier and more consistent.

I took some time away from the project and realized that the math should really be split from the api layer. I created a simple utils.py file to hold the math and consolidated it a bit. I also knew that there were better ways to calculate the sum of squares of a sequence of natural numbers and to calculate the sum of the sequence of natural numbers but didn't know the functions off the top of my head. Brute forcing the solution is fine if n<=100 but it does run in O(n) while the mathematical functions perform in O(1).

To show that this setup would allow for new services and endpoints, I created a WIP branch for the Pythagorean Triplet endpoint.  I added the input and output schema but no code to implement the math.

After dinner, I decided to take a quick look at some of the first code I wrote thinking about how I would review a PR and realized that the defaults of get_or_create could be used instead of setting values on the new object.  The changes clean up the code a bit and make it a little more readable.

Final thoughts, this was a good coding assessment.  It made me think, let me show off some of what I can bring, but wasn't too esoteric as to be confusing.  Thank you for giving me this opportunity and I hope you enjoy!<br/>
~Andrew Kettel
