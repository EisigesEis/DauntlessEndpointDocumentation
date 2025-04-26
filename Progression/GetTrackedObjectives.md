URL: https://progression-prod.steelyard.ca/progression/tracked_objectives/{PHXL ID} \
Method: GET \
Auth: Yes

---

## Comment
Get progression for tracked objectives.

## Example Request
No payload.

## Example Response
````json
{
  "code": null,
  "message": "OK",
  "payload": {
    "current_set": "D24_A_MAIN_03",
    "omitted_quests": [], // no recorded request with data here
    "phx_account_id": "U2BLWVTDHZGWLBKKLY2QG6UX4I",
    "tracked_craftables": [], // no recorded request with data here
    "tracked_quests": [] // no recorded request with data here
  }
}
```