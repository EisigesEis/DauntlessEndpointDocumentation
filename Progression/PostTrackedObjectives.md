URL: https://progression-prod.steelyard.ca/progression/tracked_objectives/{PHXL ID} \
Method: POST \
Auth: Yes

---

## Example Request
```json
{
  "phx_account_id": "XQBF5VHGFJHR5AUILEPYI55MUQ",
  "current_set": "quest_slayer_links", // quest for which progress shows in the quick menu on the right
  "omitted_quests": [],
  "tracked_quests": [
    "C83DE8BA43AFEC86BE2A588BE3F990E8",
    "64AAEADB464D757E1E812AAD4463643F"
  ],
  "tracked_craftables": []
}
```

## Example Response
```json
{
  "code": null,
  "message": "OK",
  "payload": null
}
```