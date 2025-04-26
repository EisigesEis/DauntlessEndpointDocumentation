URL: https://auth-prod.steelyard.ca/accountinfo/public \
Method: POST \
Auth: Yes

---

## Comment
Lookup own account info.

## Example Request
```json
{
   "accountId" : "U2BLWVTDHZGWLBKKLY2QG6UX4I" // PHXL ID
}
```

## Example Response
```json
{
   "accountId" : "U2BLWVTDHZGWLBKKLY2QG6UX4I", // PHXL ID
   "isSubscribed" : false,
   "language" : null,
   "linkedAccounts" : [
      {
         "accountId" : "", // epic account id
         "accountType" : "epic"
      }
   ],
   "username" : null
}
```