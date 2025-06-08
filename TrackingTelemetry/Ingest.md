URL: https://telemetry-ingest-prod.steelyard.ca/event?id=prod \
Method: POST \
Auth: Yes

---

## Comment
Client tells server its state including surroundings and previous actions.

## Example Request
## Dauntless Client
```json
[
  // array of events
  {
    "TitleId": "prod",
    "Platform": "Windows",
    "PlatformVariant": "egs",
    "Build": 682875,
    "EventName": "player_equip_weapon",
    "EventSession": "6DC596E448F4D4E3DFF4D4958460AB7C",
    "EventSequence": 190, // count which event we're at within a session
    "player_id": "U2BLWVTDHZGWLBKKLY2QG6UX4I",
    "lobby_id": "716a50d535254a699350449ab5e48f8d",
    "Timestamp": "2025-04-22T10:47:02.754Z",
    "weapon_id": "ih_shock_01_bp_C",
    "weapon_slot": 0,
    "character_id": "DFHAK6JBXJBPXHFJEAVBZ4MHZA"
  },
  {
    "TitleId": "prod",
    "Platform": "Windows",
    "PlatformVariant": "egs",
    "Build": 682875,
    "EventName": "player_load_screen_duration",
    "EventSession": "6DC596E448F4D4E3DFF4D4958460AB7C",
    "EventSequence": 191,
    "player_id": "U2BLWVTDHZGWLBKKLY2QG6UX4I",
    "lobby_id": "716a50d535254a699350449ab5e48f8d",
    "Timestamp": "2025-04-22T10:47:03.768Z",
    "load_screen_duration_sec": "+00:00:05.847",
    "load_screen_style": 0,
    "character_id": "DFHAK6JBXJBPXHFJEAVBZ4MHZA"
  },
  {
    "TitleId": "prod",
    "Platform": "Windows",
    "PlatformVariant": "egs",
    "Build": 682875,
    "EventName": "player_input_type",
    "EventSession": "6DC596E448F4D4E3DFF4D4958460AB7C",
    "EventSequence": 192,
    "lobby_id": "716a50d535254a699350449ab5e48f8d",
    "Timestamp": "2025-04-22T10:47:03.768Z",
    "player_id": "U2BLWVTDHZGWLBKKLY2QG6UX4I",
    "character_id": "DFHAK6JBXJBPXHFJEAVBZ4MHZA",
    "input_type": "mouse"
  },
  {
    "TitleId": "prod",
    "Platform": "Windows",
    "PlatformVariant": "egs",
    "Build": 682875,
    "EventName": "player_epic_friends",
    "EventSession": "6DC596E448F4D4E3DFF4D4958460AB7C",
    "EventSequence": 193,
    "player_id": "U2BLWVTDHZGWLBKKLY2QG6UX4I",
    "lobby_id": "716a50d535254a699350449ab5e48f8d",
    "Timestamp": "2025-04-22T10:47:03.770Z",
    "number_of_friends": 1,
    "friends": [
      {
        "user_id": "05e64c3790334d6f835dc4ef9d45bfda|00025e79866843b69f98a796b05314ef",
        "display_name": "Bärtiger Bär",
        "is_online": false,
        "is_playing": false,
        "platform": "",
        "presence": "Offline"
      }
    ],
    "character_id": "DFHAK6JBXJBPXHFJEAVBZ4MHZA"
  },
  {
    "TitleId": "prod",
    "Platform": "Windows",
    "PlatformVariant": "egs",
    "Build": 682875,
    "EventName": "player_platform_friends",
    "EventSession": "6DC596E448F4D4E3DFF4D4958460AB7C",
    "EventSequence": 194,
    "player_id": "U2BLWVTDHZGWLBKKLY2QG6UX4I",
    "lobby_id": "716a50d535254a699350449ab5e48f8d",
    "Timestamp": "2025-04-22T10:47:03.770Z",
    "number_of_friends": 0,
    "character_id": "DFHAK6JBXJBPXHFJEAVBZ4MHZA"
  },
  {
    "TitleId": "prod",
    "Platform": "Windows",
    "PlatformVariant": "egs",
    "Build": 682875,
    "EventName": "player_controller_gameplay_start_event",
    "EventSession": "6DC596E448F4D4E3DFF4D4958460AB7C",
    "EventSequence": 195,
    "player_id": "U2BLWVTDHZGWLBKKLY2QG6UX4I",
    "lobby_id": "716a50d535254a699350449ab5e48f8d",
    "Timestamp": "2025-04-22T10:47:03.773Z",
    "duration_from_controller_beginplay": 2.101,
    "game_mode": "City",
    "character_id": "DFHAK6JBXJBPXHFJEAVBZ4MHZA"
  },
  {
    "TitleId": "prod",
    "Platform": "Windows",
    "PlatformVariant": "egs",
    "Build": 682875,
    "EventName": "player_fps",
    "EventSession": "6DC596E448F4D4E3DFF4D4958460AB7C",
    "EventSequence": 196,
    "player_id": "U2BLWVTDHZGWLBKKLY2QG6UX4I",
    "lobby_id": "716a50d535254a699350449ab5e48f8d",
    "Timestamp": "2025-04-22T10:47:20.441Z",
    "pos_x": 142.43407121728876,
    "pos_y": -324.2098390634593,
    "pos_z": 805.14098608493805,
    "facing_x": -0.022620790298628301,
    "facing_y": 0.99118676998374,
    "facing_z": -0.1305261922200518,
    "total_gputime": 2.75125,
    "total_gamethreadtime": 2.28255,
    "total_renderthreadtime": 2.23656,
    "map_name": "ramsgate_01_persistent",
    "island_game_mode": "None",
    "hunt_id": "ShatteredIsles_TrainingDojo",
    "atmosphere_name": "/Game/World/atmospheres/blueprints/atmospheres/production/atmospheres_ramsgate_day_00_bp.atmospheres_ramsgate_day_00_bp_C",
    "total_frametime": 6.94476,
    "switch_dockstate": -1,
    "cpu_usage_pct_relative": 325.027,
    "avg_lag": 0.0578807,
    "best_lag": 0.0578807,
    "net_in_bytes_per_second": 1607,
    "net_out_bytes_per_second": 1087,
    "net_in_packets_lost": 0,
    "net_out_packets_lost": 0,
    "character_id": "DFHAK6JBXJBPXHFJEAVBZ4MHZA"
  }
]
```

