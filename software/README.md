# Software

The intended responsibilities are mission management, perception, localization, navigation, vehicle link, NFC and language/intent handling. Their contracts are described in [architecture](../docs/architecture/README.md).

This is an organizational scaffold. Existing mission and language/NFC starter implementations still need review and import.

- [src/](src/README.md) holds reusable team application packages.
- [ros2_ws/src/](ros2_ws/src/README.md) is reserved for team ROS 2 packages if ROS 2 is adopted.
- Shared runtime configuration belongs in config/.
- Behavioral tests belong in tests/ and reusable developer helpers in scripts/.

Add dependency manifests and reproducible entry points with the actual implementation. Separate device adapters from mission logic so software behavior can be tested without the car. Do not copy an entire ArduPilot or ZED SDK installation here.
