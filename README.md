Simple HTTPS Server
===================

Required Python 3.7 or later.
This is because ThreadingHTTPServer is used.

## Usage

```
usage: simple-https-server.py [-h] [-p PORT] certfile

Simple HTTPS server.

positional arguments:
  certfile    specify a file name containing both server cert and private key.

optional arguments:
  -h, --help  show this help message and exit
  -p PORT     specify the port number to be listened. (default: 8443)
```

