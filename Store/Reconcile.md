URL: https://store-prod.steelyard.ca/reconcile \
Method: POST \
Auth: Yes

---

## Comment
I think this is same as [Balance](./Balance.md). It may be explicitly asking server to check update on balance?

## Example Request
```json
{
  "authorization": "eyJ0IjoiZXBpY19pZCIsImFsZyI6IlJTMjU2Iiwia2lkIjoiV01TN0Vua0lHcGNIOURHWnN2MldjWTl4c3VGblpDdHhaamo0QWhiLV84RSJ9.eyJzdWIiOiI5ZDFmNjYxMDRhMjg0OTQ2YmZiMDg1M2M3MTc4ZTMyZSIsInBmc2lkIjoiamFja2FsIiwiZHZpZCI6ImMzZWMxMDU5MWM5MDQ4NDJhZmFiYjRkZDY5YWJiZjc1IiwiaXNzIjoiaHR0cHM6Ly9hcGkuZXBpY2dhbWVzLmRldi9lcGljL29hdXRoL3YxIiwiZG4iOiJCbMO8dGVuZGUgQmzDvHRlIiwibm9uY2UiOiJuLXhoeXVkUHNtMWt2WlJ1UDgyZDFWdFZrSG5KOD0iLCJwZnBpZCI6InByb2QtamFja2FsIiwic2VjIjoxLCJhdWQiOiIxMmM0Mjc5ODYyYWI0NDYwYTI1YzJlOWZhNTM1ZmI3ZSIsInBmZGlkIjoiNTM1NjViYTQ2N2RmNGVkYmI2ZjVhM2Q5MzlhOGI0ZjIiLCJ0IjoiZXBpY19pZCIsInNjb3BlIjoiYmFzaWNfcHJvZmlsZSBmcmllbmRzX2xpc3QgY291bnRyeSBvcGVuaWQgcHJlc2VuY2UiLCJhcHBpZCI6ImZnaGk0NTY3ck5KSHY5cE5veWN6UVhvNkRESjZSRGVxIiwiZXhwIjoxNzQ1NjYwMTQ4LCJpYXQiOjE3NDU2NTI5NDgsImp0aSI6ImNjZGFjMjk4OGI2MzQzOWI5Mjk4ZDkwNzJmOGJmNGJmIn0.F2IBOt2IaLOJeQO1L-wsTE4XSmFqop_e8ZBqDaY6hsbqsx3paMnPHd4-0CNHCHUogDF4gb7zpkT5B_dOiSXKYTvjcGqdErKvnQDgeqN9-Cej74xdpNiN0ZjI25NaBSprFm3I3b1UOfXL3XaERht4PHO-vgaWgVEkiDU7nrrVWPcn0rxKU5ZjtslLhmhlOcK3PuTUHJ2Ir27Tc-oiZOCwuIl15pU5uQ_dXNcVWIbaf9RVcW3dO9hsWBUw2OchDsjWRSvc2uJTQ5vjAXuBsmnuTas60CKgkSpBadmG2wVoR1vlw9FIIz-R3OD1fai42zwIDLxkMMRJg7u2ogNQbVDU0A"
}
```

## Example Reponse
```json
{
  "balances": {
    "CURRENCY_CELLDUST": 0,
    "CURRENCY_EVENT_DARKHARVEST": 0,
    "CURRENCY_EVENT_FROSTFALL": 0,
    "CURRENCY_EVENT_RAMSGIVING": 0,
    "CURRENCY_EVENT_SAINTSBOND": 0,
    "CURRENCY_EVENT_SPRINGTIDE": 0,
    "CURRENCY_GAUNTLET_COIN": 0,
    "CURRENCY_GAUNTLET_COIN_FADED": 0,
    "CURRENCY_MARKS_GILDED": 0,
    "CURRENCY_MARKS_STEEL": 0,
    "CURRENCY_NOTES": 6200,
    "CURRENCY_PLATINUM": 0,
    "CURRENCY_PRESTIGE": 0,
    "CURRENCY_REWARDCACHE": 0,
    "CURRENCY_S13_COIN": 0,
    "CURRENCY_S13_DAILY": 0,
    "CURRENCY_S14_COIN": 0,
    "CURRENCY_S15_COIN": 0,
    "CURRENCY_S16_COIN": 0,
    "CURRENCY_S17_COIN": 0,
    "CURRENCY_S18_COIN": 0,
    "CURRENCY_S19_COIN": 0,
    "CURRENCY_S20_COIN": 0,
    "CURRENCY_SEASONAL_COIN": 0,
    "CURRENCY_TOKEN_EXCHANGE_SPEED_UP": 0,
    "CURRENCY_WEAPON_TOKEN": 25,
    "id_currency_celldust": 0,
    "id_currency_event_darkharvest": 0,
    "id_currency_event_frostfall": 0,
    "id_currency_event_ramsgiving": 0,
    "id_currency_event_saintsbond": 0,
    "id_currency_event_springtide": 0,
    "id_currency_gauntlet_coin": 0,
    "id_currency_gauntlet_coin_faded": 0,
    "id_currency_marks_gilded": 0,
    "id_currency_marks_steel": 0,
    "id_currency_notes": 6200,
    "id_currency_platinum": 0,
    "id_currency_prestige": 0,
    "id_currency_rewardcache": 0,
    "id_currency_s13_coin": 0,
    "id_currency_s13_daily": 0,
    "id_currency_s14_coin": 0,
    "id_currency_s15_coin": 0,
    "id_currency_s16_coin": 0,
    "id_currency_s17_coin": 0,
    "id_currency_s18_coin": 0,
    "id_currency_s19_coin": 0,
    "id_currency_s20_coin": 0,
    "id_currency_seasonal_coin": 0,
    "id_currency_token_exchange_speed_up": 0,
    "id_currency_weapon_token": 25
  },
  "refreshInventory": true
}
```