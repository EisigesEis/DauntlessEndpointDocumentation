URL: https://progression-prod.steelyard.ca/game_tuning/bounty_game_data_daily \
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
      { "bounty_id": "Challenge_Daily_Bronze_ASInterrupts", "enabled": false },
      { "bounty_id": "Challenge_Daily_Bronze_AxeInterrupts", "enabled": false },
      {
        "bounty_id": "Challenge_Daily_Bronze_BreakAllPartsKill",
        "enabled": false
      },
      { "bounty_id": "Challenge_Daily_Bronze_DPInterrupts", "enabled": false },
      {
        "bounty_id": "Challenge_Daily_Bronze_GrenadeInterrupt",
        "enabled": false
      },
      {
        "bounty_id": "Challenge_Daily_Bronze_HammerBlastInterrupts",
        "enabled": false
      },
      {
        "bounty_id": "Challenge_Daily_Bronze_InterruptEnraged",
        "enabled": false
      },
      {
        "bounty_id": "Challenge_Daily_Bronze_KillRadiantWeapon",
        "enabled": false
      },
      {
        "bounty_id": "Challenge_Daily_Bronze_KillUmbralWeapon",
        "enabled": false
      },
      { "bounty_id": "Challenge_Daily_Bronze_KillRadiant", "enabled": false },
      { "bounty_id": "Challenge_Daily_Bronze_KillRage", "enabled": false },
      {
        "bounty_id": "Challenge_Daily_Bronze_PartDamageEnraged",
        "enabled": false
      },
      {
        "bounty_id": "Challenge_Daily_Bronze_PartDamageReduce",
        "enabled": false
      },
      { "bounty_id": "Challenge_Daily_Bronze_PartsEnraged", "enabled": false },
      {
        "bounty_id": "Challenge_Daily_Bronze_PikeBlastInterrupts",
        "enabled": false
      },
      {
        "bounty_id": "Challenge_Daily_Bronze_StaggerDamageEnraged",
        "enabled": false
      },
      {
        "bounty_id": "Challenge_Daily_Bronze_StaggerEnraged",
        "enabled": false
      },
      {
        "bounty_id": "Challenge_Daily_Bronze_SwordInterrupts",
        "enabled": false
      },
      {
        "bounty_id": "Challenge_Daily_Bronze_WoundDamageEnraged",
        "enabled": false
      },
      {
        "bounty_id": "Challenge_Daily_Bronze_WoundDamageReduce",
        "enabled": false
      },
      { "bounty_id": "Challenge_Daily_Bronze_WoundEnraged", "enabled": false },
      {
        "bounty_id": "Challenge_Daily_Bronze_KillWithFriends",
        "enabled": false
      },
      { "bounty_id": "Challenge_Daily_Bronze_GetHuntPassXP", "enabled": false }
    ],
    "bounty_token_grant_hour": 0,
    "bounty_token_id": "TOKEN_DAILY_CHALLENGE_DRAFT",
    "bronze_count": 1,
    "delete_claimed_bounties": false,
    "gold_count": 0,
    "history_length": 10,
    "item_grant_data": [],
    "max_slots": 1,
    "new_season_reset_bounties": true,
    "num_draft_options": 3,
    "num_spicy_options": 1,
    "num_tokens_hp_start": 1,
    "num_tokens_per_day": 0,
    "premium_bounty_token_id": "TOKEN_DAILY_CHALLENGE_DRAFT_PREMIUM",
    "silver_count": 0,
    "token_rollover_warning_days": 1000
  }
}
```