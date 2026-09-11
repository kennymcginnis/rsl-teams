# Champion Roster

Source snapshot: **champs 20260911.csv**. 525 champion copies; 371 distinct names.

Each row is an owned copy, identified by roster ID. Duplicate names are intentional. Current equipment stats are omitted because gear can be swapped between runs.

## Reading the Table

- **Hydra role** is an assessment from the team-planning work, not the official Attack/Defense/HP/Support champion type. The CSV does not export that type. Unassessed means no role has been assigned here, not that the champion is unusable.
- **Books** reports Fully booked when `BooksMissing` is zero; otherwise Incomplete. Books spent and skill-by-skill upgrades are not exported and cannot be inferred from this count. For Mythicals, inspect both forms in game.
- **Masteries** is inferred only from scroll counters. A full allocation requires 100 basic, 600 advanced, and 950 divine scrolls reported as used. A full scroll budget includes unused scrolls and does not mean a completed mastery tree. Verify unusual counters in game; the export does not identify selected masteries or their suitability.
- **Used / Unused scrolls** lists basic / advanced / divine counters for auditing the mastery status.
- **Empowerment** is the exported empowerment level, separate from rank and awakening.

## Roster Summary

| Rarity | Copies |
| --- | --- |
| Mythical | 2 |
| Legendary | 37 |
| Epic | 120 |
| Rare | 236 |
| Uncommon | 109 |
| Common | 21 |

## Mythical Champions

| Champion | ID | Rarity | Affinity | Rank | Level | Hydra role | Empowerment | Books | Books missing | Masteries | Used scrolls | Unused scrolls |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Gharol Bloodmaul | 239 | Mythical | Spirit | 6 | 60 | Damage (alternate); protection / Provoke (base) | +0 | Incomplete | 10 | Full scroll budget; allocation incomplete | 0 / 0 / 0 | 100 / 600 / 950 |
| Hierophant Lazarius | 232 | Mythical | Magic | 6 | 60 | Block Buffs / buffs / passive revive (base) | +0 | Incomplete | 6 | Full scroll budget; allocation incomplete | 0 / 0 / 0 | 100 / 600 / 950 |

## Legendary Champions

| Champion | ID | Rarity | Affinity | Rank | Level | Hydra role | Empowerment | Books | Books missing | Masteries | Used scrolls | Unused scrolls |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Arbiter | 13075 | Legendary | Void | 6 | 60 | Revive / ally turn-meter boost / Increase ATK | +0 | Fully booked | 0 | Full scroll budget; allocation incomplete | 0 / 0 / 0 | 100 / 600 / 950 |
| Artak | 37 | Legendary | Magic | 6 | 60 | HP Burn / burn activation / Decrease ATK | +0 | Fully booked | 0 | Full scroll budget; allocation incomplete | 0 / 0 / 0 | 100 / 600 / 950 |
| Astralon | 4571 | Legendary | Magic | 6 | 60 | Unassessed | +0 | Incomplete | 13 | Full scroll budget; allocation incomplete | 0 / 0 / 0 | 100 / 600 / 950 |
| Dorothy Gale | 14762 | Legendary | Spirit | 6 | 60 | Decrease DEF / Decrease ACC / Weaken / buff steal | +0 | Incomplete | 10 | Full scroll budget; allocation incomplete | 0 / 0 / 0 | 100 / 600 / 950 |
| Ezio Auditore | 242 | Legendary | Spirit | 6 | 60 | Unassessed | +0 | Incomplete | 12 | Full scroll budget; allocation incomplete | 0 / 0 / 0 | 100 / 600 / 950 |
| Haggibah the Nestmaid | 9484 | Legendary | Force | 6 | 60 | Burn activation / Leech / buff steal | +0 | Incomplete | 10 | Full scroll budget; allocation incomplete | 0 / 0 / 0 | 100 / 600 / 950 |
| Lyssandra | 70 | Legendary | Spirit | 6 | 60 | Increase SPD / ally turn-meter boost | +0 | Fully booked | 0 | Full scroll budget; allocation incomplete | 0 / 0 / 0 | 100 / 600 / 950 |
| Michelangelo | 212 | Legendary | Spirit | 6 | 60 | Unassessed | +0 | Incomplete | 10 | Full scroll budget; allocation incomplete | 0 / 0 / 0 | 100 / 600 / 950 |
| Prince Kymar | 99 | Legendary | Magic | 6 | 60 | Skill reset / buff removal | +0 | Fully booked | 0 | Full scroll budget; allocation incomplete | 0 / 0 / 0 | 100 / 600 / 950 |
| Rathalos Blademaster | 84 | Legendary | Force | 6 | 60 | Direct damage / boss Decrease DEF | +0 | Fully booked | 0 | Full scroll budget; allocation incomplete | 0 / 0 / 0 | 100 / 600 / 950 |
| Scyl of the Drakes | 65 | Legendary | Magic | 6 | 60 | Healing / revive / chance-based slow | +0 | Incomplete | 2 | Full scroll budget; allocation incomplete | 0 / 0 / 0 | 100 / 600 / 950 |
| Sun Wukong | 54 | Legendary | Spirit | 6 | 60 | Block Buffs / buff steal / damage | +0 | Fully booked | 0 | Full scroll budget; allocation incomplete | 0 / 0 / 0 | 100 / 600 / 950 |
| Talenna Soulseer | 6868 | Legendary | Spirit | 6 | 60 | Unassessed | +0 | Incomplete | 12 | Full scroll budget; allocation incomplete | 0 / 0 / 0 | 100 / 600 / 950 |
| Visix the Unbowed | 96 | Legendary | Void | 6 | 60 | Provoke / Decrease SPD / Ally Protection | +0 | Fully booked | 0 | Full scroll budget; allocation incomplete | 0 / 0 / 0 | 100 / 600 / 950 |
| Xenomorph | 234 | Legendary | Magic | 6 | 60 | Unassessed | +0 | Incomplete | 10 | Full scroll budget; allocation incomplete | 0 / 0 / 0 | 100 / 600 / 950 |
| Khamir Scald-eye | 14551 | Legendary | Magic | 6 | 58 | Speed / healing / revive / buffs | +0 | Incomplete | 8 | Partial allocation | 0 / 0 / 287 | 100 / 600 / 200 |
| The Cowardly Lion | 15597 | Legendary | Magic | 6 | 41 | DEF damage / defensive buffs / personal Fear response | +0 | Incomplete | 10 | Partial allocation | 100 / 551 / 0 | 0 / 0 / 0 |
| Wythir the Crowned | 13353 | Legendary | Force | 6 | 41 | Healing / cleanse / Increase DEF | +0 | Incomplete | 8 | Partial allocation | 100 / 313 / 0 | 0 / 0 / 0 |
| Alice the Wanderer | 165 | Legendary | Magic | 5 | 50 | Unassessed | +0 | Incomplete | 12 | Full scroll budget; allocation incomplete | 0 / 0 / 350 | 100 / 600 / 600 |
| Arashi the Riptide | 4555 | Legendary | Spirit | 5 | 50 | Unassessed | +0 | Incomplete | 14 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Arix | 3187 | Legendary | Magic | 5 | 50 | Unassessed | +0 | Incomplete | 11 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Chronicler Adelyn | 109 | Legendary | Force | 5 | 50 | Unassessed | +0 | Incomplete | 11 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Cleopterix | 3188 | Legendary | Spirit | 5 | 50 | Unassessed | +0 | Incomplete | 13 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Craklin the Blackened | 263 | Legendary | Force | 5 | 50 | Unassessed | +0 | Incomplete | 13 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Folan Silverhart | 4574 | Legendary | Spirit | 5 | 50 | Damage / Decrease DEF / debuff spread | +0 | Incomplete | 11 | Partial allocation | 0 / 0 / 158 | 100 / 600 / 400 |
| Guurda Bogbrew | 4533 | Legendary | Force | 5 | 50 | Unassessed | +0 | Incomplete | 11 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Karato Foxhunter | 13352 | Legendary | Spirit | 5 | 50 | Unassessed | +0 | Incomplete | 12 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Kroz Wallbreaker | 15576 | Legendary | Spirit | 5 | 50 | Unassessed | +0 | Incomplete | 11 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Leminisi the Gold-wing | 202 | Legendary | Force | 5 | 50 | Unassessed | +0 | Incomplete | 11 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Loki the Deceiver | 135 | Legendary | Spirit | 5 | 50 | Conditional Block Buffs spread / debuff extension | +0 | Incomplete | 10 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Mathias Blackflail | 8818 | Legendary | Force | 5 | 50 | Unassessed | +0 | Incomplete | 9 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Rhazin Scarhide | 14553 | Legendary | Force | 5 | 50 | Unassessed | +0 | Incomplete | 12 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Ronda | 4 | Legendary | Magic | 5 | 50 | Unassessed | +0 | Incomplete | 10 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Skeletor | 2147 | Legendary | Spirit | 5 | 50 | Unassessed | +0 | Incomplete | 13 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Vallaryn the Equalizer | 9432 | Legendary | Magic | 5 | 50 | Unassessed | +0 | Incomplete | 12 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Skeletor | 153 | Legendary | Spirit | 5 | 29 | Unassessed | +0 | Incomplete | 13 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Talenna Soulseer | 14555 | Legendary | Spirit | 5 | 17 | Unassessed | +0 | Incomplete | 12 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |

