URL: https://mm2-prod.steelyard.ca/party/invite \
Method: PUT \
Auth: Yes

---

## Comment
Invite player to own party

## Example Request
```json
{
  "recipientPlayerId": "3YRXP4UL3BCT7MM2C7Y5ODS4SU", // PHXL ID
  "partyId": "", // left empty to invite to own party, idk why
  "buildId": "682486_2.1.1_shipping",
  "featureOverrides": [] // purpose unclear, not captured any entries yet
}
```

## Example Response
```json
{} // empty payload on success
```