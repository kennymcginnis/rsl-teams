import argparse
import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def cell(value):
    return value.replace("|", "\\|").replace("\n", " ")


def build_factions(source):
    with source.open(newline="", encoding="utf-8-sig") as stream:
        rows = list(csv.reader(stream))
    if not rows or rows[0] != ["", "", "SS-Tier", "S-Tier", "A-Tier", "B-Tier"]:
        raise ValueError("Expected faction and role columns followed by SS-Tier, S-Tier, A-Tier, B-Tier")
    lines = [
        "# Faction Wars Planning",
        "",
        f"Source: **{source.name}**. Your working faction tiers and role assignments, preserved as entered.",
        "",
        "[See balanced five-champion teams, roles, and investment notes](faction-wars-teams.md).",
        "",
        "Blank cells and role-only rows are retained for planning. Unlabeled roles have not been inferred. "
        "Champion aliases, form labels, and tier placements are unchanged; this is not a validated five-champion "
        "team recommendation or a roster-ownership check.",
    ]
    faction = None
    for row in rows[1:]:
        if len(row) != 6:
            raise ValueError(f"Expected six columns, got {len(row)}: {row}")
        if not any(row):
            continue
        if row[0]:
            if any(row[1:]):
                raise ValueError(f"Unexpected values in faction heading: {row}")
            faction = row[0]
            lines.extend([
                "",
                f"## {faction}",
                "",
                "| Role | SS-Tier | S-Tier | A-Tier | B-Tier |",
                "| --- | --- | --- | --- | --- |",
            ])
        else:
            if faction is None:
                raise ValueError("Found a planning row before a faction heading")
            lines.append("| " + " | ".join(cell(value) for value in row[1:]) + " |")
    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser(description="Generate a Docsify Faction Wars page from the planning CSV.")
    parser.add_argument("source", nargs="?", type=Path, default=ROOT / "Raid Factions.csv")
    parser.add_argument("--output", type=Path, default=ROOT / "docs/faction-wars.md")
    args = parser.parse_args()
    args.output.write_text(build_factions(args.source), encoding="utf-8")
    print(f"Generated {args.output} from {args.source}")


if __name__ == "__main__":
    main()