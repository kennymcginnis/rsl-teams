# rsl-teams

Hydra team planning for Raid: Shadow Legends.

## Documentation

The Docsify site in [docs/index.html](docs/index.html) displays the Hydra team guide as its home page,
with sidebar navigation and full-text search across the guide and champion roster.
The raw roster CSV and guide transcript remain at the repository root; a generated roster table is published in docs.

Edit [docs/hydra-teams-2026-09-11.md](docs/hydra-teams-2026-09-11.md) to update the published guide.

## Champion Roster

[docs/champions-2026-09-11.md](docs/champions-2026-09-11.md) contains every exported champion copy, grouped by rarity, with affinity,
rank, level, assessed Hydra role, empowerment, book status, books missing, and mastery-scroll status.
Official champion types and books spent are not exported; unassessed roles are not guessed.

Regenerate the page after updating the CSV:

```sh
python3 scripts/build_roster.py "champs 20260911.csv"
```

Pass a different CSV path for a later export. The source filename is shown on the generated page.
Role assessments and scroll-status rules live in [scripts/build_roster.py](scripts/build_roster.py);
edit that generator rather than the generated page. Commit the generated Markdown with the other site files.
Python is needed only to refresh the roster, not to deploy or view the site.

## Local Preview

From the repository root, run:

```sh
python3 -m http.server 3000 --directory docs
```

Open http://localhost:3000. Docsify fetches Markdown over HTTP, so opening the HTML directly from disk
is not sufficient. There is no Node installation or build step. The theme and scripts load from jsDelivr,
which requires an internet connection.

## GitHub Pages

1. Commit and push the documentation files to the branch you want to publish.
2. In the repository's **Settings > Pages**, select **Deploy from a branch**.
3. Select that branch and the **/docs** folder, then save.
4. After GitHub finishes deployment, visit https://kennymcginnis.github.io/rsl-teams/.

The [docs/.nojekyll](docs/.nojekyll) file disables Jekyll processing. No GitHub Actions workflow is required.
Future edits to the Markdown inside `docs/` are published when pushed to the selected branch.

The site is intended to be public. Review the guide before publishing; its source links lead to the
original files on GitHub, which readers can access only if the repository permits it.
