# Falcon Sample 

A sample implementation for the python falcon micro framework

The folder structure will look like this:
```
~/environment/falcon-sample
├── app.py
├── custom_logger.py
├── json_utils.py
├── products.json
├── requirements.txt
├── docker-compose.yml
├── Dockerfile
├── README.md
└── .gitignore
```

## Available Routes
```
| HTTP METHOD | URI                                     | ACTION                      |
|-------------|-----------------------------------------|-----------------------------|
| GET         | http://[hostname]/products              | Gets all products           |
| GET         | http://[hostname]/products/<product_id> | Gets one product            |
| POST        | http://[hostname]/products              | Creates a new product       |
| PUT         | http://[hostname]/products/<product_id> | Updates an existing product |
| DELETE      | http://[hostname]/products/<product_id> | Deletes a product           |
```

## Project Set up

### Prerequisites
* docker
* python
* docker-compose
* git


### Start up 
```bash
$ docker-compose up
```

### Tear down
```bash
$ docker-compose down
```

