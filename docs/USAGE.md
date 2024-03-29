# Usage

## Steps

1. run `docker compose up -d --build`
2. Connect to PG Admin
  - as seen below
3. Create pg server
  - Name: starfire
  - Connections tab
    - Hostname: pg
    - Port 5432
    - Username: takehome
    - Password: takehome
4. Init `takehome` db
  - `docker exec -it turion-take-home-pg-1 bash`
  - `./app/init.sh`
  - `exit`
5. Test the following endpoints for basic functionality
  - ENDPOINTS
    - API -- localhost:5000
    - Sat -- localhost:5050
  - http://localhost:5000/add-satellite/object0
  - http://localhost:5000/request-image-of-satellite/object0
6. open the mcs logs and wait until `TRANSMITTING REQUESTS...` and `DOWNLOADING IMAGES...` have been logged
  - http://localhost:5000/get-images-from-droid/object0
7. image of "object0" will be stored in the api container under `app/images/object0.png` 
  - recognize the satellite? ;)
8. feel free to repeat this process with multiple "satellites"

## Development
You can start the compose project with the below docker compose command. I have found that using bind mounts help me with local development but is not necessary (you can google this).
```
docker compose up -d --build
```
The initial project comes with a simple MCS starter container. Once the project is spun up, the MCS should be printing "talking to sat..." every five seconds. You can see these print statements by looking at the docker logs: `docker logs --follow <container ID>`.

## Connect to PG Admin
PG Admin runs on port 5001. To access, navigate to `localhost:5001` in a web browser. The username and password are set in `docker-compose.yml` based on the environment variables. The defaults are:
  - user: takehome@takehome.com
  - pass: takehome

## Create a server if it doesn't exist
1. Navigate to PG admin
1. Click on `Add New Server`
1. In the `General` tab
  - Name: starfire (or whatever you want your server name to be)
1. In the `Connection` tab (all these values are defined in the docker compose file):
  - Hostname: pg (the container name used in the docker compose file)
  - Port: 5432
  - Username: takehome 
  - Password: takehome
