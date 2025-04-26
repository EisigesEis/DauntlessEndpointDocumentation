URL: https://progression-prod.steelyard.ca/game_tuning/bounty_game_data_weekly \
Method: Get \
Auth: Yes

---

## Comment
No idea what this does

## Example Request
Empty payload

## Example Response
```json
{
  "code": null,
  "message": "OK",
  "payload": {
    "automatic_claim": true,
    "automatic_draft": true,
    "bounty_data": [
      {
        "bounty_id": "26_11_7_Challenge_Season_BreakParts_Firesacs_Aether_Sally_Terra",
        "enabled": false
      },
      {
        "bounty_id": "27_7_7_Challenge_Season_BreakParts_Firesacs_Aether_Sally_Terra",
        "enabled": false
      },
      {
        "bounty_id": "27_1_3_Challenge_Season_Wound_Damage_Thorns_Warpike",
        "enabled": false
      }
    ],
    "bounty_token_grant_hour": 0,
    "bounty_token_id": "TOKEN_WEEKLY_CHALLENGE_DRAFT",
    "bronze_count": 0,
    "delete_claimed_bounties": false,
    "gold_count": 4,
    "history_length": 8,
    "item_grant_data": [],
    "max_slots": 4,
    "new_season_reset_bounties": true,
    "num_draft_options": 3,
    "num_spicy_options": 1,
    "num_tokens_hp_start": 4,
    "num_tokens_per_day": 0,
    "premium_bounty_token_id": "TOKEN_WEEKLY_CHALLENGE_DRAFT_PREMIUM",
    "silver_count": 0,
    "token_rollover_warning_days": 1000
  }
}
```