## Epic Champions

| Champion | ID | Rarity | Affinity | Rank | Level | Hydra role | Empowerment | Books | Books missing | Masteries | Used scrolls | Unused scrolls |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Akemtum | 179 | Epic | Void | 6 | 60 | Hex / debuff spread | +0 | Fully booked | 0 | Full scroll budget; allocation incomplete | 0 / 0 / 0 | 100 / 600 / 950 |
| Deacon Armstrong | 4056 | Epic | Spirit | 6 | 60 | Unassessed | +0 | Fully booked | 0 | Full scroll budget; allocation incomplete | 0 / 0 / 0 | 100 / 600 / 950 |
| Doompriest | 12178 | Epic | Force | 6 | 60 | Healing / partial cleanse / Increase ATK | +0 | Fully booked | 0 | Full scroll budget; allocation incomplete | 0 / 0 / 0 | 100 / 600 / 950 |
| Fayne | 14783 | Epic | Spirit | 6 | 60 | Unassessed | +0 | Incomplete | 15 | Partial allocation | 0 / 0 / 86 | 100 / 600 / 600 |
| Husk | 30 | Epic | Force | 6 | 60 | Enemy-MAX-HP damage / chance-based Provoke | +0 | Fully booked | 0 | Full scroll budget; allocation incomplete | 0 / 0 / 0 | 100 / 600 / 950 |
| Royal Guard | 5160 | Epic | Magic | 6 | 60 | Enemy-MAX-HP damage / partial slow and Decrease DEF | +0 | Fully booked | 0 | Full scroll budget; allocation incomplete | 0 / 0 / 0 | 100 / 600 / 950 |
| Seeker | 98 | Epic | Magic | 6 | 60 | Unassessed | +0 | Fully booked | 0 | Full scroll budget; allocation incomplete | 0 / 0 / 0 | 100 / 600 / 950 |
| Sepulcher Sentinel | 261 | Epic | Force | 6 | 60 | Unassessed | +0 | Fully booked | 0 | Full scroll budget; allocation incomplete | 0 / 0 / 0 | 100 / 600 / 950 |
| Ursala the Mourner | 78 | Epic | Void | 6 | 60 | Revive / Decrease ATK / defensive buffs | +0 | Fully booked | 0 | Full scroll budget; allocation incomplete | 0 / 0 / 0 | 100 / 600 / 950 |
| Uugo | 8808 | Epic | Magic | 6 | 60 | Block Buffs / Decrease DEF / healing | +0 | Fully booked | 0 | Full scroll budget; allocation incomplete | 0 / 0 / 0 | 100 / 600 / 950 |
| Vogoth | 210 | Epic | Spirit | 6 | 60 | Unassessed | +0 | Fully booked | 0 | Full scroll budget; allocation incomplete | 0 / 0 / 0 | 100 / 600 / 950 |
| Warcaster | 9322 | Epic | Void | 6 | 60 | Unassessed | +0 | Fully booked | 0 | Full scroll budget; allocation incomplete | 0 / 0 / 0 | 100 / 600 / 950 |
| Achak the Wendarin | 141 | Epic | Force | 5 | 50 | Unassessed | +0 | Incomplete | 15 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Alika | 8803 | Epic | Force | 5 | 50 | Unassessed | +0 | Incomplete | 20 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Atur | 43 | Epic | Magic | 5 | 50 | Unassessed | +0 | Incomplete | 10 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Bergoth the Malformed | 8828 | Epic | Spirit | 5 | 50 | Unassessed | +0 | Incomplete | 10 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Burangiri | 180 | Epic | Force | 5 | 50 | Unassessed | +0 | Fully booked | 0 | Partial allocation | 0 / 0 / 20 | 100 / 600 / 200 |
| Captain Temila | 13350 | Epic | Magic | 5 | 50 | Unassessed | +0 | Incomplete | 10 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Conellia | 5159 | Epic | Magic | 5 | 50 | Unassessed | +0 | Incomplete | 11 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Dark Elhain | 45 | Epic | Magic | 5 | 50 | Unassessed | +0 | Incomplete | 9 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Dhukk the Pierced | 8759 | Epic | Magic | 5 | 50 | Unassessed | +0 | Incomplete | 12 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Duedan the Runic | 3935 | Epic | Force | 5 | 50 | Unassessed | +0 | Incomplete | 10 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Fang Cleric | 5156 | Epic | Spirit | 5 | 50 | Unassessed | +0 | Incomplete | 12 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Galkut | 3949 | Epic | Spirit | 5 | 50 | Unassessed | +0 | Incomplete | 12 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Genbo the Dishonored | 160 | Epic | Void | 5 | 50 | Unassessed | +0 | Incomplete | 15 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Giscard the Sigiled | 8829 | Epic | Spirit | 5 | 50 | Unassessed | +0 | Incomplete | 12 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Hellgazer | 174 | Epic | Spirit | 5 | 50 | Unassessed | +0 | Incomplete | 9 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| High Khatun | 13 | Epic | Spirit | 5 | 50 | Increase SPD / chance-based slow | +0 | Incomplete | 11 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Hotatsu | 8800 | Epic | Magic | 5 | 50 | Unassessed | +0 | Incomplete | 15 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Lady Eresh | 3189 | Epic | Force | 5 | 50 | Unassessed | +0 | Incomplete | 9 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Locwain | 7084 | Epic | Magic | 5 | 50 | Unassessed | +0 | Incomplete | 13 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Melga Steelgirdle | 81 | Epic | Spirit | 5 | 50 | Unassessed | +0 | Incomplete | 7 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Morag Bronzelock | 2135 | Epic | Spirit | 5 | 50 | Unassessed | +0 | Incomplete | 9 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Mordecai | 3936 | Epic | Force | 5 | 50 | HP Burn / ally turn-meter boost | +0 | Fully booked | 0 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Rector Drath | 12124 | Epic | Force | 5 | 50 | Healing / conditional Perfect Veil / revive | +0 | Fully booked | 0 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Reinbeast | 117 | Epic | Force | 5 | 50 | Unassessed | +0 | Incomplete | 10 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Rock Breaker | 80 | Epic | Spirit | 5 | 50 | Unassessed | +0 | Incomplete | 11 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Runekeeper Dazdurk | 93 | Epic | Void | 5 | 50 | Unassessed | +0 | Incomplete | 10 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Sandlashed Survivor | 3945 | Epic | Spirit | 5 | 50 | Unassessed | +0 | Incomplete | 10 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Sanguinia | 12132 | Epic | Magic | 5 | 50 | Unassessed | +0 | Incomplete | 12 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Scion | 3191 | Epic | Magic | 5 | 50 | Unassessed | +0 | Incomplete | 10 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Skraank | 13094 | Epic | Void | 5 | 50 | Unassessed | +0 | Incomplete | 7 | Partial allocation | 0 / 59 / 0 | 100 / 480 / 0 |
| Snorting Thug | 4741 | Epic | Force | 5 | 50 | Unassessed | +0 | Incomplete | 11 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Spider | 129 | Epic | Force | 5 | 50 | Unassessed | +0 | Incomplete | 14 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Suiren | 83 | Epic | Force | 5 | 50 | Unassessed | +0 | Incomplete | 15 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Tainix Hateflower | 75 | Epic | Force | 5 | 50 | Unassessed | +0 | Incomplete | 10 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Thylessia | 225 | Epic | Force | 5 | 50 | Unassessed | +0 | Incomplete | 13 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Wysteri Vineguard | 230 | Epic | Void | 5 | 50 | Unassessed | +0 | Incomplete | 10 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Yuzan the Marooned | 6846 | Epic | Void | 5 | 50 | Unassessed | +0 | Incomplete | 11 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Zelotah | 5941 | Epic | Spirit | 5 | 50 | Unassessed | +0 | Incomplete | 14 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Archmage Hellmut | 15755 | Epic | Magic | 5 | 1 | Unassessed | +0 | Incomplete | 13 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Duhr the Hungerer | 15582 | Epic | Spirit | 5 | 1 | Unassessed | +0 | Fully booked | 0 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Kallia | 15751 | Epic | Force | 5 | 1 | Unassessed | +0 | Incomplete | 13 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Zargala | 15724 | Epic | Force | 5 | 1 | Unassessed | +0 | Incomplete | 15 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Adriel | 194 | Epic | Magic | 4 | 40 | Unassessed | +0 | Incomplete | 13 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Anchorite | 264 | Epic | Spirit | 4 | 40 | Unassessed | +0 | Incomplete | 7 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Balthus Drauglord | 15583 | Epic | Spirit | 4 | 40 | Unassessed | +0 | Incomplete | 15 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Bloodfeather | 7050 | Epic | Force | 4 | 40 | Unassessed | +0 | Incomplete | 11 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Bonekeeper | 15728 | Epic | Force | 4 | 40 | Unassessed | +0 | Incomplete | 13 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Bovos Sharphorn | 5157 | Epic | Spirit | 4 | 40 | Unassessed | +0 | Incomplete | 10 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Broadmaw | 4751 | Epic | Void | 4 | 40 | Unassessed | +0 | Incomplete | 11 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Ceez | 3190 | Epic | Force | 4 | 40 | Unassessed | +0 | Incomplete | 11 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Chancellor Yasmin | 14554 | Epic | Force | 4 | 40 | Unassessed | +0 | Incomplete | 12 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Crypt Witch | 5158 | Epic | Magic | 4 | 40 | Unassessed | +0 | Incomplete | 13 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Dark Athel | 34 | Epic | Magic | 4 | 40 | Unassessed | +0 | Incomplete | 13 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Defiled Sinner | 3955 | Epic | Force | 4 | 40 | Unassessed | +0 | Incomplete | 12 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Defiled Sinner | 4573 | Epic | Force | 4 | 40 | Unassessed | +0 | Incomplete | 12 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Duedan the Runic | 4554 | Epic | Force | 4 | 40 | Unassessed | +0 | Incomplete | 10 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Endalia | 19 | Epic | Magic | 4 | 40 | Unassessed | +0 | Incomplete | 14 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Fenax | 58 | Epic | Spirit | 4 | 40 | Unassessed | +0 | Incomplete | 13 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Flesh-Tearer | 13576 | Epic | Magic | 4 | 40 | Unassessed | +0 | Incomplete | 11 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Fren'zi the Cackler | 3932 | Epic | Void | 4 | 40 | Unassessed | +0 | Incomplete | 13 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Ghrush the Mangler | 85 | Epic | Spirit | 4 | 40 | Unassessed | +0 | Incomplete | 15 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Hexia | 4252 | Epic | Force | 4 | 40 | Unassessed | +0 | Incomplete | 10 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| High Khatun | 7607 | Epic | Spirit | 4 | 40 | Increase SPD / chance-based slow | +0 | Incomplete | 11 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Ilysinya | 8845 | Epic | Force | 4 | 40 | Unassessed | +0 | Incomplete | 11 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Jarang | 4171 | Epic | Magic | 4 | 40 | Unassessed | +0 | Incomplete | 13 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Jinglehunter | 12143 | Epic | Spirit | 4 | 40 | Unassessed | +0 | Incomplete | 14 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Jizoh | 7 | Epic | Spirit | 4 | 40 | Unassessed | +0 | Incomplete | 12 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Jotunn | 12179 | Epic | Magic | 4 | 40 | Unassessed | +0 | Incomplete | 13 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Kytis | 12174 | Epic | Spirit | 4 | 40 | Unassessed | +0 | Incomplete | 13 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Lady Quilen | 8801 | Epic | Force | 4 | 40 | Unassessed | +0 | Incomplete | 12 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Lordly Legionary | 57 | Epic | Magic | 4 | 40 | Unassessed | +0 | Incomplete | 9 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Lorn the Cutter | 4170 | Epic | Magic | 4 | 40 | Unassessed | +0 | Incomplete | 9 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Missionary | 152 | Epic | Force | 4 | 40 | Unassessed | +0 | Incomplete | 13 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Mordecai | 4558 | Epic | Force | 4 | 40 | HP Burn / ally turn-meter boost | +0 | Incomplete | 13 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Nazana | 4584 | Epic | Force | 4 | 40 | Unassessed | +0 | Incomplete | 13 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Phranox | 105 | Epic | Spirit | 4 | 40 | Unassessed | +0 | Incomplete | 15 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Prundar | 159 | Epic | Void | 4 | 40 | Unassessed | +0 | Incomplete | 20 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Relickeeper | 4761 | Epic | Force | 4 | 40 | Unassessed | +0 | Incomplete | 8 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Ripper | 3934 | Epic | Force | 4 | 40 | Unassessed | +0 | Incomplete | 12 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Runekeeper Dazdurk | 7030 | Epic | Void | 4 | 40 | Unassessed | +0 | Incomplete | 10 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Scabrius | 4544 | Epic | Magic | 4 | 40 | Unassessed | +0 | Incomplete | 14 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Sikara | 112 | Epic | Magic | 4 | 40 | Unassessed | +0 | Incomplete | 18 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Sikara | 7595 | Epic | Magic | 4 | 40 | Unassessed | +0 | Incomplete | 18 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Tainix Hateflower | 22 | Epic | Force | 4 | 40 | Unassessed | +0 | Incomplete | 10 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Thenasil | 237 | Epic | Force | 4 | 40 | Unassessed | +0 | Incomplete | 13 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Thenasil | 4572 | Epic | Force | 4 | 40 | Unassessed | +0 | Incomplete | 13 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Theresc | 7597 | Epic | Force | 4 | 40 | Unassessed | +0 | Incomplete | 15 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Tidemaster Dexikos | 15653 | Epic | Magic | 4 | 40 | Unassessed | +0 | Incomplete | 10 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Tolf the Maimed | 213 | Epic | Void | 4 | 40 | Unassessed | +0 | Incomplete | 10 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Trumborr | 7605 | Epic | Spirit | 4 | 40 | Unassessed | +0 | Incomplete | 9 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Valla | 13351 | Epic | Spirit | 4 | 40 | Unassessed | +0 | Incomplete | 10 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Vrask | 8825 | Epic | Spirit | 4 | 40 | Unassessed | +0 | Incomplete | 8 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Xanthe Seaflower | 12142 | Epic | Force | 4 | 40 | Unassessed | +0 | Incomplete | 11 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Yaga the Insatiable | 23 | Epic | Force | 4 | 40 | Unassessed | +0 | Incomplete | 15 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Achak the Wendarin | 15575 | Epic | Force | 4 | 15 | Unassessed | +0 | Incomplete | 15 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Canoness | 15577 | Epic | Magic | 4 | 15 | Unassessed | +0 | Incomplete | 12 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Canoness | 15737 | Epic | Magic | 4 | 15 | Unassessed | +0 | Incomplete | 12 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Fenax | 15570 | Epic | Spirit | 4 | 15 | Unassessed | +0 | Incomplete | 13 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Golden Reaper | 14612 | Epic | Void | 4 | 15 | Unassessed | +0 | Incomplete | 12 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Kunoichi | 15752 | Epic | Force | 4 | 15 | Unassessed | +0 | Incomplete | 12 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Mordecai | 13563 | Epic | Force | 4 | 15 | HP Burn / ally turn-meter boost | +0 | Incomplete | 13 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Relickeeper | 14552 | Epic | Force | 4 | 15 | Unassessed | +0 | Incomplete | 8 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Suiren | 13558 | Epic | Force | 4 | 15 | Unassessed | +0 | Incomplete | 10 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Terrorbeast | 15753 | Epic | Spirit | 4 | 15 | Unassessed | +0 | Incomplete | 13 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Theresc | 8802 | Epic | Force | 4 | 15 | Unassessed | +0 | Incomplete | 15 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Thylessia | 15726 | Epic | Force | 4 | 15 | Unassessed | +0 | Incomplete | 13 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Uugo | 12436 | Epic | Magic | 4 | 15 | Block Buffs / Decrease DEF / healing | +0 | Incomplete | 16 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Zelotah | 15745 | Epic | Spirit | 4 | 15 | Unassessed | +0 | Incomplete | 14 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |

