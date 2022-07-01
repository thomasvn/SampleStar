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

# Create directory for flat-file database
mkdir db

# Build & run
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

## Testing the API

```bash
# Request a new sequence of random numbers or an existing `sequenceId`.
# 
# Params:
# * requestId:        alphanumeric-only string to identify the request
# * sequenceLength:   requested amount of random numbers returned
# * tag:              a tag/description of this request
# 
# Response:
# If the `requestId` received already exists, this response will have empty
# fields except for the `sequenceId`.
# {
#     'dateProcessed': '',
#     'randomSequence': [float],
#     'request': {
#         'requestId': '',
#         'sequenceLength': '',
#         'tag': ''
#     },
#     'sequenceId': ''
# }
curl --location --request POST 'http://localhost:5000/api/randomSequence?requestId=req_0&sequenceLength=6&tag=thomasvn'

# Given a sequenceId, show the sequence and original request & reponse.
# 
# Params:
# * sequenceId:   alphanumeric-only string to identify the original request
# 
# Response:
# If the `sequenceId` received does not exist this response will have empty
# fields.
# {
#     'dateProcessed': '',
#     'randomSequence': [float],
#     'request': {
#         'requestId': '',
#         'sequenceLength': '',
#         'tag': ''
#     },
#     'sequenceId': ''
# }
curl --location --request POST 'http://localhost:5000/api/retrieveSequence?sequenceId=ss_seq_1234'
```

## Container Setup

## References

- Python
  - <https://docs.python-guide.org/writing/structure/#modules>
  - <https://stackoverflow.com/questions/19201290/how-to-save-a-dictionary-to-a-file>
