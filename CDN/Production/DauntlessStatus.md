URL: https://cdn.playdauntless.com/patcher-news/toast.json \
Method: GET \
Auth: No

---

## Comment
Launcher retrieves Dauntless status to display and possibly bar people out of logging in this way.

## Example Request
No body.
### headers
```yaml
Host: cdn.playdauntless.com
Connection: keep-alive
Accept: application/json, text/javascript, */*; q=0.01
Origin: artifact://patcherui
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
```

## Example Response
```json
{
  "title": "Dauntless Down for Maintenance until May 21st",
  "status": "error",
  "lastUpdate": "May 18, 2019 18:30 PST",
  "message": {
    "lastUpdate": "May 18, 2019 18:30 PST",
    "status": "error",
    "title": {
      "de": "Dauntless Down for Maintenance until May 21st",
      "en": "Dauntless Down for Maintenance until May 21st",
      "es_ES": "Dauntless Down for Maintenance until May 21st",
      "fr": "Dauntless Down for Maintenance until May 21st",
      "it": "Dauntless Down for Maintenance until May 21st",
      "pt_BR": "Dauntless Down for Maintenance until May 21st"
    },
    "body": {
      "de": "Slayers, the Dauntless servers will be down for maintenance until May 21st. <a href=\"https://twitter.com/PlayDauntless/status/1129916911179902976\">Please see our Twitter post for more info.</a>",
      "en": "Slayers, the Dauntless servers will be down for maintenance until May 21st. <a href=\"https://twitter.com/PlayDauntless/status/1129916911179902976\">Please see our Twitter post for more info.</a>",
      "es_ES": "Slayers, the Dauntless servers will be down for maintenance until May 21st. <a href=\"https://twitter.com/PlayDauntless/status/1129916911179902976\">Please see our Twitter post for more info.</a>",
      "fr": "Slayers, the Dauntless servers will be down for maintenance until May 21st. <a href=\"https://twitter.com/PlayDauntless/status/1129916911179902976\">Please see our Twitter post for more info.</a>",
      "it": "Slayers, the Dauntless servers will be down for maintenance until May 21st. <a href=\"https://twitter.com/PlayDauntless/status/1129916911179902976\">Please see our Twitter post for more info.</a>",
      "pt_BR": "Slayers, the Dauntless servers will be down for maintenance until May 21st. <a href=\"https://twitter.com/PlayDauntless/status/1129916911179902976\">Please see our Twitter post for more info.</a>"
    }
  }
}
```