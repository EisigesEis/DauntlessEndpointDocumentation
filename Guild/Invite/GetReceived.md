URL: https://guild-prod.steelyard.ca/guild/invite/player \
Method: GET \
Auth: Yes

---

## Comment
Check received guild invitations

## Example Request
Default headers, no payload.

## Example Response
### No Invites
```json
{ "code": null, "message": "OK", "payload": { "invites": [] } }
```

### Invites
```json
{
  "code": null,
  "message": "OK",
  "payload": {
    "invites": [
      {
        "guild_id": "e7e1fe22-a613-4f18-bd83-621fbb48fb04",
        "guild_name": "Flowery",
        "id": "4f129432-fbdd-4f95-88b1-10f18808de18",
        "invite_date": "2025-04-22T10:08:33",
        "inviter_account_id": "3YRXP4UL3BCT7MM2C7Y5ODS4SU"
      }
    ]
  }
}
```