# Nexus

## About

Nexus is a simulated mission ops environment.  

In short it consists of five individual docker containers speaking to each other.  Imaging satellites (droids) to take images of other satellites.  The database to hold information about active droids, satellites (objects being tracked), images, and requests for images.  Mission Control which handles interaction between droids and the database. An API to handle user requests for tracking more satellites or taking images.  And a dashboard to streamline user experience.

## More Docs

- [Build & Run](/docs/USAGE.md)
- [Design Strategy](docs/design.md)
- [API Documentation](/docs/api-documentation.md)
- [Future Work](/docs/future-work.md)
