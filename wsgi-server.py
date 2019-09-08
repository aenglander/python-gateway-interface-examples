import html
from urllib.parse import parse_qs
from wsgiref.simple_server import make_server


def hello(environ, start_response):
    qs = parse_qs(environ.get("QUERY_STRING"))
    name = qs.get("name", ["World"])
    text = html.escape("Hello, {}!".format(name[0])).encode()

    status = '200 OK'
    headers = [('Content-type', 'text/html; charset=utf-8')]  # HTTP Headers
    start_response(status, headers)

    body = [
        b"<HEAD><TITLE>", text, b"</TITLE></HEAD>",
        b"<BODY><H1>", text, b"</H1></BODY>"
    ]

    return body


with make_server('', 8000, hello) as httpd:
    print("Serving on port 8000...")

    # Serve until process is killed
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
