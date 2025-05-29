URL: https://api.epicgames.dev/stats/achievements/v1/player/{PUID}/unlock \
Method: Post \
Auth: Yes (EOS)

---

## Comment
Unverified if this is how it works. While the client has rights for unlock, it seems the server unlocks achievements for client.

## Example Request
```json
{
  "AchievementIds": ["achievement_id_1", "achievement_id_2"]
}
```

## Example Response
Not captured yet.