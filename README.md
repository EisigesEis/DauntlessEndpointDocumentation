# DauntlessEndpointDocumentation

## Legal
The documentation provided is intended solely for academic and informational purposes. Any unauthorized use, modification, or distribution of the information contained herein may violate legal and contractual obligations. Users are advised to review Phoenix Labs' EULA regarding data mining and other prohibited activities.

## Getting started
Please read the [authentication guide](./Login/README.md).

## Contributing
Any suggestion about restructuring or adding new requests which I have missed is welcome.

Any traffic capture from when an event was ongoing would be very interesting. I missed out on that.

A big milestone will be to decrypt their UDP traffic, which will pave the way for group play or servers. It may also cover gauntlet leaderboard as well as which trial behemoth and gauntlet season is active.
On every server instance the game joins (ramsgate, an island, training grounds, etc.) it establishes a UE Bunch channel which is encrypted presumably using [the key that was shared](./Matchmaking/Key/Generate.md). I have yet to figure out which encryption mode was used.
Another promising approach is to activate debugging console/files. Looking at the string dump of the game, they have a lot of debugging symbols which also include some UDP debugging. I've already tried launching with `-Log` to no avail.