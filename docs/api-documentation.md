# API Documentation

## General Notes

- API is hosted on port 5000 inside the container
- to access API when run in docker `localhost:5000`
- request type is not currently enforced
- all return information is in the following form

```json
{
  "Success": boolean,
  "Message": "Message about what happened or the data param",
  "Data": Any type of Data
}
```

## Track Satellites

URL: /track-satellite
Expected Parameters:
- `id`
    - id of satellite to track, this should be a POST request
    - if not provided, a list of satellites will be returned, this should be a GET request

## Create Request for Image of Satellite

URL: /request-image
Expected Parameters:
- `id`
    - id of satellite to image
    - if not provided, api errors out
 
## Get Images from Droid

URL: /images
Expected Parameters:
- `id`
    - id of satellite request
    - if not provided, error occurs # TODO: could return all images
- `droid`
    - id of droid from which images are requested
    - if not provided, "DROID" is assumed
