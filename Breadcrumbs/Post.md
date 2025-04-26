URL: https://breadcrumbs-prod.steelyard.ca/breadcrumbs/{Character ID} \
Method: POST \
Auth: Yes

---

## Comment


## Example Request
```json
{
  "breadcrumbs": [
    {
      "active_types": 2,
      "breadcrumb_id": "Item",
      "categories": ["Breadcrumb.PlayerJourney.Tabs"]
    },
    {
      "active_types": 2,
      "breadcrumb_id": "TutorialSlate_Aetherite",
      "categories": ["Breadcrumb.Journal.TutorialInfo.Equipment"]
    },
    {
      "active_types": 2,
      "breadcrumb_id": "TutorialSlate_EquipCells",
      "categories": ["Breadcrumb.Journal.TutorialInfo.Equipment"]
    },
    {
      "active_types": 2,
      "breadcrumb_id": "TutorialSlate_Equip_Gear",
      "categories": ["Breadcrumb.Journal.TutorialInfo.Equipment"]
    },
    {
      "active_types": 2,
      "breadcrumb_id": "TutorialSlate_PerksArmourCells",
      "categories": ["Breadcrumb.Journal.TutorialInfo.Equipment"]
    },
    {
      "active_types": 2,
      "breadcrumb_id": "TutorialSlate_Behemoth_Tracking",
      "categories": ["Breadcrumb.Journal.TutorialInfo.Basics"]
    },
    {
      "active_types": 2,
      "breadcrumb_id": "TutorialSlate_DamageTypeSwap",
      "categories": ["Breadcrumb.Journal.TutorialInfo.Basics"]
    },
    {
      "active_types": 2,
      "breadcrumb_id": "TutorialSlate_HuntBoard",
      "categories": ["Breadcrumb.Journal.TutorialInfo.Basics"]
    },
    {
      "active_types": 2,
      "breadcrumb_id": "TutorialSlate_Map",
      "categories": ["Breadcrumb.Journal.TutorialInfo.Basics"]
    },
    {
      "active_types": 2,
      "breadcrumb_id": "TutorialSlate_QuestInfo",
      "categories": ["Breadcrumb.Journal.TutorialInfo.Basics"]
    },
    {
      "active_types": 2,
      "breadcrumb_id": "TutorialSlate_Social",
      "categories": ["Breadcrumb.Journal.TutorialInfo.Basics"]
    },
    {
      "active_types": 2,
      "breadcrumb_id": "TutorialSlate_StarterWeapons",
      "categories": ["Breadcrumb.Journal.TutorialInfo.Basics"]
    },
    {
      "active_types": 2,
      "breadcrumb_id": "TutorialSlate_Gliders",
      "categories": ["Breadcrumb.Journal.TutorialInfo.Other"]
    },
    {
      "active_types": 2,
      "breadcrumb_id": "TutorialSlate_Linked_Slayer",
      "categories": ["Breadcrumb.Journal.TutorialInfo.Other"]
    },
    {
      "active_types": 2,
      "breadcrumb_id": "lerawr_normal",
      "categories": ["Breadcrumb.Journal.BehemothInfo"]
    },
    {
      "active_types": 2,
      "breadcrumb_id": "D24_A_MAIN_03B",
      "categories": ["Breadcrumb.Quest"]
    },
    {
      "active_types": 1,
      "breadcrumb_id": "0",
      "categories": [
        "Breadcrumb.Challenges.Daily",
        "Breadcrumb.Challenges.Weekly.00"
      ]
    },
    {
      "active_types": 2,
      "breadcrumb_id": "1",
      "categories": ["Breadcrumb.Challenges.Weekly.01"]
    },
    {
      "active_types": 2,
      "breadcrumb_id": "10",
      "categories": ["Breadcrumb.Challenges.Weekly.10"]
    },
    {
      "active_types": 2,
      "breadcrumb_id": "11",
      "categories": ["Breadcrumb.Challenges.Weekly.11"]
    },
    {
      "active_types": 2,
      "breadcrumb_id": "12",
      "categories": ["Breadcrumb.Challenges.Weekly.12"]
    },
    {
      "active_types": 2,
      "breadcrumb_id": "13",
      "categories": ["Breadcrumb.Challenges.Weekly.13"]
    },
    {
      "active_types": 2,
      "breadcrumb_id": "14",
      "categories": ["Breadcrumb.Challenges.Weekly.14"]
    },
    {
      "active_types": 2,
      "breadcrumb_id": "15",
      "categories": ["Breadcrumb.Challenges.Weekly.15"]
    },
    {
      "active_types": 2,
      "breadcrumb_id": "16",
      "categories": ["Breadcrumb.Challenges.Weekly.16"]
    },
    {
      "active_types": 2,
      "breadcrumb_id": "17",
      "categories": ["Breadcrumb.Challenges.Weekly.17"]
    },
    {
      "active_types": 2,
      "breadcrumb_id": "18",
      "categories": ["Breadcrumb.Challenges.Weekly.18"]
    },
    {
      "active_types": 2,
      "breadcrumb_id": "19",
      "categories": ["Breadcrumb.Challenges.Weekly.19"]
    },
    {
      "active_types": 2,
      "breadcrumb_id": "2",
      "categories": ["Breadcrumb.Challenges.Weekly.02"]
    },
    {
      "active_types": 2,
      "breadcrumb_id": "3",
      "categories": ["Breadcrumb.Challenges.Weekly.03"]
    },
    {
      "active_types": 2,
      "breadcrumb_id": "4",
      "categories": ["Breadcrumb.Challenges.Weekly.04"]
    },
    {
      "active_types": 2,
      "breadcrumb_id": "5",
      "categories": ["Breadcrumb.Challenges.Weekly.05"]
    },
    {
      "active_types": 2,
      "breadcrumb_id": "6",
      "categories": ["Breadcrumb.Challenges.Weekly.06"]
    },
    {
      "active_types": 2,
      "breadcrumb_id": "7",
      "categories": ["Breadcrumb.Challenges.Weekly.07"]
    },
    {
      "active_types": 2,
      "breadcrumb_id": "8",
      "categories": ["Breadcrumb.Challenges.Weekly.08"]
    },
    {
      "active_types": 2,
      "breadcrumb_id": "9",
      "categories": ["Breadcrumb.Challenges.Weekly.09"]
    }
  ],
  "version": 19
}
```

