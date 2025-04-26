URL: https://leaderboards-prod.steelyard.ca/trials/leaderboards/all \
Method: POST \
Auth: Yes

---


## Example Request
```json
{
  "difficulty": 1,
  "page": 0,
  "page_size": 100,
  "trial_id": "Arena_MatchmakerHunt_Elite_New_0075",
  "target_platforms": []
}
```

## Example Response
```json
{
  "code": null,
  "message": "OK",
  "payload": {
    "difficulty": 1,
    "guild": {},
    "page": 0,
    "page_size": 100,
    "trial_id": "Arena_MatchmakerHunt_Elite_New_0075",
    "world": {
      "group": {
        "difficulty": 1,
        "entries": [
          {
            "completion_time": 14948,
            "entries": [
              {
                "phx_account_id": "25DSUCQTFJEITBMUJN6K4JHUEM",
                "platform": "WIN",
                "platform_name": "JuanMaster.",
                "player_role_id": "PR_BASTION",
                "weapon": 1
              },
              {
                "phx_account_id": "4KMUNUWDSFBKTPQ6PB242YGU4E",
                "platform": "PSN",
                "platform_name": "Reignz_Empire711",
                "player_role_id": "PR_FRANK",
                "weapon": 5
              },
              {
                "phx_account_id": "TLRIO32HPNAP7HNPK5UWEQXOJI",
                "platform": "WIN",
                "platform_name": "Toadi .-.",
                "player_role_id": "PR_BASTION",
                "weapon": 6
              },
              {
                "phx_account_id": "XQBF5VHGFJHR5AUILEPYI55MUQ",
                "platform": "WIN",
                "platform_name": "B\u00e4rtiger B\u00e4r",
                "player_role_id": "PR_BASTION",
                "weapon": 6
              }
            ],
            "objectives_completed": 3,
            "rank": 1,
            "session_id": "647472_rel-1.14.7_shipping/bd349aec6b4d433d8cfdf30beb3dab7d"
          },
          // 99 more entries
        ]
      },
      "solo": {
        "all": {
          "difficulty": 1,
          "entries": [
            {
              "completion_time": 36500,
              "objectives_completed": 3,
              "phx_account_id": "IRO2MP5MIRBK3IBXNPYUSNAHMY",
              "platform": "WIN",
              "platform_name": "\u306e\u3042\u308b\u3068\u306e\u3044\u3068",
              "player_role_id": "PR_DARKNESS",
              "rank": 1,
              "session_id": "647472_rel-1.14.7_shipping/0bbe98452f9e4c82a1d1af22ab096629",
              "weapon": 5
            },
            // 99 more entries
          ]
        }
      }
    }
  }
}
```