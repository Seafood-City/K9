# Architecture and interfaces

The current hardware baseline is Jetson Orin Nano Super + ZED 2i + Pixhawk 6C running ArduPilot Rover, with the RC car's ESC/servo and an RC transmitter/receiver. GPS is unavailable. BrainChip is not part of this hardware baseline; record any rule discrepancy as an open decision.

| Interface | Intended contract to document |
| --- | --- |
| ZED to perception/localization | Images, depth, pose, timestamps, validity and coordinate frame |
| Perception to mission/navigation | Target identity/color, confidence, relative pose and observation age |
| Mission to navigation | Validated goal, target changes, cancellation and completion/failure |
| Navigation to vehicle link | Bounded commands, coordinate frame, command age and explicit stop behavior |
| Jetson to Pixhawk | MAVLink messages, transport, time basis, mode/arming assumptions and loss-of-link response |
| NFC to mission/reporting | Reader status, payload schema, validation, duplicate handling and timestamps |
| Language interface to mission | Validated structured intent; execution remains behind the mission/control interface |

Before integrating modules, choose and record coordinate frames, units, timestamps, error/status fields and owner for each contract. Navigation, ROS 2/MAVROS versus direct MAVLink, and language-model placement remain implementation decisions until verified in the imported source.

## Proposed software boundaries

| Module | Responsibility |
| --- | --- |
| mission | Mission state, target selection, replanning triggers and run outcome |
| perception | Color/target detection and depth-assisted observations |
| localization | GPS-denied pose input, validity, frames and reset handling |
| navigation | Path/motion planning and obstacle handling |
| vehicle_link | Pixhawk connection, telemetry and bounded command interface |
| nfc | Reader adapter, payload validation and reporting |
| language | Intent parsing and schema validation |

Use these as responsibilities, not a requirement to create seven separate processes. Record the actual package and entry-point structure after importing working code.
