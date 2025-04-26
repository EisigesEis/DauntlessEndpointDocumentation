URL: https://auth-prod.steelyard.ca/account/mapping \
Method: POST \
Auth: Yes

---

## Comment
Lookup several accounts. Why is single acc lookup even used on lookup?

## Example Request
```json
{
   "ids" : [ "05e64c3790334d6f835dc4ef9d45bfda" ], // PHXL ID array
   "srcAccountType" : "epic"
}
```

## Example Response
```json
{
   "accountMappings" : {
      "" : { // epic account id
         "accountId" : "XQBF5VHGFJHR5AUILEPYI55MUQ", // PHXL ID
         "accountType" : "phoenix"
      }
   },
   "sourceAccountType" : "epic"
}
```