## Example Reponse
```json
{
  "code": null,
  "message": "OK",
  "payload": {
    "breadcrumbs": [
      {
        "active_types": 1,
        "breadcrumb_id": "0",
        "categories": [
          "Breadcrumb.Challenges.Daily",
          "Breadcrumb.Challenges.Weekly.00"
        ],
        "timestamp": 1745622414.0
      },
      {
        "active_types": 2,
        "breadcrumb_id": "1",
        "categories": ["Breadcrumb.Challenges.Weekly.01"],
        "timestamp": 1745622414.0
      },
      {
        "active_types": 2,
        "breadcrumb_id": "10",
        "categories": ["Breadcrumb.Challenges.Weekly.10"],
        "timestamp": 1745622414.0
      },
      {
        "active_types": 2,
        "breadcrumb_id": "11",
        "categories": ["Breadcrumb.Challenges.Weekly.11"],
        "timestamp": 1745622414.0
      },
      {
        "active_types": 2,
        "breadcrumb_id": "12",
        "categories": ["Breadcrumb.Challenges.Weekly.12"],
        "timestamp": 1745622414.0
      },
      {
        "active_types": 2,
        "breadcrumb_id": "13",
        "categories": ["Breadcrumb.Challenges.Weekly.13"],
        "timestamp": 1745622414.0
      },
      {
        "active_types": 2,
        "breadcrumb_id": "14",
        "categories": ["Breadcrumb.Challenges.Weekly.14"],
        "timestamp": 1745622414.0
      },
      {
        "active_types": 2,
        "breadcrumb_id": "15",
        "categories": ["Breadcrumb.Challenges.Weekly.15"],
        "timestamp": 1745622414.0
      },
      {
        "active_types": 2,
        "breadcrumb_id": "16",
        "categories": ["Breadcrumb.Challenges.Weekly.16"],
        "timestamp": 1745622414.0
      },
      {
        "active_types": 2,
        "breadcrumb_id": "17",
        "categories": ["Breadcrumb.Challenges.Weekly.17"],
        "timestamp": 1745622414.0
      },
      {
        "active_types": 2,
        "breadcrumb_id": "18",
        "categories": ["Breadcrumb.Challenges.Weekly.18"],
        "timestamp": 1745622414.0
      },
      {
        "active_types": 2,
        "breadcrumb_id": "19",
        "categories": ["Breadcrumb.Challenges.Weekly.19"],
        "timestamp": 1745622414.0
      },
      {
        "active_types": 2,
        "breadcrumb_id": "2",
        "categories": ["Breadcrumb.Challenges.Weekly.02"],
        "timestamp": 1745622414.0
      },
      {
        "active_types": 2,
        "breadcrumb_id": "3",
        "categories": ["Breadcrumb.Challenges.Weekly.03"],
        "timestamp": 1745622414.0
      },
      {
        "active_types": 2,
        "breadcrumb_id": "4",
        "categories": ["Breadcrumb.Challenges.Weekly.04"],
        "timestamp": 1745622414.0
      },
      {
        "active_types": 2,
        "breadcrumb_id": "5",
        "categories": ["Breadcrumb.Challenges.Weekly.05"],
        "timestamp": 1745622414.0
      },
      {
        "active_types": 2,
        "breadcrumb_id": "6",
        "categories": ["Breadcrumb.Challenges.Weekly.06"],
        "timestamp": 1745622414.0
      },
      {
        "active_types": 2,
        "breadcrumb_id": "7",
        "categories": ["Breadcrumb.Challenges.Weekly.07"],
        "timestamp": 1745622414.0
      },
      {
        "active_types": 2,
        "breadcrumb_id": "8",
        "categories": ["Breadcrumb.Challenges.Weekly.08"],
        "timestamp": 1745622414.0
      },
      {
        "active_types": 2,
        "breadcrumb_id": "9",
        "categories": ["Breadcrumb.Challenges.Weekly.09"],
        "timestamp": 1745622414.0
      },
      {
        "active_types": 2,
        "breadcrumb_id": "Item",
        "categories": ["Breadcrumb.PlayerJourney.Tabs"],
        "timestamp": 1745622414.0
      },
      {
        "active_types": 2,
        "breadcrumb_id": "TutorialSlate_Aetherite",
        "categories": ["Breadcrumb.Journal.TutorialInfo.Equipment"],
        "timestamp": 1745622414.0
      },
      {
        "active_types": 2,
        "breadcrumb_id": "TutorialSlate_Behemoth_Tracking",
        "categories": ["Breadcrumb.Journal.TutorialInfo.Basics"],
        "timestamp": 1745622414.0
      },
      {
        "active_types": 2,
        "breadcrumb_id": "TutorialSlate_DamageTypeSwap",
        "categories": ["Breadcrumb.Journal.TutorialInfo.Basics"],
        "timestamp": 1745622414.0
      },
      {
        "active_types": 2,
        "breadcrumb_id": "TutorialSlate_EquipCells",
        "categories": ["Breadcrumb.Journal.TutorialInfo.Equipment"],
        "timestamp": 1745622414.0
      },
      {
        "active_types": 2,
        "breadcrumb_id": "TutorialSlate_Equip_Gear",
        "categories": ["Breadcrumb.Journal.TutorialInfo.Equipment"],
        "timestamp": 1745622414.0
      },
      {
        "active_types": 2,
        "breadcrumb_id": "TutorialSlate_Gliders",
        "categories": ["Breadcrumb.Journal.TutorialInfo.Other"],
        "timestamp": 1745622414.0
      },
      {
        "active_types": 2,
        "breadcrumb_id": "TutorialSlate_HuntBoard",
        "categories": ["Breadcrumb.Journal.TutorialInfo.Basics"],
        "timestamp": 1745622414.0
      },
      {
        "active_types": 2,
        "breadcrumb_id": "TutorialSlate_Linked_Slayer",
        "categories": ["Breadcrumb.Journal.TutorialInfo.Other"],
        "timestamp": 1745622414.0
      },
      {
        "active_types": 2,
        "breadcrumb_id": "TutorialSlate_Map",
        "categories": ["Breadcrumb.Journal.TutorialInfo.Basics"],
        "timestamp": 1745622414.0
      },
      {
        "active_types": 2,
        "breadcrumb_id": "TutorialSlate_PerksArmourCells",
        "categories": ["Breadcrumb.Journal.TutorialInfo.Equipment"],
        "timestamp": 1745622414.0
      },
      {
        "active_types": 2,
        "breadcrumb_id": "TutorialSlate_QuestInfo",
        "categories": ["Breadcrumb.Journal.TutorialInfo.Basics"],
        "timestamp": 1745622414.0
      },
      {
        "active_types": 2,
        "breadcrumb_id": "TutorialSlate_Social",
        "categories": ["Breadcrumb.Journal.TutorialInfo.Basics"],
        "timestamp": 1745622414.0
      },
      {
        "active_types": 2,
        "breadcrumb_id": "TutorialSlate_StarterWeapons",
        "categories": ["Breadcrumb.Journal.TutorialInfo.Basics"],
        "timestamp": 1745622414.0
      },
      {
        "active_types": 2,
        "breadcrumb_id": "lerawr_normal",
        "categories": ["Breadcrumb.Journal.BehemothInfo"],
        "timestamp": 1745622414.0
      },
      {
        "active_types": 2,
        "breadcrumb_id": "D24_A_MAIN_03B",
        "categories": ["Breadcrumb.Quest"],
        "timestamp": 1745622414.0
      }
    ],
    "version": 19
  }
}
```