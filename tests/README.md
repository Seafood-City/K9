# Tests

| Folder | Execution boundary |
| --- | --- |
| [unit/](unit/README.md) | Deterministic logic with no hardware |
| [integration/](integration/README.md) | Software interface checks with controlled dependencies |
| [sitl/](sitl/README.md) | ArduPilot Rover software-in-the-loop scenarios |
| [hardware/](hardware/README.md) | Explicitly invoked physical-device tests |

No behavioral tests or device drivers have been imported yet. The initial CI job checks repository hygiene and Python syntax only. Add test commands and their dependencies when actual implementation arrives.
