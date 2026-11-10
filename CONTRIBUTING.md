# Contributing to K9

## Team workflow

Use one repository and one shared main branch. Create a short-lived branch for each task; a permanent develop branch is unnecessary for this four-person team.

Suggested branch names:

- feature/nfc-reader
- fix/receiver-mapping
- docs/pixhawk-test-record
- hardware/power-schematic

Open a pull request into main and request one teammate's review. State the problem, changed behavior, validation and any unfinished work. Resolve review discussions, update the branch when needed, then squash merge and delete it. Commit titles such as "Add NFC reader adapter" are sufficient.

For Windows users, GitHub Desktop is suitable for cloning, branches, commits, pushes and pull requests. Git command-line users can start with:

    git clone https://github.com/Seafood-City/K9.git
    cd K9
    git switch -c feature/your-task
    python scripts/check_repository.py
    git add <specific-files>
    git diff --cached
    git commit -m "Describe the change"
    git push -u origin feature/your-task

Replace placeholders before running commands. Inspect staged changes before every commit.

## What to include

- Team-owned source, small configuration files, design source and documentation.
- Tests appropriate to changed behavior, with exact commands and actual results.
- Approved parameter snapshots with firmware version, vehicle identity and a related test record.
- Requirements and evidence references when a change affects vehicle behavior.

Keep secrets, local environments, generated builds, raw captures, model downloads and runtime logs out of Git. Use the [large-file policy](docs/repository/data-and-large-files.md). Add upstream projects as dependencies or pinned references and preserve their licenses.

## Vehicle changes

Record the existing configuration before changing it. Review command limits, neutral behavior, arming, manual takeover and loss-of-link behavior when relevant. Execute physical tests under the approved procedure and record the setup, stop method, operator, firmware, parameters and observed result.

Hardware and simulation tests are separate evidence. CI does not arm or drive the vehicle. Do not label a planned test as passing.

## Documentation and ownership

Use [the folder guide](docs/repository/folder-structure.md) for placement. Keep editable sources with approved exports, using descriptive filenames. Preserve the current requirements/test IDs during migration.

Subsystem responsibility is listed in [owners.csv](docs/project-management/owners.csv). Active CODEOWNERS rules should be added only after each person's exact GitHub account or organization team has been verified.
