# Hydra Teams and Investment Plan

Based on [your September 11 roster](https://github.com/kennymcginnis/rsl-teams/blob/HEAD/champs%2020260911.csv)
and [the guide transcript](https://github.com/kennymcginnis/rsl-teams/blob/HEAD/hydra-guide.md). Champion kits
were checked against the references at the end. These are proposed builds, not simulated or tested damage results.

## Recommendation and Assumptions

Build Team 1 first, then Team 2, then Team 3. This is an expected-strength and investment order with appropriate Hydra
loadouts, not a ranking based on the equipment worn in the export. Your difficulty, current rotation, available gear,
Hydra area bonuses, relics, and individual booked skill levels are unknown, so the ranking needs playtesting.

**Free gear swaps are assumed.** Save loadouts and reuse your best gear across successive keys. The three teams need 18
distinct champion copies, not 18 permanently equipped champions. All six champions within a run still need their gear
simultaneously. A saved loadout does not duplicate an item; equipping it can remove gear from another champion.
Accessory faction restrictions and different base stats also mean the same pieces will not fit or perform identically on
every champion. Restore other-content loadouts afterward, especially for speed-tuned Demon Lord teams.

Do not try to squeeze every desirable effect into all three teams at the expense of healing or damage. Prioritize Block
Buffs, control of Decay, survival, and enough damage to rescue swallowed champions. Increase SPD, Decrease SPD, and Hex
are excellent, but a nominal role is not the same as reliable uptime.

### Permanent Investment Priorities

| Champion           | Exported development                           | Recommendation                                                                                              |
| ------------------ | ---------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| Khamir Scald-eye   | Rank 6, level 58; 8 books missing              | Finish level 60. Prioritize A2 speed-buff cooldown, then A3 revive cooldown.                                |
| Rector Drath       | Rank 5, level 50; 0 books missing; 3-star soul | First new six-star recommendation: healing, conditional Perfect Veil, and revive.                           |
| Gharol Bloodmaul   | Rank 6, level 60; 10 books missing             | Commit to alternate-form damage; inspect the relevant form's skill upgrades before spending Mythical books. |
| Wythir the Crowned | Rank 6, level 41; 8 books missing              | Finish leveling, then book support cooldowns when developing Team 3. No new rank-up needed.                 |
| Mordecai, ID 3936  | Rank 5, level 50; 0 books missing              | Use this booked copy. Trial at 50; promote for Team 3 durability and full mastery/accessory access.         |
| High Khatun, ID 13 | Rank 5, level 50; 11 books missing             | A2 cooldown first. Trial at 50; six-star later if this slot proves useful.                                  |

Visix, Artak, Uugo, Lyssandra, Wukong, Husk, Royal Guard, Doompriest, Gnarlhorn, and Akemtum are already level 60 and
show zero books missing. Their current equipped SPD/ACC are **not investment problems**; use the loadout targets below.

`BooksMissing` is the export's total remaining upgrades, not a count of books needed for a particular skill. Books land
randomly; inspect the relevant skill before spending. The export also shows many champions with zero used mastery
scrolls and large unused balances. Verify their actual mastery trees: having scrolls available does not mean masteries
are selected.

## Team 1: Primary Investment Team

**Khamir Scald-eye (lead), Visix the Unbowed, Uugo, Rector Drath, Gharol Bloodmaul, Artak.**

| Champion          | Roster ID | Assigned roles                                                                                                                          |
| ----------------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| Khamir Scald-eye  | 14551     | 20% all-battles SPD aura; Increase SPD and Increase ATK; ally turn-meter boost; full-team revive, defensive buffs, and A1 team healing. |
| Visix the Unbowed | 96        | Primary Provoke, AoE Decrease SPD, Ally Protection. Her one-turn Provoke on a booked three-turn cooldown is not a permanent lock.       |
| Uugo              | 8808      | AoE Block Buffs and Decrease DEF; healing and Leech support. Her conditional revive is not the team's normal recovery plan.             |
| Rector Drath      | 12124     | Main healer, single-target revive, conditional Perfect Veil; incidental A1 Decrease ATK.                                                |
| Gharol Bloodmaul  | 239       | Main direct-damage dealer in alternate form. Do not count her base-form Provoke, cleanse, or healing as ongoing coverage in this build. |
| Artak             | 37        | AoE HP Burn, burn activation, AoE Decrease ATK; preferred Cursed-set Hex carrier if the gear meets his core stats.                      |

This puts Void control, Block Buffs/Decrease DEF, speed/healing support, and a Perfect Veil healer around Gharol. Khamir
also supplies Increase ATK for Gharol. Artak adds burn damage and Decrease ATK. Khamir's booked A2 has a three-turn
cooldown; until it is booked, Lyssandra is an already-booked substitute, but she then cannot join Team 2.

**Main gaps:** no native Hex, no planned dedicated Mischief tank, and no guaranteed full Provoke or Perfect Veil uptime.
Cursed gear can supply probabilistic Hex, but is not a prerequisite to begin testing. Rector only places her team
Perfect Veil on allies who are at full HP after her heal.

### Team 1 Loadout Targets

These are **Hard-oriented starting goals**, not a validated speed tune. Adjust ACC using the difficulty table below.
SPD, HP, DEF, and damage stats are champion-sheet targets before the leader aura and temporary battle buffs. Do not
multiply the entire displayed SPD by the aura percentage: speed auras use base SPD.

| Champion          | Target SPD | Target ACC                     | Target HP / DEF | Crit and damage targets                                      | RES priority                             |
| ----------------- | ---------- | ------------------------------ | --------------- | ------------------------------------------------------------ | ---------------------------------------- |
| Khamir Scald-eye  | 260-280    | None needed                    | 65-80k / 3k+    | No crit requirement; HP improves healing                     | Secondary to speed and bulk              |
| Visix the Unbowed | 250-270    | 250-300                        | 55-65k / 3.5k+  | No crit requirement; survive Ally Protection damage          | Secondary                                |
| Uugo              | 245-265    | 250-300                        | 60-75k / 3k+    | No crit requirement; HP improves healing                     | Secondary                                |
| Rector Drath      | 240-260    | Optional                       | 65-80k / 3k+    | No crit requirement; Artak covers Decrease ATK               | Secondary; do not force a tank threshold |
| Gharol Bloodmaul  | 220-240    | None for alternate-form damage | 40-50k / 2.5k+  | 100% CR, 200%+ CD, 4.5k+ ATK; stretch 250%+ CD and 5.5k+ ATK | Last                                     |
| Artak             | 240-260    | 250-300                        | 65-80k / 3k+    | No CR/CD/ATK requirement for burns                           | Secondary                                |

Gharol's targets refer to **alternate-form totals**. Verify that form in game or in the optimizer. Do not try to make
this same loadout both a high-ACC base-form controller and a premium damage dealer.

For Artak, use **Cursed** if available while meeting the core targets; otherwise use your best fast, durable gear. It
supplies chance-based Hex, not guaranteed uptime. No Cursed gear is assumed to exist in the export.

### Team 1 Operation

- Khamir: prioritize A2 for Increase SPD/ATK. Use A1 for healing and save the revive when recovery is needed.
- Visix: maintain A2 Decrease SPD; time A3 to intercept Decay's cleanse. One turn of Provoke on a three-turn cooldown is
  not a permanent lock at these speeds. Start with manual targeting rather than trusting auto.
- Uugo: prioritize A2, watching Blight/Mischief after respawns. Use A3 to heal/cleanse. Even booked, her Block Buffs
  chance depends on the number of living enemies; do not describe it as unconditional 100% application.
- Rector: heal before important Torment attacks. Perfect Veil requires allies to reach full HP after her heal.
- Gharol: enter alternate form and stay there for damage. Frequent follow-up attacks make Torment protection valuable
  and accelerate Wrath's revenge counter. Watch Wrath before committing burst attacks.
- Artak: open A3 to place burns, then A2 to activate them and place Decrease ATK.

**Before Rector is ready:** Scyl can temporarily replace her, but leaves Team 2 and provides less Torment protection.
**If Provoke gaps end runs:** test Husk instead of Artak. This adds backup Provoke but loses burns and reliable AoE
Decrease ATK, and removes Husk from Team 2. Gear is reusable; champions used in saved runs are not.

## Team 2: Next-Strongest Candidate

**Lyssandra (lead), Sun Wukong, Husk, Royal Guard, Scyl of the Drakes, Doompriest.**

| Champion           | Roster ID | Assigned roles                                                                                |
| ------------------ | --------- | --------------------------------------------------------------------------------------------- |
| Lyssandra          | 70        | 24% all-battles SPD aura, Increase SPD, ally turn-meter boost.                                |
| Sun Wukong         | 54        | AoE buff steal and Block Buffs, direct damage, self-revive only.                              |
| Husk               | 30        | Enemy-MAX-HP AoE damage and chance-based A1 Provoke.                                          |
| Royal Guard        | 5160      | Enemy-MAX-HP AoE damage, random-target Decrease SPD, chance-based single-target Decrease DEF. |
| Scyl of the Drakes | 65        | Passive team healing, single-target revive, chance-based A1 Decrease SPD.                     |
| Doompriest         | 12178     | Passive team healing and one random debuff removed per ally per turn; Increase ATK.           |

All six are level 60, and only Scyl has books missing. Borrow appropriate gear from Team 1 after that run. This team
offers more direct rescue damage than Team 3, but is less secure than Team 1 against Decay and Wrath. Enemy-MAX-HP
damage becomes more attractive on higher difficulties; on Normal, the burn team below may outperform it. **Team 2 versus
Team 3 is a provisional ranking, not a guaranteed damage order.**

**Main gaps:** unreliable solo Provoke, no native Hex, no Perfect Veil, no reliable Decrease ATK, and patchy Decrease
DEF/Decrease SPD. Doompriest removes Fear after it lands, and her random cleanse may remove another debuff instead. This
is a manual/semi-auto starting team, not a proven Quick Battle team.

### Team 2 Loadout Targets

Use these for Hard-oriented builds; lower ACC to the Normal range when appropriate. Do not lower targets just because
the same gear was assigned to Team 1 earlier in the week.

| Champion           | Target SPD | Target ACC  | Target HP / DEF | Crit and damage targets                            | RES priority |
| ------------------ | ---------- | ----------- | --------------- | -------------------------------------------------- | ------------ |
| Lyssandra          | 270-290    | Optional    | 60-75k / 3k+    | No crit requirement                                | Secondary    |
| Sun Wukong         | 235-255    | 250-300     | 40-50k / 2.5k+  | 100% CR, 180-220%+ CD, 4k+ ATK after speed/ACC     | Last         |
| Husk               | 235-255    | 250-300     | 55-70k / 2.8k+  | 100% CR, 180-220%+ CD; do not stack ATK for his A2 | Secondary    |
| Royal Guard        | 215-235    | 250-300     | 40-50k / 2.5k+  | 100% CR, 200-240%+ CD; survival before extra ATK   | Last         |
| Scyl of the Drakes | 245-265    | 250-300     | 55-65k / 3.5k+  | No crit requirement                                | Secondary    |
| Doompriest         | 255-280    | None needed | 55-70k / 3k+    | No crit requirement                                | Secondary    |

Lyssandra needs no ACC for team speed/turn-meter boosts. Her enemy turn-meter reductions cannot work on Hydra; ACC is
only for other applicable effects, such as transferred debuffs or an accuracy-dependent blessing.

### Team 2 Operation and Alternatives

- Lyssandra: prioritize A3; disable A2 for Hydra utility since its turn-meter depletion cannot work on the heads.
- Wukong: prioritize A3 over damage. His self-revive does not replace Scyl's team recovery role.
- Husk: disable A3. Manually A1 Decay when Provoke is needed, using A2 when control is secure. This sacrifices damage
  turns, and failed chance rolls, weak hits, and resists still happen.
- Royal Guard: retain A3 for Decrease SPD; random hits can miss Decay. Use A1 to attempt Decrease DEF on the important
  damage target and A2 for rescue damage or exposed necks.
- Scyl: choose **Cursed for Hex** or **Provoke gear for backup control**, according to the observed failure. Her Stun
  cannot control Hydra. Use A1 more for slow attempts, or keep AoE A2 useful for set applications.
- Doompriest: fast turns provide more healing/cleanses. Boosts, deaths, and respawns prevent these ranges from
  guaranteeing a cleanse immediately before every ally acts.

**Control-first alternative:** Gnarlhorn (ID 5) replaces Royal Guard, giving Husk a second Provoker. Team 3 then loses
Gnarlhorn. Establish two successful keys before spending heavily just to preserve a third lineup.

**Wrath-survival alternative:** your booked Ursala (ID 78) replaces Royal Guard for Decrease ATK and defensive support.
Target 230-250 SPD, 250-300 ACC, 55k+ HP, and 3k+ DEF. No crit requirement; RES secondary.

**Damage-debuff alternative:** Dorothy Gale (ID 14762) replaces Royal Guard for non-hit AoE Decrease DEF/Decrease ACC
and A1 Weaken. Target 240-260 SPD, 250-300 ACC, 55k+ HP, and 3k+ DEF; prioritize A2 books. She costs new legendary books
and loses Royal Guard's nuke/slow, but is worth testing if debuff coverage is the limiting factor. She does not provide
team Increase SPD, healing, Provoke, or a revive.

## Team 3: Third-Key Burn Team

**Hierophant Lazarius (lead), Gnarlhorn, Akemtum, Mordecai, Wythir the Crowned, High Khatun.**

| Champion            | Roster ID | Assigned roles                                                                                                                                              |
| ------------------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Hierophant Lazarius | 232       | Base form: 25% all-battles SPD aura, AoE Block Buffs/buff-duration reduction, Block Debuffs, Strengthen, ally turn-meter boost, passive single-ally revive. |
| Gnarlhorn           | 5         | Non-hit Provoke; self Increase DEF and Unkillable.                                                                                                          |
| Akemtum             | 179       | Native AoE Hex and debuff spreading. Hydra heads are immune to Poison; do not count on his poison damage engine here.                                       |
| Mordecai            | 3936      | Non-hit AoE HP Burn as the primary damage engine; ally turn-meter boost. Use the booked rank-5 copy.                                                        |
| Wythir the Crowned  | 13353     | Main healer, full-team cleanse, Increase DEF, Continuous Heals, incidental AoE Leech. No revive.                                                            |
| High Khatun         | 13        | Team Increase SPD and turn-meter boost; chance-based single-target A1 Decrease SPD. Use the rank-5 copy.                                                    |

Lazarius is not your third-best champion: his multiple support roles make a third team possible without taking away Team
1's control/healing package. Gear him as well as needed for this run; his team number does not assign him inferior gear.
This composition is **Normal-oriented initially**, with less direct burst than Team 2.

**Main gaps:** no Decrease DEF or reliable Decrease ATK, no team Perfect Veil, one-turn/three-turn Provoke, and limited
rescue burst. A good burn score does not guarantee you can free a swallowed champion before digestion. Wythir has
cooldown-limited cleansing, and losing Akemtum temporarily can make Mischief targeting difficult.

### Team 3 Loadout Targets

These are Normal starting goals, not ceilings. Reuse stronger loadouts when available; use Hard ACC targets if moving
this team up. No need to strip good ACC merely because it exceeds the suggested range.

| Champion            | Target SPD | Target ACC                 | Target HP / DEF | Crit and damage targets                  | RES priority                                            |
| ------------------- | ---------- | -------------------------- | --------------- | ---------------------------------------- | ------------------------------------------------------- |
| Hierophant Lazarius | 245-265    | 220-250 initially          | 60-75k / 3k+    | Base-form support; no crit requirement   | Optional 350+ for a tested Normal Mischief-target build |
| Gnarlhorn           | 240-260    | 220-250                    | 50-65k / 3k+    | No CR/CD: his A1 cannot crit             | Secondary                                               |
| Akemtum             | 225-245    | 220-250                    | 45-55k / 2.8k+  | Hex/support first; no crit requirement   | Secondary                                               |
| Mordecai            | 225-245    | 220-250                    | 50-60k / 2.8k+  | No CR/CD/ATK requirement for burns       | Secondary                                               |
| Wythir the Crowned  | 240-260    | Optional 220-250 for Leech | 70-85k / 3k+    | No crit requirement; HP improves healing | Secondary                                               |
| High Khatun         | 245-265    | 220-250 for A1 slow        | 45-55k / 2.8k+  | No crit requirement                      | Secondary                                               |

### Team 3 Operation

- Lazarius: stay in base form. Prioritize A2 Block Buffs; use A3 for Strengthen/ally turn meter. His self Increase ACC
  does not help Gnarlhorn or Akemtum. His revive is random and cooldown-limited, not guaranteed immediate recovery.
- Gnarlhorn: time A2 for Decay's cleanse. Non-hit placement avoids weak-hit failure but still requires ACC. Keep Block
  Buffs active so Mischief cannot gain and spread his Unkillable buff.
- Akemtum: prioritize A2 Hex. A1 a Hexed head with useful debuffs to spread; the spread is random, not guaranteed Block
  Buffs/slow coverage. Provoke is a control debuff and cannot be extended like ordinary damage debuffs.
- Mordecai: prioritize A3 burns. Non-hit placement can recover from Poison Cloud if burns are not resisted or blocked.
  His ally turn-meter fill works, while enemy turn-meter reduction does not.
- Wythir: cleanse before Fear disrupts critical turns. Her AoE A1 also attacks Torment and can expose her to Fear.
- High Khatun: prioritize A2, disable A3 for more A1 slow attempts, and target Decay when useful. The booked A1 slow
  chance is only 40%, before accuracy/affinity checks.

**If rescues fail:** trial your booked Rathalos Blademaster (ID 84) instead of Akemtum. Mordecai's burns support his
direct damage, but removing native Hex makes Mischief harder to target. Cursed Wythir can partly compensate. Target
210-230 SPD, 100% CR, 200%+ CD, 4k+ ATK, 40k+ HP, and 2.5k+ DEF; do not chase ACC for his boss Decrease DEF. This is a
tradeoff to test, not an automatic upgrade.

## Role Coverage

Default teams only; substitutions change these assignments. "Partial" means chance, targeting, cooldown, or health
restrictions matter. **None has a proven permanent Decay lock at the listed speeds.**

| Role             | Team 1                                                | Team 2                      | Team 3                                              |
| ---------------- | ----------------------------------------------------- | --------------------------- | --------------------------------------------------- |
| Provoke          | Visix; uptime gap                                     | Husk; chance-based          | Gnarlhorn; uptime gap                               |
| Block Buffs      | Uugo                                                  | Wukong                      | Lazarius base form                                  |
| Increase SPD     | Khamir                                                | Lyssandra                   | High Khatun                                         |
| Decrease SPD     | Visix AoE                                             | Royal Guard + Scyl; partial | High Khatun A1; partial                             |
| Revive           | Khamir + Rector                                       | Scyl; Wukong self-only      | Lazarius passive                                    |
| Healing          | Khamir + Rector + Uugo                                | Scyl + Doompriest           | Wythir                                              |
| Torment response | Rector conditional Perfect Veil; Uugo partial cleanse | Doompriest partial cleanse  | Wythir cooldown cleanse; Lazarius self Perfect Veil |
| Hex              | Optional Cursed Artak                                 | Optional Cursed Scyl        | Akemtum native                                      |
| Decrease ATK     | Artak; Rector incidental                              | Missing                     | Missing                                             |
| Decrease DEF     | Uugo AoE                                              | Royal Guard A1; partial     | Missing                                             |
| Weaken           | Missing                                               | Missing                     | Missing                                             |
| Main damage      | Gharol + Artak                                        | Husk + Royal Guard + Wukong | Mordecai burns                                      |

Hex helps target Mischief and shares direct damage; it is valuable but does not replace healing or Block Buffs. Do not
expect ordinary Hex damage sharing to multiply HP Burn ticks as if they were direct hits.

## Difficulty and Stat Rules

These are **conservative planning ranges**, not exact resistance-probability calculations or thresholds verified against
the current rotation. Check actual head stats before optimizing an exact loadout. No single SPD number guarantees
Provoke uptime: skill cooldowns, ally boosts, Decrease SPD, Fear, and respawns all affect it.

| Difficulty | Debuffer ACC target | Dedicated Mischief-target RES target | General SPD direction                     |
| ---------- | ------------------- | ------------------------------------ | ----------------------------------------- |
| Normal     | 220-250             | 350+                                 | 200-230 damage; 230-260 control/support   |
| Hard       | 250-300             | 400+                                 | 220-240 damage; 245-280 control/support   |
| Brutal     | 330-370             | 450+                                 | 230-260 damage; 260-290+ control/support  |
| Nightmare  | 400-450             | 550+                                 | 250-280+ damage; 280-320+ control/support |

- These are goals, not entry requirements. Use lower stats if they work; push higher when the observed failure requires
  it. Free swapping removes the silver penalty, not the need for sufficient gear quality.
- Compare effective in-battle ACC/RES, including known area bonuses and active buffs. Do not double-count bonuses
  already included in the export. Conditional buffs can disappear at critical moments.
- ACC cannot fix a weak hit, failed skill proc, immunity, cooldown gap, or full debuff bar.
- Most champions do **not** need the Mischief RES number. For ordinary support builds, meet speed, required ACC, and
  HP/DEF first. "Secondary RES" means no mandatory numeric target, not an instruction to reach 400 everywhere.
- A real Mischief tank needs enough RES **and the most buffs when Mischief acts**. Lazarius is a candidate due to self
  buffs, not a guaranteed tank. Gnarlhorn, Wythir's heals, and changing buff durations can change targeting. Validate
  several buff-steal attempts before counting on him.
- Block Buffs prevents Mischief from gaining stolen buffs; it does not necessarily preserve them on your ally or stop
  turn-meter theft. A correctly built RES tank provides different protection.
- Torment's special True Fear is not solved by ordinary Block Debuffs or RES. Perfect Veil prevents that trigger;
  cleanse handles it afterward. Lazarius's team Block Debuffs is not team Torment immunity.
- For harder content, work toward 45-55k HP / 3k DEF on damage dealers and 65-80k HP / 3.5k DEF on supports, where
  feasible. These are starting goals, not guarantees against every head's damage mechanics.

**Difficulty allocation:** secure a reliable Normal chest if you have not already done so. Then trial Team 1 on Hard,
Team 2 on the next difficulty where it earns your intended reward, and Team 3 on Normal. Multiple keys can go into the
same difficulty. Do not force Nightmare/Brutal/Hard just because the transcript lists them as an end goal.

## Books and Development Order

### First: Team 1

1. Verify/select masteries on the chosen champions before buying anything. Large unused-scroll balances may represent
   already-earned resources; the export does not prove a completed mastery tree.
2. Finish **Khamir to level 60**, then prioritize A2 books and A3 books. A2 falls from five turns to three; A3 falls
   from six to four. A1 books improve damage, not its stated healing percentage.
3. **Six-star Rector Drath** and finish ascension/masteries. She is already fully booked and has a 3-star soul.
4. Fund **Gharol's alternate-form skill upgrades** if committing to her damage role. Inspect the form tabs; the CSV does
   not identify which particular upgrades are missing. Trial your best damage gear before spending.

### Book Budgets

Separate rarity budgets. Do not spend higher-rarity books on lower-rarity champions.

| Priority within budget   | Champion              | Books missing in export | Target                                                                                      |
| ------------------------ | --------------------- | ----------------------- | ------------------------------------------------------------------------------------------- |
| Legendary 1              | Khamir Scald-eye      | 8                       | A2 cooldown, then A3 cooldown                                                               |
| Legendary 2, conditional | Scyl of the Drakes    | 2                       | Finish if the missing ranks improve A1 slow or A3 revive; Hydra does not need Stun upgrades |
| Legendary 3, Team 3      | Wythir the Crowned    | 8                       | A3 cleanse/heal to three turns, then A2 to three turns                                      |
| Legendary alternative    | Dorothy Gale          | 10                      | A2 chance/cooldown if adopting the Team 2 substitution                                      |
| Mythical 1 for this plan | Gharol Bloodmaul      | 10                      | Alternate-form damage upgrades; not base-form Provoke merely to fill a checklist            |
| Mythical 2 for this plan | Hierophant Lazarius   | 6                       | Base-form A2 cooldown first, then A3 cooldown                                               |
| Epic, later              | High Khatun, ID 13    | 11                      | A2 cooldown first, then A1 slow chance                                                      |
| Epic, future expansion   | Second Uugo, ID 12436 | 16                      | Keep this copy; build A2/A3 only after the primary teams work                               |

Books land randomly: these are desired skill outcomes, not claims you can choose where each book lands. If Lazarius's A2
is already booked, his remaining total alone is not a reason to postpone using him.

**No additional books needed:** selected Visix, Uugo, Rector, Artak, Lyssandra, Wukong, Husk, Royal Guard, Doompriest,
Gnarlhorn, Akemtum, and Mordecai all show `BooksMissing = 0`.

### Next: Team 2, Then Team 3

1. Team 2 needs no new six-stars. Test borrowed loadouts and confirm masteries; decide on Scyl's last books based on
   which skills are actually unfinished. Do not delay testing because of the export's equipment snapshot.
2. Finish **Wythir from level 41 to 60**. She is already rank 6, so this needs no new rank-up sacrifices.
3. Verify **Gnarlhorn and Akemtum's masteries/ascension**; both are already level 60 and booked.
4. Promote **Mordecai, ID 3936**, once a trial demonstrates this burn team is worth developing.
5. Promote **High Khatun, ID 13**, last if the additional durability/accessory access is needed. Her speed buff works at
   level 50; do not promote her simply to make every portrait level 60.

### Not First for Hydra

- **Talenna / Xenomorph:** poison-focused kits do not translate well to poison-immune Hydra heads. They can be strong
  elsewhere, but they are not the first missing Hydra support role to fund.
- **Haggibah:** burn activation and Leech are interesting, but her bomb-focused kit does not replace reliable Block
  Buffs, Provoke, or a main healer.
- **The Cowardly Lion:** personal Fear handling, defensive buffs, and damage are useful; they are not teamwide Fear
  immunity, Provoke, Block Buffs, or revive. A later damage experiment, not the first support investment.
- **Folan Silverhart:** a credible later damage/Decrease DEF project, especially with your 5-star soul. Needs level 60
  and books; finish the first team's role coverage before committing resources.
- **Loki:** useful manual debuff extension and conditional Block Buffs spread. Veil requirements, random spread, and
  ally/enemy A2 targeting make him less straightforward than the default providers. He cannot extend Provoke.
- **Kymar / Arbiter:** fallback reset/recovery tools, not automatic Hydra upgrades. Their Arena speed auras do not apply
  here. Free gear transfers do not change their missing Provoke/Hex roles.
- **Ezio / Michelangelo / other unbooked damage dealers:** not required to launch this plan. This is not an exhaustive
  claim that all excluded champions are worse. Michelangelo's full kit could not be independently retrieved during this
  review, so no book recommendation depends on an assumed skill set.

## Loadouts, Masteries, and Blessings

- **Optimize six at a time.** Save Team 1's loadouts, run it, then transfer available pieces to Team 2 and Team 3. Check
  final totals on each recipient. Do not allocate weaker gear merely because a champion belongs to a later key.
- **Stats before sets.** Speed, Perception, and strong mixed pieces are fine. SPD boots and HP%/DEF% main stats are
  typical for supports; core debuffers commonly need ACC banners. Faction-locked accessories limit sharing.
- **Cursed:** optional on Artak/Scyl, reusable between runs where slots permit. Check actual Hex uptime after respawns.
  Native debuffs still need ACC even if the artifact effect follows separate application rules.
- **Provoke gear:** backup control, not a guaranteed lock. Scyl is a candidate, but it competes with her Cursed build.
  Stun/Freeze sets do not solve Hydra control because the heads are immune.
- **Reflex/Relentless:** useful for cycling/healing when targets remain met, not a guaranteed timing solution. Extra
  turns consume buff duration too; watch Perfect Veil rather than assuming more turns always stay protected.
- **Masteries:** Warmaster is a common PvE option for frequent hitters; Helmsmasher is a direct-damage option for
  Gharol; Akemtum's triple-hit skills suit Giant Slayer. Support/Defense trees can be more useful on survival
  specialists. Mastery resets are separate from free gear swaps; do not assume those are free too.
- **Blessings:** do not infer names from numeric blessing IDs alone. Inspect them in game. One useful Cruelty carrier
  per team is a reasonable starting point; Husk's 4-star soul is worth considering for Team 2. Existing low-star souls
  do not provide six-star-only benefits. Souls are not the first investment ahead of core development.
- **Brimstone:** consider one eligible awakened legendary/mythical per team where useful. Low awakening has application
  restrictions and requires ACC. A champion listed with no/optional ACC needs an appropriate ACC loadout if assigned an
  accuracy-dependent blessing. Do not assume gear swaps also make blessing changes free.

## Test Before Saving Keys

1. Start on your established difficulty. Save a result only after you finish experimenting with those champion copies
   for the week; subsequent teams can reuse equipment, not those locked champions.
2. Watch the first Decay cleanses: was Provoke resisted, on cooldown, prevented by Fear, or simply mistimed? Only the
   first is primarily an ACC problem.
3. Verify Block Buffs on Blight/Mischief at the moment they act, especially after respawns.
4. Track what ends the run: deaths, Fear, missed control, missing Hex, or inadequate rescue damage. Use the
   substitutions to address that failure rather than ranking champions solely by personal damage totals.
5. Rescue swallowed champions promptly. A consumed champion cannot simply be returned with a normal revive.
6. Record difficulty, rotation, damage, approximate turns, and failure reason. Compare repeated runs on the same
   difficulty. None of these lineups has been validated for unattended Quick Battle.

The transcript is a useful checklist, but contains transcription errors and some patch-sensitive mechanics. Do not
interpret "reducing incoming damage to 100%" as a usable Serpent's Will rule or assume every buff can be stripped.
Follow the current in-game head descriptions for exact mechanics.

## References and Limits

Kit references consulted September 11, 2026. Assignments/stat targets are recommendations derived from the roster and
kits, not source-author prescriptions or simulated results. Detailed skill text takes precedence over overview prose
where they disagree; current in-game behavior is the final check.

- Team 1: [Khamir](https://hellhades.com/raid/champions/khamir-scald-eye/),
  [Visix](https://hellhades.com/raid/champions/visix-the-unbowed/), [Uugo](https://hellhades.com/raid/champions/uugo/),
  [Rector](https://hellhades.com/raid/champions/rector-drath/),
  [Gharol](https://hellhades.com/raid/champions/gharol-bloodmaul/).
- Team 2: [Lyssandra](https://hellhades.com/raid/champions/lyssandra/),
  [Wukong](https://hellhades.com/raid/champions/sun-wukong/), [Husk](https://hellhades.com/raid/champions/husk/),
  [Royal Guard](https://hellhades.com/raid/champions/royal-guard/),
  [Scyl](https://hellhades.com/raid/champions/scyl-of-the-drakes/),
  [Doompriest](https://hellhades.com/raid/champions/doompriest/).
- Team 3: [Lazarius](https://hellhades.com/raid/champions/hierophant-lazarius/),
  [Gnarlhorn](https://hellhades.com/raid/champions/gnarlhorn/),
  [Akemtum](https://hellhades.com/raid/champions/akemtum/), [Mordecai](https://hellhades.com/raid/champions/mordecai/),
  [Wythir](https://hellhades.com/raid/champions/wythir-the-crowned/),
  [High Khatun](https://hellhades.com/raid/champions/high-khatun/).
- Alternatives: [Dorothy](https://hellhades.com/raid/champions/dorothy-gale/),
  [Folan](https://hellhades.com/raid/champions/folan-silverhart/),
  [Loki](https://hellhades.com/raid/champions/loki-the-deceiver/),
  [The Cowardly Lion](https://hellhades.com/raid/champions/the-cowardly-lion/).
- [Hydra overview](https://hellhades.com/hydra-clan-boss-guide/) and
  [Mischief guide](https://hellhades.com/hydra-guide-the-head-of-mischief/): conceptual references with some older
  numeric mechanics, not treated as current patch-specific thresholds.
- [Raid Stages Tool](https://hellhades.com/raid/stages-tool/): check actual head stats before fine-tuning ACC/RES. The
  conservative planning ranges above were not extracted from a live stages-tool result.

**Bottom line:** build around Khamir, Visix, Uugo, Rector, Gharol, and Artak first. Your key permanent investments are
Khamir's cooldowns, Rector's rank-up, and appropriate Gharol upgrades. Save strong Hydra loadouts and share gear between
keys; do not treat today's equipped stats as a reason to exclude a champion.
