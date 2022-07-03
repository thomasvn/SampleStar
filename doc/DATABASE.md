# Database Schema

Currently, this app uses flat files on a shared filesystem as its database.
This will very soon need to be transitioned to a relational database.

## Index

An index of all existing requestIds is maintained in the `requestId_to_sequenceId.json`.
An example is shown below:

```json
{
    "req_6": "seq_SvipSCJCeucbzQfl",
    "req_3": "seq_FsE2h1RJ04NHrN5N"
}
```

## Sequences

Each sequence gets its own `json` file named by its sequence ID.
To check the existence of a sequence given a sequenceId, we simply need to check if a file exists corresponding to the sequenceId!
An example of a sequence's `json` file is shown below:

```json
// seq_FsE2h1RJ04NHrN5N.json
{
    "dateProcessed": "2022-07-03 12:12:46.053940",
    "randomSequence": [
        0.9202063689921551,
        0.7361624161854777,
        0.8565393713911911
    ],
    "request": {
        "requestId": "req_3",
        "sequenceLength": "3",
        "tag": "thomasvn"
    },
    "sequenceId": "seq_FsE2h1RJ04NHrN5N"
}
```
