URL: https://account-public-service-prod03.ol.epicgames.com/account/api/oauth/verify \
Method: GET \
Auth: Yes (EOS)

---

## Comment
Yet another tokenInfo.

## Example Request
No payload.

## Example Response
```json
{
  "token": "REDACTED", // same token as in auth header
  "session_id": "916e13e1f8564a7eb987eed9e4590e0c",
  "token_type": "bearer",
  "client_id": "12c4279862ab4460a25c2e9fa535fb7e",
  "internal_client": false,
  "client_service": "prod-jackal",
  "account_id": "REDACTED", // egs acc id
  "expires_in": 7169,
  "expires_at": "2025-05-29T22:06:32.137Z",
  "auth_method": "steam",
  "display_name": "REDACTED", // egs display name
  "ext_auth_id": "76561198146688171",
  "ext_auth_type": "steam",
  "ext_auth_method": "steam_session_ticket",
  "ext_auth_display_name": "REDACTED", // steam display name
  "app": "prod-jackal",
  "in_app_id": "REDACTED", // egs acc id
  "scope": ["basic_profile", "friends_list", "country", "openid", "presence"],
  "product_id": "prod-jackal",
  "sandbox_id": "jackal",
  "deployment_id": "53565ba467df4edbb6f5a3d939a8b4f2",
  "application_id": "fghi4567rNJHv9pNoyczQXo6DDJ6RDeq",
  "acr": "urn:epic:loa:aal1",
  "auth_time": "2025-05-29T20:06:32.130Z"
}
```