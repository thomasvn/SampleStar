# SampleStar (a service that provides genuinely random numbers to users)

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
-->

<!--
TODO:
- STUB APP (generate pseudo-random numbers)
  - ensure that all stubs created are logged and recorded for auditability
  - containerize this stub and make API requests to this stub
  - describe how this stub automatically query from the hardware device (ASSUMPTION) ??
- API DOCS
- add more documentation in the "doc" directory (?)
- KUBERNETES ?
  - AWS EKS for demo
  - enable horizontal scalability
-->

<!--
FUTURE:
- pass an authentication token to the API request
- how do we scale? do we put our hardware device in datacenters across the globe? or do we accept we will always be constrained by internet latency?
-->