## Rare Champions

| Champion | ID | Rarity | Affinity | Rank | Level | Hydra role | Empowerment | Books | Books missing | Masteries | Used scrolls | Unused scrolls |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Bellower | 3933 | Rare | Void | 6 | 60 | Unassessed | +0 | Fully booked | 0 | Full scroll budget; allocation incomplete | 0 / 0 / 0 | 100 / 600 / 950 |
| Gnarlhorn | 5 | Rare | Spirit | 6 | 60 | Provoke | +0 | Fully booked | 0 | Full scroll budget; allocation incomplete | 0 / 0 / 0 | 100 / 600 / 950 |
| Apothecary | 933 | Rare | Magic | 5 | 50 | Unassessed | +0 | Fully booked | 0 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Elhain | 4040 | Rare | Magic | 5 | 50 | Unassessed | +0 | Incomplete | 3 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Fanatic | 86 | Rare | Void | 5 | 50 | Unassessed | +0 | Incomplete | 8 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Frozen Banshee | 4552 | Rare | Magic | 5 | 50 | Unassessed | +0 | Incomplete | 13 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Galek | 127 | Rare | Magic | 5 | 50 | Unassessed | +0 | Fully booked | 0 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Geargrinder | 103 | Rare | Void | 5 | 50 | Unassessed | +0 | Fully booked | 0 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Kael | 1 | Rare | Magic | 5 | 50 | Unassessed | +0 | Fully booked | 0 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Lifetaker | 124 | Rare | Magic | 5 | 50 | Unassessed | +0 | Fully booked | 0 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Meatcarver Tolog | 205 | Rare | Force | 5 | 50 | Unassessed | +0 | Incomplete | 5 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Paragon | 15 | Rare | Void | 5 | 50 | Unassessed | +0 | Fully booked | 0 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Reliquary Tender | 130 | Rare | Void | 5 | 50 | Unassessed | +0 | Fully booked | 0 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Renegade | 6850 | Rare | Void | 5 | 50 | Unassessed | +0 | Incomplete | 9 | Partial allocation | 0 / 0 / 188 | 100 / 600 / 200 |
| Totem | 4551 | Rare | Spirit | 5 | 50 | Unassessed | +0 | Incomplete | 11 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Vagabond | 6 | Rare | Spirit | 5 | 50 | Unassessed | +0 | Incomplete | 12 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Hound Spawn | 15129 | Rare | Force | 5 | 17 | Unassessed | +0 | Incomplete | 15 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Abyssal | 215 | Rare | Spirit | 4 | 40 | Unassessed | +0 | Incomplete | 9 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Acolyte of the Slither | 4044 | Rare | Spirit | 4 | 40 | Unassessed | +0 | Incomplete | 10 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Amarantine Skeleton | 6853 | Rare | Void | 4 | 40 | Unassessed | +0 | Incomplete | 15 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Avir the Alchemage | 241 | Rare | Magic | 4 | 40 | Unassessed | +0 | Incomplete | 12 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Berserker | 142 | Rare | Spirit | 4 | 40 | Unassessed | +0 | Fully booked | 0 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Bogwalker | 249 | Rare | Force | 4 | 40 | Unassessed | +0 | Incomplete | 13 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Branch-arm Lasair | 253 | Rare | Void | 4 | 40 | Unassessed | +0 | Incomplete | 10 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Bulwark | 197 | Rare | Void | 4 | 40 | Unassessed | +0 | Incomplete | 11 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Centurion | 29 | Rare | Void | 4 | 40 | Unassessed | +0 | Incomplete | 9 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Fellhound | 3931 | Rare | Void | 4 | 40 | Unassessed | +0 | Incomplete | 5 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Gnarlhorn | 4563 | Rare | Spirit | 4 | 40 | Provoke | +0 | Incomplete | 7 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Graybeard | 25 | Rare | Magic | 4 | 40 | Unassessed | +0 | Incomplete | 15 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Ironclad | 17 | Rare | Force | 4 | 40 | Unassessed | +0 | Incomplete | 5 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Kurzad Deepheart | 254 | Rare | Void | 4 | 40 | Unassessed | +0 | Incomplete | 16 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Marquess | 171 | Rare | Spirit | 4 | 40 | Unassessed | +0 | Incomplete | 15 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Metalshaper | 10449 | Rare | Spirit | 4 | 40 | Unassessed | +0 | Incomplete | 12 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Mycolus | 187 | Rare | Void | 4 | 40 | Unassessed | +0 | Incomplete | 9 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Ogryn Jailer | 24 | Rare | Force | 4 | 40 | Unassessed | +0 | Incomplete | 14 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Painsmith | 38 | Rare | Void | 4 | 40 | Unassessed | +0 | Incomplete | 14 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Petrifya Rockroot | 199 | Rare | Magic | 4 | 40 | Unassessed | +0 | Incomplete | 14 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Shadowbow Tirlac | 1925 | Rare | Spirit | 4 | 40 | Unassessed | +0 | Incomplete | 11 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Skink | 138 | Rare | Magic | 4 | 40 | Unassessed | +0 | Incomplete | 13 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Teryx the Restless | 6861 | Rare | Void | 4 | 40 | Unassessed | +0 | Incomplete | 8 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Treefeller | 227 | Rare | Force | 4 | 40 | Unassessed | +0 | Incomplete | 14 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Valerie | 4042 | Rare | Magic | 4 | 40 | Unassessed | +0 | Incomplete | 7 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Vanguard | 26 | Rare | Void | 4 | 40 | Unassessed | +0 | Incomplete | 9 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Wanderer | 188 | Rare | Spirit | 4 | 40 | Unassessed | +0 | Incomplete | 11 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Abyssal | 8038 | Rare | Spirit | 3 | 11 | Unassessed | +0 | Incomplete | 11 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Adjudicator | 9 | Rare | Magic | 3 | 11 | Unassessed | +0 | Incomplete | 17 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Amarantine Skeleton | 6856 | Rare | Void | 3 | 11 | Unassessed | +0 | Incomplete | 15 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Anointed | 11489 | Rare | Force | 3 | 11 | Unassessed | +0 | Incomplete | 8 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Apothecary | 9446 | Rare | Magic | 3 | 11 | Unassessed | +0 | Incomplete | 10 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Arcanist | 9558 | Rare | Force | 3 | 11 | Unassessed | +0 | Incomplete | 8 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Ashwalker | 3927 | Rare | Void | 3 | 11 | Unassessed | +0 | Incomplete | 17 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Assassin | 15746 | Rare | Magic | 3 | 11 | Unassessed | +0 | Incomplete | 16 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Athel | 66 | Rare | Magic | 3 | 11 | Unassessed | +0 | Incomplete | 12 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Athel | 16423 | Rare | Magic | 3 | 11 | Unassessed | +0 | Incomplete | 12 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Avenger | 15733 | Rare | Magic | 3 | 11 | Unassessed | +0 | Incomplete | 14 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Avir the Alchemage | 9042 | Rare | Magic | 3 | 11 | Unassessed | +0 | Incomplete | 11 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Banshee | 9560 | Rare | Magic | 3 | 11 | Unassessed | +0 | Incomplete | 9 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Berserker | 4564 | Rare | Spirit | 3 | 11 | Unassessed | +0 | Incomplete | 11 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Bladerider | 13584 | Rare | Magic | 3 | 11 | Unassessed | +0 | Incomplete | 12 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Bloodbraid | 4173 | Rare | Spirit | 3 | 11 | Unassessed | +0 | Incomplete | 14 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Bloodhorn | 14550 | Rare | Void | 3 | 11 | Unassessed | +0 | Incomplete | 6 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Bloodmask | 13924 | Rare | Force | 3 | 11 | Unassessed | +0 | Incomplete | 11 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Bloodpainter | 12149 | Rare | Force | 3 | 11 | Unassessed | +0 | Incomplete | 13 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Boltsmith | 15571 | Rare | Force | 3 | 11 | Unassessed | +0 | Incomplete | 11 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Bombardier | 15260 | Rare | Force | 3 | 11 | Unassessed | +0 | Incomplete | 14 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Cagebound | 32 | Rare | Void | 3 | 11 | Unassessed | +0 | Incomplete | 10 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Candleguard | 13566 | Rare | Magic | 3 | 11 | Unassessed | +0 | Incomplete | 8 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Castigator | 4055 | Rare | Magic | 3 | 11 | Unassessed | +0 | Incomplete | 8 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Cataphract | 163 | Rare | Spirit | 3 | 11 | Unassessed | +0 | Incomplete | 9 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Chaplain | 15446 | Rare | Force | 3 | 11 | Unassessed | +0 | Incomplete | 6 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Chopper | 181 | Rare | Magic | 3 | 11 | Unassessed | +0 | Incomplete | 14 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Coffin Smasher | 4579 | Rare | Magic | 3 | 11 | Unassessed | +0 | Incomplete | 14 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Conquerer | 9559 | Rare | Spirit | 3 | 11 | Unassessed | +0 | Incomplete | 14 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Corpulent Cadaver | 3151 | Rare | Spirit | 3 | 11 | Unassessed | +0 | Incomplete | 15 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Courtier | 16349 | Rare | Force | 3 | 11 | Unassessed | +0 | Incomplete | 13 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Crimson Pegason | 12265 | Rare | Force | 3 | 11 | Unassessed | +0 | Incomplete | 8 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Crimson Slayer | 2655 | Rare | Spirit | 3 | 11 | Unassessed | +0 | Incomplete | 19 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Crossbowman | 7591 | Rare | Magic | 3 | 11 | Unassessed | +0 | Incomplete | 8 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Cudgeler | 148 | Rare | Magic | 3 | 11 | Unassessed | +0 | Incomplete | 13 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Daywalker | 12125 | Rare | Void | 3 | 11 | Unassessed | +0 | Incomplete | 5 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Deathchanter | 8805 | Rare | Magic | 3 | 11 | Unassessed | +0 | Incomplete | 17 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Denid the Tusk Knight | 558 | Rare | Void | 3 | 11 | Unassessed | +0 | Incomplete | 9 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Diabolist | 16246 | Rare | Magic | 3 | 11 | Unassessed | +0 | Incomplete | 10 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Diabolist | 16252 | Rare | Magic | 3 | 11 | Unassessed | +0 | Incomplete | 10 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Diabolist | 16441 | Rare | Magic | 3 | 11 | Unassessed | +0 | Incomplete | 10 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Diabolist | 16445 | Rare | Magic | 3 | 11 | Unassessed | +0 | Incomplete | 10 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Diabolist | 16482 | Rare | Magic | 3 | 11 | Unassessed | +0 | Incomplete | 10 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Diabolist | 16483 | Rare | Magic | 3 | 11 | Unassessed | +0 | Incomplete | 10 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Dilgol | 6847 | Rare | Void | 3 | 11 | Unassessed | +0 | Incomplete | 15 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Draconis | 6859 | Rare | Void | 3 | 11 | Unassessed | +0 | Incomplete | 8 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Drowned Bloatwraith | 14609 | Rare | Void | 3 | 11 | Unassessed | +0 | Incomplete | 10 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Dunestrider | 7662 | Rare | Magic | 3 | 11 | Unassessed | +0 | Incomplete | 14 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Elder | 552 | Rare | Magic | 3 | 11 | Unassessed | +0 | Incomplete | 6 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Eviscerator | 14604 | Rare | Void | 3 | 11 | Unassessed | +0 | Incomplete | 10 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Executioner | 4587 | Rare | Magic | 3 | 11 | Unassessed | +0 | Incomplete | 12 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Executioner | 8615 | Rare | Magic | 3 | 11 | Unassessed | +0 | Incomplete | 12 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Flailer | 120 | Rare | Magic | 3 | 11 | Unassessed | +0 | Incomplete | 11 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Flesheater | 4540 | Rare | Spirit | 3 | 11 | Unassessed | +0 | Incomplete | 9 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Flesheater | 16334 | Rare | Spirit | 3 | 11 | Unassessed | +0 | Incomplete | 9 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Fleshmonger | 5166 | Rare | Magic | 3 | 11 | Unassessed | +0 | Incomplete | 13 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Flinger | 13564 | Rare | Spirit | 3 | 11 | Unassessed | +0 | Incomplete | 13 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Fortress Goon | 8822 | Rare | Magic | 3 | 11 | Unassessed | +0 | Incomplete | 12 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Furystoker | 113 | Rare | Spirit | 3 | 11 | Unassessed | +0 | Incomplete | 8 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Galek | 7656 | Rare | Magic | 3 | 11 | Unassessed | +0 | Incomplete | 13 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Galek | 13553 | Rare | Magic | 3 | 11 | Unassessed | +0 | Incomplete | 13 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Geargrinder | 6854 | Rare | Void | 3 | 11 | Unassessed | +0 | Incomplete | 11 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Ghoulish Ranger | 1077 | Rare | Spirit | 3 | 11 | Unassessed | +0 | Incomplete | 15 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Glensage Cithrel | 14608 | Rare | Void | 3 | 11 | Unassessed | +0 | Incomplete | 11 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Gloril Brutebane | 126 | Rare | Spirit | 3 | 11 | Unassessed | +0 | Incomplete | 12 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Goremask | 8819 | Rare | Force | 3 | 11 | Unassessed | +0 | Incomplete | 17 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Grandmaster | 9214 | Rare | Magic | 3 | 11 | Unassessed | +0 | Incomplete | 12 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Grappler | 56 | Rare | Spirit | 3 | 11 | Unassessed | +0 | Incomplete | 15 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Gravechill Killer | 9064 | Rare | Magic | 3 | 11 | Unassessed | +0 | Incomplete | 8 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Graybeard | 3743 | Rare | Magic | 3 | 11 | Unassessed | +0 | Incomplete | 15 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Graybeard | 16416 | Rare | Magic | 3 | 11 | Unassessed | +0 | Incomplete | 15 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Grinner | 12136 | Rare | Force | 3 | 11 | Unassessed | +0 | Incomplete | 14 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Guardian | 4174 | Rare | Spirit | 3 | 11 | Unassessed | +0 | Incomplete | 12 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Hatchet Slinger | 121 | Rare | Spirit | 3 | 11 | Unassessed | +0 | Incomplete | 11 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Headsman | 5909 | Rare | Spirit | 3 | 11 | Unassessed | +0 | Incomplete | 10 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Heiress | 8833 | Rare | Force | 3 | 11 | Unassessed | +0 | Incomplete | 8 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Heiress | 9554 | Rare | Force | 3 | 11 | Unassessed | +0 | Incomplete | 8 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Hellborn Sprite | 4463 | Rare | Spirit | 3 | 11 | Unassessed | +0 | Incomplete | 11 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Hellfang | 27 | Rare | Spirit | 3 | 11 | Unassessed | +0 | Incomplete | 17 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Hellfreak | 4038 | Rare | Spirit | 3 | 11 | Unassessed | +0 | Incomplete | 15 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Hexweaver | 8821 | Rare | Spirit | 3 | 11 | Unassessed | +0 | Incomplete | 11 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Hill Nomad | 12150 | Rare | Magic | 3 | 11 | Unassessed | +0 | Incomplete | 10 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Hollow | 6862 | Rare | Void | 3 | 11 | Unassessed | +0 | Incomplete | 12 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Honor Guard | 15966 | Rare | Force | 3 | 11 | Unassessed | +0 | Incomplete | 17 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Hospitaller | 1736 | Rare | Magic | 3 | 11 | Unassessed | +0 | Incomplete | 10 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Hound Spawn | 16055 | Rare | Force | 3 | 11 | Unassessed | +0 | Incomplete | 15 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Hound Spawn | 16228 | Rare | Force | 3 | 11 | Unassessed | +0 | Incomplete | 15 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Hound Spawn | 16248 | Rare | Force | 3 | 11 | Unassessed | +0 | Incomplete | 15 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Hound Spawn | 16263 | Rare | Force | 3 | 11 | Unassessed | +0 | Incomplete | 15 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Hound Spawn | 16295 | Rare | Force | 3 | 11 | Unassessed | +0 | Incomplete | 15 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Huntress | 14549 | Rare | Void | 3 | 11 | Unassessed | +0 | Incomplete | 11 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Hyria | 1732 | Rare | Spirit | 3 | 11 | Unassessed | +0 | Incomplete | 10 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Interceptor | 6849 | Rare | Void | 3 | 11 | Unassessed | +0 | Incomplete | 11 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Ironclad | 15735 | Rare | Force | 3 | 11 | Unassessed | +0 | Incomplete | 5 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Itinerant | 15091 | Rare | Force | 3 | 11 | Unassessed | +0 | Incomplete | 9 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Judge | 15742 | Rare | Magic | 3 | 11 | Unassessed | +0 | Incomplete | 8 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Judicator | 4051 | Rare | Spirit | 3 | 11 | Unassessed | +0 | Incomplete | 14 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Justiciar | 6858 | Rare | Void | 3 | 11 | Unassessed | +0 | Incomplete | 9 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Lamellar | 13596 | Rare | Force | 3 | 11 | Unassessed | +0 | Incomplete | 8 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Lamibur | 8823 | Rare | Spirit | 3 | 11 | Unassessed | +0 | Incomplete | 10 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Lifetaker | 14834 | Rare | Magic | 3 | 11 | Unassessed | +0 | Incomplete | 11 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Loneblade Riab | 8839 | Rare | Force | 3 | 11 | Unassessed | +0 | Incomplete | 13 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Loneblade Riab | 16468 | Rare | Force | 3 | 11 | Unassessed | +0 | Incomplete | 13 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Longsword Torrux | 1163 | Rare | Spirit | 3 | 11 | Unassessed | +0 | Incomplete | 14 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Madman | 6695 | Rare | Spirit | 3 | 11 | Unassessed | +0 | Incomplete | 12 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Magister | 7176 | Rare | Force | 3 | 11 | Unassessed | +0 | Incomplete | 13 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Magmablood | 7670 | Rare | Force | 3 | 11 | Unassessed | +0 | Incomplete | 14 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Magus | 15741 | Rare | Magic | 3 | 11 | Unassessed | +0 | Incomplete | 14 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Maiden | 4562 | Rare | Spirit | 3 | 11 | Unassessed | +0 | Incomplete | 13 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Malbranche | 203 | Rare | Void | 3 | 11 | Unassessed | +0 | Incomplete | 14 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Marauder | 13568 | Rare | Spirit | 3 | 11 | Unassessed | +0 | Incomplete | 14 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Marked | 9791 | Rare | Magic | 3 | 11 | Unassessed | +0 | Incomplete | 12 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Marquess | 3417 | Rare | Spirit | 3 | 11 | Unassessed | +0 | Incomplete | 15 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Marquis | 7279 | Rare | Void | 3 | 11 | Unassessed | +0 | Incomplete | 11 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Meatcarver Tolog | 16355 | Rare | Force | 3 | 11 | Unassessed | +0 | Incomplete | 8 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Medicus | 50 | Rare | Spirit | 3 | 11 | Unassessed | +0 | Incomplete | 12 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Misericord | 236 | Rare | Magic | 3 | 11 | Unassessed | +0 | Incomplete | 8 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Mother Superior | 7590 | Rare | Spirit | 3 | 11 | Unassessed | +0 | Incomplete | 10 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Muckstalker | 3711 | Rare | Magic | 3 | 11 | Unassessed | +0 | Incomplete | 11 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Myrmidon | 13748 | Rare | Magic | 3 | 11 | Unassessed | +0 | Incomplete | 17 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Mystic Hand | 14568 | Rare | Force | 3 | 11 | Unassessed | +0 | Incomplete | 12 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Odachi | 15720 | Rare | Force | 3 | 11 | Unassessed | +0 | Incomplete | 11 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Ogryn Jailer | 7108 | Rare | Force | 3 | 11 | Unassessed | +0 | Incomplete | 14 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Ox | 14610 | Rare | Void | 3 | 11 | Unassessed | +0 | Incomplete | 12 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Pain Keeper | 14601 | Rare | Void | 3 | 11 | Unassessed | +0 | Incomplete | 15 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Pain Keeper | 14607 | Rare | Void | 3 | 11 | Unassessed | +0 | Incomplete | 15 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Panthera | 4241 | Rare | Void | 3 | 11 | Unassessed | +0 | Incomplete | 17 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Paragon | 3928 | Rare | Void | 3 | 11 | Unassessed | +0 | Incomplete | 10 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Paragon | 14605 | Rare | Void | 3 | 11 | Unassessed | +0 | Incomplete | 10 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Petrifya Rockroot | 14566 | Rare | Magic | 3 | 11 | Unassessed | +0 | Incomplete | 14 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Pigsticker | 7603 | Rare | Magic | 3 | 11 | Unassessed | +0 | Incomplete | 13 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Pounder | 7596 | Rare | Magic | 3 | 11 | Unassessed | +0 | Incomplete | 8 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Preserver | 12133 | Rare | Force | 3 | 11 | Unassessed | +0 | Incomplete | 13 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Prosecutor | 4559 | Rare | Spirit | 3 | 11 | Unassessed | +0 | Incomplete | 9 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Quaestor | 15779 | Rare | Force | 3 | 11 | Unassessed | +0 | Incomplete | 9 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Ragemonger | 9326 | Rare | Void | 3 | 11 | Unassessed | +0 | Incomplete | 13 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Raider | 15739 | Rare | Spirit | 3 | 11 | Unassessed | +0 | Incomplete | 13 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Redcloak Taneko | 15759 | Rare | Magic | 3 | 11 | Unassessed | +0 | Incomplete | 9 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Renegade | 12180 | Rare | Void | 3 | 11 | Unassessed | +0 | Incomplete | 10 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Retainer | 12131 | Rare | Void | 3 | 11 | Unassessed | +0 | Incomplete | 13 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Ripperfist | 137 | Rare | Void | 3 | 11 | Unassessed | +0 | Incomplete | 13 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Riscarm | 1953 | Rare | Spirit | 3 | 11 | Unassessed | +0 | Incomplete | 10 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Rocktooth | 11600 | Rare | Magic | 3 | 11 | Unassessed | +0 | Incomplete | 14 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Rotting Mage | 73 | Rare | Spirit | 3 | 11 | Unassessed | +0 | Incomplete | 10 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Ruffstone | 7606 | Rare | Force | 3 | 11 | Unassessed | +0 | Incomplete | 13 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Runic Warder | 13362 | Rare | Magic | 3 | 11 | Unassessed | +0 | Incomplete | 12 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Sanctum Protector | 2835 | Rare | Spirit | 3 | 11 | Unassessed | +0 | Incomplete | 13 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Scrapper | 170 | Rare | Void | 3 | 11 | Unassessed | +0 | Incomplete | 15 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Selinia Nightcloak | 12176 | Rare | Void | 3 | 11 | Unassessed | +0 | Incomplete | 14 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Shadowbow Tirlac | 8835 | Rare | Spirit | 3 | 11 | Unassessed | +0 | Incomplete | 11 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Siegebreaker | 14580 | Rare | Spirit | 3 | 11 | Unassessed | +0 | Incomplete | 14 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Silvain the Paramour | 6863 | Rare | Void | 3 | 11 | Unassessed | +0 | Incomplete | 8 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Skink | 15283 | Rare | Magic | 3 | 11 | Unassessed | +0 | Incomplete | 13 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Skirmisher | 3946 | Rare | Void | 3 | 11 | Unassessed | +0 | Incomplete | 14 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Skullsworn | 13556 | Rare | Force | 3 | 11 | Unassessed | +0 | Incomplete | 10 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Slitherbrute | 11273 | Rare | Magic | 3 | 11 | Unassessed | +0 | Incomplete | 11 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Soulbond Bowyer | 13569 | Rare | Spirit | 3 | 11 | Unassessed | +0 | Incomplete | 16 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Soulbond Bowyer | 15574 | Rare | Spirit | 3 | 11 | Unassessed | +0 | Incomplete | 16 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Spymaster | 15579 | Rare | Force | 3 | 11 | Unassessed | +0 | Incomplete | 14 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Steadfast Marshal | 12127 | Rare | Void | 3 | 11 | Unassessed | +0 | Incomplete | 6 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Stitched Beast | 6860 | Rare | Void | 3 | 11 | Unassessed | +0 | Incomplete | 15 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Sunken Sentinel | 6855 | Rare | Void | 3 | 11 | Unassessed | +0 | Incomplete | 12 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Templar | 9561 | Rare | Spirit | 3 | 11 | Unassessed | +0 | Incomplete | 10 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Templar | 13555 | Rare | Spirit | 3 | 11 | Unassessed | +0 | Incomplete | 10 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Templar | 13559 | Rare | Spirit | 3 | 11 | Unassessed | +0 | Incomplete | 10 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Temptress | 15730 | Rare | Magic | 3 | 11 | Unassessed | +0 | Incomplete | 11 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Theurgist | 11926 | Rare | Magic | 3 | 11 | Unassessed | +0 | Incomplete | 11 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Tigersoul | 111 | Rare | Spirit | 3 | 11 | Unassessed | +0 | Incomplete | 19 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Tormentor | 6671 | Rare | Magic | 3 | 11 | Unassessed | +0 | Incomplete | 14 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Totem | 259 | Rare | Spirit | 3 | 11 | Unassessed | +0 | Incomplete | 12 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Treefeller | 13574 | Rare | Force | 3 | 11 | Unassessed | +0 | Incomplete | 14 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Tribuck Colwyn | 102 | Rare | Magic | 3 | 11 | Unassessed | +0 | Incomplete | 9 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Twinclaw Disciple | 7269 | Rare | Force | 3 | 11 | Unassessed | +0 | Incomplete | 11 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Vagabond | 3956 | Rare | Spirit | 3 | 11 | Unassessed | +0 | Incomplete | 12 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Valerie | 12177 | Rare | Magic | 3 | 11 | Unassessed | +0 | Incomplete | 9 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Vanguard | 164 | Rare | Void | 3 | 11 | Unassessed | +0 | Incomplete | 9 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Vanguard | 9327 | Rare | Void | 3 | 11 | Unassessed | +0 | Incomplete | 9 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Wagonbane | 14562 | Rare | Magic | 3 | 11 | Unassessed | +0 | Incomplete | 17 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Wanderer | 9740 | Rare | Spirit | 3 | 11 | Unassessed | +0 | Incomplete | 14 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Warmaiden | 10093 | Rare | Force | 3 | 11 | Unassessed | +0 | Incomplete | 13 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Warmaiden | 13372 | Rare | Force | 3 | 11 | Unassessed | +0 | Incomplete | 13 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Warmaiden | 15946 | Rare | Force | 3 | 11 | Unassessed | +0 | Incomplete | 13 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Warpriest | 280 | Rare | Spirit | 3 | 11 | Unassessed | +0 | Incomplete | 11 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Witness | 69 | Rare | Magic | 3 | 11 | Unassessed | +0 | Incomplete | 12 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Wretch | 15723 | Rare | Force | 3 | 11 | Unassessed | +0 | Incomplete | 12 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Wyvernbane | 7657 | Rare | Spirit | 3 | 11 | Unassessed | +0 | Incomplete | 10 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Coffin Smasher | 15851 | Rare | Magic | 3 | 10 | Unassessed | +0 | Incomplete | 14 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Diabolist | 16251 | Rare | Magic | 3 | 1 | Unassessed | +0 | Incomplete | 10 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Diabolist | 16268 | Rare | Magic | 3 | 1 | Unassessed | +0 | Incomplete | 10 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Diabolist | 16269 | Rare | Magic | 3 | 1 | Unassessed | +0 | Incomplete | 10 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Diabolist | 16294 | Rare | Magic | 3 | 1 | Unassessed | +0 | Incomplete | 10 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Diabolist | 16367 | Rare | Magic | 3 | 1 | Unassessed | +0 | Incomplete | 10 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |

