# API Documentation

## General Notes

- API is hosted on port 5000 inside the container
- To access API when run in docker `localhost:5000`
- Request type is not currently enforced
- All return information is in the following form

```
{
  "Success": boolean,
  "Message": "Message about what happened or the data param",
  "Data": Any type of Data
}
```

## Track Satellites

URL: `/track-satellite`  
Request types: `POST/PUT`, `GET`  
Expected Parameters:
- `id`
    - id of satellite to track
    - if not provided, a list of satellites objects will be returned
        - this should be a GET request

## Create Request for Image of Satellite

URL: `request-image`  
Request types: `POST`  
Expected Parameters:
- `id`
    - id of satellite to image
    - if not provided, function errors out
 
## Get Images from Droid

URL: `/images`  
Request types: `GET`  
Expected Parameters:
- `id`
    - id of satellite request
    - if not provided, all images are returned
- `droid`
    - id of droid that images are requested from
    - if not provided, "DROID" is assumed
