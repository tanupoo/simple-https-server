#!/usr/bin/env python

from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
import ssl
from argparse import ArgumentParser
from argparse import ArgumentDefaultsHelpFormatter

ap = ArgumentParser(
        description="Simple HTTPS server.",
        formatter_class=ArgumentDefaultsHelpFormatter)
ap.add_argument("certfile", help="specify a file name containing "
                "both server cert and private key.")
ap.add_argument("-p", action="store", dest="port", type=int, default=8443,
                help="specify the port number to be listened.")
opt = ap.parse_args()

httpd = ThreadingHTTPServer(("", opt.port), SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket(httpd.socket,
                               certfile=opt.certfile,
                               server_side=True)
print(f"HTTPS server has started on port# {opt.port}.")
httpd.serve_forever()
