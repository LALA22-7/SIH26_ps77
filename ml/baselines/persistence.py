"""
Baseline 1: Persistence / Advection

Extrapolates current rain/cloud fields forward in time.
Purpose: establish how much can be achieved without AI.

TODO:
- [ ] Implement persistence baseline (current state = future state)
- [ ] Implement simple advection (optical-flow-based extrapolation)
- [ ] Evaluate with POD, FAR, CSI at each lead time
"""


def persistence_forecast(current_field, lead_hours: int):
    """Simply copies the current field as the forecast."""
    return current_field


def advection_forecast(field_sequence, lead_hours: int):
    """Extrapolates using estimated motion vectors (optical flow)."""
    raise NotImplementedError
