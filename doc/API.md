# SampleStar API Documentation

## POST /api/randomSequence

```python
"""Request a new sequence of random numbers or an existing `sequenceId`.

Params:
* requestId:        string (alphanumerics and "_") to identify the request
* sequenceLength:   requested amount of random numbers returned
* tag:              string (alphanumerics and "_") with tag/description of 
                    this request

Response:
If the `requestId` received already exists, this response will have empty
fields except for the `sequenceId`.
{
    'dateProcessed': '',
    'randomSequence': [float],
    'request': {
        'requestId': '',
        'sequenceLength': '',
        'tag': ''
    },
    'sequenceId': ''
}

200: Ok
400: Bad Request. Invalid input

"""
```

```bash
# Example
curl --location --request POST 'http://samplestar.thomasvn.dev/api/randomSequence' \
--header 'Content-Type: application/json' \
--data-raw '{
    "requestId" : "req_3",
    "sequenceLength": "3",
    "tag": "thomasvn"
}'
```

## POST /api/retrieveSequence

```bash
"""Given a sequenceId, show the sequence and original request & reponse.

Params:
* sequenceId:   string (alphanumerics and "_") to identify the original
                request

Response:
{
    'dateProcessed': '',
    'randomSequence': [float],
    'request': {
        'requestId': '',
        'sequenceLength': '',
        'tag': ''
    },
    'sequenceId': ''
}

200: Ok
400: Bad Request. Invalid Input
404: Not Found. Requested resource (`sequenceId`) doesn't exist

"""
```

```bash
# Example
curl --location --request POST 'http://samplestar.thomasvn.dev/api/retrieveSequence' \
--header 'Content-Type: application/json' \
--data-raw '{
    "sequenceId": "seq_FsE2h1RJ04NHrN5N"
}'
```
