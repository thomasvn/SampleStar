# SampleStar Application Stub

NOTE.
This code is a temporary stub.
Our developers are hard at work building the real application which queries our innovative hardware device with near-zero latency.

This stub will provide the same [API specifications](../doc/API.md) as the real app.
However this stub only generates pseudo-random numbers.

The API handlers were built using Flask App (python).
The database is currently a shared filesystem where each worker will read/write to this filesystem.
Gunicorn on Nginx is used as the web server.

## Run this app locally

```bash
# Setup tooling
python3 -m venv .venv
source .venv/bin/activate
pip3 install flask

# Build & run
export FLASK_APP=application.py
export FLASK_ENV=development
flask run
```

## Testing the API

For more details, visit the [API Doc](../doc/API.md)

```bash
# Request a sequence of random numbers
curl --location --request POST 'http://localhost:5000/api/randomSequence' \
--header 'Content-Type: application/json' \
--data-raw '{
    "requestId" : "req_3",
    "sequenceLength": "3",
    "tag": "thomasvn"
}'

# Query for a previously generated sequence
curl --location --request POST 'http://localhost:5000/api/retrieveSequence' \
--header 'Content-Type: application/json' \
--data-raw '{
    "sequenceId": "seq_FsE2h1RJ04NHrN5N"
}'
```

## References

- Python
  - <https://docs.python-guide.org/writing/structure/#modules>
  - <https://stackoverflow.com/questions/19201290/how-to-save-a-dictionary-to-a-file>
