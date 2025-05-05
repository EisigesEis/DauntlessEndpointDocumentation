URL: https://guild-prod.steelyard.ca/guild/invite/guild \
Method: GET \
Auth: Yes

---

## Comment
Check sent invitations by guild.

## Example Request
Default headers, no payload.

## Example Response
### Check invites as member
```json
{
  "code": "SlyAdorableQuillshot",
  "message": "Insufficient guild privileges.",
  "payload": null
}
```

### no invites
```json
{
  "code": null,
  "message": "OK",
  "payload": {
    "guild_id": "439fdb55-b311-4f96-a8ca-bec688e00ca2",
    "invites": []
  }
}
```

### invites
```json
{
  "code": null,
  "message": "OK",
  "payload": {
    "guild_id": "439fdb55-b311-4f96-a8ca-bec688e00ca2",
    "invites": [
      {
        "id": "1f00bc90-bd55-4b1d-aacc-81eeea672f1f",
        "invite_date": "2025-05-05T11:42:10",
        "inviter_account_id": "U2BLWVTDHZGWLBKKLY2QG6UX4I",
        "phx_account_id": "3YRXP4UL3BCT7MM2C7Y5ODS4SU"
      }
    ]
  }
}
```