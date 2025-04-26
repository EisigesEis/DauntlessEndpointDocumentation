URL: https://guild-prod.steelyard.ca/guild \
Method: GET \
Auth: Yes

---

## Comment
Retrieve guild which requester is member in.

## Example Request
Default Headers, no payload.

## Example Response
### no guild membership
204 No Content, no payload

### guild membership
```json
{
  "code": null,
  "message": "OK",
  "payload": {
    "created_date": "2022-11-30T19:22:56",
    "id": "2422b73b-0138-4117-8ea2-e9a4c2c16775",
    "last_modified_date": "2022-11-30T19:22:56",
    "leader_account_id": "XQBF5VHGFJHR5AUILEPYI55MUQ", // me
    "maximum_guild_members": 100,
    "members": [
      {
        "joined_date": "2024-10-06T12:58:38",
        "last_modified_date": "2024-10-06T12:58:38",
        "phx_account_id": "2CUCYVYHYZGOPGBRMVDLCPMA3Y", // Alex6941
        "rank": "member"
      },
      {
        "joined_date": "2024-07-02T17:26:58",
        "last_modified_date": "2024-07-02T17:26:58",
        "phx_account_id": "2HWB53YTNJDIFHKTEMEQIUISB4", // Myūツ
        "rank": "member"
      },
      {
        "joined_date": "2024-11-04T18:23:37",
        "last_modified_date": "2024-11-04T18:23:37",
        "phx_account_id": "2XQSJ45JTJEDVFGC5FZVUPHRME", // Acee96TV
        "rank": "member"
      },
      {
        "joined_date": "2024-08-21T22:54:27",
        "last_modified_date": "2024-08-21T22:54:27",
        "phx_account_id": "2XSBHQEMGJCNLNV7Y3TQHD4B74", // biliousDrake +
        "rank": "member"
      },
      {
        "joined_date": "2024-05-26T13:33:17",
        "last_modified_date": "2024-05-26T13:33:17",
        "phx_account_id": "2YEWZ5FF4VHG7NSXNDB2BQ43GY", // SiilverOriginZ +
        "rank": "officer"
      },
      {
        "joined_date": "2024-10-14T07:30:52",
        "last_modified_date": "2024-10-14T07:30:52",
        "phx_account_id": "34AVW3IWEFH3ZORNK4DBD4DFAQ", // zenox_vk
        "rank": "member"
      },
      {
        "joined_date": "2024-10-05T06:23:54",
        "last_modified_date": "2024-10-05T06:23:54",
        "phx_account_id": "3RQHZZOENNGHPIYV5YH5XSXZHE", // Paló D Dawg
        "rank": "member"
      },
      {
        "joined_date": "2024-10-19T21:52:43",
        "last_modified_date": "2024-10-19T21:52:43",
        "phx_account_id": "4JUKRBIZ75A3RFNHNQBPBU2OAM", // SailEmツ
        "rank": "member"
      },
      {
        "joined_date": "2024-10-24T18:00:46",
        "last_modified_date": "2024-10-24T18:00:46",
        "phx_account_id": "5D6MDOXHWJEZPKMNVXEEAQV4EQ", // Veronica +
        "rank": "member"
      },
      {
        "joined_date": "2024-10-23T22:38:00",
        "last_modified_date": "2024-10-23T22:38:00",
        "phx_account_id": "5MB3PUD2ZJCJZFXJQR7VVO3L5Y", // DAN_TE_IN_FER_NO
        "rank": "member"
      },
      {
        "joined_date": "2022-12-03T14:30:05",
        "last_modified_date": "2022-12-03T14:30:05",
        "phx_account_id": "5MNK4SOLFBF5REWZRWLL7Z7IYM", // ppapp107 or steam:(76561198331861352 => 天真) +
        "rank": "member"
      },
      {
        "joined_date": "2024-07-03T10:19:37",
        "last_modified_date": "2024-07-03T10:19:37",
        "phx_account_id": "5RITV4R4PFHJTJR2ERQWJ7UZDQ", // HotCocoanut
        "rank": "member"
      },
      {
        "joined_date": "2023-10-12T16:08:40",
        "last_modified_date": "2023-10-12T16:08:40",
        "phx_account_id": "5TWWPRGJOJHVVDQUMSJYR4JPYI", // Daishinkan__90 +
        "rank": "member"
      },
      {
        "joined_date": "2024-08-16T12:23:21",
        "last_modified_date": "2024-08-16T12:23:21",
        "phx_account_id": "7BL45SRYE5DJXGXVGOOAWPKRLM", // StepSlayer
        "rank": "member"
      },
      {
        "joined_date": "2023-12-08T10:43:26",
        "last_modified_date": "2023-12-08T10:43:26",
        "phx_account_id": "7KMTYGFCTJC2TGUIJGKJEUN7AI", // フランユ or steam:(76561198296106858 => \uD83D\uDC52) or franchu +
        "rank": "member"
      },
      {
        "joined_date": "2024-07-02T17:40:44",
        "last_modified_date": "2024-07-02T17:40:44",
        "phx_account_id": "7NMPYEIE25E2NDMS3PDFAFH23M", // TDP VeRyGooD
        "rank": "member"
      },
      {
        "joined_date": "2024-08-15T22:02:52",
        "last_modified_date": "2024-08-15T22:02:52",
        "phx_account_id": "AV6FH3CE75GG3B4Q4UYEX3P42A", // でもツ (lindeno)
        "rank": "member"
      },
      {
        "joined_date": "2024-10-10T18:37:31",
        "last_modified_date": "2024-10-10T18:37:31",
        "phx_account_id": "AVX3GIT3TREOLITOHVFQPECIGY", // alefra234_
        "rank": "member"
      },
      {
        "joined_date": "2024-04-19T12:07:23",
        "last_modified_date": "2024-04-19T12:07:23",
        "phx_account_id": "CBINND7FPNCNLBCGMJDICBXZ2E", // xxLUXIONxx
        "rank": "member"
      },
      {
        "joined_date": "2023-04-28T15:28:36",
        "last_modified_date": "2023-04-28T15:28:36",
        "phx_account_id": "DSRMFXFUQBDSPK3GDIV3X6AI4E", // AIZY +
        "rank": "member"
      },
      {
        "joined_date": "2024-10-04T16:36:05",
        "last_modified_date": "2024-10-04T16:36:05",
        "phx_account_id": "E4B4DM5NSJAGZHIRNBHZRMI3LQ", // Ironhidedu42100
        "rank": "member"
      },
      {
        "joined_date": "2024-09-29T21:14:19",
        "last_modified_date": "2024-09-29T21:14:19",
        "phx_account_id": "E7IRZUNZRNFEXIJZIVSH2AEM5A", // Bluelife971
        "rank": "member"
      },
      {
        "joined_date": "2024-05-03T00:41:09",
        "last_modified_date": "2024-05-03T00:41:09",
        "phx_account_id": "EFFIQT2Z4FEPBMIM2S3S67VUZI", // TX_Saul
        "rank": "member"
      },
      {
        "joined_date": "2023-12-08T12:30:34",
        "last_modified_date": "2023-12-08T12:30:34",
        "phx_account_id": "EFZFZVNRSFHY5I2W43B5OOOBO4", // yhioss +
        "rank": "officer"
      },
      {
        "joined_date": "2024-09-30T03:38:10",
        "last_modified_date": "2024-09-30T03:38:10",
        "phx_account_id": "EG4UFZYHZ5ERTBPEZ3HRU2EJUQ", // Urska gavemeptsd
        "rank": "member"
      },
      {
        "joined_date": "2024-10-13T18:22:17",
        "last_modified_date": "2024-10-13T18:22:17",
        "phx_account_id": "EMB7ZLOFPJGWTMCHUICUQHFL4Q", // Leopoldo_Gong +
        "rank": "member"
      },
      {
        "joined_date": "2024-10-08T15:59:53",
        "last_modified_date": "2024-10-08T15:59:53",
        "phx_account_id": "EOPKHJGUGZGEDE6ERDXLHM235A", // PRONO BALIĞI
        "rank": "member"
      },
      {
        "joined_date": "2023-01-19T12:05:23",
        "last_modified_date": "2023-01-19T12:05:23",
        "phx_account_id": "ETTSKCIFSFC3JIKUTXHDNR4W4Y", // Zzz_hikaru +
        "rank": "member"
      },
      {
        "joined_date": "2024-08-30T15:12:31",
        "last_modified_date": "2024-08-30T15:12:31",
        "phx_account_id": "EW2J33ECN5H2BHYJCGAP5PAAB4", // Yaraky.
        "rank": "member"
      },
      {
        "joined_date": "2023-10-26T14:22:26",
        "last_modified_date": "2023-10-26T14:22:26",
        "phx_account_id": "EX2HTT6N75HFRLSYYGQRQWRBAE", // Adriana_Almond +
        "rank": "member"
      },
      {
        "joined_date": "2024-07-17T16:17:32",
        "last_modified_date": "2024-07-17T16:17:32",
        "phx_account_id": "F2U3VSVJQBHZZMGKAZFII6W7VE", // SAG_MissKelly
        "rank": "member"
      },
      {
        "joined_date": "2023-12-13T04:10:05",
        "last_modified_date": "2023-12-13T04:10:05",
        "phx_account_id": "FE6PVH72KJEYJHW234MUGSU4HU", // Storm o_o +
        "rank": "member"
      },
      {
        "joined_date": "2024-07-02T16:44:28",
        "last_modified_date": "2024-07-02T16:44:28",
        "phx_account_id": "FJGPFDKA25FY7GFCGTOEC6L46Y", // kgb (le boss arthur)
        "rank": "member"
      },
      {
        "joined_date": "2024-10-09T11:18:20",
        "last_modified_date": "2024-10-09T11:18:20",
        "phx_account_id": "FRJGVHATI5BFXF4XYZ7N35PZYI", // Mellakal34
        "rank": "member"
      },
      {
        "joined_date": "2024-02-29T22:44:07",
        "last_modified_date": "2024-02-29T22:44:07",
        "phx_account_id": "H2HYMA2DTVFJFGKMAFIDN3AMLQ", // Polfyy +
        "rank": "member"
      },
      {
        "joined_date": "2024-03-12T14:41:32",
        "last_modified_date": "2024-03-12T14:41:32",
        "phx_account_id": "H6BQSPUXQVC4XNVF7MGY57QWCM", // SY_Samu
        "rank": "member"
      },
      {
        "joined_date": "2024-04-11T05:23:21",
        "last_modified_date": "2024-04-11T05:23:21",
        "phx_account_id": "HDT7IDSKHREATDOQODL7YIRHMY", // DKLM DekerLemon
        "rank": "member"
      },
      {
        "joined_date": "2024-10-20T23:07:14",
        "last_modified_date": "2024-10-20T23:07:14",
        "phx_account_id": "HFTUFBVJ4JFNVIKOEF6YE3IWOY", // Dxvvo
        "rank": "member"
      },
      {
        "joined_date": "2023-04-18T12:14:23",
        "last_modified_date": "2023-04-18T12:14:23",
        "phx_account_id": "HI2RCV47UZHLTMP4SAQAZGMUZY", // JstDhruvツ +
        "rank": "member"
      },
      {
        "joined_date": "2024-05-24T14:45:35",
        "last_modified_date": "2024-05-24T14:45:35",
        "phx_account_id": "HLNKOZRMSNEPBHTPC5UNZYUGAQ", // Moykaaaaa
        "rank": "member"
      },
      {
        "joined_date": "2024-10-20T19:38:17",
        "last_modified_date": "2024-10-20T19:38:17",
        "phx_account_id": "HVC6IABHCJDHVMHPAY6WH2R4DA", // Shivvy P
        "rank": "member"
      },
      {
        "joined_date": "2024-07-04T20:21:55",
        "last_modified_date": "2024-07-04T20:21:55",
        "phx_account_id": "I5SKGTG2TRHMJGF7PM4SRBV7Q4", // SheHulk04
        "rank": "member"
      },
      {
        "joined_date": "2024-08-21T06:10:39",
        "last_modified_date": "2024-08-21T06:10:39",
        "phx_account_id": "IGD3NISLTJDXZBKZ4YBDYFZRUM", // xexviatan
        "rank": "member"
      },
      {
        "joined_date": "2024-08-16T11:03:50",
        "last_modified_date": "2024-08-16T11:03:50",
        "phx_account_id": "IRO2MP5MIRBK3IBXNPYUSNAHMY", // のあるとのいと
        "rank": "member"
      },
      {
        "joined_date": "2024-04-24T08:09:37",
        "last_modified_date": "2024-04-24T08:09:37",
        "phx_account_id": "IVM5DS4GONC37HMU4HON54VUXM", // jee2418
        "rank": "member"
      },
      {
        "joined_date": "2024-04-16T12:10:00",
        "last_modified_date": "2024-04-16T12:10:00",
        "phx_account_id": "JATWCQLA5JFDFN7X7SVLMAZPRY", // sky.cos or nintendo:(98d255658db54c47) +
        "rank": "member"
      },
      {
        "joined_date": "2024-08-14T12:00:12",
        "last_modified_date": "2024-08-14T12:00:12",
        "phx_account_id": "JI6FMPD23RGBPO2VUT3EH25C7A", // lotamma / On3L3G3NDS00
        "rank": "member"
      },
      {
        "joined_date": "2024-08-26T12:47:48",
        "last_modified_date": "2024-08-26T12:47:48",
        "phx_account_id": "JL3E73Y5R5DP5NPMP6ASJ33NBQ", // BLACKVEIL-
        "rank": "member"
      },
      {
        "joined_date": "2024-08-15T21:49:44",
        "last_modified_date": "2024-08-15T21:49:44",
        "phx_account_id": "JO22YQPE6VG37MC7M7SLKBRCTM", // sir_escanor21
        "rank": "member"
      },
      {
        "joined_date": "2024-01-24T19:31:00",
        "last_modified_date": "2024-01-24T19:31:00",
        "phx_account_id": "K47BZAMKT5F6LACXYUPGV4MERU", // ThePikeOfDestiny +
        "rank": "member"
      },
      {
        "joined_date": "2023-11-16T16:23:44",
        "last_modified_date": "2023-11-16T16:23:44",
        "phx_account_id": "K5CLRVB47NDTPKYN5P7EMDOGG4", // Wings Freim-_- +
        "rank": "member"
      },
      {
        "joined_date": "2023-09-27T16:08:40",
        "last_modified_date": "2023-09-27T16:08:40",
        "phx_account_id": "KA6YLIDSXNDYNJY4OXL6RJD74E", // Aw--MaaKiiNaaFK +
        "rank": "member"
      },
      {
        "joined_date": "2024-10-08T22:11:26",
        "last_modified_date": "2024-10-08T22:11:26",
        "phx_account_id": "KD5XKNZNDZB45IRER72UX5INFA", // Skaal Resident
        "rank": "member"
      },
      {
        "joined_date": "2024-04-27T16:03:02",
        "last_modified_date": "2024-04-27T16:03:02",
        "phx_account_id": "KVEFFNGWUZEWDJFTF7LXYDR7PM", // Schnemley
        "rank": "member"
      },
      {
        "joined_date": "2024-03-06T07:42:47",
        "last_modified_date": "2024-03-06T07:42:47",
        "phx_account_id": "LG2ZFY6II5HTDMGRQWLQUYBSC4", // SeishunSick +
        "rank": "member"
      },
      {
        "joined_date": "2022-12-07T05:56:16",
        "last_modified_date": "2022-12-07T05:56:16", // who is he?
        "phx_account_id": "LININZEWEFGNFAA5STVOKGOGZM", // 打完架放个补给箱吧
        "rank": "member"
      },
      {
        "joined_date": "2024-10-29T18:20:09",
        "last_modified_date": "2024-10-29T18:20:09",
        "phx_account_id": "LUT5EMEULBBVHBQWH4GIUGMYJY", // Oazi / Nagato
        "rank": "member"
      },
      {
        "joined_date": "2023-11-28T13:53:16",
        "last_modified_date": "2023-11-28T13:53:16",
        "phx_account_id": "MJMPQKG56RECPJK3QUXG53QABE", // Amancio ツ +
        "rank": "member"
      },
      {
        "joined_date": "2024-07-11T17:29:16",
        "last_modified_date": "2024-07-11T17:29:16",
        "phx_account_id": "N43NVVX54NBI3KNN6FYMFXK4VA", // MereLeopon664
        "rank": "member"
      },
      {
        "joined_date": "2023-01-20T18:31:44",
        "last_modified_date": "2023-01-20T18:31:44",
        "phx_account_id": "NAHOHG5JIVDRPPHAXXX5HDBNJI", // koku +
        "rank": "member"
      },
      {
        "joined_date": "2023-01-19T23:38:30",
        "last_modified_date": "2023-01-19T23:38:30",
        "phx_account_id": "NL4NJUXWHBFZTMMK7W56HT4L4Q", // ΩLördPrístiñöΩ ツ
        "rank": "officer"
      },
      {
        "joined_date": "2024-04-19T19:53:39",
        "last_modified_date": "2024-04-19T19:53:39",
        "phx_account_id": "NXOS6XGSBJECPNKFO7BUNFEXMI", // nkm78 or max2109 +
        "rank": "member"
      },
      {
        "joined_date": "2024-08-16T09:46:46",
        "last_modified_date": "2024-08-16T09:46:46",
        "phx_account_id": "O2DQN4U7RZBBNEIFGLP5UFZOFI", // Andruik1
        "rank": "member"
      },
      {
        "joined_date": "2024-04-22T19:01:56",
        "last_modified_date": "2024-04-22T19:01:56",
        "phx_account_id": "OTSPQXXXY5AMRP3UFGWRPOR47Y", // Danilo-68
        "rank": "member"
      },
      {
        "joined_date": "2023-02-17T17:07:54",
        "last_modified_date": "2023-02-17T17:07:54",
        "phx_account_id": "PKHHKELSBRE3VHEE4S6FYVY7CI", // MacVilla +
        "rank": "member"
      },
      {
        "joined_date": "2024-08-20T20:34:50",
        "last_modified_date": "2024-08-20T20:34:50",
        "phx_account_id": "QNV5R5UFFRD6JG6VU2ZDRNL25M", // Cryptホ
        "rank": "member"
      },
      {
        "joined_date": "2024-07-08T16:18:37",
        "last_modified_date": "2024-07-08T16:18:37",
        "phx_account_id": "QUIYOF5WSZD2DP7JWRO7IZXXWY", // vassili2510
        "rank": "member"
      },
      {
        "joined_date": "2023-12-16T10:56:34",
        "last_modified_date": "2023-12-16T10:56:34",
        "phx_account_id": "RDA2C6VAKNC7TLYIFL4CIR36FU", // Distant Years +
        "rank": "officer"
      },
      {
        "joined_date": "2024-08-15T21:38:14",
        "last_modified_date": "2024-08-15T21:38:14",
        "phx_account_id": "RGIY675NQ5BV3E7IP6ZNRHJ65E", // NqToP
        "rank": "member"
      },
      {
        "joined_date": "2024-09-28T08:52:04",
        "last_modified_date": "2024-09-28T08:52:04",
        "phx_account_id": "RPG2TSYXHZFPRMN3EHS43G4V6U", // TheRooshBoi
        "rank": "member"
      },
      {
        "joined_date": "2024-08-19T13:02:50",
        "last_modified_date": "2024-08-19T13:02:50",
        "phx_account_id": "RRTDLEI2XJFU5HEWWKQIZN4HBI", // TheGdKite
        "rank": "member"
      },
      {
        "joined_date": "2024-08-15T21:43:32",
        "last_modified_date": "2024-08-15T21:43:32",
        "phx_account_id": "RXD4WFDUBZAETPQEXKGMGRYTU4", // Killer9747723
        "rank": "member"
      },
      {
        "joined_date": "2023-03-28T16:18:59",
        "last_modified_date": "2023-03-28T16:18:59",
        "phx_account_id": "S5MMSEHCMVDJNNVYEFKS5CU6V4", // vikas2508 +
        "rank": "member"
      },
      {
        "joined_date": "2024-08-30T11:13:37",
        "last_modified_date": "2024-08-30T11:13:37",
        "phx_account_id": "S7R4MG7XPRDNRMAS5EDFZH3OGU", // Yago
        "rank": "member"
      },
      {
        "joined_date": "2024-05-28T22:11:19",
        "last_modified_date": "2024-05-28T22:11:19",
        "phx_account_id": "SAY266H6FBF2FIGZJTTMAUUMLM", // Xix_SNiPs_xiX
        "rank": "member"
      },
      {
        "joined_date": "2024-10-04T15:16:56",
        "last_modified_date": "2024-10-04T15:16:56",
        "phx_account_id": "SEMN7KWZURAABJMES5HJCHDB2I", // Luckxsz
        "rank": "member"
      },
      {
        "joined_date": "2024-08-19T16:30:41",
        "last_modified_date": "2024-08-19T16:30:41",
        "phx_account_id": "SOMCWXQ7MFAZLORJ23MTS72IP4", // zenοx_vk
        "rank": "member"
      },
      {
        "joined_date": "2024-04-17T17:09:14",
        "last_modified_date": "2024-04-17T17:09:14",
        "phx_account_id": "TBFW2ZRGBFGHXATW6IWXN7LPAQ", // ImZeus-l-
        "rank": "member"
      },
      {
        "joined_date": "2024-08-22T11:16:29",
        "last_modified_date": "2024-08-22T11:16:29",
        "phx_account_id": "TWOHISPC2FGQJE7HG7URWV2DBM", // abyssvortexx
        "rank": "member"
      },
      {
        "joined_date": "2024-10-10T17:05:30",
        "last_modified_date": "2024-10-10T17:05:30",
        "phx_account_id": "TYKQ5DRNWRDCDDN7T6ZYMO3QJU", // RyZe_YT0 +
        "rank": "member"
      },
      {
        "joined_date": "2024-05-06T13:37:16",
        "last_modified_date": "2024-05-06T13:37:16",
        "phx_account_id": "UJTIVREOZBFYTGLZNVB5KJHB3U", // Urska_x
        "rank": "member"
      },
      {
        "joined_date": "2024-05-31T16:32:11",
        "last_modified_date": "2024-05-31T16:32:11",
        "phx_account_id": "V3WHJ6ECUJDZRHA4OSW2HXYLUI", // el4a3er
        "rank": "member"
      },
      {
        "joined_date": "2024-05-31T10:37:40",
        "last_modified_date": "2024-05-31T10:37:40",
        "phx_account_id": "VEOTL2UFFZEN3K67ECZUK6NHVA", // Medieval_WOLF
        "rank": "member"
      },
      {
        "joined_date": "2024-07-30T18:04:48",
        "last_modified_date": "2024-07-30T18:04:48",
        "phx_account_id": "VOFA5EOLKVELBD26MCTP4WOOOY", // kolbrion
        "rank": "member"
      },
      {
        "joined_date": "2024-05-24T16:56:30",
        "last_modified_date": "2024-05-24T16:56:30",
        "phx_account_id": "VR65CVOL6JAUHDEML4KWHLJDR4", // SNIPs_ツ
        "rank": "member"
      },
      {
        "joined_date": "2023-07-03T17:46:42",
        "last_modified_date": "2023-07-03T17:46:42",
        "phx_account_id": "VSSOL42ML5GAPJK4SDPILXMC64", // WaxyThrone
        "rank": "member"
      },
      {
        "joined_date": "2024-01-03T22:39:31",
        "last_modified_date": "2024-01-03T22:39:31",
        "phx_account_id": "W3O6SN7AL5BVRAMITAZ4ZQURHE", // NOT_A_SCOP
        "rank": "member"
      },
      {
        "joined_date": "2024-10-10T02:47:40",
        "last_modified_date": "2024-10-10T02:47:40",
        "phx_account_id": "WCB6AQCCTJDFBB52NHXADKEKRM", // DrDriffツ
        "rank": "member"
      },
      {
        "joined_date": "2024-07-24T12:44:43",
        "last_modified_date": "2024-07-24T12:44:43",
        "phx_account_id": "WHVLLQFZFJHFLLFI2PWOCYQTHQ", // Marie
        "rank": "member"
      },
      {
        "joined_date": "2024-09-03T18:54:30",
        "last_modified_date": "2024-09-03T18:54:30",
        "phx_account_id": "WISX5Z37IVEHDMQ3OV6PHKVT3M", // ziinox_vk (nizorix?)
        "rank": "member"
      },
      {
        "joined_date": "2023-12-08T22:09:43",
        "last_modified_date": "2023-12-08T22:09:43",
        "phx_account_id": "WPGIGWFMAZGTXFS3TX6OQEQ7XU", // Teaddo
        "rank": "member"
      },
      {
        "joined_date": "2024-08-19T15:35:21",
        "last_modified_date": "2024-08-19T15:35:21",
        "phx_account_id": "X7ONOCF25BDFNK5MHP66A6NBUQ", // rY WarZz
        "rank": "member"
      },
      {
        "joined_date": "2023-09-18T05:22:54",
        "last_modified_date": "2023-09-18T05:22:54",
        "phx_account_id": "XQBF5VHGFJHR5AUILEPYI55MUQ", // me
        "rank": "leader"
      },
      {
        "joined_date": "2024-08-30T16:56:41",
        "last_modified_date": "2024-08-30T16:56:41",
        "phx_account_id": "XYJOOWRC7BDUTIB2B5UVDIZOIE", // Oppiess
        "rank": "member"
      },
      {
        "joined_date": "2024-08-20T11:41:33",
        "last_modified_date": "2024-08-20T11:41:33",
        "phx_account_id": "Y6MT3BGF5FFORIWDTH4BCOJWMQ", // XnebuR_Fr
        "rank": "member"
      },
      {
        "joined_date": "2024-05-02T18:11:34",
        "last_modified_date": "2024-05-02T18:11:34",
        "phx_account_id": "YGCW2QNUTFD4NME2MH4U2HCS2U", // ninjaCat_1986
        "rank": "member"
      },
      {
        "joined_date": "2023-02-06T16:16:46",
        "last_modified_date": "2023-02-06T16:16:46",
        "phx_account_id": "ZDNGSC67PVH5HLDTFRNXWJNAKM", // Th3 MasterChief +
        "rank": "officer"
      },
      {
        "joined_date": "2024-04-13T11:45:16",
        "last_modified_date": "2024-04-13T11:45:16",
        "phx_account_id": "ZP4QYPPV7RFCTPOISPPMRSA4LM", // DeerEdits +
        "rank": "officer"
      },
      {
        "joined_date": "2023-04-24T06:26:25",
        "last_modified_date": "2023-04-24T06:26:25",
        "phx_account_id": "ZSOHUWKWT5CDHB5SPLSLFCBJYQ", // Théméro +
        "rank": "officer"
      },
      {
        "joined_date": "2024-04-10T13:29:28",
        "last_modified_date": "2024-04-10T13:29:28",
        "phx_account_id": "ZUIUIBCWEZD6JNJPQY3TCZMGYM", // 工0uxx
        "rank": "member"
      }
    ],
    "name": "ThraxEnjoyers",
    "nameplate": "THRAAX"
  }
}

```