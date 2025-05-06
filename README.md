# Nexus

## About

Nexus is a simulated mission ops environment.  

It consists of four individual docker containers passing messages to each other.

- Imaging satellites (droids) to take images of other satellites
- The database to hold information about active droids, satellites (objects being tracked), images, and requests for images
- Mission Control to handle interactions between droids and the gound control/database
- An API to handle user requests for tracking more satellites or taking images

## More Docs

- [Build & Run](/docs/USAGE.md)
- [Design Strategy](docs/design.md)
- [API Documentation](/docs/api-documentation.md)
- [Future Work](/docs/TODO.md)
