URL: https://store-prod.steelyard.ca/lootbox/list?requiredTags=webstore \
Method: GET \
Auth: Yes

---

## Comment
Get a list of all lootboxes.

## Example Request
Empty payload.

## Example Response
```json
{
  "lootboxes": [
    {
      "lootboxId": "deep_sea_box",
      "tags": [
        "d24_season1_store",
        "store_tab_new_featured",
        "webstore",
        "rarity_legendary",
        "cat_item_canister"
      ],
      "displayPriority": 600,
      "displayName": "Deep Sea Canister",
      "displayDescription": "It IS that deep. Each purchase grants you one (1) item from the ALL NEW Deep Sea Canister at random. Previously owned items cannot be earned again.",
      "prices": [
        {
          "currencyId": "id_currency_platinum",
          "price": 300,
          "salesPrice": null
        }
      ],
      "images": {
        "standard": "Engine.Texture2D'/Game/UI/Textures/Canisters/ico_canisters_deepsea.ico_canisters_deepsea'"
      },
      "availableFrom": "2024-10-31T00:00:00Z",
      "availableTo": "2025-06-01T00:00:00Z"
    },
    {
      "lootboxId": "arcslayer_box",
      "tags": [
        "d24_season1_store",
        "store_tab_new_featured",
        "webstore",
        "rarity_epic",
        "cat_item_canister"
      ],
      "displayPriority": 700,
      "displayName": "Arcslayer Canister",
      "displayDescription": "Everything you need to claim your identity as an Arcslayer. Each purchase grants you one (1) item from the Arcslayer Canister at random. Previously owned items cannot be earned again.",
      "prices": [
        {
          "currencyId": "id_currency_platinum",
          "price": 125,
          "salesPrice": null
        }
      ],
      "images": {
        "standard": "Engine.Texture2D'/Game/UI/Textures/Canisters/ico_canisters_arcslayer.ico_canisters_arcslayer'"
      },
      "availableFrom": "2024-10-31T00:00:00Z",
      "availableTo": "2025-06-01T00:00:00Z"
    }
  ]
}
```