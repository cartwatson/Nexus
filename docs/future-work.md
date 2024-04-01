# Questions/Clarifications

## Notes about future work

- DB
    - ability to expand to have multiple "DROID"s
    - add more columns as needed to `droids` and `satellites`
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
        - all systems would need minor touchups but they were built with this idea in mind
            - mcs would require the most significant rework
            - satellite would likely take the role of simulating contact with mcs using the random sleep timer
            - api should be mostly updated for this already, but it may be useful to change how /images behaves by default
            - db is good to go as is
    - enhanced file naming, include datetime when the image was taken
        - this would allow more than one "image" of a satellite at a time
- api
    - enforce request type for security purposes
    - ability to upload images directly to db with /images
    - enforce satellite naming conventions via regex, currently "" is a valid object name
- misc
    - some chunks of code are reused throughout multiple files/containers there may be benefit in consolidating some aspects (eg: db connection/init validation)
        - this could be done with the creation of a package/gem/crate/etc
