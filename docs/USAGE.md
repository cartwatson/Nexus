# Usage

## Steps

*Technically step 2 is not essential but it does add convenience*

1. Run `./build-and-run.sh`
    - Details below
1. Connect to PG Admin and create pg server
    - Details below
1. Make the following api calls, note the ports and their associated services*
    - http://localhost:5000/track-satellite?id=object0
    - http://localhost:5000/request-image?id=object0
    - Endpoints/Ports
      - API -- localhost:5000
      - Sat -- localhost:5050
1. Open the MCS logs and wait until `TRANSMITTING REQUESTS...` and `DOWNLOADING IMAGES...` have been logged
1. Make the following api call
    - http://localhost:5000/images?id=object0
1. Image of "object0" will be stored in the api container under `app/images/object0.png` 
    - Recognize the image? ;)
1. Feel free to repeat this process with multiple "satellites"
    - The image "taken" will be a random selection of four images of the real droid

\* The ports will be changed if `docker-compose.yml` is modified

## Build-and-Run.sh

*The build-and-run script does the following under the hood*  

1. Run `docker compose up -d --build`
2. Init `takehome` database
    - `docker exec -it turion-take-home-pg-1 bash`
    - runs [db/init.sh](../db/init.sh) as sudo on the `turion-take-home-pg-1` container
    - `exit`

## Connect to PG Admin and Create Server

### Connect to PG Admin

PG Admin runs on port 5001. To access, navigate to `localhost:5001` in a web browser. The username and password are set in `docker-compose.yml` based on the environment variables.  

- The defaults are:
    - Username: takehome@takehome.com
    - Password: takehome

### Create Server

*If `docker-compose.yml` is modified it will change the following values*

1. Navigate to PG admin
1. Click on `Add New Server`
1. In the `General` tab
    - Name: starfire
1. In the `Connection` tab
    - Hostname: pg
    - Port: 5432
    - Username: takehome
    - Password: takehome

