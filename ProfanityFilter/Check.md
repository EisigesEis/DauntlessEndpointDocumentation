URL: https://profanity-filter-prod.steelyard.ca/check \
Method: POST \
Auth: No

---

## Comment
Why no auth? Anyways. Check profanity of chat message, rate it and sanitize. I assume rating is for auto check chat history on report?

Also detects common profanity in other languages regardless of lang value.

## Example Request
```json
{
  "string": "fck",
  "lang": "en" // I think this doesn't matter as it checks for all languages anyways?
}
```

## Example Response
```json
{ "rating": 1.0, "sanitized": "***", "string": "fck" }
```

```json
{ "rating": 200.0, "sanitized": "****", "string": "fuck" }
```

```json
{
  "rating": 0,
  "sanitized": "shithead",
  "string": "shithead"
}
```

```json
{
  "rating": 201.0,
  "sanitized": "holy ******* ****",
  "string": "holy fucking shit"
}
```

```json
{ "rating": 1.0, "sanitized": "*********", "string": "Hurensohn" }
```

```json
{ "rating": -1.0, "sanitized": "9/11", "string": "9/11" }
```

```json
{ "rating": 0.0, "sanitized": "assets", "string": "assets" }
```

```json
{ "rating": 400.0, "sanitized": "**** fuck", "string": "fuck fuck" } // why only sanitize first one?
```

````json
{
  "rating": 2.0,
  "sanitized": "********* Hurensohn", // repeated cursing is fine bc why not
  "string": "Hurensohn Hurensohn"
}
```