### login events
[login events](./loginevents.json)

### load map
```json
{
  "Build": 682875,
  "EventName": "map_load_duration",
  "EventSequence": 23,
  "EventSession": "89AD5BCA457D280AA1F1FD83BE19E244",
  "Platform": "Windows",
  "PlatformVariant": "egs",
  "Timestamp": "2025-05-06T13:01:50.565Z",
  "TitleId": "prod",
  "duration": 0.0,
  "lobby_id": "",
  "map_id": "adventure_destroyed_ramsgate_00",
  "player_id": "XQBF5VHGFJHR5AUILEPYI55MUQ"
}
```

### chat message client sends
```json
[
  {
    "Build": 682875,
    "EventName": "chat_sent_room",
    "EventSequence": 396,
    "EventSession": "643A0A7840D28AD4EBC0FCB880030137",
    "Platform": "Windows",
    "PlatformVariant": "egs",
    "Timestamp": "2025-05-05T15:44:40.308Z",
    "TitleId": "prod",
    "lobby_id": "f3740cd4d87845188b34f5aee00176e2",
    "message": "suspect",
    "player_id": "05e64c3790334d6f835dc4ef9d45bfda|00025e79866843b69f98a796b05314ef",
    "room": "Hunt-f3740cd4d87845188b34f5aee00176e2"
  },
  {
    "Build": 682875,
    "EventName": "chat_sent_room",
    "EventSequence": 397,
    "EventSession": "643A0A7840D28AD4EBC0FCB880030137",
    "Platform": "Windows",
    "PlatformVariant": "egs",
    "Timestamp": "2025-05-05T15:44:43.691Z",
    "TitleId": "prod",
    "lobby_id": "f3740cd4d87845188b34f5aee00176e2",
    "message": "suspect",
    "player_id": "05e64c3790334d6f835dc4ef9d45bfda|00025e79866843b69f98a796b05314ef",
    "room": "Party-5a85dec5a5124b0d9c001984f3555fc9_NjgyNDg2XzIuMS4xX3NoaXBwaW5n"
  },
  {
    "Build": 682875,
    "EventName": "chat_sent_room",
    "EventSequence": 398,
    "EventSession": "643A0A7840D28AD4EBC0FCB880030137",
    "Platform": "Windows",
    "PlatformVariant": "egs",
    "Timestamp": "2025-05-05T15:44:45.969Z",
    "TitleId": "prod",
    "lobby_id": "f3740cd4d87845188b34f5aee00176e2",
    "message": "suspect",
    "player_id": "05e64c3790334d6f835dc4ef9d45bfda|00025e79866843b69f98a796b05314ef",
    "room": "Guild-439fdb55-b311-4f96-a8ca-bec688e00ca2"
  }
]
```

