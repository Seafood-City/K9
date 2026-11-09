# K9

Ground-only autonomous vehicle system for Team 3's Raytheon AVC capstone, maintained by Seafood City.

**Repository status:** initial project organization. Module folders describe intended responsibilities; they do not claim working autonomous navigation or completed hardware tests.

## Vehicle architecture

| Component | Responsibility |
| --- | --- |
| Jetson Orin Nano Super | Mission logic, perception, localization, planning, language interface and NFC integration |
| ZED 2i | Stereo images, depth and visual-inertial tracking input |
| Pixhawk 6C / ArduPilot Rover | Steering/throttle control, vehicle state and configured failsafes |
| RC transmitter and receiver | Manual operation and operator takeover through the verified receiver interface |
| ESC, steering servo and chassis | Vehicle actuation and mechanical platform |

Jetson and Pixhawk communicate using MAVLink. Navigation is designed for operation without GPS. BrainChip is outside the current hardware baseline; any discrepancy with competition requirements stays open in the requirements decision record.

## Start here

1. Read the [setup guide](docs/getting-started/README.md).
2. Review the [folder guide](docs/repository/folder-structure.md) before moving existing files.
3. Follow the [contribution workflow](CONTRIBUTING.md).
4. Apply the remaining [GitHub settings](docs/repository/github-settings.md).
5. Add existing implementation and evidence through separate, reviewable pull requests.

## Project map

| Path | Contents |
| --- | --- |
| [software/](software/README.md) | Team application source and optional ROS 2 workspace |
| [config/](config/README.md) | Versioned runtime configuration and Pixhawk parameter snapshots |
| [hardware/](hardware/README.md) | Altium source, wiring, power and mechanical designs |
| [docs/](docs/README.md) | Requirements, design, procedures, test records and project deliverables |
| [tests/](tests/README.md) | Automated software checks, simulation and explicitly invoked hardware tests |
| [scripts/](scripts/README.md) | Development and repository utilities |
| [data/](data/README.md) | Dataset/model references and small reproducible fixtures |
| [logs/](logs/README.md) | Local runtime output, excluded from version control |

Run repository checks from the root with Python 3.10 or later:

    python scripts/check_repository.py

The CI job validates repository files and Python syntax. It does not operate a vehicle, install the Jetson stack or prove a hardware test passed.

## License

This repository retains its existing [MIT license](LICENSE), Copyright (c) 2026 Seafood City. Third-party firmware, SDKs, models, datasets and copied code retain their own licenses; record them in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
