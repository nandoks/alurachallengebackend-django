# alurachallengebackend-django


This is a backend challenge made by Alura, we will be making the aluraflix backend REST API.


### fixture for initial data ###
There is a fixture video/initial_data.json that can be used to populate the DB with 3 initial values.

### if using the docker ###
You can use the Dockerfile to run the project on docker.
Don't forget to add a secret key to the .env.empty and change its name to .env

### if not using docker ###
Inside settings/dev.py under DATABASE you can comment the postgres config and uncomment the sql3lite config so it can sur locally if you don't have docker.

