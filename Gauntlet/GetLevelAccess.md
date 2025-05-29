URL: https://gauntlet-prod.steelyard.ca/progression/level_access/gauntlet-season{season number}?account_id={PHXL ID} \
Method: GET \
Auth: No

---

## Example Request
No payload. If in a party, will iteratively ask, adding one party member at a time. So, `?account_id={PHXL ID1}` then `?account_id={PHXL ID1}&account_id={PHXL_ID2}` and `?account_id={PHXL ID1}&account_id={PHXL_ID2}&account_id={PHXL_ID3}`.

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