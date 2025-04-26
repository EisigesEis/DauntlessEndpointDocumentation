URL: https://social-prod.steelyard.ca/slayerlink/status_good \
Method: GET \
Auth: Yes

---

## Comment
Retrieve status of invites and established slayer links.

## Example Request
Default headers, no payload.

## Example Response
```json
{
  "code": null,
  "message": "OK",
  "payload": {
    "config": { "invite_expiry_hours": 48, "link_duration_hours": 168 },
    "invites": [
      {
        "account_id": "XQBF5VHGFJHR5AUILEPYI55MUQ",
        "direction": "sent",
        "expires": "2025-04-27T18:51:34Z",
        "link_id": "a81143be-6261-4251-9825-7d27fef0ef9f",
        "slot": 3,
        "status": "cancelled" // pending, cancelled, expired, 
      }
    ],
    "links": [
            {
        "account_id": "PLNTNCL7PNFUHBRPEBVSTAZ47A",
        "ends": "2021-05-25T21:39:20Z",
        "link_id": "5e0655d9-fb25-4ab7-b256-31d1b276759f",
        "linked_account_id": "PLNTNCL7PNFUHBRPEBVSTAZ47A",
        "prize_pool": [
          {
            "catalog_id": "TOKEN_BOUNTY_DRAFT",
            "quantity": 2,
            "received_for_level": 2
          },
          {
            "catalog_id": "CURRENCY_PJM_AIRSHIP",
            "quantity": 10,
            "received_for_level": -1
          },
          {
            "catalog_id": "TOKEN_BOUNTY_DRAFT",
            "quantity": 2,
            "received_for_level": -1
          },
          {
            "catalog_id": "TOKEN_BOUNTY_DRAFT",
            "quantity": 4,
            "received_for_level": -1
          },
          {
            "catalog_id": "CURRENCY_TOKEN_EXCHANGE_SPEED_UP",
            "quantity": 25,
            "received_for_level": -1
          },
          {
            "catalog_id": "CURRENCY_NOTES",
            "quantity": 7500,
            "received_for_level": -1
          },
          {
            "catalog_id": "CURRENCY_NOTES",
            "quantity": 5000,
            "received_for_level": -1
          },
          {
            "catalog_id": "TOKEN_DAILY_PATROL_BONUS_PURCHASED",
            "quantity": 5,
            "received_for_level": 4
          },
          {
            "catalog_id": "CURRENCY_NOTES",
            "quantity": 3000,
            "received_for_level": -1
          },
          {
            "catalog_id": "CURRENCY_PJM_AIRSHIP",
            "quantity": 15,
            "received_for_level": -1
          },
          {
            "catalog_id": "TOKEN_DAILY_PATROL_BONUS_PURCHASED",
            "quantity": 5,
            "received_for_level": 1
          },
          {
            "catalog_id": "CURRENCY_TOKEN_EXCHANGE_SPEED_UP",
            "quantity": 10,
            "received_for_level": 3
          }
        ],
        "slot": 1
      },
      {
        "account_id": "DQQCP4PBLVA4NH4U2UR3CNMKOI",
        "ends": "2021-05-25T21:39:51Z",
        "link_id": "68b9cc06-8713-4188-95c5-bfb264f1e159",
        "linked_account_id": "DQQCP4PBLVA4NH4U2UR3CNMKOI",
        "prize_pool": [
          {
            "catalog_id": "TOKEN_BOUNTY_DRAFT",
            "quantity": 8,
            "received_for_level": 3
          },
          {
            "catalog_id": "CURRENCY_TOKEN_EXCHANGE_SPEED_UP",
            "quantity": 100,
            "received_for_level": -1
          },
          {
            "catalog_id": "CURRENCY_NOTES",
            "quantity": 2000,
            "received_for_level": -1
          },
          {
            "catalog_id": "TOKEN_BOUNTY_DRAFT",
            "quantity": 2,
            "received_for_level": -1
          },
          {
            "catalog_id": "CURRENCY_PJM_AIRSHIP",
            "quantity": 15,
            "received_for_level": -1
          },
          {
            "catalog_id": "CURRENCY_NOTES",
            "quantity": 4000,
            "received_for_level": 1
          },
          {
            "catalog_id": "CURRENCY_TOKEN_EXCHANGE_SPEED_UP",
            "quantity": 10,
            "received_for_level": 4
          },
          {
            "catalog_id": "CURRENCY_NOTES",
            "quantity": 5000,
            "received_for_level": -1
          },
          {
            "catalog_id": "CURRENCY_NOTES",
            "quantity": 1000,
            "received_for_level": -1
          },
          {
            "catalog_id": "CURRENCY_NOTES",
            "quantity": 3000,
            "received_for_level": 2
          },
          {
            "catalog_id": "TOKEN_BOUNTY_DRAFT",
            "quantity": 4,
            "received_for_level": -1
          },
          {
            "catalog_id": "CURRENCY_NOTES",
            "quantity": 500,
            "received_for_level": -1
          }
        ],
        "slot": 2
      }
    ]
  }
}
```