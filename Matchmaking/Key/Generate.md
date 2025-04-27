URL: https://mm2-prod.steelyard.ca/key/generate \
Method: GET \
Auth: Yes

---

## Comment
256 bit FEAESKey. But why is nonce 43B long?

As soon as matchmaking is done they generate a key that is not used in any request. I assume this is what's used to encode UDP. By the consistency of the packets start I can guess they're using [UE Bunch packets](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/Net/FInBunch) and then encrypting. I'm unsure which method of encryption they're using. Either from UE library or custom. A good starting point might be [FEncryptionData](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UObject/FEncryptionData) since it can take key and fingerprint/nonce.

## Example Request
```json
{ "candidateId": "euw11$e90ae40b8b2d4020b4bda5450c56be82" }
```

## Example Response
```json
{
  "key": "428b75ad8ba6cc78d4f887700d7dde6ad94eec42c5b2545b26f4af536ab30add", // https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/Misc/FAES/FAESKey
  "nonce": "eg9MrkNzuiRj3gfq8s5GqhB1SG4NyKFE_cfE3h8Avrg", // presumably fingerprint 
  "token": "eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJVMkJMV1ZUREhaR1dMQktLTFkyUUc2VVg0SSIsImlzcyI6ImdhbWVfc2Vzc2lvbl9hcGkiLCJpYXQiOjE3NDUzMTQ5NDksInNlc3Npb24tdXVpZCI6ImM5NGNhN2U1YzczNjRkY2Q4ZDNjODE3NTg5N2Y0MTEwIiwiZGlzcGxheV9uYW1lIjoiQmxcdTAwZmN0ZW5kZSBCbFx1MDBmY3RlIiwicGxhdGZvcm0iOiJ3aW4ifQ.KDD9TdOzgIWIUHFQsh8fQT9CARiS1i469bQrmUFWTdknbvfRN7CC9i3QCkizP5BUZtSODfH1q-YoXvn3ddn7Hg=21a6b16923a845e6b6f9ef451a555228" // Login/GameSession/GetSessionToken.md gamesession id = Matchmaking/Candidate/GetStatus.md session id
}
```