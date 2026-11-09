# Development utilities

Run the initial repository check from any working directory:

    python /path/to/K9/scripts/check_repository.py

It inspects tracked/staged files: required foundation files, accidental secret/local-output paths, the 10 MiB per-file project limit, JSON/CSV structure, Python syntax and local Markdown link destinations. It does not execute application or hardware code and is not a full secret scanner.

GitHub CI runs the same command. Add behavioral test jobs when application code and its dependency manifests are introduced.