### island entry animation
In this case from gauntlet entry.
```json
{
  "Build": 682875,
  "EventName": "player_cinematic_start",
  "EventSequence": 33,
  "EventSession": "89AD5BCA457D280AA1F1FD83BE19E244",
  "Platform": "Windows",
  "PlatformVariant": "egs",
  "Timestamp": "2025-05-06T13:02:52.657Z",
  "TitleId": "prod",
  "character_id": "ONH4QI3DDNFV5OQYK7GBHVCWEE",
  "cinematic": "cine_islandintro_shot00_02",
  "lobby_id": "ce40d61f774b42e0b0ad566a214a8138",
  "player_id": "XQBF5VHGFJHR5AUILEPYI55MUQ",
  "position": {
    "x": 155285.0,
    "y": 940973.0,
    "z": 102355
  },
  "start_time": 62.0
}
```

```json
{
  "Build": 682875,
  "EventName": "player_cinematic_end",
  "EventSequence": 35,
  "EventSession": "89AD5BCA457D280AA1F1FD83BE19E244",
  "Platform": "Windows",
  "PlatformVariant": "egs",
  "Timestamp": "2025-05-06T13:03:10.075Z",
  "TitleId": "prod",
  "character_id": "ONH4QI3DDNFV5OQYK7GBHVCWEE",
  "cinematic": "cine_islandintro_shot00_02",
  "end_time": 79.0,
  "lobby_id": "ce40d61f774b42e0b0ad566a214a8138",
  "player_id": "XQBF5VHGFJHR5AUILEPYI55MUQ",
  "position": {
    "x": -113.0,
    "y": -11247.0,
    "z": 298.0
  },
  "reason": "Finished"
}
```

### location sync
```json
{
  "Build": 682875,
  "EventName": "player_correction",
  "EventSequence": 36,
  "EventSession": "89AD5BCA457D280AA1F1FD83BE19E244",
  "Platform": "Windows",
  "PlatformVariant": "egs",
  "Timestamp": "2025-05-06T13:03:50.718Z",
  "TitleId": "prod",
  "character_id": "ONH4QI3DDNFV5OQYK7GBHVCWEE",
  "lobby_id": "ce40d61f774b42e0b0ad566a214a8138",
  "magnitude": 1198.0,
  "new_location_x": 2271.0,
  "new_location_y": -2605.0,
  "new_location_z": 193.0,
  "old_location_x": 1985.0,
  "old_location_y": -1443.0,
  "old_location_z": 268.0,
  "player_id": "XQBF5VHGFJHR5AUILEPYI55MUQ"
}
```

### die
```json
{
  "Build": 682875,
  "EventName": "player_bleed_out",
  "EventSequence": 38,
  "EventSession": "89AD5BCA457D280AA1F1FD83BE19E244",
  "Platform": "Windows",
  "PlatformVariant": "egs",
  "Timestamp": "2025-05-06T13:04:23.336Z",
  "TitleId": "prod",
  "character_id": "ONH4QI3DDNFV5OQYK7GBHVCWEE",
  "game_time": 153.0,
  "killer_id": "lerawr_alpha_bp_C",
  "lobby_id": "ce40d61f774b42e0b0ad566a214a8138",
  "player_id": "XQBF5VHGFJHR5AUILEPYI55MUQ",
  "pos_x": 1943.0,
  "pos_y": -3098.0,
  "pos_z": 265.0
}
```

### store
```json
{
  "Build": 682875,
  "EventName": "store_viewed",
  "EventSequence": 58,
  "EventSession": "89AD5BCA457D280AA1F1FD83BE19E244",
  "Platform": "Windows",
  "PlatformVariant": "egs",
  "Timestamp": "2025-05-06T13:10:32.660Z",
  "TitleId": "prod",
  "character_id": "ONH4QI3DDNFV5OQYK7GBHVCWEE",
  "lobby_id": "5c8988d3b7074d4dbd1001198d90da47",
  "player_id": "XQBF5VHGFJHR5AUILEPYI55MUQ",
  "screen_name": "gauntlet_store",
  "source": "player",
  "store_type": "SeasonalStore",
  "total_duration": "9.97",
  "visited_items": ""
}
```

