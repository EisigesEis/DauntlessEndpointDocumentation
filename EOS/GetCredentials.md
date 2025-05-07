URL: https://api.epicgames.dev/auth/v1/turn/credentials?service=turn&username= \
Method: POST \
Auth: Yes (EOS)

---

## Comment
Game retrieves EOS credentials once on start. Dauntless devs call `ProductUserId` (`PUID`) as `playerId` which is a unique identifier for a player in a game on a per-game-basis (it wont be the same for other game) separate from epicgames accId.

## Example Request
No payload.

## Example Response
```json
{
  "username": "{10 digits non-zero start}:{playerId / PUID, 32 digits can begin with zero}",
  "password": "{27 characters}=",
  "ttl": 3600000, // how long it's valid for
  "uris": [] // unsure what's the use
}
```