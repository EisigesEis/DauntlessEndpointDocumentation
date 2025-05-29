URL: https://gauntlet-prod.steelyard.ca/progression/level_access/gauntlet-season{season number}?account_id={PHXL ID} \
Method: GET \
Auth: Yes

---

## Example Request
No payload. If in a party, will iteratively ask, adding one party member at a time. So, `?account_id={PHXL ID1}` then `?account_id={PHXL ID1}&account_id={PHXL_ID2}` and `?account_id={PHXL ID1}&account_id={PHXL_ID2}&account_id={PHXL_ID3}`. PHXL_ID1 will always have to be your own.

## Example Response
```json
{
  "code": null,
  "message": "OK",
  "payload": 1 // ranges from 1 to final level+1
}
```

for some reason the game sometimes sends this without auth
```json
{
  "code": "MajesticAdorableGnasher",
  "message": "Missing Authorization header",
  "payload": null
}
```

### invalid character in acc id
`gauntlet-season18?account_id=ßßß` results in `500 Internal Server Error` with:
```json
{
  "code": null,
  "message": "Internal Server Error",
  "payload": null
}
```

### multiple times same acc id
You can even search for access for yourself multiple times `?account_id=XQBF5VHGFJHR5AUILEPYI55MUQ&account_id=XQBF5VHGFJHR5AUILEPYI55MUQ`. I'm not sure if this does individual db searches. You will reach `400 Bad Request` with `Request Line is too large (4578 > 4094)` once you look up too many times.

### one account id empty
`?account_id=&account_id=XQBF5VHGFJHR5AUILEPYI55MUQ`
Request takes fairly long to process (presumably searching a lot for that id) then concludes the invalid id doesn't have any gauntlet progress.
```json
{
  "code": null,
  "message": "OK",
  "payload": 1
}
```

### no ? and no acc ids lookup
204 No Content

### invalid season or acc id
`gauntlet_season0?account_id=0`
```json
{
  "code": "CasualShaggyAlyra",
  "message": "Forbidden",
  "payload": null
}
```