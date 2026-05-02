# Project Setup and Usage

This repository depends heavily on:

- https://github.com/cloudflarearchive/odoh-server-go
- https://github.com/cloudflare/odoh-client-go

The project idea is based on this issue:

- https://github.com/cloudflarearchive/odoh-server-go/issues/30

## Requirements

Install the following packages:

- Go
- mkcert
- Python
- Flask
- Docker / Docker Compose

## Setup

In the `server-docker` directory, generate a random binary file:

```bash
dd if=/dev/urandom of=./random.bin bs=1M count=100 status=progress
```
Redirect Test

Use the redirect Docker Compose file:

mv redirect-compose.yml docker-compose.yml
docker compose up

Send a POST request through the proxy:

curl -X POST -k -v \
  -d '{"a":"b"}' \
  "https://localhost:4567/proxy?targethost=mylocal:8081&targetpath=/loopA"

Access the private endpoint through the proxy:

curl -X POST -k \
  -d '{"a":"b"}' \
  "https://localhost:4567/proxy?targethost=mylocal:8081&targetpath=/secret"

Access the private endpoint directly:

curl -X POST -k "https://mylocal:8081/secret"
Memory Overflow Test

Use the memory test Docker Compose file:

mv mem-compose.yml docker-compose.yml
docker compose up

Then run the Python client:

python client.py



This repo depends heavily on https://github.com/cloudflarearchive/odoh-server-go?tab=readme-ov-file and https://github.com/cloudflare/odoh-client-go?tab=readme-ov-file,
and the idea is from https://github.com/cloudflarearchive/odoh-server-go/issues/30

Needed packages:
golang, mkcert, python, Flask

Set up:
run dd if=/dev/urandom of=./random.bin bs=1M count=100 status=progres in server-docker directory

redirect:
use the redirect compose.yml file
curl -X POST -k -v -d '{"a":"b"}' "https://localhost:4567/proxy?targethost=mylocal:8081&targetpath=/loopA"
access private data
curl -X POST -k -d '{"a":"b"}' "https://localhost:4567/proxy?targethost=mylocal:8081&targetpath=/secret"
curl -X POST -k "https://mylocal:8081/secret"

mem overflow:
default to 500MB
mv mem-compose.yml docker-compose.yml and run python client.py 
