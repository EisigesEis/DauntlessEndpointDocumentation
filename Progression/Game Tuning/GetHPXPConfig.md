URL: https://progression-prod.steelyard.ca/game_tuning/huntpass_xp_config \
Method: GET \
Auth: Yes

---

## Comment
Retrieve what objectives give what hp progress currently.

## Example Request
No payload.

## Example Response
```json
{
   "code" : null,
   "message" : "OK",
   "payload" : {
      "EventConfigs" : [
         {
            "Event" : "hunt_completed",
            "EventMultiplier" : 1,000000000000000,
            "FirstTimeMultiplier" : 1,000000000000000,
            "Rules" : [
               {
                  "ItemToMatch" : "CR19_PlayerHunt_FTUE_Pursuit_Beta_Beaver",
                  "Name" : "Beta_FTUE_Beaver",
                  "Priority" : 100,
                  "XpToGrant" : 0
               },
               {
                  "ItemToMatch" : "CR19_PlayerHunt_FTUE_Pursuit_Beta_Fulgar",
                  "Name" : "Beta_FTUE_Fulgar",
                  "Priority" : 100,
                  "XpToGrant" : 0
               },
               {
                  "ItemToMatch" : "CR19_PlayerHunt_FTUE_Pursuit_Beta_Host",
                  "Name" : "Beta_FTUE_Host",
                  "Priority" : 100,
                  "XpToGrant" : 0
               },
               {
                  "ItemToMatch" : "CR19_PlayerHunt_FTUE_Pursuit_Beta_LeRawr",
                  "Name" : "Beta_FTUE_LeRawr",
                  "Priority" : 100,
                  "XpToGrant" : 0
               },
               {
                  "ItemToMatch" : "CR19_PlayerHunt_Pursuit_Bullseye_Beta",
                  "Name" : "Beta_FTUE_Bullseye",
                  "Priority" : 100,
                  "XpToGrant" : 0
               },
               {
                  "Name" : "Normal Pursuits",
                  "Priority" : 10,
                  "TagsToMatch" : [ "hunt.pursuit" ],
                  "XpToGrant" : 0
               },
               {
                  "Name" : "Dire Pursuits",
                  "Priority" : 20,
                  "TagsToMatch" : [ "hunt.pursuit", "hunt.alpha" ],
                  "XpToGrant" : 0
               },
               {
                  "Name" : "Heroic Pursuits",
                  "Priority" : 20,
                  "TagsToMatch" : [ "hunt.pursuit", "hunt.heroic" ],
                  "XpToGrant" : 20,00000000000000
               },
               {
                  "Name" : "Heroic+ Pursuits",
                  "Priority" : 30,
                  "TagsToMatch" : [ "hunt.pursuit", "hunt.heroicplus" ],
                  "XpToGrant" : 0
               },
               {
                  "Name" : "Normal Patrols",
                  "Priority" : 0,
                  "TagsToMatch" : [ "hunt.patrol" ],
                  "XpToGrant" : 0
               },
               {
                  "Name" : "Dire Patrols",
                  "Priority" : 30,
                  "TagsToMatch" : [ "hunt.patrol", "hunt.alpha" ],
                  "XpToGrant" : 0
               },
               {
                  "Name" : "Heroic Patrols",
                  "Priority" : 40,
                  "TagsToMatch" : [ "hunt.patrol", "hunt.heroic" ],
                  "XpToGrant" : 0
               },
               {
                  "Name" : "Heroic+ Patrols",
                  "Priority" : 50,
                  "TagsToMatch" : [ "hunt.patrol", "hunt.heroicplus" ],
                  "XpToGrant" : 0
               },
               {
                  "Name" : "Escalation_Shock_Easy",
                  "Priority" : 10,
                  "TagsToMatch" : [ "hunt.escalation.shock.easy" ],
                  "XpToGrant" : 0
               },
               {
                  "Name" : "Escalation_Shock_Hard",
                  "Priority" : 100,
                  "TagsToMatch" : [ "hunt.escalation.shock.hard" ],
                  "XpToGrant" : 0
               },
               {
                  "Name" : "Escalation_Blaze_Easy",
                  "Priority" : 10,
                  "TagsToMatch" : [ "hunt.escalation.blaze.easy" ],
                  "XpToGrant" : 0
               },
               {
                  "Name" : "Escalation_Blaze_Hard",
                  "Priority" : 100,
                  "TagsToMatch" : [ "hunt.escalation.blaze.hard" ],
                  "XpToGrant" : 0
               },
               {
                  "Name" : "Escalation_Umbral_Easy",
                  "Priority" : 10,
                  "TagsToMatch" : [ "hunt.escalation.umbral.easy" ],
                  "XpToGrant" : 0
               },
               {
                  "Name" : "Escalation_Umbral_Hard",
                  "Priority" : 100,
                  "TagsToMatch" : [ "hunt.escalation.umbral.hard" ],
                  "XpToGrant" : 0
               },
               {
                  "Name" : "Escalation_Terra_Easy",
                  "Priority" : 10,
                  "TagsToMatch" : [ "hunt.escalation.terra.easy" ],
                  "XpToGrant" : 0
               },
               {
                  "Name" : "Escalation_Terra_Hard",
                  "Priority" : 100,
                  "TagsToMatch" : [ "hunt.escalation.terra.hard" ],
                  "XpToGrant" : 0
               },
               {
                  "Name" : "Easy_Trials",
                  "Priority" : 10,
                  "TagsToMatch" : [ "hunt.arena.easy" ],
                  "XpToGrant" : 0
               },
               {
                  "Name" : "Hard_Trials",
                  "Priority" : 10,
                  "TagsToMatch" : [ "hunt.arena.hard" ],
                  "XpToGrant" : 0
               },
               {
                  "Name" : "Dauntless_Trials",
                  "Priority" : 10,
                  "TagsToMatch" : [ "hunt.arena.elite" ],
                  "XpToGrant" : 0
               },
               {
                  "ItemToMatch" : "CR19_PlayerHunt_Event_Spring_2020",
                  "Name" : "Springtide Event XP",
                  "Priority" : 100,
                  "XpToGrant" : 0
               }
            ]
         },
         {
            "DefaultXPAwarded" : 0,
            "Event" : "quest_completed",
            "EventMultiplier" : 1,000000000000000,
            "FirstTimeMultiplier" : 1,000000000000000,
            "Rules" : [
               {
                  "Name" : "Gold Quests",
                  "Priority" : 20,
                  "TagsToMatch" : [ "quest.hpxp.gold" ],
                  "XpToGrant" : 0
               },
               {
                  "ItemToMatch" : "CR19_S2_Q1_MegaQuest_8",
                  "Name" : "Into the Maelstrom HACK",
                  "Priority" : 100,
                  "XpToGrant" : 0,0000000000000000
               },
               {
                  "Name" : "Silver Quests",
                  "Priority" : 10,
                  "TagsToMatch" : [ "quest.hpxp.silver" ],
                  "XpToGrant" : 0
               },
               {
                  "Name" : "Bronze Quests",
                  "Priority" : 10,
                  "TagsToMatch" : [ "quest.hpxp.bronze" ],
                  "XpToGrant" : 0
               }
            ]
         },
         {
            "Event" : "bounty_completed",
            "EventMultiplier" : 1,000000000000000,
            "FirstTimeMultiplier" : 1,000000000000000,
            "Rules" : [
               {
                  "Name" : "Bounty-Bronze",
                  "TagsToMatch" : [ "bounty.bronze" ],
                  "XpToGrant" : 20,00000000000000
               },
               {
                  "Name" : "Bounty-Silver",
                  "TagsToMatch" : [ "bounty.silver" ],
                  "XpToGrant" : 40,00000000000000
               },
               {
                  "Name" : "Bounty-Gold",
                  "TagsToMatch" : [ "bounty.gold" ],
                  "XpToGrant" : 100,0000000000000
               }
            ]
         }
      ],
      "GlobalConfig" : {
         "DifficultyBias" : 1,000000000000000,
         "GlobalMultiplier" : 1,000000000000000,
         "MaxXPAwarded" : 200
      }
   }
}
```