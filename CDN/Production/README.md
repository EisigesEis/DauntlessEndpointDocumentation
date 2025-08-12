## Launcher requests
### headers
`User-Agent: Phoenix Labs; .NET`

### typical flow
0. Build up tcp with telemetry.steelyard.ca (unable to check what is sent since this service is down). This is attempted every 40ms.
1. Send a HEAD request to [GetPatcherCodePath](./PatcherCode/GetPath.md).
2. Retrieve [Dauntless Status](./DauntlessStatus.md)
3. Send a HEAD request to [GetPatcherUICodePath](./PatcherUI/GetPath.md).
4. Send a HEAD request to [GetDauntlessPath](./Dauntless/GetPath.md).

#### user login
Begins by asking for OPTIONS on [Login](../../Login/LoginQueue/Login.md). 