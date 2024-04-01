# Questions/Clarifications

## Notes about future work

- overall
    - some chunks of code are reused throughout multiple files/containers there may be benefit in consolidating some aspects (eg: db connection/init validation)
- DB
    - ability to expand to have multiple "DROID"s
    - init tables script, weird approach, would spend more time learning the "right way"
- MCS
    - ability to handle multiple droids
        - add droids to system while up to ensure no downtime/missed contacts
        - add ability to request image of satellite from specific droid
- satellite
    - /docker make port assignment dynamics so multiple "satellites/droids" can be used at once
    - file naming
        - find way to incorporate datetime when the image was taken
        - find way to take more than one image of a satellite
- api
    - enforce request type for security purposes
    - might be worth using PUT request type in some places
    - ability to upload images directly to db with /images
    - enfore satellite naming conventions, currently "" is a valid object name
