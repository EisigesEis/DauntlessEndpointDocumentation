URL: https://api.epicgames.dev/telemetry/data/datarouter/api/v1/public/data?SessionID=%7BCA79BBF4-4A3F-A338-AA52-418D0D31A9FD%7D&AppID=EOSSDK.PhaseRelease.ReleaseBuild&AppVersion=1.16.0-26821782%20-%20%2B%2BEOSSDK%2BRelease-1.16-CL-26821782&UserID=&AppEnvironment=Production&UploadType=sdkevents \
Method: POST \
Auth: Yes (EOS)

---

## Comment
Every so often the game reports back to EOS server.

## Example Request
```json
{
  "Events": [
    {
      "EventName": "EOSSDK.Heartbeat",
      "DateOffset": "+00:00:56.909",
      "UserAgent": "EOS-SDK/1.16.0-26821782 (Windows/10.0.26100.3912.64bit) Dauntless///phx-archon/release/2.1.1-CL-682875",
      "ProductName": "Dauntless",
      "ProductVersion": "//phx-archon/release/2.1.1-CL-682875",
      "CallingLanguage": "C",
      "ProductId": "prod-jackal",
      "SandboxId": "jackal",
      "DeploymentId": "53565ba467df4edbb6f5a3d939a8b4f2",
      "OSName": "Windows",
      "OSVer": "10.0.26100.3912.64bit",
      "SDKVer": "1.16.0-26821782",
      "IntegratedPlatform": "UNKNOWN",
      "Components": {
        "Auth": { "CurrentLoggedInUsers": 1, "NumLogins": 0, "NumLogouts": 0 },
        "Connect": {
          "CurrentLoggedInUsers": 1,
          "NumLogins": 0,
          "NumLogouts": 0
        },
        "Platform": {
          "PlatformAgeInSeconds": 1440.071392801,
          "SecondsSinceLastHeartbeat": 60.000214599,
          "TickHz": 143.96615175,
          "NumTicks": 8638
        }
      }
    },
    {
      "EventName": "EOSSDK.HTTP.Complete",
      "DateOffset": "+00:00:56.792",
      "UserAgent": "EOS-SDK/1.16.0-26821782 (Windows/10.0.26100.3912.64bit) Dauntless///phx-archon/release/2.1.1-CL-682875",
      "ProductName": "Dauntless",
      "ProductVersion": "//phx-archon/release/2.1.1-CL-682875",
      "CallingLanguage": "C",
      "ProductId": "prod-jackal",
      "SandboxId": "jackal",
      "DeploymentId": "53565ba467df4edbb6f5a3d939a8b4f2",
      "OSName": "Windows",
      "OSVer": "10.0.26100.3912.64bit",
      "SDKVer": "1.16.0-26821782",
      "IntegratedPlatform": "UNKNOWN",
      "ServiceName": "Metrics",
      "OperationName": "SendBackendEvent",
      "HttpStatusCode": 200,
      "StatusText": "success",
      "RequestProperties": {
        "CorrelationId": "EOS-MNm3CPFuLkGUexhIoTtuwQ-H-yfFx5V8UC6NpfwmqARtw"
      }
    },
    {
      "EventName": "UsageMetric",
      "DateOffset": "+00:00:33.114",
      "UserAgent": "EOS-SDK/1.16.0-26821782 (Windows/10.0.26100.3912.64bit) Dauntless///phx-archon/release/2.1.1-CL-682875",
      "ProductName": "Dauntless",
      "ProductVersion": "//phx-archon/release/2.1.1-CL-682875",
      "CallingLanguage": "C",
      "ProductId": "prod-jackal",
      "SandboxId": "jackal",
      "DeploymentId": "53565ba467df4edbb6f5a3d939a8b4f2",
      "OSName": "Windows",
      "OSVer": "10.0.26100.3912.64bit",
      "SDKVer": "1.16.0-26821782",
      "IntegratedPlatform": "UNKNOWN",
      "ComponentName": "AntiCheatClient",
      "ApiName": "EOS_AntiCheatClient_ReceiveMessageFromServer",
      "SuccessCount": 3,
      "FailureCount": 0,
      "InvalidUsageCount": 0,
      "ThrottledCount": 0,
      "DurationSeconds": 60.006016,
      "RetryCount": 0
    },
    {
      "EventName": "EOSSDK.HTTP.Complete",
      "DateOffset": "+00:00:28.460",
      "UserAgent": "EOS-SDK/1.16.0-26821782 (Windows/10.0.26100.3912.64bit) Dauntless///phx-archon/release/2.1.1-CL-682875",
      "ProductName": "Dauntless",
      "ProductVersion": "//phx-archon/release/2.1.1-CL-682875",
      "CallingLanguage": "C",
      "ProductId": "prod-jackal",
      "SandboxId": "jackal",
      "DeploymentId": "53565ba467df4edbb6f5a3d939a8b4f2",
      "OSName": "Windows",
      "OSVer": "10.0.26100.3912.64bit",
      "SDKVer": "1.16.0-26821782",
      "IntegratedPlatform": "UNKNOWN",
      "ServiceName": "OAuth",
      "OperationName": "TokenInfov2",
      "HttpStatusCode": 200,
      "StatusText": "success",
      "RequestProperties": {
        "CorrelationId": "EOS-MNm3CPFuLkGUexhIoTtuwQ-r8S9Zf1gnUG-qSQHuQw4-Q"
      }
    }
  ]
}
```

