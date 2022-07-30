# Bookstore Demo REST API

## Installation Instructions
* Copy the `env-template` file to a `.env` file and adapt the parameters where relevant.
 I used an AWS-hosted Postgresql database for development.
### Local development:
1. Set up the virtual environment
    
From the root of the repository, run:
```
pipenv shell
pipenv install
```
2. To initialize the database and load some demo data, run:
```
python initialize_data.py
```

3. To test the API locally, run: `uvicorn main:app`
4. You should now be able to test the various endpoints using 

### Docker Container
1. Build the Docker container:
```
docker build -t <image_name> ./
docker run -d --name <container_name> -p 80:80 <image_name>
```

## Recommendations
* Add CORS for front end accessibility
* For the speed of development, various resources were grouped into single files (eg the persistence folder). As the project scales, these should be separated into individual modules, i.e. a 'models' folder with a file for each model type.
* Password storage for database - hidden rather than entered in .env file
* Database migrations have not been configured and should be added (eg using Alembic)
* Joining of query parameters on the 'books' resource.

### Project Shortfalls:
* Option to return XML based on the 'Content-Type' header
* API tests for each endpoint


**References:**

* https://fastapi.tiangolo.com
* https://github.com/tiangolo/full-stack-fastapi-postgresql