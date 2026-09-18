"""
StormSight — Physics-Guided Feature Engineering

Derives physically meaningful atmospheric features from raw data:
- IWV (Integrated Water Vapor) and ΔIWV
- CAPE / CIN from vertical profiles
- Low-level convergence
- Vertical wind shear
- CTT (Cloud Top Temperature) and ΔCTT (cooling rate)
- Moisture flux convergence
- Lifted Index
- K-Index

These features are computed BEFORE the neural network, giving it
known physical structure rather than asking it to rediscover meteorology.

TODO:
- [ ] Implement IWV computation from humidity profiles
- [ ] Implement ΔIWV (temporal change)
- [ ] Implement CAPE/CIN from temperature/humidity profiles
- [ ] Implement vertical wind shear from wind profiles
- [ ] Implement low-level convergence from wind fields
- [ ] Implement CTT extraction and ΔCTT cooling rate
- [ ] Implement moisture flux convergence
- [ ] Implement derived indices (LI, KI, TT)
"""


def compute_iwv(specific_humidity_profile, pressure_levels):
    """Integrated Water Vapor from humidity profile."""
    raise NotImplementedError


def compute_delta_iwv(iwv_current, iwv_previous, dt_hours: float):
    """Temporal change in IWV."""
    raise NotImplementedError


def compute_cape_cin(temperature_profile, dewpoint_profile, pressure_levels):
    """CAPE and CIN from vertical profiles (parcel theory)."""
    raise NotImplementedError


def compute_vertical_shear(u_wind, v_wind, pressure_levels, lower_hpa=850, upper_hpa=200):
    """Vertical wind shear between two pressure levels."""
    raise NotImplementedError


def compute_convergence(u_wind, v_wind, dx, dy):
    """Low-level horizontal wind convergence."""
    raise NotImplementedError


def compute_ctt_cooling_rate(ctt_sequence, dt_minutes: float):
    """Cloud Top Temperature cooling rate (ΔCTT/Δt)."""
    raise NotImplementedError
