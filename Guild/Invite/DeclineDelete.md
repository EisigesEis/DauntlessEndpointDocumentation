URL: https://guild-prod.steelyard.ca/guild/invite/{invite id} \
Method: DELETE \
Auth: Yes

---

## Comment
Decline an invite you received or delete an invite of the guild

## Example Request
No payload

## Example Response
### Invite already declined
```json
{
  "code": "UninvitedAdorableQuillshot",
  "message": "Guild invitation 9ecfd9e2-6f4f-45f4-a10a-9f794a770aa7 not found.",
  "payload": null
}
```

### Success
```json
{"code":null,"message":"OK","payload":{}}
```