URL: https://mm2-prod.steelyard.ca/party \
Method: POST \
Auth: Yes

---

## Comment
Retrieve own party status.

## Example Request
```json
{
  "buildId": "682486_2.1.1_shipping", "featureOverrides": [] // purpose unclear, not captured any entries yet
}
```

## Example Response
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