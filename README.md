# BVG Grabber API

An alternative web API for [Berlin's public transportation authority](http://www.bvg.de/en/) based on [bvg-grabber](https://github.com/MarkusH/bvg-grabber) by @MarkusH.

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

- ```/scheduled?station=S%20Prenzlauer%20Allee&vehicles=BUS,S&limit=2```
- ```/actual?station=S%20Prenzlauer%20Allee```


## Development Information

This app is based on Heroku's [Getting Started with Python on Heroku tutorial](https://devcenter.heroku.com/articles/getting-started-with-python) and has been upgraded to support Python 3.4.2 according to some very useful [information on Stack Overflow](http://stackoverflow.com/questions/26315455/in-heroku-python-tutorial-virtualenv-issues-installing-wsgiref-ez-setup-syntax).



