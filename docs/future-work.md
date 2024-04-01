# Questions/Clarifications

## Notes about future work

- DB
    - ability to expand to have multiple "DROID"s
    - init tables script, weird approach, would spend more time learning the "right way"
- MCS
    - ability to handle multiple droids
        - add droids to system while up to ensure no downtime/missed contacts
    - ability to handle request priority
        - should be able to give a request a certain priority
            - currently sorted by time, first come first serve
- satellite
    - docker make port assignment dynamics so multiple "satellites/droids" can be used at once
        - this would be necessary for mcs to support multiple satellites at once
        - mcs would also require major changes, although not breaking changes
    - file naming
        - find way to incorporate datetime when the image was taken
        - find way to take more than one "image" of a satellite
- api
    - enforce request type for security purposes
    - ability to upload images directly to db with /images
    - enfore satellite naming conventions, currently "" is a valid object name
- misc
    - some chunks of code are reused throughout multiple files/containers there may be benefit in consolidating some aspects (eg: db connection/init validation)
