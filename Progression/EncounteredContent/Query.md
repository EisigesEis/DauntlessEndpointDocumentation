URL: https://progression-prod.steelyard.ca/encountered-content/query/{Character ID} \
Auth: Yes \
Method: POST

---

## Comment
Client asks for encountered content (when opening Journal).

## Example Request
```json
{
  "content_types" : [
    0, // unknown
    1, // Behemoths first encounter
    2, // NPC first talk
    3, // Tutorial Hints first read
    4, // COL island discovery
    5, // Lore island discovery
    6, // lookout spots (the ones with flying camera view)
    7 // unknown
  ]
}
```

## Example Response
```json
{
   "code" : null,
   "message" : "OK",
   "payload" : {
      "content_types" : [
         {
            "content" : [ "LeRawr", "dummy", "lerawr_normal" ],
            "content_type" : 1
         },
         {
            "content" : [
               "NPC_AdmiralZai",
               "NPC_BosunMarkus",
               "NPC_KatSorrel",
               "NPC_MoyraHeigsketter",
               "NPC_TrainerRosk",
               "NPC_WilsBormen"
            ],
            "content_type" : 2
         },
         {
            "content" : [
               "TutorialSlate_Aetherite",
               "TutorialSlate_Behemoth_Tracking",
               "TutorialSlate_Bounty_Tokens",
               "TutorialSlate_DamageTypeSwap",
               "TutorialSlate_EquipCells",
               "TutorialSlate_Equip_Gear",
               "TutorialSlate_Gliders",
               "TutorialSlate_HuntBoard",
               "TutorialSlate_Linked_Slayer",
               "TutorialSlate_Map",
               "TutorialSlate_PerksArmourCells",
               "TutorialSlate_QuestInfo",
               "TutorialSlate_Social",
               "TutorialSlate_StarterWeapons"
            ],
            "content_type" : 3
         },
         {
            "content" : [ "player_journey_tabs_bpw" ],
            "content_type" : 7
         }
      ],
      "success" : true
   }
}
```

