Python Gateway Interface Examples
=========================

This project has a simple "Hello" application
implemented as a CGI, WSGI, and ASGI application. 

CGI Server
----------

The CGI Server uses the Python built-in web server

```bash
pipenv run python -m http.server --cgi 8000
```


WSGI Server
-----------

The WSGI Server uses the Python WSGI reference server

```bash
pipenv run python wsgi-server.py
```

ASGI Server
-----------

The ASGI Server uses Daphne from the Django Project as there
is no reference server.

```bash
pipenv install
pipenv run daphne -b 0.0.0.0 -p 8000 asgi-server:hello

```

Accessing the Apps
------------------

Every one of the example apps can be reached via the URL:
[http://localhost:8000/cgi-bin/hello.py?name=World](http://localhost:8000/cgi-bin/hello.py?name=World)

Only the CGI app requires the script path. However, the other
apps ignore the path and work just the same.
