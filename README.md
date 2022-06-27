# SampleStar

An internet-accessible API for you to request genuinely random numbers.

This service is backed by hardware devices that use a sample of radioactive material.
This underlying physics of the radioactivity models true randomness (unlike [pseudorandomness](https://en.wikipedia.org/wiki/Pseudorandomness)).

## Usage

These genuinely random numbers can be queried from our service over internet api.

```bash
curl -k -X GET http://nuclear-unicorns.kubernetes.aws.com
    -d '{}'
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
-->

<!--
TODO:
- STUB APP (generate pseudo-random numbers)
  - ensure that all stubs created are logged and recorded for auditability
  - input sanitization
  - containerize this stub and make API requests to this stub
  - describe how this stub automatically query from the hardware device (ASSUMPTION) ??
- PRODUCTION DEPLOY
  - This should not use `flask run`. May require a legitimate HTTP server
  - https://flask.palletsprojects.com/en/2.1.x/deploying/
  - https://www.fullstackpython.com/wsgi-servers.html
- DOCUMENTATION
  - API
  - DATABASE STRUCTURE
- AVAILABILITY ?
  - Deploy to multiple regions?
- KUBERNETES ?
  - AWS EKS for demo
  - enable horizontal scalability
- AUTHENTICATION ?
  - API token?
  - what if somebody tries to use an ID which already belongs to another customer?
  - how long should IDs be made available for?

FUTURE:
- how do we scale? do we put our hardware device in datacenters across the globe? or do we accept we will always be constrained by internet latency?
-->

<!--
DONE:
- Generate initial documentation describing the (1) assumptions, (2) example usage criteria by the user, and (3) concept of operations
- Give the project a fun & memorable name (SampleStar)
- Begin coding the API in Flask (python). This will act as a "stub" since it can only generate pseudo-random numbers.
-->
