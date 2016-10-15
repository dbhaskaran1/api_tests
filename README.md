## Setting up a local test API
* Visit https://github.com/typicode/json-server to read about json-server
* On the command line sudo npm install -g json-server
* Download data.json from https://github.com/typicode/jsonplaceholder/blob/master/data.json to a local path (~/code/json-server e.g)
* Start the api with 'json-server --watch  data.json'
* Test if you are able to hit the server at http://localhost:3000

## Start Testing

### Set up environment
* install pip for managing python and its packages
* Setup a virtual environment for your python using instructions at http://virtualenvwrapper.readthedocs.io/en/latest/install.html
* mkvirtualenv api_tests
* workon api_tests
* pip install -r requirements
* At this point your environment is all set to run tests.

### Hitting the API with tests
```nosetests -sv test_json_api.py```

### Running only those tests tagged as smoke tests ('smoke')
```nosetests -a smoke```

