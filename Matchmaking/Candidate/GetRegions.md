URL: https://mm2-prod.steelyard.ca/candidate/regions \
Method: GET \
Auth: Yes

---

## Comment
Get regions (before each matchmaking).

## Example Request
No payload.

## Example Response
```json
{
  "code": 200,
  "message": "success",
  "payload": {
    "maxPingingStepTime": 3,
    "pingCount": 5,
    "pingFrequency": 0.25,
    "regionUrls": [ // Each of these, client will ping as specified. GET to base URL. Websites answer with `<!DOCTYPE html><html><body>pong</body></html>`
      "http://us-central1.gce.latency-test.steelyard.ca",
      "http://us-west1.gce.latency-test.steelyard.ca",
      "http://us-east1.gce.latency-test.steelyard.ca",
      "http://europe-west1.gce.latency-test.steelyard.ca",
      "http://europe-west4.gce.latency-test.steelyard.ca",
      "http://asia-east1.gce.latency-test.steelyard.ca",
      "http://australia-southeast1.gce.latency-test.steelyard.ca"
    ]
  }
}
```