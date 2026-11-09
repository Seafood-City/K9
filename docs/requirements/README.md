# Requirements and decisions

Migrate the existing requirements traceability matrix here as the authoritative source, preserving its requirement IDs, verification IDs, owners and evidence links. This setup does not recreate its content from memory.

Each requirement should link to its design location, verification method, test/procedure, latest result and evidence. Keep NOT RUN distinct from PASS.

Store the current rules version and interpretations in [competition/](../competition/README.md). Record unresolved architecture/rules discrepancies with owner, source/version, decision date and resolution evidence. In particular, resolve any requirement that assumes BrainChip against the current Jetson/Pixhawk baseline rather than silently marking compliance.

Use traceability.csv only as an empty import format if it fits the team's existing matrix; do not maintain competing copies.
