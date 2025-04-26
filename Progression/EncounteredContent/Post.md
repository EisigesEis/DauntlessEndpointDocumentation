URL: https://progression-prod.steelyard.ca/encountered-content/{Character ID} \
Method: POST \
Auth: Yes

---

https://progression-prod.steelyard.ca/encountered-content/query/DFHAK6JBXJBPXHFJEAVBZ4MHZA

## Comment
Client tells server to hand in content and progress further. Content IDs can be same for Quest and Hint if they are at the same progression stage (appear together).

## Example Request
```json
{
  "content_type": 2, // 1 => ?, 2 => main storyline, 3 => hint, 4 => ?, 5 => lore journal entry
  "content_id": "NPC_KatSorrel" // 1 => ?, 2 => which NPC, 3 => name of hint
}
```

## Example Response
```json
{ "code": null, "message": "OK", "payload": {} }
```