URL: https://mm2-prod.steelyard.ca/candidate/status \
Method: GET \
Auth: Yes

---

## Comment
Retrieve own party status.

## Example Request
No payload.

## Example Response
```json
{
  "candidateId": "euw11$e90ae40b8b2d4020b4bda5450c56be82",
  "candidateStatusPeriodMillis": 10000,
  "gameMode": "ISLAND",
  "huntId": "Adventure_IslandA_D24",
  "playerStates": {
    "3YRXP4UL3BCT7MM2C7Y5ODS4SU": {},
    "U2BLWVTDHZGWLBKKLY2QG6UX4I": {}
  },
  "status": "QUEUED_FOR_START", // QUEUED_FOR_START -> MATCHING -> IN_PROGRESS
  "statusDuration": 0.07524657249450684,
  "statusReason": null // no idea what this is used for
}
```