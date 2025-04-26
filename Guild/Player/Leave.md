URL: https://guild-prod.steelyard.ca/guild/player \
Method: DELETE \
Auth: Yes

---

## Comment
Leave own guild.

## Example Request
No payload.

## Example Response
```json
{ "code": null, "message": "OK", "payload": {} }
```

```json
{
  "code": "ExcludedAdorableQuillshot",
  "message": "Account U2BLWVTDHZGWLBKKLY2QG6UX4I is not in a guild.",
  "payload": null
}
```

```json
{
  "code": "ChiefAdorableQuillshot",
  "message": "Guild leader cannot leave the guild. Use /guild/rank to change leaders.",
  "payload": null
}
```