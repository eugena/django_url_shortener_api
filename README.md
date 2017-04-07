# URL Shortener API #

URL Shortener API is meant for obtaining short URLs. Installation guide, features, as well as API endpoints are listed below.

## Installation

Note: It is tested to run on Python 2.7.

    virtualenv .shortener
    source .shortener/bin/activate
    pip install -r requirements.txt
    python manage.py migrate

## Testing

    python manage.py test

## Server Start

    python manage.py runserver 8001

## API Endpoints

Note: API requests should be JSON formatted. All responses are JSON formatted.

###  Retrieving a list of all existing shortened URLs:
```
    GET /[version]
```

Request Example:

```bash
    $ curl -X GET -H "Content-Type: application/json" "http://127.0.0.1:8001/0.1/"
```

    
Response Example:
```javascript
    [
        {
            "code": "SFJrW8V",
            "url": "https://ln.wikipedia.org/wiki/Lok%C3%A1s%C3%A1_ya_libos%C3%B3",
            "created": "2017-04-06T15:58:03.062646Z",
            "qty": 1,
            "target": "m",
            "short_url": "http://127.0.0.1:8001/SFJrW8V"
        },
        ...
        {
            "code": "TrhrmWr",
            "url": "http://www.google.com/",
            "created": "2017-04-06T16:43:17.128749Z",
            "qty": 0,
            "target": "d",
            "short_url": "http://127.0.0.1:8001/TrhrmWr"
        }
    ]
```

###  Summitting a new URL:

```
    POST /[version] [payload]
```

Payload parameters: 

  * **url** (required) should be a correct URL
  * **target** (optional) device type, can be "d" - desktop (default), "m" - mobile or "t" - tablet



Request Example:

```bash
    $ curl -X POST -H "Content-Type: application/json" -d '{"url":"http://www.coursera.org/", "target": "t"}' "http://127.0.0.1:8001/0.1/"
```

    
Response Example:
```javascript
{
    "short_url": "http://127.0.0.1:8001/rzptAxO"
}
```

After executing of this command navigating to http://127.0.0.1:8001/rzptAxO will redirect you to http://www.coursera.org.


Use swagger to view API documentation and check API viewpoints http://127.0.0.1:8001/docs/.

    

    
