# DauntlessEndpointDocumentation

## Legal
The documentation provided is intended solely for academic and informational purposes. Any unauthorized use, modification, or distribution of the information contained herein may violate legal and contractual obligations. Users are advised to review Phoenix Labs' EULA regarding data mining and other prohibited activities.

## Getting started
Please read the [authentication guide](./Login/README.md).

## Contributing
Any suggestions about restructuring or adding new requests which have been missed are welcome.

A traffic capture from when an event was ongoing would be very interesting.

A big milestone will be to decrypt UDP traffic, which will pave the way for group play or servers. It may also cover gauntlet leaderboard as well as which trial behemoth and gauntlet season is active.
On every server instance the game joins (ramsgate, an island, training grounds, etc.) it establishes a UE Bunch channel which is encrypted presumably using [the key that was shared](./Matchmaking/Key/Generate.md). The encryption algorithm used is unknown so far.
Another promising approach is to activate debugging console/files. Looking at the string dump of the game, the game has a lot of debugging symbols which also include some UDP debugging. Launching with `-Log` does not work.
