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

## Create self-signed certificate and key

```
openssl req -x509 -newkey rsa:4096 -keyout certkey.pem -out certkey.pem -sha256 -days 3650 -nodes -subj "/C=Internet/ST=StateName/L=CityName/O=CompanyName/OU=CompanySectionName/CN=CommonNameOrHostname"
```
