URL: https://leaderboards-prod.steelyard.ca/trials/leaderboards/solo/individual \
Method: POST \
Auth: Yes

---

## Comment
When running trials between runs the game retrieves own run data to display.
There should be very similar for group ranking but I didn't manage to capture that.

## Example Request
```json
{
  "difficulty": 1,
  "trial_id": "Arena_MatchmakerHunt_Elite_New_0122",
  "phx_account_id": "XQBF5VHGFJHR5AUILEPYI55MUQ"
}
```

## Example Response
```json
{
  "code": null,
  "message": "OK",
  "payload": {
    "completion_time": 11268,
    "difficulty": "1",
    "objectives_completed": 3,
    "phx_account_id": "XQBF5VHGFJHR5AUILEPYI55MUQ",
    "platform": "",
    "platform_name": "REDACTED",
    "player_role_id": "PR_DARKNESS",
    "secondary_weapon": 1,
    "session_id": "682486_2.1.1_shipping/061eb2542ff74d27875c4b6a685981ad",
    "trial_id": "Arena_MatchmakerHunt_Elite_New_0122",
    "weapon": 2
  }
}
```