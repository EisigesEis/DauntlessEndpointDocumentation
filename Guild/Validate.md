URL: https://guild-prod.steelyard.ca/guild/validate \
Method: POST \
Auth: Yes

---

## Comment
Game checks for availability of guild name/nameplate.
I'm assuming this creates a guild on valid? Couldn't find explicit request that creates the guild.

## Example Request
```json
{
  "leader_account_id": "U2BLWVTDHZGWLBKKLY2QG6UX4I",
  "name": "Flowery",
  "nameplate": "FLOWRY"
}
```

## Example Response
### name used
409 Conflict
```json
{
  "code": "SeizedAdorableQuillshot",
  "message": "Guild name {name} is already in use.",
  "payload": null
}
```

### invalid characters in name
400 Bad Request
```json
{
  "code": "ObedientAdorableQuillshot",
  "message": "Guild name must contain 4-15 english letters and digits.",
  "payload": null
}
```

### invalid length of nameplate
400 Bad Request
```json
{
  "code": "DutifulAdorableQuillshot",
  "message": "Guild nameplate must contain 2-6 english letters and digits.",
  "payload": null
}
```

### name 6 letters in a row
400 Bad Request
```json
{
  "code": "LetteredAdorableQuillshot",
  "message": "Guild name may not contain more than 6 of the same letter in a row.",
  "payload": null
}
```

### nameplate used
409 Conflict
```json
{
  "code": "CapturedAdorableQuillshot",
  "message": "Guild nameplate {nameplate} is already in use.",
  "payload": null
}
```

### both valid
```json
{ "code": null, "message": "OK", "payload": {} }
```