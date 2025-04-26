URL: https://gauntlet-prod.steelyard.ca/rewards/guild \
Method: POST \
Auth: Yes

---

## Example Request
```json
{
  "account_id":"{PHXL ID}",
  "gauntlet_id":"gauntlet-season{season number}"
}
```

## Example Response
```json
{"code":null,"message":"OK","payload":[{"catalog_id":"CURRENCY_GAUNTLET_COIN","quantity":1,"type":"stacked"},{"catalog_id":"CURRENCY_GAUNTLET_COIN","quantity":1,"type":"stacked"},{"catalog_id":"CURRENCY_GAUNTLET_COIN","quantity":1,"type":"stacked"},{"catalog_id":"CURRENCY_GAUNTLET_COIN","quantity":1,"type":"stacked"},{"catalog_id":"CURRENCY_GAUNTLET_COIN","quantity":1,"type":"stacked"},{"catalog_id":"CURRENCY_GAUNTLET_COIN","quantity":1,"type":"stacked"},{"catalog_id":"CURRENCY_GAUNTLET_COIN","quantity":1,"type":"stacked"},{"catalog_id":"CURRENCY_GAUNTLET_COIN","quantity":1,"type":"stacked"}]}
```