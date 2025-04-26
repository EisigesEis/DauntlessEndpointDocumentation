URL: https://store-prod.steelyard.ca/token/platinum/{catalogId} \
Method: GET \
Auth: Yes

---

## Comment
Generate purchase token for any catalogId from shop to then purchase.

## Example Request
Additional header: X-EpicAuthToken
No payload

## Example Response
```json
{
  "purchaseToken": "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJVMkJMV1ZUREhaR1dMQktLTFkyUUc2VVg0SSIsImV4cCI6MTc0NTMxOTY2Miwib3JkZXJjb2RlIjoiMDE5NjVEMUY2QzU5NzQ2MUIwOThERkJCODYxRTAwRkQifQ.txPWRbE1nNs5XEA7wloW7NnGUgbvePk8bK2yj0p54Qcjp_zPqV1PvxGGJ73XeM7K4KSSddnn1bSBxp0HtDJXbQ"
}
```