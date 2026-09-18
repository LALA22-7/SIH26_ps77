"""
Event-window extraction and labelling.

For each confirmed severe weather event, constructs:
  T-6h, T-5h, ..., T-1h, T, T+1h temporal sequences.

Labels each window according to hazard type and lead time.

TODO:
- [ ] Parse IMD event catalog (events_catalog.csv)
- [ ] Extract temporal windows around each event
- [ ] Assign multi-hazard labels per timestep
- [ ] Generate event_manifest.csv
"""

raise NotImplementedError("Implement event labelling pipeline")
