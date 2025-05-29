URL: https://api.epicgames.dev/epic/oauth/v2/tokenInfo \
Method: POST \
Auth: Yes (EOS)

---

## Comment
Game asks for validity and expiration through this url.

## Example Request
```
token=REDACTED
```

## Exmaple Response
```json
{
  "active": true,
  "scope": "basic_profile friends_list country openid presence",
  "token_type": "bearer",
  "expires_in": 7199,
  "expires_at": "2025-05-29T22:06:32.167Z",
  "account_id": "REDACTED", // egs acc id
  "client_id": "12c4279862ab4460a25c2e9fa535fb7e",
  "application_id": "fghi4567rNJHv9pNoyczQXo6DDJ6RDeq"
}
```