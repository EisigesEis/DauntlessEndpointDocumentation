URL: https://mm2-prod.steelyard.ca/party \
Method: POST \
Auth: Yes

---

## Comment
Retrieve own party status.

## Example Request
```json
{
  "buildId": "682486_2.1.1_shipping", // no checks in place, can create for arbitrary versioning a party
  "featureOverrides": [] // purpose unclear, not captured any entries yet
}
```

### invalid buildId and no profile patch
```json
{   "buildId" : "1.1.1_shipping",   "featureOverrides" : []}
```

## Example Response
`playerHuntId` as described in [GetStatus](./Candidate/GetStatus.md).

### Ramsgate hunt arrived
```json
{
  "candidateId": "euw11$413508d7ba0d4fafa43d8301887609fc",
  "candidateState": "IN_PROGRESS", // QUEUED_FOR_START -> MATCHING -> IN_PROGRESS
  "gauntletLevel": null,
  "leaderPlayerId": "U2BLWVTDHZGWLBKKLY2QG6UX4I",
  "partyId": "34cda5fce86d48fca6cdd78956cf244e_NjgyNDg2XzIuMS4xX3NoaXBwaW5n",
  "playerHuntId": "ShatteredIsles_ReturnToRamsgate",
  "playerStates": [
    {
      "consoleSessionId": null,
      "displayName": "Bl\u00fctende Bl\u00fcte",
      "isMemberOfCandidate": true, // true when creator is also lead?
      "platform": "win",
      "playerId": "U2BLWVTDHZGWLBKKLY2QG6UX4I"
    },
    {
      "consoleSessionId": null,
      "displayName": "Lee Roy Jenk\u00eens",
      "isMemberOfCandidate": false,
      "platform": "win",
      "playerId": "3YRXP4UL3BCT7MM2C7Y5ODS4SU"
    }
  ]
}
```

### Gauntlet
```json
{
  "candidateId": "euw11$a4f038c54f724ed8800e3922e3a71128",
  "candidateState": "QUEUED_FOR_START",
  "gauntletLevel": 180000781, // Supposed format of this number: `Season`0000`LeveL`
  "leaderPlayerId": "XQBF5VHGFJHR5AUILEPYI55MUQ",
  "partyId": "ac947aabb95a4a96b5641718f0fd19f8_NjgyNDg2XzIuMS4xX3NoaXBwaW5n",
  "playerHuntId": "CR19_PlayerHunt_Gauntlet",
  "playerStates": [
    {
      "consoleSessionId": null,
      "displayName": "Bärtiger Bär",
      "isMemberOfCandidate": true,
      "platform": "win",
      "playerId": "XQBF5VHGFJHR5AUILEPYI55MUQ"
    }
  ]
}
```

### invalid buildId and no profile patch
```json
{
  "candidateId": null,
  "candidateState": null,
  "leaderPlayerId": "U2BLWVTDHZGWLBKKLY2QG6UX4I",
  "partyId": "d2ae0138f178424b8584ecb633c56cce_MS4xLjFfc2hpcHBpbmc=",
  "playerHuntId": null,
  "playerStates": [
    {
      "consoleSessionId": null,
      "displayName": null,
      "isMemberOfCandidate": false,
      "platform": null,
      "playerId": "U2BLWVTDHZGWLBKKLY2QG6UX4I"
    }
  ]
}
```