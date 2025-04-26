URL: https://guild-prod.steelyard.ca/guild/rank/{PHYL ID}/{rank} \
Method: PUT \
Auth: Yes

---

## Comment
Set rank of a member.

Possible ranks are: `member`, `officer`, `leader`

Invalid rank section gives insight to valid ranks.

## Example Request
No payload.

## Example Response
### Not in a guild
```json
{
  "code": "ExcludedAdorableQuillshot",
  "message": "Account {PHXL ID} is not in a guild.",
  "payload": null
}
```

### Invalid rank
```json
{
  "code": "DocileAdorableQuillshot",
  "message": "Invalid rank {rank}. Valid values are [{'leader': ['members.view', 'members.update', 'members.delete', 'invites.view', 'invites.create', 'invites.delete', 'guild.delete'], 'officer': ['members.view', 'invites.view', 'invites.create', 'invites.delete', 'members.delete'], 'member': ['members.view']}].",
  "payload": null
}
```

### No auth
```json
{
  "code": "MajesticAdorableGnasher",
  "message": "Missing Authorization header",
  "payload": null
}
```

### In guild as leader, valid rank
```json
{
  "code": null,
  "message": "OK",
  "payload": {
    "guild": "e7e1fe22-a613-4f18-bd83-621fbb48fb04",
    "joined_date": "2025-04-22T10:05:40",
    "last_modified_date": "2025-04-22T10:05:40",
    "phx_account_id": "3YRXP4UL3BCT7MM2C7Y5ODS4SU",
    "rank": "officer"
  }
}
```