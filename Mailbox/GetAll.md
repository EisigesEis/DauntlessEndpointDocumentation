URL: https://mailbox-prod.steelyard.ca/all/ \
Method: GET \
Auth: Yes

---

## Comment
Get mailbox content

## Example Request
No payload.

## Example Response
```json
{
  "code": null,
  "message": "OK",
  "payload": {
    "messages": [
      {
        "body": "Join the Dauntless email list today and we'll send you a bundle of <bold>in-game rewards</>, including:\r\n\r\n- The <bold>Bound Fury Sword Skin</> (a subscriber exclusive!)\r\n- 10 Patrol Keys\r\n- 10 Premium Bounty Tokens\r\n\r\nYou'll also get the <bold>Dauntless newsletter</>: an occasional email full of useful info about upcoming events, new features, and more!",
        "can_delete": 0,
        "cta": {
          "cta_action": ["newsletter_signup"],
          "cta_text": "SIGN UP NOW"
        },
        "image": "https://cdn.playdauntless.com/motd/images/motd-image_c4549122-a51d-4701-b912-2a0536d984da_v3.jpg",
        "menu_title": "Sign up for newsletter rewards",
        "message_category": "newsletter",
        "message_id": "c4549122-a51d-4701-b912-2a0536d984da",
        "promotional": 1,
        "status": "read",
        "subtitle_text": "",
        "timestamp": "2021-04-16T16:08:46Z",
        "title": "Get Your Rewards"
      },
      {
        "body": "Hello Slayer,\r\n\r\nThank you for your bug report regarding tracker resetting. \r\n\r\nWe are aware of this issue and are currently working to fix it.\r\n\r\nYou can follow the progress on some of our known issues here:\r\nhttps://playdauntless.com/known-issues\r\n\r\nIf you require any additional assistance, please contact us by opening up a support ticket here:\r\nhttps://playdauntless.com/support\r\n\r\nWith kind regards,\r\nPhoenix Labs Player Support",
        "can_delete": 1,
        "image": null,
        "menu_title": "You have a message from player support!",
        "message_category": "direct",
        "message_id": "DIRECT#627d4e8c-4fb4-4dd2-aa5e-376eeec360b0",
        "promotional": 0,
        "status": "read",
        "subtitle_text": "Thank you for contacting us.",
        "timestamp": "2024-01-15T20:09:36Z",
        "title": "We received your bug report."
      },
      {
        "body": "Hello Slayer,\r\n\r\nThank you for your bug report regarding The challenge being displayed as complete over and over again. \r\n\r\nTo properly investigate this potential issue, we need more information from you. Please provide us with more details (such as a video or screenshot) by creating a support ticket at https://playdauntless.com/support\r\n\r\nPlease include this ticket number (358750) in your new support ticket so that we can reference your original bug report.\r\n\r\nWe truly appreciate your effort in helping to improve Dauntless!\r\n\r\nWith kind regards,\r\nPhoenix Labs Player Support",
        "can_delete": 1,
        "image": null,
        "menu_title": "You have a message from player support!",
        "message_category": "direct",
        "message_id": "DIRECT#fa726c81-13f5-41be-aa39-9c4f778113a1",
        "promotional": 0,
        "status": "read",
        "subtitle_text": "Thank you for contacting us.",
        "timestamp": "2024-03-20T19:43:46Z",
        "title": "We received your bug report."
      },
      {
        "body": "Congratulations, Slayer! \r\n\r\nYour guild made it to the <bold>Top 5</> on the Gauntlet Leaderboard!\r\n\r\nYou have received the following titles:\r\n<bold>Monarch</>\r\n<bold>Noble</>\r\n<bold>Nobody</> \r\n\r\nClear skies!",
        "can_delete": 1,
        "image": "https://cdn.playdauntless.com/motd/images/motd-image_23145cdc-7866-47e7-88e1-89ca3dc5e939_v1.jpg",
        "menu_title": "Your Gauntlet Season 13 Reward Titles",
        "message_category": "general",
        "message_id": "1d6171a1-b20b-4194-8f14-eb152f49d675",
        "parcelStatus": "unredeemed",
        "promotional": 0,
        "sku": "sku_title_gauntlet_top5_s13",
        "status": "unread",
        "subtitle_text": "<italic>Your new titles await you.</>",
        "timestamp": "2024-07-04T18:07:41Z",
        "title": "Gauntlet Season 13 Has Ended"
      }
    ],
    "survey": null
  }
}
```