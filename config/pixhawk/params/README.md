# Parameter snapshots

Export full before/after .param files from Mission Planner. Suggested name: YYYY-MM-DD_IT-03_vehicle-id_after.param.

For each snapshot, include a same-name Markdown metadata record with:

- Vehicle and board identity.
- Exact firmware version and board target.
- Mission Planner version and export timestamp.
- Purpose, changed settings and reviewer.
- Related procedure, test ID and execution record.
- Known calibration assumptions and limitations.

Approved .param files remain tracked. Device-local overrides ending in .local.param are ignored. No actual parameters are supplied by this scaffold.