## Uncommon Champions

| Champion | ID | Rarity | Affinity | Rank | Level | Hydra role | Empowerment | Books | Books missing | Masteries | Used scrolls | Unused scrolls |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Incubus | 15128 | Uncommon | Force | 5 | 17 | Unassessed | +0 | Incomplete | 10 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Incubus | 15164 | Uncommon | Force | 5 | 17 | Unassessed | +0 | Incomplete | 10 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Incubus | 16208 | Uncommon | Force | 5 | 17 | Unassessed | +0 | Incomplete | 10 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Incubus | 16209 | Uncommon | Force | 5 | 17 | Unassessed | +0 | Incomplete | 10 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Archer | 15977 | Uncommon | Magic | 3 | 11 | Unassessed | +0 | Incomplete | 11 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Battle Sister | 16233 | Uncommon | Magic | 3 | 11 | Unassessed | +0 | Incomplete | 10 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Branchweaver | 15957 | Uncommon | Spirit | 3 | 11 | Unassessed | +0 | Incomplete | 4 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Crusher | 16185 | Uncommon | Spirit | 3 | 11 | Unassessed | +0 | Incomplete | 8 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Crusher | 16258 | Uncommon | Spirit | 3 | 11 | Unassessed | +0 | Incomplete | 8 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Crusher | 16314 | Uncommon | Spirit | 3 | 11 | Unassessed | +0 | Incomplete | 8 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Dervish | 16332 | Uncommon | Magic | 3 | 11 | Unassessed | +0 | Incomplete | 9 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Dervish | 16380 | Uncommon | Magic | 3 | 11 | Unassessed | +0 | Incomplete | 9 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Duelist | 16283 | Uncommon | Force | 3 | 11 | Unassessed | +0 | Incomplete | 13 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Elfguard | 16105 | Uncommon | Spirit | 3 | 11 | Unassessed | +0 | Incomplete | 9 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Head Taker | 15972 | Uncommon | Magic | 3 | 11 | Unassessed | +0 | Incomplete | 10 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Incubus | 16267 | Uncommon | Force | 3 | 11 | Unassessed | +0 | Incomplete | 10 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Incubus | 16291 | Uncommon | Force | 3 | 11 | Unassessed | +0 | Incomplete | 10 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Incubus | 16292 | Uncommon | Force | 3 | 11 | Unassessed | +0 | Incomplete | 10 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Incubus | 16293 | Uncommon | Force | 3 | 11 | Unassessed | +0 | Incomplete | 10 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Incubus | 16440 | Uncommon | Force | 3 | 11 | Unassessed | +0 | Incomplete | 10 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Incubus | 16442 | Uncommon | Force | 3 | 11 | Unassessed | +0 | Incomplete | 10 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Incubus | 16443 | Uncommon | Force | 3 | 11 | Unassessed | +0 | Incomplete | 10 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Incubus | 16444 | Uncommon | Force | 3 | 11 | Unassessed | +0 | Incomplete | 10 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Incubus | 16477 | Uncommon | Force | 3 | 11 | Unassessed | +0 | Incomplete | 10 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Incubus | 16478 | Uncommon | Force | 3 | 11 | Unassessed | +0 | Incomplete | 10 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Incubus | 16479 | Uncommon | Force | 3 | 11 | Unassessed | +0 | Incomplete | 10 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Intercessor | 16447 | Uncommon | Force | 3 | 11 | Unassessed | +0 | Incomplete | 8 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Redeemer | 16282 | Uncommon | Force | 3 | 11 | Unassessed | +0 | Incomplete | 9 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Redeemer | 16436 | Uncommon | Force | 3 | 11 | Unassessed | +0 | Incomplete | 9 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Redeemer | 16453 | Uncommon | Force | 3 | 11 | Unassessed | +0 | Incomplete | 9 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Redeemer | 16472 | Uncommon | Force | 3 | 11 | Unassessed | +0 | Incomplete | 9 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Ritualist | 16245 | Uncommon | Magic | 3 | 11 | Unassessed | +0 | Incomplete | 9 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Spiritwalker | 16345 | Uncommon | Force | 3 | 11 | Unassessed | +0 | Incomplete | 7 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Vilespawn | 16317 | Uncommon | Spirit | 3 | 11 | Unassessed | +0 | Incomplete | 12 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Word Bearer | 16412 | Uncommon | Magic | 3 | 11 | Unassessed | +0 | Incomplete | 10 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Word Bearer | 16422 | Uncommon | Magic | 3 | 11 | Unassessed | +0 | Incomplete | 10 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Zephyr Sniper | 15953 | Uncommon | Spirit | 3 | 11 | Unassessed | +0 | Incomplete | 5 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Zephyr Sniper | 16388 | Uncommon | Spirit | 3 | 11 | Unassessed | +0 | Incomplete | 5 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Elfguard | 16013 | Uncommon | Spirit | 3 | 10 | Unassessed | +0 | Incomplete | 9 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Throatcutter | 16067 | Uncommon | Spirit | 3 | 10 | Unassessed | +0 | Incomplete | 10 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Armiger | 15633 | Uncommon | Spirit | 2 | 1 | Unassessed | +0 | Incomplete | 9 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Armiger | 15899 | Uncommon | Spirit | 2 | 1 | Unassessed | +0 | Incomplete | 9 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Armiger | 16006 | Uncommon | Spirit | 2 | 1 | Unassessed | +0 | Incomplete | 9 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Conscript | 15471 | Uncommon | Spirit | 2 | 1 | Unassessed | +0 | Incomplete | 11 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Conscript | 15527 | Uncommon | Spirit | 2 | 1 | Unassessed | +0 | Incomplete | 11 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Conscript | 15713 | Uncommon | Spirit | 2 | 1 | Unassessed | +0 | Incomplete | 11 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Conscript | 15820 | Uncommon | Spirit | 2 | 1 | Unassessed | +0 | Incomplete | 11 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Conscript | 16091 | Uncommon | Spirit | 2 | 1 | Unassessed | +0 | Incomplete | 11 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Conscript | 16451 | Uncommon | Spirit | 2 | 1 | Unassessed | +0 | Incomplete | 11 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Crusader | 16413 | Uncommon | Force | 2 | 1 | Unassessed | +0 | Incomplete | 9 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Elfguard | 16476 | Uncommon | Spirit | 2 | 1 | Unassessed | +0 | Incomplete | 9 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Frontline Warrior | 15634 | Uncommon | Spirit | 2 | 1 | Unassessed | +0 | Incomplete | 4 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Frontline Warrior | 15931 | Uncommon | Spirit | 2 | 1 | Unassessed | +0 | Incomplete | 4 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Glenspear | 16427 | Uncommon | Magic | 2 | 1 | Unassessed | +0 | Incomplete | 4 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Herald | 15478 | Uncommon | Spirit | 2 | 1 | Unassessed | +0 | Incomplete | 7 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Herald | 15648 | Uncommon | Spirit | 2 | 1 | Unassessed | +0 | Incomplete | 7 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Herald | 15918 | Uncommon | Spirit | 2 | 1 | Unassessed | +0 | Incomplete | 7 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Herald | 16449 | Uncommon | Spirit | 2 | 1 | Unassessed | +0 | Incomplete | 7 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Hungerer | 16391 | Uncommon | Force | 2 | 1 | Unassessed | +0 | Incomplete | 8 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Incubus | 16446 | Uncommon | Force | 2 | 1 | Unassessed | +0 | Incomplete | 10 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Incubus | 16481 | Uncommon | Force | 2 | 1 | Unassessed | +0 | Incomplete | 10 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Incubus | 16484 | Uncommon | Force | 2 | 1 | Unassessed | +0 | Incomplete | 10 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Incubus | 16485 | Uncommon | Force | 2 | 1 | Unassessed | +0 | Incomplete | 10 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Jaeger | 15530 | Uncommon | Spirit | 2 | 1 | Unassessed | +0 | Incomplete | 10 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Jaeger | 15667 | Uncommon | Spirit | 2 | 1 | Unassessed | +0 | Incomplete | 10 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Lemure | 16465 | Uncommon | Magic | 2 | 1 | Unassessed | +0 | Incomplete | 7 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Line Infantry | 16406 | Uncommon | Force | 2 | 1 | Unassessed | +0 | Incomplete | 13 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Militia | 15651 | Uncommon | Spirit | 2 | 1 | Unassessed | +0 | Incomplete | 8 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Militia | 15832 | Uncommon | Spirit | 2 | 1 | Unassessed | +0 | Incomplete | 8 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Militia | 16177 | Uncommon | Spirit | 2 | 1 | Unassessed | +0 | Incomplete | 8 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Militia | 16322 | Uncommon | Spirit | 2 | 1 | Unassessed | +0 | Incomplete | 8 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Militia | 16409 | Uncommon | Spirit | 2 | 1 | Unassessed | +0 | Incomplete | 8 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Outlander | 15345 | Uncommon | Spirit | 2 | 1 | Unassessed | +0 | Incomplete | 11 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Outlander | 15428 | Uncommon | Spirit | 2 | 1 | Unassessed | +0 | Incomplete | 11 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Outlander | 15982 | Uncommon | Spirit | 2 | 1 | Unassessed | +0 | Incomplete | 11 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Outlander | 16045 | Uncommon | Spirit | 2 | 1 | Unassessed | +0 | Incomplete | 11 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Outrider | 15646 | Uncommon | Spirit | 2 | 1 | Unassessed | +0 | Incomplete | 9 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Outrider | 16030 | Uncommon | Spirit | 2 | 1 | Unassessed | +0 | Incomplete | 9 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Outrider | 16180 | Uncommon | Spirit | 2 | 1 | Unassessed | +0 | Incomplete | 9 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Outrider | 16255 | Uncommon | Spirit | 2 | 1 | Unassessed | +0 | Incomplete | 9 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Sandbow | 15508 | Uncommon | Spirit | 2 | 1 | Unassessed | +0 | Incomplete | 12 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Sandbow | 16174 | Uncommon | Spirit | 2 | 1 | Unassessed | +0 | Incomplete | 12 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Satyr | 15528 | Uncommon | Spirit | 2 | 1 | Unassessed | +0 | Incomplete | 11 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Satyr | 15649 | Uncommon | Spirit | 2 | 1 | Unassessed | +0 | Incomplete | 11 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Satyr | 15935 | Uncommon | Spirit | 2 | 1 | Unassessed | +0 | Incomplete | 11 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Saurus | 15467 | Uncommon | Spirit | 2 | 1 | Unassessed | +0 | Incomplete | 7 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Saurus | 16075 | Uncommon | Spirit | 2 | 1 | Unassessed | +0 | Incomplete | 7 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Saurus | 16182 | Uncommon | Spirit | 2 | 1 | Unassessed | +0 | Incomplete | 7 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Shieldguard | 15355 | Uncommon | Spirit | 2 | 1 | Unassessed | +0 | Incomplete | 11 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Shieldguard | 15440 | Uncommon | Spirit | 2 | 1 | Unassessed | +0 | Incomplete | 11 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Shieldguard | 15624 | Uncommon | Spirit | 2 | 1 | Unassessed | +0 | Incomplete | 11 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Shieldguard | 15707 | Uncommon | Spirit | 2 | 1 | Unassessed | +0 | Incomplete | 11 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Shieldguard | 15833 | Uncommon | Spirit | 2 | 1 | Unassessed | +0 | Incomplete | 11 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Shieldguard | 16277 | Uncommon | Spirit | 2 | 1 | Unassessed | +0 | Incomplete | 11 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Skullsquire | 16421 | Uncommon | Force | 2 | 1 | Unassessed | +0 | Incomplete | 10 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Slicer | 16226 | Uncommon | Spirit | 2 | 1 | Unassessed | +0 | Incomplete | 11 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Stalker | 16385 | Uncommon | Magic | 2 | 1 | Unassessed | +0 | Incomplete | 9 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Stalker | 16426 | Uncommon | Magic | 2 | 1 | Unassessed | +0 | Incomplete | 9 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Stalker | 16450 | Uncommon | Magic | 2 | 1 | Unassessed | +0 | Incomplete | 9 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Suntribe | 16480 | Uncommon | Magic | 2 | 1 | Unassessed | +0 | Incomplete | 8 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Thrasher | 15688 | Uncommon | Spirit | 2 | 1 | Unassessed | +0 | Incomplete | 8 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Thrasher | 16316 | Uncommon | Spirit | 2 | 1 | Unassessed | +0 | Incomplete | 8 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Tunnel Steward | 15435 | Uncommon | Spirit | 2 | 1 | Unassessed | +0 | Incomplete | 13 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Tunnel Steward | 15872 | Uncommon | Spirit | 2 | 1 | Unassessed | +0 | Incomplete | 13 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Tunnel Steward | 16273 | Uncommon | Spirit | 2 | 1 | Unassessed | +0 | Incomplete | 13 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Tunnel Steward | 16356 | Uncommon | Spirit | 2 | 1 | Unassessed | +0 | Incomplete | 13 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Vigilante | 15524 | Uncommon | Spirit | 2 | 1 | Unassessed | +0 | Incomplete | 10 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Vigilante | 15927 | Uncommon | Spirit | 2 | 1 | Unassessed | +0 | Incomplete | 10 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Vigilante | 16085 | Uncommon | Spirit | 2 | 1 | Unassessed | +0 | Incomplete | 10 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |

