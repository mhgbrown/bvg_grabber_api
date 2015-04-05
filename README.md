# [BVG Grabber API](https://bvg-grabber-api.herokuapp.com/)

An alternative JSON API for [Berlin's public transportation authority](http://www.bvg.de/en/) based on [bvg-grabber](https://github.com/MarkusH/bvg-grabber) by @MarkusH.

## Usage

```/scheduled``` returns scheduled departure times and accepts the following options:
* ```station``` - the station from which to retrieve departures
* ```vehicles```- the medium(s) of transport to look up (accepts S,U,TRAM,BUS,FERRY,RB,IC)
* ```limit``` - the number of results to return

```/actual``` returns actual departure times and accepts the following options:
* ```station``` - the station from which to retrieve departures

### Response
The JSON response is a list of depatures:

    [
        ["S Prenzlauer Allee", [{
            "start": "S Prenzlauer Allee",
            "remaining": -300,
            "line": "S41\n\n(Gl. 1)",
            "end": "Ringbahn S 41"
        }, {
            "start": "S Prenzlauer Allee",
            "remaining": -300,
            "line": "S41\n\n(Gl. 1)",
            "end": "Ringbahn S 41"
        }]]
    ]


### Examples

- [https://bvg-grabber-api.herokuapp.com/scheduled?station=S%20Prenzlauer%20Allee%20(Berlin)&vehicles=BUS,S&limit=2](https://bvg-grabber-api.herokuapp.com/scheduled?station=S%20Prenzlauer%20Allee%20(Berlin)&vehicles=BUS,S&limit=2)
- [https://bvg-grabber-api.herokuapp.com/actual?station=S%20Prenzlauer%20Allee%20(Berlin)](https://bvg-grabber-api.herokuapp.com/actual?station=S%20Prenzlauer%20Allee%20(Berlin))

## Motivation

Although [BVG provides an API for web developers](http://www.vbb.de/de/article/webservices/schnittstellen-fuer-webentwickler/5070.html), one must submit an application for its use. This API provides some of the features of the official API without the hassle of applying.

## Development Information

This app is based on Heroku's [Getting Started with Python on Heroku tutorial](https://devcenter.heroku.com/articles/getting-started-with-python) and has been upgraded to support Python 3.4.2 according to some very useful [information on Stack Overflow](http://stackoverflow.com/questions/26315455/in-heroku-python-tutorial-virtualenv-issues-installing-wsgiref-ez-setup-syntax).

### Running Locally

Make sure you have Python [installed properly](http://install.python-guide.org).

```sh
$ pip install -r requirements.txt
$ foreman start web
```