```json
{
  "code": null,
  "message": "OK",
  "payload": {
    "content_types": [
      {
        "content": [
          "Amber",
          "Armstrong",
          "Beaver",
          "Bugbear",
          "Bullseye",
          "Crowbear",
          "Crudge",
          "Electroquill",
          "FULGAR_ALPHA",
          "Fulgar",
          "Funguy",
          "Glitter",
          "Habanero",
          "Host",
          "Lavaroller",
          "LeRawr",
          "Mantis",
          "McRollin",
          "Mint",
          "Moonface",
          "Paper",
          "Randall",
          "Sally",
          "Salt",
          "Scissors",
          "Shadowcat",
          "Shockmane",
          "Snowflake",
          "Terramane",
          "Wolf",
          "amber_normal",
          "armstrong_normal",
          "beaver_alpha",
          "beaver_beta",
          "beaver_blaze",
          "beaver_frost",
          "beaver_heroic",
          "beaver_normal",
          "bugbear_blaze",
          "bugbear_normal",
          "bullseye_alpha",
          "bullseye_beta",
          "bullseye_blaze",
          "bullseye_heroic",
          "bullseye_normal",
          "crowbear_clone",
          "crowbear_normal",
          "crudge_normal",
          "dummy",
          "dummy_normal",
          "electroquill_alpha",
          "electroquill_heroic",
          "electroquill_normal",
          "electroquill_umbral",
          "fulgar_beta",
          "fulgar_normal",
          "fulgar_umbral",
          "funguy_normal",
          "glitter_normal",
          "habanero_normal",
          "host_alpha",
          "host_beta",
          "host_heroic",
          "host_normal",
          "host_radiant",
          "lavaroller_alpha",
          "lavaroller_heroic",
          "lavaroller_normal",
          "lerawr_alpha",
          "lerawr_beta",
          "lerawr_frostwolf",
          "lerawr_heroic",
          "lerawr_normal",
          "lerawr_terra",
          "lerawr_terramane",
          "mantis_normal",
          "mcrollin_alpha",
          "mcrollin_heroic",
          "mcrollin_normal",
          "mint_normal",
          "moonface_alpha",
          "moonface_beta",
          "moonface_heroic",
          "moonface_normal",
          "paper_heroic",
          "paper_normal",
          "paper_radiant",
          "paper_umbral",
          "randall_normal",
          "rock",
          "rock_alpha",
          "rock_frost",
          "rock_heroic",
          "rock_normal",
          "sally_alpha",
          "sally_heroic",
          "sally_nemesis",
          "sally_normal",
          "sally_terra",
          "sally_terrogg",
          "salt_heroic",
          "salt_normal",
          "scissors_alpha",
          "scissors_heroic",
          "scissors_normal",
          "shadowcat_heroic",
          "shadowcat_normal",
          "shockmane_alpha",
          "shockmane_heroic",
          "shockmane_normal",
          "snowflake_alpha",
          "snowflake_alpha_oneeye",
          "snowflake_heroic",
          "snowflake_normal",
          "terramane_alpha",
          "terramane_normal",
          "thunderbird",
          "thunderbird_normal",
          "wolf_normal"
        ],
        "content_type": 1
      },
      {
        "content": [
          "NPC_AdmiralZai",
          "NPC_ArkanDrew",
          "NPC_AuntieVeeta",
          "NPC_BosunMarkus",
          "NPC_DoctorPriyani",
          "NPC_GregarioFlynt",
          "NPC_HonestOzz",
          "NPC_KatSorrel",
          "NPC_LadyLuck",
          "NPC_Linnea_Queen",
          "NPC_Middleman",
          "NPC_MoyraHeigsketter",
          "NPC_ScarredMaster",
          "NPC_TrainerRosk",
          "NPC_WilsBormen",
          "NPC_XelyaTheFarslayer",
          "None",
          "npc_linnea"
        ],
        "content_type": 2
      },
      {
        "content": [
          "TutorialAudio_HellionTips_01",
          "TutorialAudio_HellionTips_02",
          "TutorialAudio_RiftstalkerTips_02",
          "TutorialAudio_StormclawTips_02",
          "TutorialSlate_AetherCores",
          "TutorialSlate_Aetherite",
          "TutorialSlate_Behemoth_Tracking",
          "TutorialSlate_Bounty_Tokens",
          "TutorialSlate_DamageTypeSwap",
          "TutorialSlate_DangerMeter_HG",
          "TutorialSlate_Dodging",
          "TutorialSlate_Elemental_Relationships",
          "TutorialSlate_Equip_Gear",
          "TutorialSlate_Esca",
          "TutorialSlate_EssenceTalents",
          "TutorialSlate_Frostbite",
          "TutorialSlate_Gauntlet",
          "TutorialSlate_GliderTrack",
          "TutorialSlate_Gliders",
          "TutorialSlate_HardEsca",
          "TutorialSlate_HuntBoard",
          "TutorialSlate_Interrupts",
          "TutorialSlate_Linked_Slayer",
          "TutorialSlate_Map",
          "TutorialSlate_Omnicells",
          "TutorialSlate_Patrol_Chests",
          "TutorialSlate_PerksArmourCells",
          "TutorialSlate_QuestInfo",
          "TutorialSlate_Slayer_Path",
          "TutorialSlate_Social",
          "TutorialSlate_Stamina_1",
          "TutorialSlate_Stamina_2",
          "TutorialSlate_StarterWeapons",
          "TutorialSlate_Supply_Crates",
          "TutorialSlate_Trackers",
          "TutorialSlate_Trials",
          "TutorialSlate_TrialsHard"
        ],
        "content_type": 3
      },
      {
        "content": [
          "COL_SEASON_S10B_LORE_02",
          "COL_SEASON_S10B_LORE_03",
          "COL_SEASON_S10B_LORE_04",
          "COL_SEASON_S10B_LORE_05",
          "COL_SEASON_S10B_PAGE_01",
          "COL_SEASON_S10B_PAGE_02",
          "COL_SEASON_S11A_PAGE_00",
          "COL_SEASON_S12B_PAGE_00",
          "COL_SEASON_S14B_ZAIS_REPORT"
        ],
        "content_type": 4
      },
      {
        "content": [
          "LORE_NODES_CRYSTALARMOUR_00",
          "LORE_NODES_DH_05",
          "LORE_NODES_DH_RECRUIT_01",
          "LORE_NODES_DH_RECRUIT_02",
          "LORE_NODES_DH_RECRUIT_03",
          "LORE_NODES_DH_RECRUIT_04",
          "LORE_NODES_DH_RECRUIT_05",
          "LORE_NODES_DH_RECRUIT_06",
          "LORE_NODES_ESCAFROST_00",
          "LORE_NODES_ESCAFROST_01",
          "LORE_NODES_ESCAFROST_02",
          "LORE_NODES_EXOTICS_MOLTENEDICT_00",
          "LORE_NODES_EXOTICS_PRISMATICGRACE_00",
          "LORE_NODES_EXOTICS_THEGODHAND_00",
          "LORE_NODES_EXOTICS_THEHUNGER_00",
          "LORE_NODES_EXOTICS_THESKULLFORGE_00",
          "LORE_NODES_EXOTICS_TRAGICECHO_00",
          "LORE_NODES_FF_BLADE",
          "LORE_NODES_FF_POMMEL",
          "LORE_NODES_FF_SIGIL",
          "LORE_NODES_ISLAND_A_01",
          "LORE_NODES_ISLAND_E_01",
          "LORE_NODES_ISLAND_G_01",
          "LORE_NODES_ISLAND_G_SEEDS",
          "LORE_NODES_ISLAND_G_SOIL",
          "LORE_NODES_ISLAND_H_01",
          "LORE_NODES_ISLAND_J_01",
          "LORE_NODES_ISLAND_K_01",
          "LORE_NODES_ISLAND_L_01",
          "LORE_NODES_ISLAND_M_01",
          "LORE_NODES_ISLAND_N_01",
          "LORE_NODES_ISLAND_O_01",
          "LORE_NODES_ISLAND_P_01",
          "LORE_NODES_ISLAND_Q_01",
          "LORE_NODES_ISLAND_R_01",
          "LORE_NODES_ISLAND_R_02",
          "LORE_NODES_ISLAND_U_00",
          "LORE_NODES_ISLAND_U_01",
          "LORE_NODES_ISLAND_U_02",
          "LORE_NODES_ISLAND_U_03",
          "LORE_NODES_ISLAND_U_04",
          "LORE_NODES_KROLACHI_FOOD",
          "LORE_NODES_KROLACHI_FOOD_EMPTY",
          "LORE_NODES_MUTATION",
          "LORE_NODES_MUTATION3",
          "LORE_NODES_S10B_00",
          "LORE_NODES_S10B_01",
          "LORE_NODES_S10B_02",
          "LORE_NODES_S10B_03",
          "LORE_NODES_S10B_04",
          "LORE_NODES_S10B_05",
          "LORE_NODES_S10B_06",
          "LORE_NODES_S10B_07",
          "LORE_NODES_S10B_08",
          "LORE_NODES_S10B_09",
          "LORE_NODES_S10B_10",
          "LORE_NODES_S10B_13",
          "LORE_NODES_S10B_14",
          "LORE_NODES_S10B_15",
          "LORE_NODES_S10C_00",
          "LORE_NODES_S13A_01",
          "LORE_NODES_S13A_02",
          "LORE_NODES_S18_PORTENT2",
          "LORE_NODES_ST_BRONZE",
          "LORE_NODES_ST_GEM",
          "LORE_NODES_ST_GOLD",
          "LORE_NODES_ST_PLATING"
        ],
        "content_type": 5
      },
      {
        "content": [
          "VP_RAMGSATE_BAZAAR",
          "VP_RAMGSATE_ESCALATION_TOWER",
          "VP_RAMGSATE_FRONT_ENTRANCE",
          "VP_RAMGSATE_KATS_BUILDING",
          "VP_RAMGSATE_LADY_LUCK_TRIALS"
        ],
        "content_type": 6
      },
      {
        "content": ["player_journey_tabs_bpw"],
        "content_type": 7
      }
    ],
    "success": true
  }
}
```