## Common Champions

| Champion | ID | Rarity | Affinity | Rank | Level | Hydra role | Empowerment | Books | Books missing | Masteries | Used scrolls | Unused scrolls |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Bandit | 16338 | Common | Spirit | 2 | 1 | Unassessed | +0 | Incomplete | 6 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Bandit | 16342 | Common | Spirit | 2 | 1 | Unassessed | +0 | Incomplete | 6 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Hellhound | 16336 | Common | Spirit | 2 | 1 | Unassessed | +0 | Incomplete | 5 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Troglodyte | 16344 | Common | Spirit | 2 | 1 | Unassessed | +0 | Incomplete | 4 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Death Hound | 16457 | Common | Magic | 1 | 1 | Unassessed | +0 | Incomplete | 8 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Deathknight | 16467 | Common | Magic | 1 | 1 | Unassessed | +0 | Incomplete | 7 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Deathknight | 16470 | Common | Magic | 1 | 1 | Unassessed | +0 | Incomplete | 7 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Hellhound | 16448 | Common | Spirit | 1 | 1 | Unassessed | +0 | Incomplete | 5 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Hellhound | 16466 | Common | Spirit | 1 | 1 | Unassessed | +0 | Incomplete | 5 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Knecht | 16460 | Common | Spirit | 1 | 1 | Unassessed | +0 | Incomplete | 4 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Lurker | 16456 | Common | Magic | 1 | 1 | Unassessed | +0 | Incomplete | 6 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Lurker | 16474 | Common | Magic | 1 | 1 | Unassessed | +0 | Incomplete | 6 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Novitiate | 16452 | Common | Spirit | 1 | 1 | Unassessed | +0 | Incomplete | 6 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Novitiate | 16455 | Common | Spirit | 1 | 1 | Unassessed | +0 | Incomplete | 6 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Pikeman | 16459 | Common | Magic | 1 | 1 | Unassessed | +0 | Incomplete | 7 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Pikeman | 16471 | Common | Magic | 1 | 1 | Unassessed | +0 | Incomplete | 7 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Swordsman | 16454 | Common | Magic | 1 | 1 | Unassessed | +0 | Incomplete | 4 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Swordsman | 16469 | Common | Magic | 1 | 1 | Unassessed | +0 | Incomplete | 4 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Troglodyte | 16461 | Common | Spirit | 1 | 1 | Unassessed | +0 | Incomplete | 4 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Troglodyte | 16463 | Common | Spirit | 1 | 1 | Unassessed | +0 | Incomplete | 4 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
| Warboy | 16462 | Common | Magic | 1 | 1 | Unassessed | +0 | Incomplete | 4 | No scrolls reported | 0 / 0 / 0 | 0 / 0 / 0 |
