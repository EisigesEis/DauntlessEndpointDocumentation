URL: https://api.epicgames.dev/auth/v1/oauth/token \
Method: POST \
Auth: Yes (EOS)

---

## Example Request
```
grant_type=client_credentials&deployment_id=53565ba467df4edbb6f5a3d939a8b4f2
```

## Example Response
```json
{
  "access_token": "",
  "token_type": "bearer",
  "expires_at": "2025-05-07T17:06:18.703Z",
  "features": ["Achievements", "AntiCheat", "Ecom", "Voice"],
  "organization_id": "o-krlzxj88qrtb69fredeuaf887bl5az",
  "product_id": "prod-jackal",
  "sandbox_id": "jackal",
  "deployment_id": "53565ba467df4edbb6f5a3d939a8b4f2",
  "expires_in": 3599
}
```