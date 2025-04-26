URL: https://tracking-prod.steelyard.ca/heartbeat \
Method: POST \
Auth: Yes

---

## Comment
Client tells server its status every 20s.

## Example Request
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

## Example Response
```json
20000 // time until next heartbeat should be sent I'm guessing
```