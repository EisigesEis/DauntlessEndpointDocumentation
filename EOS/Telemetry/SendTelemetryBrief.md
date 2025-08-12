URL: https://api.epicgames.dev/datarouter/api/v1/public/data/clients?AppID=prod-jackal&AppVersion=1.16.0-26821782&AppEnvironment=jackal&UploadType=eteventstream&SessionID=D6E6E2F3417D6AC10454C1952E90531B \
Method: POST \
Auth: Yes (EOS)

---

## Comment

## Example Request
### GameStartup
```json
{
  "Events" : [
  {
    "EventName" : "GameStartup",
    "deploymentId" : "53565ba467df4edbb6f5a3d939a8b4f2",
    "platform" : "Windows 10 (Release 2009) 10.0.26100.1.256.64bit",
    "source" : "client"
  }
  ]
}
```

### GameHeartbeat
```json
{
  "Events" : [
    {
      "EventName" : "GameHeartbeat",
      "deploymentId" : "53565ba467df4edbb6f5a3d939a8b4f2",
      "platform" : "Windows 10 (Release 2009) 10.0.26100.1.256.64bit",
      "source" : "client"
    }
  ]
}
```

## Example Response
```json
{}
```