```json
{
  "Events": [
    {
      "EventName": "UsageMetric",
      "DateOffset": "+00:00:45.880",
      "UserAgent": "EOS-SDK/1.16.0-26821782 (Windows/10.0.26100.3912.64bit) Dauntless///phx-archon/release/2.1.1-CL-682875",
      "ProductName": "Dauntless",
      "ProductVersion": "//phx-archon/release/2.1.1-CL-682875",
      "CallingLanguage": "C",
      "ProductId": "prod-jackal",
      "SandboxId": "jackal",
      "DeploymentId": "53565ba467df4edbb6f5a3d939a8b4f2",
      "OSName": "Windows",
      "OSVer": "10.0.26100.3912.64bit",
      "SDKVer": "1.16.0-26821782",
      "IntegratedPlatform": "UNKNOWN",
      "ComponentName": "ConnectClient",
      "ApiName": "EOS_Connect_QueryExternalAccountMappings",
      "SuccessCount": 5,
      "FailureCount": 0,
      "InvalidUsageCount": 0,
      "ThrottledCount": 0,
      "DurationSeconds": 60.005711,
      "RetryCount": 0
    },
    {
      "EventName": "UsageMetric",
      "DateOffset": "+00:00:45.568",
      "UserAgent": "EOS-SDK/1.16.0-26821782 (Windows/10.0.26100.3912.64bit) Dauntless///phx-archon/release/2.1.1-CL-682875",
      "ProductName": "Dauntless",
      "ProductVersion": "//phx-archon/release/2.1.1-CL-682875",
      "CallingLanguage": "C",
      "ProductId": "prod-jackal",
      "SandboxId": "jackal",
      "DeploymentId": "53565ba467df4edbb6f5a3d939a8b4f2",
      "OSName": "Windows",
      "OSVer": "10.0.26100.3912.64bit",
      "SDKVer": "1.16.0-26821782",
      "IntegratedPlatform": "UNKNOWN",
      "ComponentName": "UserInfoClient",
      "ApiName": "EOS_UserInfo_QueryUserInfo",
      "SuccessCount": 5,
      "FailureCount": 0,
      "InvalidUsageCount": 0,
      "ThrottledCount": 0,
      "DurationSeconds": 60.005474,
      "RetryCount": 0
    },
    {
      "EventName": "UsageMetric",
      "DateOffset": "+00:00:00.617",
      "UserAgent": "EOS-SDK/1.16.0-26821782 (Windows/10.0.26100.3912.64bit) Dauntless///phx-archon/release/2.1.1-CL-682875",
      "ProductName": "Dauntless",
      "ProductVersion": "//phx-archon/release/2.1.1-CL-682875",
      "CallingLanguage": "C",
      "ProductId": "prod-jackal",
      "SandboxId": "jackal",
      "DeploymentId": "53565ba467df4edbb6f5a3d939a8b4f2",
      "OSName": "Windows",
      "OSVer": "10.0.26100.3912.64bit",
      "SDKVer": "1.16.0-26821782",
      "IntegratedPlatform": "UNKNOWN",
      "ComponentName": "AntiCheatClient",
      "ApiName": "EOS_AntiCheatClient_ReceiveMessageFromServer",
      "SuccessCount": 3,
      "FailureCount": 0,
      "InvalidUsageCount": 0,
      "ThrottledCount": 0,
      "DurationSeconds": 60.006016,
      "RetryCount": 0
    }
  ]
}
```

## Example Response
```json
{}
```