URL: https://telemetry-ingest-prod.steelyard.ca/event?id=prod \
Method: POST \
Auth: Yes

---

## Comment
Client tells server its state including surroundings.

## Example Request
```json
[
  {
    "TitleId": "prod",
    "Platform": "Windows",
    "PlatformVariant": "egs",
    "Build": 682875,
    "EventName": "player_equip_weapon",
    "EventSession": "6DC596E448F4D4E3DFF4D4958460AB7C",
    "EventSequence": 190,
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

## Example Response
```json
OK
```