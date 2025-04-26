This folder contains all requests on the dauntless specific api related to the game client logging in.

# Getting Started
## Example
An example python program [TrialsLeaderboard.py](./TrialsLeaderboard.py) which retrieves the trials leaderboard is provided.

## Typical Headers
### EOS
Will be made using the following User-Agent header:
```
"EOS-SDK/1.16.0-25515828 (Windows/10.0.19041.4406.64bit) Dauntless/1.0.0"
```

### PXHL api without required Auth
A request without required auth to a phxl endpoint has the following headers:
```json
{
  "Accept": "*/*",
  "Accept-Encoding": "deflate, gzip",
  "User-Agent": "Archon/++dauntless+rel-1.14.7-CL-647472 Windows/10.0.19045.1.256.64bit",
  "Content-Length": 0,
  "Content-Type": "application/json; charset=utf-8",
  "X-Archon-Console": "(Windows)",
  "Connection": "Keep-Alive", // present only when kept alive
  "Host": "steelyard.online" // the base url, depends on request
}
```

### PHXL api with required Auth
Additionally use `BEARER SessionToken` as Authorization header.

## Authorization Process
1. Retrieve [Exchange Code](https://github.com/LeleDerGrasshalmi/FortniteEndpointsDocumentation/blob/main/EpicGames/AccountService/Authentication/ExchangeCode/Create.md)
2. Retrieve [Access Token](./AccessToken.md)
3. Retrieve [Session Token](./GameSession/GetSessionToken.md)

### Good Manners
Before auth:
- Check server status (yes both versions).
- [Login](./LoginQueue/Login.md)
- Get link, tags, features.

After:
- Kill other tokens (DELETE https://account-public-service-prod03.ol.epicgames.com/account/api/oauth/sessions/kill?killType=OTHERS_ACCOUNT_CLIENT_SERVICE)
- Leave party
- [Matchmaking](../Matchmaking/README.md) to Ramsgate

Keep up:
- Send heartbeats and telemetry