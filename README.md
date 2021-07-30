
# HACKERNEWS-SCRAPER

##Description
HackerNews is a popular news site, linking different tech news sources into a single place,
This app is built to periodically scrape the tech news (jobs inclusive) at a default time of (every 5 minutes).
You can also search for news, conveniently paginate through the lists, filter and there's an api provided to post your own news, delete and even update. This api endpoints can be plugged easily into any front end of any framework.

  

live-url : `hi`

## Technology Stack

  

  

- Django

  

- DRF(Django Rest Framework)

  

- Postgres

- HTML

- CSS (BOOTSTRAP)

  

### Setting Up For Local Development

  

  

- Check that python 3 is installed:

  

  

```

  

python --version

  

>> Python 3.7.0

  

```

  

  

- Install virtualenv:

- Clone the Hackernews repo and cd into it:

  

  

```

pip install virtualenv

  

git clone https://github.com/gotahia/ecommerce_api.git

  
  
  

```

Create a virtual enviroment:

```

virtualenv venv

  

```

  

- Activate the virtual enviroment:

  

- On Linux/Mac:

  

```

  

source venv/bin/activate

  

```

  

- On Windows:

  

```

  

cd venv/scripts

  

activate

  

```

  

Feel free to use other tools such as pipenv

  

  

- Install dependencies from requirements.txt file:

  

  

```

  

pip install -r requirements.txt

  

```

  

- Setup up local postgres db

  

```

  

Download and install postgres locally

  

Here is a useful guide for windows

  

[Install Postgres on Windows](https://www.guru99.com/download-install-postgresql.html)

  

  

For MacOS install the psogress app

  

[Install Postgres on Mac](https://postgresapp.com/)

  

Start postgres

  

Create and visualize the databse using [Postico](https://eggerapps.at/postico/)

  

For linux, PGAdmin4 or DBeaver can be used

```

  

- Make a copy of the .env.sample file in the app folder and rename it to .env and update the variables accordingly:

  

  

```

  

SECRET_KEY=generate a random django key # https://www.miniwebtool.com/django-secret-key-generator/

  

DB_NAME=dbname

DB_USER=dbuser

DB_PASSWORD=secretpassword

DB_HOST='127.0.0.1'

DB_PORT='5432'

```

- Apply migrations:

```python
python manage.py makemigrations
```
```
python manage.py migrate

```

* Start up Redis to act as the message broker:

  

To setup a local redis server, install redis on your PC then run:

  

```

redis-server

```

Alternatively you can get a redis broker url from services like Heroku

* Start up celery to scrape data:

```

celery -A hackernews worker -B -l INFO

```

* Run the application with the command

  

```

python manage.py runserver

```
* Default port is http://127.0.0.1:8000

### Running Tests

  

* Run all tests

  

```

  

python manage.py test

  

```

  

  

* Run a particular test script (using testnewsscrape.py inside the unit module as an example)

  

```
python manage.py test api.tests.unit.testnewsscrape
```
* Run test in a particular folder:
```
python manage.py test <folder>
```

  

### API Endpoints
A full documentation of the API endpoints can be found at `api/docs/ ` route.
