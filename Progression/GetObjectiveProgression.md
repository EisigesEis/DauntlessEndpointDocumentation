URL: https://progression-prod.steelyard.ca/progression/objectives/{PHXL ID} \
Method: GET \
Auth: Yes

---

## Comment
Gives progress on achievements and mastery objectives.

Others' PHXL IDs get 403 Forbidden... Why have PHXL ID in url then?

## Example Request
No Payload.

## Example Response
```json
{
  "code": null,
  "message": "OK",
  "payload": [
    {
      "completed_count": 1,
      "created_date": "2025-04-25T22:46:52.544242+00:00",
      "last_modified_date": "2025-04-22T09:44:22",
      "objective_id": "AchievementObjective_Craft_AllElements_Blaze_New",
      "phx_account_id": "U2BLWVTDHZGWLBKKLY2QG6UX4I",
      "progress": 1
    },
    {
      "completed_count": 1,
      "created_date": "2025-04-25T22:46:52.544553+00:00",
      "last_modified_date": "2025-04-22T09:43:57",
      "objective_id": "AchievementObjective_Craft_AllElements_Frost_New",
      "phx_account_id": "U2BLWVTDHZGWLBKKLY2QG6UX4I",
      "progress": 1
    },
    {
      "completed_count": 1,
      "created_date": "2025-04-25T22:46:52.544700+00:00",
      "last_modified_date": "2025-04-22T09:44:22",
      "objective_id": "AchievementObjective_Craft_AllElements_Shock_New",
      "phx_account_id": "U2BLWVTDHZGWLBKKLY2QG6UX4I",
      "progress": 1
    },
    {
      "completed_count": 1,
      "created_date": "2025-04-25T22:46:52.544831+00:00",
      "last_modified_date": "2025-04-22T09:44:22",
      "objective_id": "AchievementObjective_Craft_AllElements_Terra_New",
      "phx_account_id": "U2BLWVTDHZGWLBKKLY2QG6UX4I",
      "progress": 1
    },
    {
      "completed_count": 1,
      "created_date": "2025-04-25T22:46:52.545029+00:00",
      "last_modified_date": "2025-04-22T09:44:22",
      "objective_id": "AchievementObjective_Craft_DP_AllElements_Blaze",
      "phx_account_id": "U2BLWVTDHZGWLBKKLY2QG6UX4I",
      "progress": 1
    },
    {
      "completed_count": 1,
      "created_date": "2025-04-25T22:46:52.545159+00:00",
      "last_modified_date": "2025-04-22T09:43:57",
      "objective_id": "AchievementObjective_Craft_DP_AllElements_Frost",
      "phx_account_id": "U2BLWVTDHZGWLBKKLY2QG6UX4I",
      "progress": 1
    },
    {
      "completed_count": 1,
      "created_date": "2025-04-25T22:46:52.545282+00:00",
      "last_modified_date": "2025-04-22T09:44:22",
      "objective_id": "AchievementObjective_Craft_DP_AllElements_Shock",
      "phx_account_id": "U2BLWVTDHZGWLBKKLY2QG6UX4I",
      "progress": 1
    },
    {
      "completed_count": 1,
      "created_date": "2025-04-25T22:46:52.545403+00:00",
      "last_modified_date": "2025-04-22T09:44:22",
      "objective_id": "AchievementObjective_Craft_DP_AllElements_Terra",
      "phx_account_id": "U2BLWVTDHZGWLBKKLY2QG6UX4I",
      "progress": 1
    },
    {
      "completed_count": 1,
      "created_date": "2025-04-25T22:46:52.545524+00:00",
      "last_modified_date": "2025-04-22T10:50:25",
      "objective_id": "AchievementObjective_Crafter_Craft",
      "phx_account_id": "U2BLWVTDHZGWLBKKLY2QG6UX4I",
      "progress": 1
    },
    {
      "completed_count": 0,
      "created_date": "2025-04-25T22:46:52.545646+00:00",
      "last_modified_date": "2025-04-22T10:55:29",
      "objective_id": "AchievementObjective_Equip_CellEffect_Six_LvlSix",
      "phx_account_id": "U2BLWVTDHZGWLBKKLY2QG6UX4I",
      "progress": 5
    },
    {
      "completed_count": 0,
      "created_date": "2025-04-25T22:46:52.545764+00:00",
      "last_modified_date": "2025-04-22T10:57:30",
      "objective_id": "AchievementObjective_Reforge_AnyWeapon",
      "phx_account_id": "U2BLWVTDHZGWLBKKLY2QG6UX4I",
      "progress": 3
    },
    {
      "completed_count": 0,
      "created_date": "2025-04-25T22:46:52.545904+00:00",
      "last_modified_date": "2025-04-22T09:47:31",
      "objective_id": "MasteryObjective_Behemoth_Embermane_Boop",
      "phx_account_id": "U2BLWVTDHZGWLBKKLY2QG6UX4I",
      "progress": 1
    },
    {
      "completed_count": 0,
      "created_date": "2025-04-25T22:46:52.546047+00:00",
      "last_modified_date": "2025-04-22T09:47:31",
      "objective_id": "MasteryObjective_Behemoth_Embermane_Boop_X_Times",
      "phx_account_id": "U2BLWVTDHZGWLBKKLY2QG6UX4I",
      "progress": 1
    },
    {
      "completed_count": 0,
      "created_date": "2025-04-25T22:46:52.546164+00:00",
      "last_modified_date": "2025-04-22T09:47:31",
      "objective_id": "MasteryObjective_Behemoth_Embermane_Boop_Y_Times",
      "phx_account_id": "U2BLWVTDHZGWLBKKLY2QG6UX4I",
      "progress": 1
    },
    {
      "completed_count": 0,
      "created_date": "2025-04-25T22:46:52.546281+00:00",
      "last_modified_date": "2025-04-22T09:47:31",
      "objective_id": "MasteryObjective_Behemoth_Embermane_Break_X_Times",
      "phx_account_id": "U2BLWVTDHZGWLBKKLY2QG6UX4I",
      "progress": 6
    },
    {
      "completed_count": 0,
      "created_date": "2025-04-25T22:46:52.546396+00:00",
      "last_modified_date": "2025-04-22T09:47:31",
      "objective_id": "MasteryObjective_Behemoth_Embermane_Break_Y_Times",
      "phx_account_id": "U2BLWVTDHZGWLBKKLY2QG6UX4I",
      "progress": 6
    },
    {
      "completed_count": 0,
      "created_date": "2025-04-25T22:46:52.546512+00:00",
      "last_modified_date": "2025-04-22T09:47:31",
      "objective_id": "MasteryObjective_Behemoth_Embermane_Break_Z_Times",
      "phx_account_id": "U2BLWVTDHZGWLBKKLY2QG6UX4I",
      "progress": 6
    },
    {
      "completed_count": 1,
      "created_date": "2025-04-25T22:46:52.546628+00:00",
      "last_modified_date": "2025-04-22T10:50:27",
      "objective_id": "MasteryObjective_Behemoth_Embermane_Craft_Armor",
      "phx_account_id": "U2BLWVTDHZGWLBKKLY2QG6UX4I",
      "progress": 1
    },
    {
      "completed_count": 0,
      "created_date": "2025-04-25T22:46:52.546744+00:00",
      "last_modified_date": "2025-04-22T09:47:42",
      "objective_id": "MasteryObjective_Behemoth_Embermane_Damage",
      "phx_account_id": "U2BLWVTDHZGWLBKKLY2QG6UX4I",
      "progress": 20141
    },
    {
      "completed_count": 1,
      "created_date": "2025-04-25T22:46:52.546860+00:00",
      "last_modified_date": "2025-04-22T09:47:30",
      "objective_id": "MasteryObjective_Behemoth_Embermane_Kill",
      "phx_account_id": "U2BLWVTDHZGWLBKKLY2QG6UX4I",
      "progress": 1
    },
    {
      "completed_count": 0,
      "created_date": "2025-04-25T22:46:52.547194+00:00",
      "last_modified_date": "2025-04-22T09:47:31",
      "objective_id": "MasteryObjective_Behemoth_Embermane_Stagger",
      "phx_account_id": "U2BLWVTDHZGWLBKKLY2QG6UX4I",
      "progress": 1
    },
    {
      "completed_count": 0,
      "created_date": "2025-04-25T22:46:52.547346+00:00",
      "last_modified_date": "2025-04-22T09:47:31",
      "objective_id": "MasteryObjective_Behemoth_Embermane_Stagger_X_Times",
      "phx_account_id": "U2BLWVTDHZGWLBKKLY2QG6UX4I",
      "progress": 1
    },
    {
      "completed_count": 0,
      "created_date": "2025-04-25T22:46:52.547477+00:00",
      "last_modified_date": "2025-04-22T09:47:31",
      "objective_id": "MasteryObjective_Behemoth_Embermane_Stagger_Y_Times",
      "phx_account_id": "U2BLWVTDHZGWLBKKLY2QG6UX4I",
      "progress": 1
    },
    {
      "completed_count": 0,
      "created_date": "2025-04-25T22:46:52.547614+00:00",
      "last_modified_date": "2025-04-22T09:47:42",
      "objective_id": "MasteryObjective_Behemoth_Embermane_XP",
      "phx_account_id": "U2BLWVTDHZGWLBKKLY2QG6UX4I",
      "progress": 112
    },
    {
      "completed_count": 1,
      "created_date": "2025-04-25T22:46:52.547740+00:00",
      "last_modified_date": "2025-04-22T09:46:31",
      "objective_id": "MasteryObjective_Weapon_Axe_FuryOfTheMountain_Craft",
      "phx_account_id": "U2BLWVTDHZGWLBKKLY2QG6UX4I",
      "progress": 1
    },
    {
      "completed_count": 0,
      "created_date": "2025-04-25T22:46:52.547884+00:00",
      "last_modified_date": "2025-04-22T09:47:42",
      "objective_id": "MasteryObjective_Weapon_Hammer_Generic_Damage1",
      "phx_account_id": "U2BLWVTDHZGWLBKKLY2QG6UX4I",
      "progress": 20141
    },
    {
      "completed_count": 0,
      "created_date": "2025-04-25T22:46:52.548012+00:00",
      "last_modified_date": "2025-04-22T09:47:42",
      "objective_id": "MasteryObjective_Weapon_Hammer_Generic_Damage2",
      "phx_account_id": "U2BLWVTDHZGWLBKKLY2QG6UX4I",
      "progress": 20141
    },
    {
      "completed_count": 0,
      "created_date": "2025-04-25T22:46:52.548132+00:00",
      "last_modified_date": "2025-04-22T09:47:42",
      "objective_id": "MasteryObjective_Weapon_Hammer_Generic_Damage3",
      "phx_account_id": "U2BLWVTDHZGWLBKKLY2QG6UX4I",
      "progress": 20141
    },
    {
      "completed_count": 0,
      "created_date": "2025-04-25T22:46:52.548254+00:00",
      "last_modified_date": "2025-04-22T09:47:42",
      "objective_id": "MasteryObjective_Weapon_Hammer_Generic_Damage4",
      "phx_account_id": "U2BLWVTDHZGWLBKKLY2QG6UX4I",
      "progress": 20141
    },
    {
      "completed_count": 0,
      "created_date": "2025-04-25T22:46:52.548374+00:00",
      "last_modified_date": "2025-04-22T09:47:42",
      "objective_id": "MasteryObjective_Weapon_Hammer_Generic_Damage5",
      "phx_account_id": "U2BLWVTDHZGWLBKKLY2QG6UX4I",
      "progress": 20141
    },
    {
      "completed_count": 0,
      "created_date": "2025-04-25T22:46:52.548514+00:00",
      "last_modified_date": "2025-04-22T09:47:42",
      "objective_id": "MasteryObjective_Weapon_Hammer_Generic_Damage6",
      "phx_account_id": "U2BLWVTDHZGWLBKKLY2QG6UX4I",
      "progress": 20141
    },
    {
      "completed_count": 0,
      "created_date": "2025-04-25T22:46:52.548643+00:00",
      "last_modified_date": "2025-04-22T09:47:42",
      "objective_id": "MasteryObjective_Weapon_Hammer_Generic_Damage7",
      "phx_account_id": "U2BLWVTDHZGWLBKKLY2QG6UX4I",
      "progress": 20141
    },
    {
      "completed_count": 0,
      "created_date": "2025-04-25T22:46:52.548763+00:00",
      "last_modified_date": "2025-04-22T09:47:42",
      "objective_id": "MasteryObjective_Weapon_Hammer_Generic_Damage8",
      "phx_account_id": "U2BLWVTDHZGWLBKKLY2QG6UX4I",
      "progress": 20141
    },
    {
      "completed_count": 0,
      "created_date": "2025-04-25T22:46:52.548897+00:00",
      "last_modified_date": "2025-04-22T09:47:31",
      "objective_id": "MasteryObjective_Weapon_Hammer_Generic_Kills1",
      "phx_account_id": "U2BLWVTDHZGWLBKKLY2QG6UX4I",
      "progress": 1
    },
    {
      "completed_count": 0,
      "created_date": "2025-04-25T22:46:52.549159+00:00",
      "last_modified_date": "2025-04-22T09:47:31",
      "objective_id": "MasteryObjective_Weapon_Hammer_Generic_Kills2",
      "phx_account_id": "U2BLWVTDHZGWLBKKLY2QG6UX4I",
      "progress": 1
    },
    {
      "completed_count": 0,
      "created_date": "2025-04-25T22:46:52.549288+00:00",
      "last_modified_date": "2025-04-22T09:47:31",
      "objective_id": "MasteryObjective_Weapon_Hammer_Generic_Kills3",
      "phx_account_id": "U2BLWVTDHZGWLBKKLY2QG6UX4I",
      "progress": 1
    },
    {
      "completed_count": 0,
      "created_date": "2025-04-25T22:46:52.549418+00:00",
      "last_modified_date": "2025-04-22T09:47:31",
      "objective_id": "MasteryObjective_Weapon_Hammer_Generic_Kills4",
      "phx_account_id": "U2BLWVTDHZGWLBKKLY2QG6UX4I",
      "progress": 1
    },
    {
      "completed_count": 0,
      "created_date": "2025-04-25T22:46:52.549539+00:00",
      "last_modified_date": "2025-04-22T09:47:31",
      "objective_id": "MasteryObjective_Weapon_Hammer_Generic_Kills5",
      "phx_account_id": "U2BLWVTDHZGWLBKKLY2QG6UX4I",
      "progress": 1
    },
    {
      "completed_count": 0,
      "created_date": "2025-04-25T22:46:52.549671+00:00",
      "last_modified_date": "2025-04-22T09:47:31",
      "objective_id": "MasteryObjective_Weapon_Hammer_Generic_Kills6",
      "phx_account_id": "U2BLWVTDHZGWLBKKLY2QG6UX4I",
      "progress": 1
    },
    {
      "completed_count": 0,
      "created_date": "2025-04-25T22:46:52.549787+00:00",
      "last_modified_date": "2025-04-22T09:47:31",
      "objective_id": "MasteryObjective_Weapon_Hammer_Generic_Kills7",
      "phx_account_id": "U2BLWVTDHZGWLBKKLY2QG6UX4I",
      "progress": 1
    },
    {
      "completed_count": 0,
      "created_date": "2025-04-25T22:46:52.549941+00:00",
      "last_modified_date": "2025-04-22T09:47:31",
      "objective_id": "MasteryObjective_Weapon_Hammer_Generic_Kills8",
      "phx_account_id": "U2BLWVTDHZGWLBKKLY2QG6UX4I",
      "progress": 1
    },
    {
      "completed_count": 0,
      "created_date": "2025-04-25T22:46:52.550062+00:00",
      "last_modified_date": "2025-04-22T09:47:42",
      "objective_id": "MasteryObjective_Weapon_Hammer_Generic_Shock_Damage1",
      "phx_account_id": "U2BLWVTDHZGWLBKKLY2QG6UX4I",
      "progress": 20141
    },
    {
      "completed_count": 0,
      "created_date": "2025-04-25T22:46:52.550178+00:00",
      "last_modified_date": "2025-04-22T09:47:42",
      "objective_id": "MasteryObjective_Weapon_Hammer_Generic_Shock_Damage2",
      "phx_account_id": "U2BLWVTDHZGWLBKKLY2QG6UX4I",
      "progress": 20141
    },
    {
      "completed_count": 0,
      "created_date": "2025-04-25T22:46:52.550294+00:00",
      "last_modified_date": "2025-04-22T09:47:42",
      "objective_id": "MasteryObjective_Weapon_Hammer_Generic_Shock_Damage3",
      "phx_account_id": "U2BLWVTDHZGWLBKKLY2QG6UX4I",
      "progress": 20141
    },
    {
      "completed_count": 0,
      "created_date": "2025-04-25T22:46:52.550411+00:00",
      "last_modified_date": "2025-04-22T09:47:42",
      "objective_id": "MasteryObjective_Weapon_Hammer_Generic_Shock_Damage4",
      "phx_account_id": "U2BLWVTDHZGWLBKKLY2QG6UX4I",
      "progress": 20141
    },
    {
      "completed_count": 0,
      "created_date": "2025-04-25T22:46:52.550527+00:00",
      "last_modified_date": "2025-04-22T09:47:42",
      "objective_id": "MasteryObjective_Weapon_Hammer_Generic_Shock_Damage5",
      "phx_account_id": "U2BLWVTDHZGWLBKKLY2QG6UX4I",
      "progress": 20141
    },
    {
      "completed_count": 0,
      "created_date": "2025-04-25T22:46:52.550655+00:00",
      "last_modified_date": "2025-04-22T09:47:42",
      "objective_id": "MasteryObjective_Weapon_Hammer_Generic_Shock_Damage6",
      "phx_account_id": "U2BLWVTDHZGWLBKKLY2QG6UX4I",
      "progress": 20141
    },
    {
      "completed_count": 0,
      "created_date": "2025-04-25T22:46:52.550771+00:00",
      "last_modified_date": "2025-04-22T09:47:42",
      "objective_id": "MasteryObjective_Weapon_Hammer_Generic_Shock_Damage7",
      "phx_account_id": "U2BLWVTDHZGWLBKKLY2QG6UX4I",
      "progress": 20141
    },
    {
      "completed_count": 0,
      "created_date": "2025-04-25T22:46:52.550903+00:00",
      "last_modified_date": "2025-04-22T09:47:42",
      "objective_id": "MasteryObjective_Weapon_Hammer_Generic_Shock_Damage8",
      "phx_account_id": "U2BLWVTDHZGWLBKKLY2QG6UX4I",
      "progress": 20141
    },
    {
      "completed_count": 0,
      "created_date": "2025-04-25T22:46:52.551096+00:00",
      "last_modified_date": "2025-04-22T09:47:31",
      "objective_id": "MasteryObjective_Weapon_Hammer_Generic_Stagger1",
      "phx_account_id": "U2BLWVTDHZGWLBKKLY2QG6UX4I",
      "progress": 1
    },
    {
      "completed_count": 0,
      "created_date": "2025-04-25T22:46:52.551218+00:00",
      "last_modified_date": "2025-04-22T09:47:31",
      "objective_id": "MasteryObjective_Weapon_Hammer_Generic_Stagger2",
      "phx_account_id": "U2BLWVTDHZGWLBKKLY2QG6UX4I",
      "progress": 1
    },
    {
      "completed_count": 0,
      "created_date": "2025-04-25T22:46:52.551336+00:00",
      "last_modified_date": "2025-04-22T09:47:31",
      "objective_id": "MasteryObjective_Weapon_Hammer_Generic_Stagger3",
      "phx_account_id": "U2BLWVTDHZGWLBKKLY2QG6UX4I",
      "progress": 1
    },
    {
      "completed_count": 0,
      "created_date": "2025-04-25T22:46:52.551507+00:00",
      "last_modified_date": "2025-04-22T09:47:31",
      "objective_id": "MasteryObjective_Weapon_Hammer_Generic_Stagger4",
      "phx_account_id": "U2BLWVTDHZGWLBKKLY2QG6UX4I",
      "progress": 1
    },
    {
      "completed_count": 0,
      "created_date": "2025-04-25T22:46:52.551649+00:00",
      "last_modified_date": "2025-04-22T09:47:31",
      "objective_id": "MasteryObjective_Weapon_Hammer_Generic_Stagger5",
      "phx_account_id": "U2BLWVTDHZGWLBKKLY2QG6UX4I",
      "progress": 1
    },
    {
      "completed_count": 0,
      "created_date": "2025-04-25T22:46:52.551768+00:00",
      "last_modified_date": "2025-04-22T09:47:31",
      "objective_id": "MasteryObjective_Weapon_Hammer_Generic_Stagger6",
      "phx_account_id": "U2BLWVTDHZGWLBKKLY2QG6UX4I",
      "progress": 1
    },
    {
      "completed_count": 0,
      "created_date": "2025-04-25T22:46:52.551903+00:00",
      "last_modified_date": "2025-04-22T09:47:31",
      "objective_id": "MasteryObjective_Weapon_Hammer_Generic_Stagger7",
      "phx_account_id": "U2BLWVTDHZGWLBKKLY2QG6UX4I",
      "progress": 1
    },
    {
      "completed_count": 0,
      "created_date": "2025-04-25T22:46:52.552021+00:00",
      "last_modified_date": "2025-04-22T09:47:31",
      "objective_id": "MasteryObjective_Weapon_Hammer_Generic_Stagger8",
      "phx_account_id": "U2BLWVTDHZGWLBKKLY2QG6UX4I",
      "progress": 1
    },
    {
      "completed_count": 1,
      "created_date": "2025-04-25T22:46:52.552138+00:00",
      "last_modified_date": "2025-04-22T09:46:31",
      "objective_id": "MasteryObjective_Weapon_Hammer_SkiesOfOstia_Craft",
      "phx_account_id": "U2BLWVTDHZGWLBKKLY2QG6UX4I",
      "progress": 1
    },
    {
      "completed_count": 0,
      "created_date": "2025-04-25T22:46:52.552253+00:00",
      "last_modified_date": "2025-04-22T09:47:42",
      "objective_id": "MasteryObjective_Weapon_Hammer_SkiesOfOstia_XP",
      "phx_account_id": "U2BLWVTDHZGWLBKKLY2QG6UX4I",
      "progress": 112
    },
    {
      "completed_count": 1,
      "created_date": "2025-04-25T22:46:52.552368+00:00",
      "last_modified_date": "2025-04-22T09:46:31",
      "objective_id": "MasteryObjective_Weapon_Pike_LivingBranch_Craft",
      "phx_account_id": "U2BLWVTDHZGWLBKKLY2QG6UX4I",
      "progress": 1
    },
    {
      "completed_count": 1,
      "created_date": "2025-04-25T22:46:52.552500+00:00",
      "last_modified_date": "2025-04-22T09:44:24",
      "objective_id": "MasteryObjective_Weapon_Sword_SilverSword_Craft",
      "phx_account_id": "U2BLWVTDHZGWLBKKLY2QG6UX4I",
      "progress": 1
    }
  ]
}
```