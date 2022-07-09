# ⭐️ 🧪 SampleStar

An internet-accessible API for you to request genuinely random numbers.

This service is backed by hardware devices that use a sample of radioactive material.
The underlying physics of the radioactive material model true randomness (unlike [pseudorandomness](https://en.wikipedia.org/wiki/Pseudorandomness)).

## Usage

```bash
# Request a sequence of random numbers
# 
# Params:
# * requestId:        string (alphanumerics and "_") to identify the request
# * sequenceLength:   requested amount of random numbers returned
# * tag:              string (alphanumerics and "_") with tag/description of
#                     this request
curl --location --request POST 'http://samplestar.thomasvn.dev/api/randomSequence' \
--header 'Content-Type: application/json' \
--data-raw '{
    "requestId" : "req_3",
    "sequenceLength": "3",
    "tag": "thomasvn"
}'

# Query for a previously generated sequence
# 
# Params:
# * sequenceId:   string (alphanumerics and "_") to identify the original
#                 request
curl --location --request POST 'http://samplestar.thomasvn.dev/api/retrieveSequence' \
--header 'Content-Type: application/json' \
--data-raw '{
    "sequenceId": "seq_zGTVFHjUy2PpVVRq"
}'
```

## To Learn More ...

- Assumptions about the [underlying hardware](./doc/ASSUMPTIONS.md)
- Running the [app locally](./app/README.md)
- [API specifications](./doc/API.md)
- [Database specifications](./doc/DATABASE.md)
- Deploying the app to [AWS Elastic Beanstalk](./deploy/README.md)
- List of pros/cons when choosing [deployment method](./deploy/CONSIDERATIONS.md)

## Future Roadmap

- logic to generate/store/validate authentication tokens for paying customers
- upgrade from flat-file database to relational database
- safety guarantees when multiple instances are reading/writing to the same record
- improved monitoring & alerting automation
- deploy app to multiple regions, then multiple clouds
- use DNS to round-robin between all deployments
