# Getting started

## Windows development laptop

Use GitHub Desktop or Git with VS Code to clone the repository. Windows is suitable for documentation, Mission Planner and source editing. WSL2 can provide Linux development tools for software-only work. Actual Jetson/ZED integration must be validated on the compatible device stack.

From the cloned repository root, run the repository check with Python 3.10 or later:

    python scripts/check_repository.py

Use a project-local .venv when application dependencies are introduced. Keep it ignored. No application dependencies are installed by the repository scaffold.

## Jetson

Record the actual Jetson image, JetPack/L4T release, Ubuntu release, Python, ZED SDK, optional ROS 2 distribution and installation sources before choosing compatible dependencies. Fill in [versions.csv](../../config/versions.csv) using measured versions. Earlier suggested versions are not proof of what is installed.

Use VS Code Remote SSH if useful, and keep SSH keys outside the repository. Work on a feature branch. Fetch SDKs and upstream packages from their publishers rather than copying binaries into Git.

## Pixhawk

Use Mission Planner to verify the board, exact Rover firmware and receiver/actuator setup. Save before/after parameter snapshots under [config/pixhawk/params/](../../config/pixhawk/params/README.md), with metadata and the related test ID. A parameter file from another vehicle is not an approved baseline.

## First implementation imports

1. Import and run the existing mission prototype in a software-only environment.
2. Import language/NFC components with their provenance and dependencies.
3. Add simulation checks around the imported behavior.
4. Bring in verified device adapters and their documented configuration.
5. Link actual hardware results to the existing integration test plan.

The scaffold has no vehicle launch command because working application entry points have not yet been imported.
