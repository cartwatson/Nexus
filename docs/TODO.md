# TODO

- [ ] *section*    description

- [ ] *api*        ensure compatibility with postman
- [ ] *api*        expose necessary ports, use service-name not IP
- [ ] *api-feat*   add tracked satellite to db
- [ ] *api-feat*   get images of tracked satellite take by DROID
- [ ] *api-feat*   request image of a tracked satellite, store these requests
- [ ] *database*   create/init necessary tables
- [ ] *general*    figure out to return images with api
- [ ] *general*    figure out to store images
- [ ] *mcs-feat*   mechanism to intermittely "contact" satellite
- [ ] *mcs-feat*   periodically send "download all images" command to satellite
- [ ] *mcs-feat*   when contact established; send imaging requests from db
- [ ] *sat-feat-1* receive imaging requests from MCS
- [ ] *sat-feat-1* take fake image, store locally
- [ ] *sat-feat-2* receive image download requests, send images to MCS
- [ ] *satellite*  expose necessary ports, use service-name not IP
- [X] *api*        add docker image to docker compose
- [X] *api*        create docker image
- [X] *docker*     get default docker containers spun up
- [X] *docs*       create/organize docs from given materials
- [X] *misc*       init .gitignore
- [X] *satellite*  add docker image to docker compose
- [X] *satellite*  create container (possibly like REST API
