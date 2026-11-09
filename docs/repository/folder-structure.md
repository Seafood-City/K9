# Folder structure and migration guide

Use lowercase folder names for consistent paths on Windows and Linux. Keep code and configuration outside documentation folders.

## Directory responsibilities

| Path | Put here |
| --- | --- |
| .github/ | CI, Dependabot, issue forms, pull request template and verified code-owner rules |
| software/src/ | Team-owned application packages; choose package boundaries from the architecture |
| software/ros2_ws/src/ | Team ROS 2 packages if ROS 2 is adopted; build/install/log stay ignored |
| config/pixhawk/params/ | Reviewed Mission Planner parameter snapshots and related metadata |
| config/jetson/ | Reviewed device/runtime configuration, with sanitized examples |
| config/missions/ | Mission scenarios, field maps and test inputs small enough for Git |
| hardware/electronics/ | Altium projects, schematics, PCB/library source, wiring and power documentation |
| hardware/mechanical/ | Chassis, mounting, CAD source and approved fabrication exports |
| docs/requirements/ | Current requirements matrix, test mapping and decisions |
| docs/architecture/ | Interfaces, coordinate conventions and system design |
| docs/verification/plans/ | Test plans and procedures |
| docs/verification/records/ | Completed test records and their configuration references |
| docs/verification/evidence/ | Small evidence images and an index of externally stored large evidence |
| docs/project-management/ | Proposal, schedule, owners and design-review presentation sources/exports |
| docs/competition/ | Rule references, clarifications and submission checklist |
| tests/unit/ | Deterministic software tests without devices |
| tests/integration/ | Module/interface tests with fakes or controlled software dependencies |
| tests/sitl/ | ArduPilot Rover simulation scenarios and expected outcomes |
| tests/hardware/ | Explicitly invoked hardware tests with prerequisites and a test procedure |
| scripts/ | Repository and development helpers |
| data/ | Artifact manifests and small fixtures that are safe to redistribute |
| data/raw/ and data/models/ | Local, ignored captures and downloaded model weights |
| logs/ | Local, ignored runtime output |

## Migrate existing work in reviewable groups

| Existing material | Destination and handling |
| --- | --- |
| avc_mission_starter.zip | Extract and inspect; move team application source into software/src/ and its tests into tests/. Record provenance. |
| AVC_Language_NFC_Starter(1).zip | Extract language/NFC source into software/src/; preserve licenses and identify any overlap before importing. |
| Team_3_System_Integration_and_Test_Plan.pdf | docs/verification/plans/ after the team confirms this is the current revision |
| Pixhawk_Vehicle_Control_Guide_and_Test_Record.docx | Procedure in docs/verification/plans/; retain completed execution records separately in docs/verification/records/ |
| Mission Planner .param exports | config/pixhawk/params/ with exact firmware, board, date and test record |
| Receiver photos and basic-test videos | Curated photos in docs/verification/evidence/; large videos linked in the evidence index |
| Requirements traceability matrix | docs/requirements/ with existing IDs and verification links preserved |
| Altium source | hardware/electronics/; exclude generated history/cache/output folders |
| Design review PowerPoint files | docs/project-management/; select one current editable source and an approved export |

Do not commit starter archives as the working implementation. Copy source files without their embedded .git directory, environments, credentials or generated output. Import one working module at a time, document how to run it, and keep tests aligned with its actual behavior.
