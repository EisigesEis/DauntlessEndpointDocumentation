URL: https://social-prod.steelyard.ca/slayerlink/availability \
Method: POST \
Auth: Yes

---

## Comment
Called to check availability of friends to slayer link.

## Example Request
```json
{
  "account_ids": [
    "XQBF5VHGFJHR5AUILEPYI55MUQ" // array of PHXL IDs
  ]
}
```

## Example Response
```json
{
  "code": null,
  "message": "OK",
  "payload": {
    "availability": [
      { "account_id": "XQBF5VHGFJHR5AUILEPYI55MUQ", "available": true } // available if other dude has slot
    ]
  }
}
```