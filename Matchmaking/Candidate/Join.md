URL: https://mm2-prod.steelyard.ca/candidate/join \
Method: POST \
Auth: Yes

---

## Comment
Create match from ping data and match type.

## Example Request
```json
{
  "buildId": "682486_2.1.1_shipping",
  "gameMode": "ISLAND",
  "gameType": "HUNTING_GROUND",
  "gameArgs": "",
  "regionUrlsPings": {
    "http://us-central1.gce.latency-test.steelyard.ca": [
      0.12675, 0.120229, 0.120232, 0.120236, 0.120244
    ],
    "http://us-west1.gce.latency-test.steelyard.ca": [
      0.166826, 0.155302, 0.155318, 0.155291, 0.155439
    ],
    "http://us-east1.gce.latency-test.steelyard.ca": [
      0.121748, 0.110236, 0.10521, 0.105212, 0.10521
    ],
    "http://europe-west1.gce.latency-test.steelyard.ca": [
      0.0480999, 0.0250453, 0.0250482, 0.0250498, 0.0250389
    ],
    "http://europe-west4.gce.latency-test.steelyard.ca": [
      0.0390845, 0.0200318, 0.0150268, 0.0200428, 0.015035
    ],
    "http://asia-east1.gce.latency-test.steelyard.ca": [
      0.271548, 0.249992, 0.249997, 0.249981, 0.249994
    ],
    "http://australia-southeast1.gce.latency-test.steelyard.ca": [
      0.336688, 0.300078, 0.300093, 0.300082, 0.303085
    ]
  },
  "isPrivate": true,
  "privateMatch": true,
  "playerId": "",
  "partyId": "c6e088cbc9f547778ff13ffea2886f56_NjgyNDg2XzIuMS4xX3NoaXBwaW5n",
  "hunts": ["Adventure_IslandA_D24"],
  "playerHuntId": "ShatteredIsles_IslandA_D24",
  "allow_crossplay": true,
  "session_id": "eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJVMkJMV1ZUREhaR1dMQktLTFkyUUc2VVg0SSIsImlzcyI6ImdhbWVfc2Vzc2lvbl9hcGkiLCJpYXQiOjE3NDUzMTQ5NDksInNlc3Npb24tdXVpZCI6ImM5NGNhN2U1YzczNjRkY2Q4ZDNjODE3NTg5N2Y0MTEwIiwiZGlzcGxheV9uYW1lIjoiQmxcdTAwZmN0ZW5kZSBCbFx1MDBmY3RlIiwicGxhdGZvcm0iOiJ3aW4ifQ.KDD9TdOzgIWIUHFQsh8fQT9CARiS1i469bQrmUFWTdknbvfRN7CC9i3QCkizP5BUZtSODfH1q-YoXvn3ddn7Hg"
}
```

## Example Response
```json
{
  "candidateId": "euw11$e90ae40b8b2d4020b4bda5450c56be82",
  "gameMode": "ISLAND",
  "huntId": null,
  "status": "MATCHING",
  "statusReason": null
}
```