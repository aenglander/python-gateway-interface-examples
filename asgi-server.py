import html
from urllib.parse import parse_qs


async def hello(scope, receive, send):
    qs = parse_qs(scope.get("query_string"))
    name = qs.get(b"name", [b"World"])
    text = html.escape("Hello, {}!".format(name[0].decode())).encode()

    await send({
        'type': 'http.response.start',
        'status': 200,
        'headers': [
            [b'content-type', b'text/html'],
        ]
    })

    body = b"<HEAD><TITLE>" + text + b"</TITLE></HEAD>" \
           b"<BODY><H1>" + text + b"</H1></BODY>"

    await send({
        'type': 'http.response.body',
        'body': body,
    })
