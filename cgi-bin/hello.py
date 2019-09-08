#!/usr/bin/env python3
import html
from os import environ
from urllib.parse import parse_qs

qs = parse_qs(environ.get("QUERY_STRING"))
name = qs.get("name", ["World"])
text = html.escape("Hello, {}!".format(name[0]))

print("Content-Type: text/html")
print()
print("<HTML>")
print("<HEAD><TITLE>{}</TITLE></HEAD>".format(text))
print("<BODY><H1>{}</H1></BODY>".format(text))
print("</HTML>")
