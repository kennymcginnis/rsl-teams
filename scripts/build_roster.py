import argparse
import csv
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RARITIES = {1: "Common", 2: "Uncommon", 3: "Rare", 4: "Epic", 5: "Legendary", 6: "Mythical"}
AFFINITIES = {1: "Magic", 2: "Force", 3: "Spirit", 4: "Void"}
MASTERY_LIMITS = (100, 600, 950)
HYDRA_ROLES = {
    "Khamir Scald-eye": "Speed / healing / revive / buffs",
    "Visix the Unbowed": "Provoke / Decrease SPD / Ally Protection",
    "Uugo": "Block Buffs / Decrease DEF / healing",
    "Rector Drath": "Healing / conditional Perfect Veil / revive",
    "Gharol Bloodmaul": "Damage (alternate); protection / Provoke (base)",
    "Artak": "HP Burn / burn activation / Decrease ATK",
    "Lyssandra": "Increase SPD / ally turn-meter boost",
    "Sun Wukong": "Block Buffs / buff steal / damage",
    "Husk": "Enemy-MAX-HP damage / chance-based Provoke",
    "Royal Guard": "Enemy-MAX-HP damage / partial slow and Decrease DEF",
    "Scyl of the Drakes": "Healing / revive / chance-based slow",
    "Doompriest": "Healing / partial cleanse / Increase ATK",
    "Hierophant Lazarius": "Block Buffs / buffs / passive revive (base)",
    "Gnarlhorn": "Provoke",
    "Akemtum": "Hex / debuff spread",
    "Mordecai": "HP Burn / ally turn-meter boost",
    "Wythir the Crowned": "Healing / cleanse / Increase DEF",
    "High Khatun": "Increase SPD / chance-based slow",
    "Ursala the Mourner": "Revive / Decrease ATK / defensive buffs",
    "Dorothy Gale": "Decrease DEF / Decrease ACC / Weaken / buff steal",
    "Rathalos Blademaster": "Direct damage / boss Decrease DEF",
    "Folan Silverhart": "Damage / Decrease DEF / debuff spread",
    "Loki the Deceiver": "Conditional Block Buffs spread / debuff extension",
    "The Cowardly Lion": "DEF damage / defensive buffs / personal Fear response",
    "Haggibah the Nestmaid": "Burn activation / Leech / buff steal",
    "Prince Kymar": "Skill reset / buff removal",
    "Arbiter": "Revive / ally turn-meter boost / Increase ATK",
}


def mastery_status(champion):
    used = tuple(int(champion[f"UsedT{tier}MasScrolls"]) for tier in range(1, 4))
    unused = tuple(int(champion[f"UnUsedT{tier}MasScrolls"]) for tier in range(1, 4))
    if all(spent >= limit for spent, limit in zip(used, MASTERY_LIMITS)):
        return "Full allocation reported"
    if all(spent + available >= limit for spent, available, limit in zip(used, unused, MASTERY_LIMITS)):
        return "Full scroll budget; allocation incomplete"
    if any(used):
        return "Partial allocation"
    if any(unused):
        return "Some scrolls; none allocated"
    return "No scrolls reported"


def cell(value):
    return str(value).replace("|", "\\|").replace("\n", " ")


def build_roster(source):
    with source.open(newline="", encoding="utf-8-sig") as stream:
        champions = list(csv.DictReader(stream))
    identifiers = [champion["ID"] for champion in champions]
    if len(set(identifiers)) != len(identifiers):
        raise ValueError("The export contains duplicate champion IDs")
    counts = Counter(int(champion["Rarity"]) for champion in champions)
    lines = [
        "# Champion Roster",
        "",
        f"Source snapshot: **{source.name}**. {len(champions)} champion copies; "
        f"{len({champion['Name'] for champion in champions})} distinct names.",
        "",
        "Each row is an owned copy, identified by roster ID. Duplicate names are intentional. "
        "Current equipment stats are omitted because gear can be swapped between runs.",
        "",
        "## Reading the Table",
        "",
        "- **Hydra role** is an assessment from the team-planning work, not the official "
        "Attack/Defense/HP/Support champion type. The CSV does not export that type. "
        "Unassessed means no role has been assigned here, not that the champion is unusable.",
        "- **Books** reports Fully booked when `BooksMissing` is zero; otherwise Incomplete. "
        "Books spent and skill-by-skill upgrades are not exported and cannot be inferred from this count. "
        "For Mythicals, inspect both forms in game.",
        "- **Masteries** is inferred only from scroll counters. A full allocation requires "
        "100 basic, 600 advanced, and 950 divine scrolls reported as used. "
        "A full scroll budget includes unused scrolls and does not mean a completed mastery tree. "
        "Verify unusual counters in game; the export does not identify selected masteries or their suitability.",
        "- **Used / Unused scrolls** lists basic / advanced / divine counters for auditing the mastery status.",
        "- **Empowerment** is the exported empowerment level, separate from rank and awakening.",
        "",
        "## Roster Summary",
        "",
        "| Rarity | Copies |",
        "| --- | --- |",
    ]
    for rarity in sorted(counts, reverse=True):
        lines.append(f"| {RARITIES[rarity]} | {counts[rarity]} |")
    for rarity in sorted(counts, reverse=True):
        lines.extend([
            "",
            f"## {RARITIES[rarity]} Champions",
            "",
            "| Champion | ID | Rarity | Affinity | Rank | Level | Hydra role | Empowerment | Books | Books missing | Masteries | Used scrolls | Unused scrolls |",
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
        ])
        group = sorted(
            (champion for champion in champions if int(champion["Rarity"]) == rarity),
            key=lambda champion: (-int(champion["Rank"]), -int(champion["Level"]), champion["Name"], int(champion["ID"])),
        )
        for champion in group:
            missing = int(champion["BooksMissing"])
            used = " / ".join(champion[f"UsedT{tier}MasScrolls"] for tier in range(1, 4))
            unused = " / ".join(champion[f"UnUsedT{tier}MasScrolls"] for tier in range(1, 4))
            values = [
                champion["Name"], champion["ID"], RARITIES[rarity], AFFINITIES[int(champion["Affinity"])],
                champion["Rank"], champion["Level"], HYDRA_ROLES.get(champion["Name"], "Unassessed"),
                f"+{champion['EmpowerLevel']}", "Fully booked" if missing == 0 else "Incomplete", missing,
                mastery_status(champion), used, unused,
            ]
            lines.append("| " + " | ".join(cell(value) for value in values) + " |")
    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser(description="Generate the Docsify champion roster from a Raid CSV export.")
    parser.add_argument("source", nargs="?", type=Path, default=ROOT / "champs 20260911.csv")
    parser.add_argument("--output", type=Path, default=ROOT / "docs/champions-2026-09-11.md")
    args = parser.parse_args()
    content = build_roster(args.source)
    args.output.write_text(content, encoding="utf-8")
    print(f"Generated {args.output} from {args.source}")


if __name__ == "__main__":
    main()