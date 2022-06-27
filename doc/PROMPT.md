# DevOps SWE Take Home Challenge

> Take as long as you like, but if you’re going to take longer than a week, please let us know.

> Use any technology stack you like, and deliver the specification in any form you like.

> Feel free to choose a focus area if you feel it will better showcase your skills.

## Introduction

We have developed a hardware device that uses a sample of radioactive material to generate genuinely random sequences of numbers, permutations, and selections.
We intend to deliver these random sequences through an internet api to high-value customers such as online casinos, national lottery operators and the like.
The idea is that players will not have to trust the gaming operator, they need only trust us (and we have no interest in the game’s outcome).

## Functional requirements:

- A paying customer will request a number (or a sequence of numbers) from us, specifying the numbers they require, a tag to identify the sequence, and the ID of their previous response. The service will respond with either:
  - If the previous ID has not already been used: A new sequence of numbers, with date, time, tag, ID, and enough metadata to identify the hardware generators used to create the sequence;
  - Otherwise: the ID of the previously-issued sequence
- Anybody may request a repeat of a sequence, by quoting its ID. The response will include the original request, and the original response. (A user may inspect this to validate the game operator is being honest).

## Non-functional requirements:

- We require eight-nines availability. This service will be used by some high-visibility, and very prestigious games;
- 100% audit-ability. If we ever issue a response, we should be capable of reissuing it.

## Your task:

We’d like you to design and specify the system used to deliver this. You may assume you have a development team available for any custom software and hardware, but you will be responsible for constructing and maintaining the system.
