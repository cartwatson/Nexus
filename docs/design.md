# Design Thoughts & Process

*Note: I may reference the docker container "satellite" as "droid", this is to make a distinction between the satellite taking photos (droid in this case), and the satellite(s) being tracked*  

## API

The API was designed in a manner such that all functions/URLs should have similar syntax and results. Additionally, the URL should be useful for both POST/PUT and GET requests, query parameters decide (and eventually request type) should determine how requests get routed.  

All return values consist of the same three json key-value pairs: Success, Message, and Data.  These three were chosen with the following ideas in mind: success gives an easy to parse and read return value, message explains what went wrong or provides more context for the data being recieved, and data transmits the payload.  

All functions in the API operate as GET and POST/PUT requests where possible.  If no parameters are provided the request attempts to return all of the specified resource.  

## MCS

The mechanism to simulate ground contact is simply to make mcs sleep for a period of time.  In hindsight it may have been more realistic to make the droid sleep for a period of time.  

The choice was made to have MCS query for images every time it makes contact with the satellite. This is because currently the droid is only able to store one image at a time of each satellite (this is acknowledged in future work). Additionally once MCS recieves an image it inserts it into the database and marks the request fulfilled so the same request is not sent to the satellite twice.  

I'll touch on this more later but MCS was designed to be able to easy add the capability to talk to multiple droids/satellites.  

## Satellite/Droid

The satellite was designed very similarly to the API.  It only needs two aspects of functionality currently: the ability to take an image and to transmit that image. As such the design for satellite came together very quickly. It's design does leave a little to be desired as a REST API but it functions fully in it's contact with MCS. Due to it's simply nature and current design, expanding it's functionality would not be difficult.  

## Database

### Requests
The requests table uses the time the request was made as it's primary key.  This value is used to sort requests prior to being sent to the satellite.  The `target_sat` is used to determine which satellite to take a picture of, it has a foreign key relation to `satellites`. `pending` and `fulfilled` are used to determine the stage of the request.  It may be more human reable to use something like an enum in place of those two columns in the future, the original way would save on storage though in some cases, due to differences in bool/enum storage. 

### Satellites
The satellites table is very bare.  I only implemented what I needed for an MVP which in this case was just an id.  Future work could very easily expand this to include a description, or extra data.  This would be a trivial change and could be done within an hour.  

### Droids
The droids table is likewise bare, for the same reasons as the satellite. Again, I would recommend expanding it to include more usable and human readable info in the future should more work be done on this project.  

### Images
The images table was built with future work in mind.  The `time_taken` value would ideally be the time an image was taken and currenlty serves as the primary key. In the future the primary key should change to a UUID to ensure there are no strange conflicts.  The `taken_by` value would allow the user to query the db for images taken by a specific droid (the api currently has this functionality, the hold up is on MCS not supporting multiple droids). Additionally the `taken_by` value must match an entry in the `droids` table. `id_sat` is simply the given id of the satellite of which the image was requested, it must match a value in the `satellites` table. Lastly, the `img` is the raw binary data of the png, including header in this case.  

## What's left to do now?

Overall the program works well. The feature that I would like to add would be to be able to have multiple droids (in this case satellite docker containers). Ideally what would happen is a droid (container) would launch and the user would add an id and port (or communication id) to the DB. From there MCS would pull that info from the DB and start communicating without down time (it could do this in between contacts). The effort to accomplish that goal wouldn't be outlandish but it may take a single engineer a day or two to work out, the mcs program was built with this idea in mind.  

Currently there is no POST/PUT request on images but it may be nice functionality to have incase an operator manually got an image from a droid or for any other reason.  

More notes & ideas can be found in [future-work](/docs/future-work.md)  
