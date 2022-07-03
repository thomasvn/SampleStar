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
    "sequenceId": "seq_FsE2h1RJ04NHrN5N"
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

<!--
ASSUMPTIONS:
- we can deploy our kubernetes cluster on-prem co-located with our hardware device
- the hardware device is never the bottleneck (near-zero latency for all requests to/from hardware device)
- what is the range of the random numbers ??
- Describe how the program will query the hardware device ??
- how do we scale? do we put our hardware device in datacenters across the globe? or do we accept we will always be constrained by internet latency?
- Error codes if network requests from API to hardware don't work
-->

<!--
FURTHER CONSIDERATION:
- this demo presents random numbers bounded by INT_MIN and INT_MAX in python
  - https://stackoverflow.com/questions/7604966/maximum-and-minimum-values-for-ints
- choice of Flask (over Django)
- choice of deployment method
- Usage of POST over GET
  - https://stackoverflow.com/questions/46585/when-do-you-use-post-and-when-do-you-use-get
- HTTP Params vs Header vs Body
  - https://stackoverflow.com/questions/51429617/http-requests-body-vs-param-vs-headers-vs-data
- Database. Not my strength. Opted for simplicity of flat files. However, this method is bounded by the speed of File I/O. In the future we would want to build something much more robust.
- Logging how often this sequenceId was accessed? Thought about it. But realized it would add more bloat and more I/O ops. Benefits didn't necessarily outweight the costs.
-->

<!--
TODO:
- Documentation
  - API
  - DATABASE STRUCTURE
-->

<!--
DONE:
- Generate initial documentation describing the (1) assumptions, (2) example usage criteria by the user, and (3) concept of operations
- Give the project a fun & memorable name (SampleStar)
- Begin coding the API in Flask (python). This will act as a "stub" since it can only generate pseudo-random numbers.
- Flat file database setup
- Code for both "/api/randomSequence" and "/api/retrieveSequence".
- Input validation and error codes
- Successfully deploy to Elastic Beanstalk
- Elastic FileSystem acting as database
- Architecture Diagrams
-->
