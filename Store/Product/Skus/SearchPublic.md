URL: https://store-prod.steelyard.ca/product/skus/public?requiredTags={tags} \
Method: GET \
Auth: Yes

---

## Comment
tags:
- `webstore` retrieves whole store.

## Example Request
No payload.

## Example Response
### missing requiredTags
`/public`
```json
{
  "code": "400",
  "message": "missing requiredTags query parameter"
}
```

### tags=dyes
[dyes.json](./dyes.json)

### tags=loadout_slots
[loadout_slots.json](./loadout_slots.json)

### tags=d24_season1_pass
It does this response on my main account. I'm pretty sure that's indication for when hunt pass was bought already.
```json
[]
```

It does this response on alt account where I don't own huntpass:
[d24_season1_pass.json](./d24_season1_pass.json)

### tags=huntpass_store
[huntpass_store.json](./huntpass_store.json)

### tags=hp_level_skip_rank
[hp_level_skip_rank.json](./hp_level_skip_rank.json)

### tags=mailbox
[mailbox.json](./mailbox.json)

### tags=webstore
[awakening_webstore.json](./awakening_webstore.json)

### tags=gauntlet_store
[gauntlet_store.json](./gauntlet_store.json)

### tags=ladyluckstore
[ladyluckstore.json](./ladyluckstore.json)