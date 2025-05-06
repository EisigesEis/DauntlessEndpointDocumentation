URL: https://tracking-prod.steelyard.ca/heartbeat \
Method: POST \
Auth: Yes

---

## Comment
Client tells server its status every 20s.

## Example Request
`content` is current build number `682875`

There is no differentiation between heroic, surged or normal island for `map` identifier. Even map rebrands share the same id.
| map | actual name |
|-|-|
| Map_LoginMenu | Login Menu |
| ramsgate_01_persistent | Ramsgate |
| adventure_moss_triforce | Embermane Cove |
| adventure_moss_falls | Iron Falls |
| adventure_moss_poodle | Aulric's Peak / Razorcliff Isle |
| adventure_moss_cave | Undervald Defile |
| adventure_snow_jen | Boreal Outpost |
| adventure_snow_big | The Snowblind Waste |
| adventure_snow_vega | Coldrunner Key |
| adventure_shock_rose_p | Cape Fury |
| adventure_moss_croissant | Revelation Rock |
| adventure_moss_jamima | Brightwood |
| adventure_arid_valley | Sunderstone |
| adventure_arid_rose | Hades Reach |
| adventure_tundra_jamima | The Blazeworks |
| adventure_umbral_cave_01 | Twilight's Domain |
| adventure_radiant_cave | Conundrum Rocks |
| adventure_radiant_valley | The Paradox Breaks |
| escalation_island_00 | Escalation |
| adventure_destroyed_ramsgate_00 | Gauntlet |
| arena_ramsgate_00 | trials |
| training_dojo_persistent | Training Grounds |


### main menu
```json
{
  "build": {
    "code": 682486,
    "content": 682875
  },
  "map": "Map_LoginMenu",
  "ping": -1,
  "platform": "egs",
  "playtime": 39.0,
  "region": "",
  "server": "",
  "session": "",
  "state": "menu"
}
```

### ramsgate
```json
{
	"build":
	{
		"code": 682486,
		"content": 682875
	},
	"platform": "egs",
	"state": "city",
	"region": "US",
	"server": "gke-game1-production-gameserver-nodes-a1707ccb-4std",
	"session": "716a50d535254a699350449ab5e48f8d",
	"map": "ramsgate_01_persistent",
	"ping": 57,
	"playtime": 3931.0785770006478
}
```

### hunting grounds island
```json
{
  "build": {
    "code": 682486,
    "content": 682875
  },
  "map": "adventure_moss_triforce",
  "ping": 34,
  "platform": "egs",
  "playtime": 115.0,
  "region": "US",
  "server": "gke-game1-production-gameserver-nodes-a1707ccb-grr7",
  "session": "ef62f6b35b1d4d61b0e524664f4a8abb",
  "state": "island" // On airship hunts: `lobby` (meaning airship before hunt) into `island` (outside airship)
}
```



## Example Response
```json
20000 // time until next heartbeat should be sent I'm guessing
```