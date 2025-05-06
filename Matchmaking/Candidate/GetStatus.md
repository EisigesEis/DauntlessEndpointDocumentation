URL: https://mm2-prod.steelyard.ca/candidate/status \
Method: GET \
Auth: Yes

---

## Comment
Retrieve own party status.

## Example Request
No payload.

## Example Response
Island names before awakening are undocumented. Presented are the base names of huntId. Actual huntId would be extended by the post-fix `_D24` (regular difficulty) or `_heroic` (surge difficulty). For an escalation `gameMode` is `ISLAND`.

| huntId | actual name |
|-|-|
| null | Ramsgate |
| Adventure_IslandA_D24 | Emberthorn Cove |
| Adventure_IslandE | Iron Falls |
| Adventure_IslandG | Aulric's Peak |
| Adventure_IslandN | Undervald Defile |
| Adventure_IslandB | Boreal Outpost |
| Adventure_IslandM | The Snowblind Waste |
| Adventure_IslandL | Coldrunner Key |
| Adventure_IslandO | Cape Fury |
| Adventure_IslandC | Revelation Rock |
| Adventure_IslandK | Brightwood |
| Adventure_IslandF | Sunderstone |
| Adventure_IslandP | Hades Reach |
| Adventure_IslandU | The Blazeworks |
| Adventure_IslandQ | Razorcliff Isle |
| Adventure_IslandR | Twilight's Domain |
| Adventure_IslandT | Conundrum Rocks |
| Adventure_IslandS | The Paradox Breaks |

Escalations have post-fixes `_Easy` (1-13), `_Hard` (10-50), `_Heroic` (51-90). Patrol only has the easy and hard post-fix.
| huntId | actual name |
|-|-|
| CR19_MatchmakerHunt_Escalation_Thunderbird | Shock Escalation |
| CR19_MatchmakerHunt_Escalation_Armstrong | Blaze Escalation |
| CR19_MatchmakerHunt_Escalation_Funguy | Terra Escalation |
| CR19_MatchmakerHunt_Escalation_Randall | Umbral Escalation |
| CR19_MatchmakerHunt_Escalation_Mint | Frost Escalation |
| CR19_MatchmakerHunt_Escalation_Glitter | Radiant Escalation |
| CR19_PlayerHunt_Escalation_Patrol | Escalation Patrol |

Gauntlet: CR19_MatchmakerHunt_Gauntlet into CR19_PlayerHunt_Gauntlet

Trials: and CR19_PlayerHunt_Arena_Elite Arena_MatchmakerHunt_Elite_New_001

### Ramsgate multiple states
```json
{
  "candidateId": "euw11$cb35c40dcd19456e8b894dc22c68494e",
  "candidateStatusPeriodMillis": 10000,
  "gameMode": "CITY",
  "huntId": null,
  "playerStates": {
    "XQBF5VHGFJHR5AUILEPYI55MUQ": {}
  },
  "serverInfo": {
    "buildId": "683165_2.1.1_shipping",
    "gameSessionId": "63dd1692ccf443018381c1715af692d3",
    "host": "34.78.192.2",
    "port": 9468
  },
  "status": "IN_PROGRESS",
  "statusDuration": 0.0,
  "statusReason": null
}
```

### Matched
```json
{
  "candidateId" : "euw11$6bca33ac8e014efc90f1ed09457800b4",
  "candidateStatusPeriodMillis" : 10000,
  "gameMode" : "SHARED",
  "huntId" : "Adventure_IslandE_D24",
  "playerStates" : {
    "XQBF5VHGFJHR5AUILEPYI55MUQ" : {}
  },
  "status" : "MATCHED",
  "statusDuration" : 0.0,
  "statusReason" : null
}
```

### Queued for start
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
  "status": "QUEUED_FOR_START", // QUEUED_FOR_START -> IN_PROGRESS
  "statusDuration": 0.07524657249450684,
  "statusReason": null // no idea what this is used for
}
```

### Cancelled
This one was triggered bc skipped public queue escalation. Game will then start new "private" matchmaking (as in, potentially with other ppl already found). This skip is only possible when `MATCHING` status is active before it.
```json
{
  "candidateId" : "euw11$e9b689e690b24344b1a336a7de07f7d9",
  "candidateStatusPeriodMillis" : 10000,
  "gameMode" : "ISLAND",
  "huntId" : null,
  "playerStates" : {
    "XQBF5VHGFJHR5AUILEPYI55MUQ" : {}
  },
  "status" : "CANCELED",
  "statusDuration" : 9.0,
  "statusReason" : "LEADER_CANCELED"
}
```

### In Progress
Hunt has arrived and you have 30s to enter. If this time expires you will be auto-entered (local logic through game).
```json
{
  "candidateId": "euw11$b2d2413a4bf442698a34bfdbed0d1530",
  "candidateStatusPeriodMillis": 10000,
  "gameMode": "ISLAND",
  "huntId": "Adventure_IslandA_D24",
  "playerStates": {
    "XQBF5VHGFJHR5AUILEPYI55MUQ": {}
  },
  "serverInfo": {
    "buildId": "683165_2.1.1_shipping",
    "gameSessionId": "ef62f6b35b1d4d61b0e524664f4a8abb",
    "host": "34.76.22.246",
    "port": 9024
  },
  "status": "IN_PROGRESS",
  "statusDuration": 1.0,
  "statusReason": null
}
```