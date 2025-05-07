URL: https://api.epicgames.dev/epic/friends/v1/{epicgames accId} \
Method: GET \
Auth: Yes (EOS)

---

## Comment
Game looks up friends in one big request.

## Example Request
No payload.

## Example Response
```json
{
  "friends": [
    {
      "accountId": "", // epic games accId
      "created": "2020-12-23T13:02:16.000Z",
      "favorite": false // not sure what's the use, haven't seen true yet
    }
  ],
  "blockList": [
    {
      "accountId": "8e6ee8e758e6437aae864844aefd62d0", // epic games accId
      "created": "2024-01-05T11:06:08.577Z" // seems to be optional
    },
    { "accountId": "5a8bc57bfddb42a6bfcec236647959ed" },
    { "accountId": "e0925b9953ad4422a93fbb15c6287223" }
  ]
}
```