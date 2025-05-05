URL: https://gauntlet-prod.steelyard.ca/progression/level_access/gauntlet-season{season number}?account_id={PHXL ID} \
Method: GET \
Auth: No

---

## Example Request
No payload.

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