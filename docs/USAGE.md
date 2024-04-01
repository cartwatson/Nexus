# Usage

## Steps

*technically steps 2-3 are not essential but they do add convenience*

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
4. Init `takehome` database
    - `docker exec -it turion-take-home-pg-1 bash`
    - `./app/init.sh`
    - `exit`
5. Make the following api calls, note the ports and their associated services
    - http://localhost:5000/add-satellite/object0
    - http://localhost:5000/request-image-of-satellite/object0
    - Endpoints/Ports
      - API -- localhost:5000
      - Sat -- localhost:5050
6. open the mcs logs and wait until `TRANSMITTING REQUESTS...` and `DOWNLOADING IMAGES...` have been logged, then make the following api call
    - http://localhost:5000/get-images-from-droid/object0
7. image of "object0" will be stored in the api container under `app/images/object0.png` 
    - recognize the satellite? ;)
8. feel free to repeat this process with multiple "satellites"
    - the image "taken" will be a random selection of four images of the real droid

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
