URL: https://api.epicgames.dev/epic/id/v2/sdk/accounts?accountId={epicgames accId 1}&accountId={epicgames accId 2} (can be arbitrarily many) \
Method: GET \
Auth: Yes (EOS)

---

## Comment
On startup game looks up own account and then looks up all friends from [GetFriends.md](../Friends/GetFriends.md).

## Example Request
No payload.

## Example Response
```json
[
  {
    "accountId": "", // epic games accId
    "displayName": "Mustermann",
    "preferredLanguage": "de",
    "linkedAccounts": [
      {
        "identityProviderId": "psn",
        "accountId": "", // platform specific accId
        "displayName": "Mustermann"
      }
    ]
  } // for each accId lookup in the url one of these response objects in the array
]
```