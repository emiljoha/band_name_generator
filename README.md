# Wikipedia band name generator

Use the only truly scientific way to generate bandnames and first album titles.

Draws a random wikipedia article and uses the title as the band name. The first album name is choosen as the last 4 words of a random Aristotle quote.

## Installation

The easiest way to get the web server up and running is with docker. 

If you have not already make sure you have installed
[docker](https://docs.docker.com/get-docker/) and
[docker-compose](https://docs.docker.com/compose/install/)

Create a file `.env` containing the enviroment variables needed to configure
the service.

```shell
DOMAIN=0.0.0.0
PORT=8080
FLICKR_API_KEY=<api-key>
FLICKR_API_SECRET=<secret>
```

You can get the flickr api keys and secret from
[here](https://www.flickr.com/services/api/misc.api_keys.html)

In the project root, build and start the webserver with the command

``` shell
docker-compose up
```
