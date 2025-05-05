URL: https://guild-prod.steelyard.ca/guild/invite/{PHXL ID} \
Method: PUT \
Auth: Yes

---

## Comment
Invite player to guild.

## Example Request
No payload.

## Example Response
### invite without inviter guild membership
```json
{
  "code": "ExcludedAdorableQuillshot",
  "message": "Account U2BLWVTDHZGWLBKKLY2QG6UX4I is not in a guild.", // own phxl id
  "payload": null
}
```

### invite as member
```json
{
  "code": "SlyAdorableQuillshot",
  "message": "Insufficient guild privileges.",
  "payload": null
}
```

### full guild
```json
{
  "code": "StuffedAdorableQuillshot",
  "message": "Guild 2422b73b-0138-4117-8ea2-e9a4c2c16775 is full.",
  "payload": null
}
```

### invite self
```json
{
  "code": "ClonedAdorableQuillshot",
  "message": "Account XQBF5VHGFJHR5AUILEPYI55MUQ is already in guild 439fdb55-b311-4f96-a8ca-bec688e00ca2.",
  "payload": null
}
```

### invite again
```json
{
  "code": "RedundantAdorableQuillshot",
  "message": "Account U2BLWVTDHZGWLBKKLY2QG6UX4I is already invited to guild 439fdb55-b311-4f96-a8ca-bec688e00ca2.",
  "payload": null
}
```

### all good
```json
{
  "code": null,
  "message": "OK",
  "payload": {
    "guild": "e7e1fe22-a613-4f18-bd83-621fbb48fb04",
    "id": "92297ac1-95a4-466e-988e-048c8cf7b8ff",
    "invite_date": "2025-04-22T10:04:17.250453+00:00",
    "inviter_account_id": "U2BLWVTDHZGWLBKKLY2QG6UX4I",
    "phx_account_id": "3YRXP4UL3BCT7MM2C7Y5ODS4SU"
  }
}
```