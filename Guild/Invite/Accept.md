URL: https://guild-prod.steelyard.ca/guild/invite/accept/{Invite ID} \
Method: POST \
Auth: Yes

---

## Comment
Accept guild invite.

## Example Request
No payload.

## Example Response
### Invalid invite id
```json
{
  "code": "UninvitedAdorableQuillshot",
  "message": "Guild invitation {Invite ID} not found.",
  "payload": null
}
```

### Valid invite
Same as [GetOwnGuild](../GetOwnGuild.md)
````json
{
  "code": null,
  "message": "OK",
  "payload": {
    "created_date": "2025-04-22T10:04:07",
    "id": "e7e1fe22-a613-4f18-bd83-621fbb48fb04",
    "last_modified_date": "2025-04-22T10:04:07",
    "leader_account_id": "3YRXP4UL3BCT7MM2C7Y5ODS4SU",
    "maximum_guild_members": 100,
    "members": [
      {
        "joined_date": "2025-04-22T10:05:40",
        "last_modified_date": "2025-04-22T10:05:40",
        "phx_account_id": "3YRXP4UL3BCT7MM2C7Y5ODS4SU",
        "rank": "leader"
      },
      {
        "joined_date": "2025-04-22T10:08:59",
        "last_modified_date": "2025-04-22T10:08:59",
        "phx_account_id": "U2BLWVTDHZGWLBKKLY2QG6UX4I",
        "rank": "member"
      }
    ],
    "name": "Flowery",
    "nameplate": "FLOWRY"
  }
}
```