### main menu
```json
[
  {
    "Build": 682875,
    "EventName": "mainmenu_item_clicked",
    "EventSequence": 59,
    "EventSession": "89AD5BCA457D280AA1F1FD83BE19E244",
    "Platform": "Windows",
    "PlatformVariant": "egs",
    "Timestamp": "2025-05-06T13:10:33.540Z",
    "TitleId": "prod",
    "character_id": "ONH4QI3DDNFV5OQYK7GBHVCWEE",
    "lobby_id": "5c8988d3b7074d4dbd1001198d90da47",
    "mainmenu_item_clicks_gauntlet_store": 1,
    "mainmenu_item_clicks_hunt_pass": 1,
    "player_id": "XQBF5VHGFJHR5AUILEPYI55MUQ",
    "screen_name": "main_menu",
    "source": "player",
    "total_duration": "12.06"
  },
  {
    "Build": 682875,
    "EventName": "mainmenu_item_clicked",
    "EventSequence": 134,
    "EventSession": "643A0A7840D28AD4EBC0FCB880030137",
    "Platform": "Windows",
    "PlatformVariant": "egs",
    "Timestamp": "2025-05-05T15:11:23.518Z",
    "TitleId": "prod",
    "character_id": "ONH4QI3DDNFV5OQYK7GBHVCWEE",
    "lobby_id": "7b373c04728e4dbc82d726fb85afd546",
    "mainmenu_item_clicks_gauntlet_store": 1,
    "mainmenu_item_clicks_hunt_pass": 1,
    "mainmenu_item_clicks_trials_store": 1,
    "player_id": "XQBF5VHGFJHR5AUILEPYI55MUQ",
    "screen_name": "main_menu",
    "source": "player",
    "total_duration": "16.72"
  }
]
```

### mastery, I think??
```json
{
  "Build": 682875,
  "EventName": "weapon_overview_screen_interaction",
  "EventSequence": 533,
  "EventSession": "643A0A7840D28AD4EBC0FCB880030137",
  "Platform": "Windows",
  "PlatformVariant": "egs",
  "Timestamp": "2025-05-05T15:57:42.579Z",
  "TitleId": "prod",
  "archon_wep_overveiw_chains": 1.0,
  "archon_wep_overview_axe": 0.0,
  "archon_wep_overview_hammer": 1.0,
  "archon_wep_overview_pike": 1.0,
  "archon_wep_overview_repeaters": 1.0,
  "archon_wep_overview_strikers": 1.0,
  "archon_wep_overview_sword": 1.0,
  "character_id": "ONH4QI3DDNFV5OQYK7GBHVCWEE",
  "lobby_id": "5834b404f48a416fa76ceee5143a8d34",
  "player_id": "XQBF5VHGFJHR5AUILEPYI55MUQ",
  "time_screen_closed": 44.0,
  "time_screen_opened": 34.0
}
```

### slayers path
```json
{
  "Build" : 682875,
  "EventName" : "slayer_path_screen_viewed",
  "EventSequence" : 164,
  "EventSession" : "643A0A7840D28AD4EBC0FCB880030137",
  "Platform" : "Windows",
  "PlatformVariant" : "egs",
  "Timestamp" : "2025-05-05T15:13:07.788Z",
  "TitleId" : "prod",
  "character_id" : "ONH4QI3DDNFV5OQYK7GBHVCWEE",
  "lobby_id" : "b872e14f758349a0b437e7c2921af062",
  "player_id" : "XQBF5VHGFJHR5AUILEPYI55MUQ",
  "screen_name" : "PlayerJourney",
  "source" : "player",
  "total_duration" : "0.63"
}
```

### quick chat
```json
{
  "Build" : 682875,
  "EventName" : "quick_chat",
  "EventSequence" : 169,
  "EventSession" : "643A0A7840D28AD4EBC0FCB880030137",
  "Platform" : "Windows",
  "PlatformVariant" : "egs",
  "Timestamp" : "2025-05-05T15:13:21.915Z",
  "TitleId" : "prod",
  "character_id" : "ONH4QI3DDNFV5OQYK7GBHVCWEE",
  "error" : "",
  "interaction_id" : "TY_EMOTE_FROSTFALL2020_CHEERS",
  "interaction_place" : "Island",
  "interaction_type" : "Curiosity",
  "lobby_id" : "b872e14f758349a0b437e7c2921af062",
  "player_id" : "XQBF5VHGFJHR5AUILEPYI55MUQ"
}
```

