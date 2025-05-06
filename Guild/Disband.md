URL: https://guild-prod.steelyard.ca/guild/{Guild ID} \
Method: DELETE \
Auth: Yes

---

## Comment
Disband guild.

## Example Request
No payload.

## Example Response
### not member of guild
```json
{
  "code": "ExcludedAdorableQuillshot",
  "message": "Account U2BLWVTDHZGWLBKKLY2QG6UX4I is not in guild e7e1fe22-a613-4f18-bd83-621fbb48fb04.",
  "payload": null
}
```

### disband without leader role
```json
{
  "code": "SlyAdorableQuillshot",
  "message": "Insufficient guild privileges.",
  "payload": null
}
```

### success
```json
{ "code": null, "message": "OK", "payload": {} }
```