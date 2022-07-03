# ⭐️ 🧪 SampleStar

An internet-accessible API for you to request genuinely random numbers.

This service is backed by hardware devices that use a sample of radioactive material.
The underlying physics of the radioactive material model true randomness (unlike [pseudorandomness](https://en.wikipedia.org/wiki/Pseudorandomness)).

## Usage

```bash
# Request a randomSequence
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

# Query for a previously generated randomSequence
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

<!--
ASSUMPTIONS:
- we can deploy our kubernetes cluster on-prem co-located with our hardware device
- the hardware device is never the bottleneck (near-zero latency for all requests to/from hardware device)
- what is the range of the random numbers ??
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
  - Generate the documentation from the flask app??
  - API
  - DATABASE STRUCTURE
  - https://medium.com/blueriders/python-autogenerated-documentation-3-tools-that-will-help-document-your-project-c6d7623814ef
  - https://www.geeksforgeeks.org/how-to-generate-a-documentation-using-python/
  - https://docs.python.org/3/library/pydoc.html

FUTURE:
- Concurrency
  - Multiple reads/writes to the database at the same moment
- Availability
  - Deploy to multiple regions?
  - DNS to resolve to the hosts within multiple regions?
  - Deploy to multiple clouds?
- Authentication ?
  - API token?
  - what if somebody tries to use an ID which already belongs to another customer?
  - how long should IDs be made available for?
- Describe how the program will query the hardware device ??
- how do we scale? do we put our hardware device in datacenters across the globe? or do we accept we will always be constrained by internet latency?
- Error codes if network requests from API to hardware don't work
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
