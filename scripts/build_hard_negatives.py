"""
Construct hard-negative samples.

Hard negatives are situations where:
- Moisture was high
- CAPE was high
- Cloud growth occurred
- Rainfall increased
...but NO severe event ultimately developed.

Critical for teaching the model that high CAPE ≠ disaster.

TODO:
- [ ] Identify favorable-but-non-event periods from IMDAA/INSAT
- [ ] Extract temporal windows matching the same format as positive events
- [ ] Label as negative across all hazard types
- [ ] Add to event_manifest.csv
"""

raise NotImplementedError("Implement hard-negative construction")
