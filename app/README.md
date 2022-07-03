# SampleStar Application Stub

NOTE.
This code is a temporary stub in place of the real application.
Our developers are hard at work building an application to query our innovative hardware device with near-zero latency.

This code is a Flask App that provides the same API specifications as the real application, but only serves pseudo-random numbers to the users.

## Local Setup

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
# Request a randomSequence
curl --location --request POST 'http://localhost:5000/api/randomSequence' \
--header 'Content-Type: application/json' \
--data-raw '{
    "requestId" : "req_3",
    "sequenceLength": "3",
    "tag": "thomasvn"
}'

# Query for a previously generated randomSequence
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