### retry trials
```json
{
  "Build": 682875,
  "EventName": "player_retry_event",
  "EventSequence": 75,
  "EventSession": "89AD5BCA457D280AA1F1FD83BE19E244",
  "Platform": "Windows",
  "PlatformVariant": "egs",
  "Timestamp": "2025-05-06T13:13:46.226Z",
  "TitleId": "prod",
  "character_id": "ONH4QI3DDNFV5OQYK7GBHVCWEE",
  "find_retry_hunt_success": true,
  "game_mode_type": "Trials",
  "lobby_id": "78562d049fdb4288b9bbd435974348b2",
  "player_id": "XQBF5VHGFJHR5AUILEPYI55MUQ",
  "private_hunt": true,
  "retry_hunt_id": "CR19_PlayerHunt_Arena_Elite",
  "timed_out_switch_to_private_retry_hack": false
},
{
  "Build": 682875,
  "EventName": "player_retry_event",
  "EventSequence": 76,
  "EventSession": "89AD5BCA457D280AA1F1FD83BE19E244",
  "Platform": "Windows",
  "PlatformVariant": "egs",
  "Timestamp": "2025-05-06T13:13:46.496Z",
  "TitleId": "prod",
  "character_id": "ONH4QI3DDNFV5OQYK7GBHVCWEE",
  "find_retry_hunt_success": true,
  "game_mode_type": "Trials",
  "lobby_id": "78562d049fdb4288b9bbd435974348b2",
  "player_id": "XQBF5VHGFJHR5AUILEPYI55MUQ",
  "private_hunt": true,
  "retry_hunt_id": "CR19_PlayerHunt_Arena_Elite",
  "timed_out_switch_to_private_retry_hack": false
}
```

### creature spawn
[creaturespawn.json](./creaturespawn.json)

### hunt player friendship
Public hunt report friendship.
[playerhuntfriendship.json](./playerhuntfriendship.json)

### hunt pass claim rewards
```json
[
  {
    "Build": 682875,
    "EventName": "hunting_pass_claim_rewards",
    "EventSequence": 78,
    "EventSession": "643A0A7840D28AD4EBC0FCB880030137",
    "Platform": "Windows",
    "PlatformVariant": "egs",
    "Timestamp": "2025-05-05T15:07:20.112Z",
    "TitleId": "prod",
    "character_id": "ONH4QI3DDNFV5OQYK7GBHVCWEE",
    "confirmed_premium_rank": 2514,
    "confirmed_rank": 2515,
    "id": "d24_season1",
    "lobby_id": "a3cf85a90dad4489b05817dc52482060",
    "player_id": "XQBF5VHGFJHR5AUILEPYI55MUQ",
    "premium_rank": 0,
    "rank": 2515,
    "time": 2.0
  },
  {
    "Build": 682875,
    "EventName": "hunting_pass_interaction", // assuming this is opening hunt pass
    "EventSequence": 79,
    "EventSession": "643A0A7840D28AD4EBC0FCB880030137",
    "Platform": "Windows",
    "PlatformVariant": "egs",
    "Timestamp": "2025-05-05T15:07:20.307Z",
    "TitleId": "prod",
    "character_id": "ONH4QI3DDNFV5OQYK7GBHVCWEE",
    "duration": 2.0,
    "id": "d24_season1",
    "lobby_id": "a3cf85a90dad4489b05817dc52482060",
    "player_id": "XQBF5VHGFJHR5AUILEPYI55MUQ",
    "points": 251441,
    "premium": true,
    "rank": 2515
  }
]
```

## Dauntless Launcher
[Dauntless Launcher](../CDN/Production/README.md) refers to the standalone launcher before Dauntless was on Epic Games Launcher.

Yes, back then a single json was ingested per request.
### time to ui
```json
{
  "type": "cef",
  "time": 0.3926754,
  "version": 97904,
  "InstallationID": "fc0422b0-6f77-416d-9ac2-73c4d20cd88e",
  "SessionID": "b4a4e275-e1bb-4fd0-a069-b6cb2b93bad0",
  "EventName": "time_to_ui",
  "ThreadID": 1,
  "ThreadName": null,
  "ThreadIsBackground": false
}
```

### failed to retrieve patcher
```json
{
  "version": 97904,
  "ErrorShort": "Failed to retrieve the package information for '{0}'",
  "Error": "Error: Failed to retrieve the package information for 'Patcher'",
  "InstallationID": "fc0422b0-6f77-416d-9ac2-73c4d20cd88e",
  "SessionID": "b4a4e275-e1bb-4fd0-a069-b6cb2b93bad0",
  "EventName": "patcher_error",
  "ThreadID": 15,
  "ThreadName": "Package Update Thread",
  "ThreadIsBackground": true
}
```

## Example Response
```json
OK
```