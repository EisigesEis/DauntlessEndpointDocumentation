URL: https://migration-prod.steelyard.ca/migration/trigger \
Method: POST \
Auth: Yes

---

## Comment
Check migration status, potentially migrate. No idea when this is triggered and what happens when gotta migrate i.e. player profile to new game version. Only allowed when inventory returned code NONE.

## Example Request
No payload.

## Example Response
```json
{
  "migration_failed": false,
  "migration_finished": true
}
```