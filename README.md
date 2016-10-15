## Setting up a local test API
* Visit https://github.com/typicode/json-server to read about json-server
* On the command line sudo npm install -g json-server
* Download data.json from https://github.com/typicode/jsonplaceholder/blob/master/data.json to a local path (~/code/json-server e.g)
* Start the api with 'json-server --watch  data.json'
* Test if you are able to hit the server at http://localhost:3000

## Hitting the API with tests
* nosetests -sv test_json_api.py  

## Running only those tests tagged as smoke tests ('smoke')
* nosetests -a smoke

