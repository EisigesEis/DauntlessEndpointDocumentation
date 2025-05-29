URL: https://auth-prod.steelyard.ca/accountinfo \
Method: GET \
Auth: Yes

---

## Comment
Lookup own account info.

## Example Request
No payload.

## Example Response
```json
{
   "accountId" : "U2BLWVTDHZGWLBKKLY2QG6UX4I",
   "creationDate" : "2025-04-22 00:00:00", // they don't even count the time here only the day
   "email" : null, // legacy feature from when dauntless was outside of epic games store
   "preferredLanguage" : null, // legacy feature from when dauntless was outside of epic games store
   "username" : null, // legacy feature from when dauntless was outside of epic games store
   "verified" : false // Either it's newsletter subscribed once or from legacy.
}
```