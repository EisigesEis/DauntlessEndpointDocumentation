URL: https://login-queue-prod.steelyard.ca/login \
Method: POST \
Auth Required: Yes (Access Token)

---

## Comment
Called by the game after retrieving Access Token and before retrieving the Session Token.

## Example Request
```json
{
  "email": "05e64c3790334d6f835dc4ef9d45bfda",
  "env": "prod",
  "lang": "en"
}
```

## Example Response
```json
{
  "error_code": "TicketRateOk",
  "message": "",
  "state": "OPEN",
  "timeout": 8000,
  "title": ""
}
```