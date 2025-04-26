URL: https://social-prod.steelyard.ca/slayerlink/invite \
Method: PUT \
Auth: Yes

---

## Comment
Called when inviting or cancelling a slayer link.

## Example Request
```json
{
  "account_id": "XQBF5VHGFJHR5AUILEPYI55MUQ", // PHXL ID
  "slot": 1, // slots 1-3
  "action": "cancel", // not present => defaults to invite.
  "action_source": "social_panel" // seen so far: social_panel, dedicated_screen
}
```

## Example Response
```json
{
  "code": null,
  "message": "OK",
  "payload": { "link_id": "a81143be-6261-4251-9825-7d27fef0ef9f" }
}
```