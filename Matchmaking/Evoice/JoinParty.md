URL: https://mm2-prod.steelyard.ca/evoice/join/party \
Method: POST \
Auth: Yes

---

## Comment

## Example Request
```json
{
	"product_user_id": "" // part of epic username id here, from https://api.epicgames.dev/auth/v1/turn/credentials where username=useless:product_user_id
}
```

## Example Response
```json
{
  "channel_name": "PARTY.34cda5fce86d48fca6cdd78956cf244e",
  "client_base_url": "wss://signaling-service-prod.euc1.live.rtcp.on.epicgames.com/api/v1/websocket_route?ms=wss://10.150.186.8:8443/3c7c3e08-95a3-4269-8816-82e4ee3b91e2&productId=prod-jackal&token=eyJ0eXAiOiJKV1QiLCJhbGciOiJFZERTQSJ9.eyJzdWIiOiJXU19DT05OX0VTVEFCTElTSCIsInRhcmdldEhvc3QiOiIxMC4xNTAuMTg2LjgiLCJpc3MiOiJydGNwLW1hbmFnZXIiLCJndWlkIjoiM2M3YzNlMDgtOTVhMy00MjY5LTg4MTYtODJlNGVlM2I5MWUyIiwiZXhwIjoxNzQ1MzIyNjA2LCJpYXQiOjE3NDUzMTU0MDZ9.Kbzn3o6tIfRdAd9QxD1-K-pbjPu9X3L8G_sQDgfD-3bSSsPG18NPxO-KSo4gbEg2412vTCZTfvVcRM_L81BaCA",
  "participant_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJFZERTQSJ9.eyJzdWIiOiJDT05ORUNUIiwidGFyZ2V0SG9zdCI6IjEwLjE1MC4xODYuOCIsImNsaWVudElkIjoiMDAwMjc5NTdkMzFlNDdjMWEyNTAyMDUwNzgwYzdiYWQiLCJjb25mZXJlbmNlSWQiOiJQQVJUWS4zNGNkYTVmY2U4NmQ0OGZjYTZjZGQ3ODk1NmNmMjQ0ZSIsImlzcyI6InJ0Y3AtbWFuYWdlciIsIm5hbWVzcGFjZSI6IlZvaWNlXzUzNTY1YmE0NjdkZjRlZGJiNmY1YTNkOTM5YThiNGYyIiwiZ3VpZCI6IjNjN2MzZTA4LTk1YTMtNDI2OS04ODE2LTgyZTRlZTNiOTFlMiIsImV4cCI6MTc0NTMyMjYwNiwiaWF0IjoxNzQ1MzE1NDA2LCJlb3NQcm9wZXJ0aWVzIjp7ImRlcGxveW1lbnRJZCI6IjUzNTY1YmE0NjdkZjRlZGJiNmY1YTNkOTM5YThiNGYyIiwib3JnYW5pemF0aW9uSWQiOiJvLWtybHp4ajg4cXJ0YjY5ZnJlZGV1YWY4ODdibDVheiIsInByb2R1Y3RJZCI6InByb2QtamFja2FsIiwic2FuZGJveElkIjoiamFja2FsIn19.aPZy9-TQG6yld-GXD3Ikql3pA34J2V_lmwlDJ9xSm39bzavtdrtMNqbam4ISiS7my_bpk8jndOJkEJTetCBHDQ",
  "party_id": "34cda5fce86d48fca6cdd78956cf244e_NjgyNDg2XzIuMS4xX3NoaXBwaW5n"
}
```