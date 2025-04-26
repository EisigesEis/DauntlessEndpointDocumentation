URL: https://mailbox-prod.steelyard.ca/patchnotes/{language}/{gameversion} \
Method: GET \
Auth: No

---

## Comment
Retrieve patch notes for i.e. language=`en` and gameversion=`647472_rel-1.14.7_shipping`

## Example Request
No payload.

## Example Response
```json
{
  "code": null,
  "message": "OK",
  "payload": {
    "date": "2024-12-19T18:00:00.000+00:00",
    "description": "2.1.1 Frostfall, loads of bug fixes, and more!",
    "language": "en",
    "notes": [
      {
        "sections": [
          {
            "changes": [
              {
                "list": [
                  "Please note these Patch Notes are being published a few days **early** to give exposure to the upcoming fixes. Changes will go live on **December 19th**!"
                ]
              }
            ],
            "title": "Early Patch Notes",
            "type": "default"
          },
          {
            "background": "/assets/media/posts/news/frostfall_2024_MOTD.jpg",
            "description": "Frostfall is here, including a new Event hunt, facing off against the Cheerless Charrogg:<br/><br/>*The Cheerless Charrogg has long been a fairytale told to ill-tempered children of the isles during Frostfall.*<br/><br/>*This season, however, the childrens' collective petulance reverberated far enough to penetrate into dense deposits of unstable Aether and it has erupted from innocent imagination into grim reality.*<br/><br/>*Beware, The Cheerless Charrogg is an unstoppable humbug that can be damaged, but not killed. Pummel it with all the snowballs and holiday cheer possible to survive until it retreats back into the fireside folklore it came from.*<br/><br/>More details in your Inbox!",
            "title": "Frostfall",
            "type": "featured"
          }
        ],
        "title": "New to Dauntless",
        "type": "new_to_dauntless"
      },
      {
        "sections": [
          {
            "changes": [
              {
                "list": [
                  "Fixed an issue with Behemoth attacks becoming **out of sync** between the game client and server after enrage, resulting in players being hit by attacks that did not visually seem to have hit them yet",
                  "Fixed an issue where **Epic parts** were not correctly dropping from some Dire Behemoths that used to have Heroic versions pre-*Awakening*",
                  "Fixed an issue that caused players to **not always be staggered** in the correct direction by heavy Behemoth attacks",
                  "Fixed **Karkonos'** parts being unintentionally hard to break during the Titan's Awakening event",
                  "Fixed **Karkonos'** umbral pools not doing damage to players",
                  "Fixed **Karkonos'** missile attack no longer activating after the first few salvos",
                  "Fixed a rare issue where **Karkonos** could turn invisible temporarily",
                  "Fixed horn parts for **Boreus**, **Chronovore**, **Embermane**, and **Karkonos** incorrectly being set as a second head so it wasn't breaking to the intended weapons",
                  "Fixed **Embermane** sometimes not spawning a fireball when intended during attacks",
                  "Fixed an issue causing **Frostwülf's** ice pools to spawn collision above the ground",
                  "Re-enabled mounting attack on **Malkarion** that had previously been disabled in a server hotfix to temporarily address a crash",
                  "Fixed **Shrike's** tornado attack visual effect sometimes not spawning"
                ]
              }
            ],
            "title": "Behemoths",
            "type": "boreus"
          },
          {
            "changes": [
              {
                "list": [
                  "Fixed **Alluring Moons**-spawned Chaox having player collision blocking movement",
                  "Fixed an exploit that allowed players to spawn infinite Chaox using **Alluring Moons**",
                  "Removed a debug visualization that could spawn around **Firestorm's** projectiles",
                  "Fixed **Golden Claws'** Passive III talent stacking infinitely, and also addressed it doing unintentionally high increased damage even without stacking",
                  "Fixed **The Hunger** and **Molten Edict** retaining equipped mod slots from pre-*Awakening* loadout",
                  "Fixed an issue that could cause a texture to stretch from the model for **Reaper's Edge**",
                  "Fixed **The Anvil** being able to max Speed stacks by weapon swapping with Passive talent IV",
                  "Fixed **The Godhand's** passive glyph continuing to trigger after swapping to another weapon"
                ]
              }
            ],
            "title": "Weapons",
            "type": "repeaters"
          },
          {
            "changes": [
              {
                "list": [
                  "Fixed an issue resulting in the intended weekly **Heroic Escalation** rewards not being granted on completion",
                  "Fixed **Escalation 10-50s** still spawning Heroic Behemoths",
                  "Fixed **combat audio** not playing during Escalations",
                  "Fixed the **Planar Voyage** modifier sometimes giving an unintended -10 Defense stacks at the end of the round",
                  "Removing the **Chronostones** reward from the Radiant Escalation puzzle"
                ]
              }
            ],
            "title": "Escalations",
            "type": "escalation"
          },
          {
            "changes": [
              {
                "list": [
                  "Replaced the **Scorchstone Hellion** spawn on **Cape Fury (Surge)** with the intended **Bloodfire Embermane**, giving them two guaranteed spawns each, and addressing a blocker in the Behemoth Survey: Cape Fury (Surge) side quest",
                  "Stopped **Chronostones** dropping from island events on The Paradox Breaks",
                  "Fixed an issue that could cause fauna, gatherables, and patrol chests to not spawn on the following Surge islands: **Hades Reach**, **Undervald Defile**, **Aulric's Peak**, **Razorcliff Isle**, **Cape Fury**, and **Snowblind Waste**",
                  "Fixed an issue causing the big storm-nado to not appear in the middle of **Cape Fury**'s Surge version"
                ]
              }
            ],
            "title": "Hunting Grounds",
            "type": "hunting_grounds"
          },
          {
            "changes": [
              {
                "list": [
                  "Fixed some **lanterns** near Kat in Ramsgate giving off an unintended purple glow"
                ]
              }
            ],
            "title": "Ramsgate",
            "type": "ramsgate"
          },
          {
            "changes": [
              {
                "list": [
                  "Fixed **Rezakiri's** armour pieces requiring the Level 15 recipe at Level 10 as well"
                ]
              }
            ],
            "title": "Armour & Perks",
            "type": "armour"
          },
          {
            "changes": [
              {
                "list": [
                  "Fixed the **Reaching** the Apex main quest unlocking earlier than intended in progression",
                  "Fixed the dye Rumours for **Koshai**, **Riftstalker**, and **Valomyr** requiring kills of the now-removed Heroic versions",
                  "Fixed a missing objective string in Rumour: **Exquisite Sunburn (III)**",
                  "Removed a reference to the Middleman in Rumour: **Toxic Phage (II)**"
                ]
              }
            ],
            "title": "Quests",
            "type": "quests"
          },
          {
            "changes": [
              {
                "list": [
                  "Fixed **Curiosities not being consumed** from inventory when used. *Pack it up folks, party's over!*",
                  "Fixed **Hunt Pass Prestige Cores** not being listed separately from other Rare cores in the Core Breaker",
                  "Fixed **Assault Tonic** count reducing by 2 when only 1 is used",
                  "Fixed **Banners** not being individually customizable per loadout slot",
                  "Fixed **Head Accessories** being the same across all loadouts, despite the My Slayer screen showing the intended one equipped",
                  "Fixed the **Wildland Flute** emote's audio not stopping when the emote does",
                  "Fixed the rarity of the **Champion's Repeaters** transmog from Rare to Epic",
                  "Fixed the cosmetic versions of the pre-*Awakening* **lanterns** still granting gameplay effects",
                  "Fixed the **Quickslot 4** keyboard input still activating an item if it had been equipped to the slot pre-*Awakening*"
                ]
              }
            ],
            "title": "Items",
            "type": "default"
          },
          {
            "changes": [
              {
                "list": [
                  "Fixed crafting items that had been pinned pre-*Awakening* still remaining on the **Quest Tracker**",
                  "Fixed some quests unintentionally showing old crafting schematics as rewards in the **Quest Log** screen",
                  "Fixed effect layering obscuring the **weapon active ability** slot",
                  "Fixed **tracker information** sometimes not displaying correctly in player overheads",
                  "Fixed **“breadcrumbs”** not clearing after viewing the item in a number of cases in the **My Slayer** screen",
                  "Fixed a missing controller input prompt for Continue on the **Canister results** screen",
                  "Fixed a case that could cause **popups to stack multiple times** when trying to purchase more Platinum from the Canister results screen",
                  "Fixed the **Canister opening animation** being unintentionally stretched on wider aspect ratios",
                  "Fixed a poorly-visible Continue prompt on the **Message of the Day** popup",
                  "Fixed a **broken UI texture** that sometimes appeared around button prompts on Xbox One",
                  "Fixed a purchase confirmed text string showing when cancelling out of a Platinum purchase on **Steam**",
                  "Fixed some **long quest titles** flowing out of the NPC interaction screen",
                  "Fixed **unintended audio** behavior with hold prompts",
                  "Fixed videos in the **Move List** screen not looping on PlayStation 4 and PlayStation 5",
                  "Removed an input that could still allow access to the **Reward Cache**",
                  "Removed an input that could allow access to a work-in-progress version of the **Hunt screen**",
                  "Fixed item names in the **Steam** checkout popup from appearing in the correct language"
                ]
              }
            ],
            "title": "UI",
            "type": "ui"
          },
          {
            "changes": [
              {
                "list": [
                  "Enabled **dynamic resolution** (with a lower bound of 70% of 4K) as a short-term assist to performance on **PlayStation 5** and **Xbox Series X**. Please note that improving performance more generally across all our platforms remains high on our priority list"
                ]
              }
            ],
            "title": "Performance",
            "type": "performance"
          },
          {
            "changes": [
              {
                "list": [
                  "Fixed an issue causing **timeouts** loading into the game on accounts that had heavily customized their cosmetic setup per loadout, and had a high number of loadouts",
                  "Fixed a **server crash** that could occur when mounting Malkarion due to a missing file in the game package",
                  "Fixed a rare server crash related to **weapon swapping**",
                  "Fixed a rare client crash in the **colour picker UI**",
                  "Fixed a rare client crash related to **breadcrumbs**",
                  "Fixed a rare client crash related to the **Umbral elemental effect**"
                ]
              }
            ],
            "title": "Stability",
            "type": "default"
          },
          {
            "changes": [
              {
                "list": [
                  "Fixed an issue with the Steam version of the game not detecting **language** correctly",
                  "Fixed an issue with a portion of UI strings not displaying correctly in **Spanish**, and falling back to English",
                  "Miscellaneous **text and localization** fixes"
                ]
              }
            ],
            "title": "Localization",
            "type": "default"
          }
        ],
        "title": "Bug Fixes",
        "type": "bug_fixes"
      },
      {
        "sections": [
          {
            "changes": [
              {
                "list": [
                  "**Moonreaver Shrike's** wing swipe projectile now adds the **Shocked** debuff if hit",
                  "Allowed **Sporestruck Charrogg** to use more of its moves outside Enrage, to reduce encounter downtime"
                ]
              }
            ],
            "title": "Behemoths",
            "type": "shrike"
          },
          {
            "changes": [
              {
                "list": [
                  "Removed the **Steel Marks** requirement for the third Weapon Talent unlock on all weapons",
                  "Fixed **Fury of the Mountain's** Special IV talent so it correctly gives a Determination gain of 15 (was 5)",
                  "Increased duration of **Oathkeeper's** legendary ability from a default of 15 seconds to 30 seconds",
                  "Increased **Oathkeeper's** Legendary III talent from 5 to 10 seconds",
                  "Stopped players from being able to hit or redirect lightning orbs spawned by **Skies of Ostia** turrets, as they can get in the way and cause you to do less damage",
                  "Lowered **The Living Branch's** legendary ability default cooldown from 60 to 40 seconds (and with the talent, 40 seconds to 20 seconds)",
                  "Lowered **The Silver Sword's** legendary ability cooldown from 90 to 50 seconds"
                ]
              }
            ],
            "title": "Weapons",
            "type": "axe"
          },
          {
            "changes": [
              {
                "list": [
                  "Basic **attack damage** increased by 10-20% each",
                  "Light attacks grant **3 meter** per hit",
                  "**Active talent II** buffed from 5% to 15%",
                  "**Passive talent I** buffed from 30% to 40%",
                  "**Passive talent II** now also works with **Passive talent V**",
                  "**Passive talent V** no longer gives a defense penalty, now just gives 4 Defense while in Verge of Night"
                ]
              }
            ],
            "title": "Buffing The Hunger",
            "type": "sword"
          },
          {
            "changes": [
              {
                "list": [
                  "Added existing Blazeworks **75% XP boost** to all Level 60 Hunting Grounds, and removed it from the Level 30 Blazeworks",
                  "Tuned down the power level of Behemoths on Level 60 islands, as they were hitting harder than intended"
                ]
              }
            ],
            "title": "Hunting Grounds",
            "type": "hunting_grounds"
          },
          {
            "changes": [
              {
                "list": [
                  "Replaced the **Predator** perk on Shrike armour with **Cunning**, and on Malkarion armour with **Sharpened**",
                  "The **Predator** perk’s cost has been reduced from 8 to 5",
                  "The **Strategist** perk now stacks up to 500 shields (please note that the text string will be updated in the next patch)",
                  "The **Fortress** perk increased from 120 to 150 shields"
                ]
              }
            ],
            "title": "Armour & Perks",
            "type": "armour"
          },
          {
            "changes": [
              {
                "list": [
                  "Rebalanced Hunt Pass **Prestige Core** drop tables to give more guaranteed Rams and Aetherite",
                  "Significantly increased **Rams** rewards from (almost) all **Main** and **Side quests**, and added **Rams** rewards to a few **Side Quests** that didn't have them",
                  "Increased average **Rams** dropped from **Patrol Chests**",
                  "Increased **Rams** dropped from Behemoth kills from a range of 100-500 to 115-1000, based on Behemoth level",
                  "Adjusted **Chaox** kill Ram drops to better balance with Behemoth kill drops"
                ]
              }
            ],
            "title": "Economy",
            "type": "balance"
          }
        ],
        "title": "Balance",
        "type": "balance"
      },
      {
        "sections": [
          {
            "changes": [
              {
                "list": [
                  "Removed **weapon swap combos** from the move list panel in the **Training Grounds**, to avoid confusion for early game players who only have one weapon equipped, and so cannot complete them. They still show in the full Move List menu"
                ]
              }
            ],
            "title": "Training Grounds",
            "type": "hunting_grounds"
          },
          {
            "changes": [
              {
                "list": [
                  "Fixed **Emberthorn Cove** sometimes matchmaking in other players - it is intended to be a tutorial island for new players"
                ]
              }
            ],
            "title": "Hunting Grounds",
            "type": "embermane"
          },
          {
            "changes": [
              {
                "list": [
                  "Re-added the HUD icon for the **Pulse** perk for better tracking"
                ]
              }
            ],
            "title": "Armour & Perks",
            "type": "armour"
          },
          {
            "changes": [
              {
                "list": [
                  "The main quest **A Heroic Accomplishment** no longer requires main quest **Karkonos Rising** to be completed first, to allow players faster access to **Dauntless Trials** and **Heroic Escalation**",
                  "The side quest **Medicinal Purposes** (which unlocks tonic crafting) no longer requires the side quest The Slayer's Path to be completed first",
                  "Main quests **Welcome Back, Slayer!** and **Basic Slaying** now both unlock from the start for returning players, to avoid a rare case where they could get stuck unable to unlock Basic Slaying in order to proceed through the game"
                ]
              }
            ],
            "title": "Quests",
            "type": "quests"
          }
        ],
        "title": "Quality of Life",
        "type": "quality_of_life"
      }
    ],
    "permalink": "/patch-notes/2-1-1/",
    "release_version": "2.1.1",
    "title": "Awakening"
  }
}
```