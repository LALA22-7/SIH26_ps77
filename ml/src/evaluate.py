"""
StormSight — Evaluation Module

Implements severe-weather-specific evaluation metrics:
- POD (Probability of Detection)
- FAR (False Alarm Ratio)
- CSI (Critical Success Index)
- FSS (Fractions Skill Score)
- Brier Score
- Calibration analysis

Evaluates at multiple lead times (T+1h through T+6h).

TODO:
- [ ] Implement POD, FAR, CSI for binary thresholded predictions
- [ ] Implement FSS for spatial verification
- [ ] Implement Brier Score for probabilistic evaluation
- [ ] Implement calibration curve / reliability diagram
- [ ] Per-lead-time evaluation loop
- [ ] Generate evaluation report (JSON + markdown)
"""


def compute_pod(predictions, observations, threshold: float = 0.5):
    """Probability of Detection = hits / (hits + misses)"""
    raise NotImplementedError


def compute_far(predictions, observations, threshold: float = 0.5):
    """False Alarm Ratio = false_alarms / (hits + false_alarms)"""
    raise NotImplementedError


def compute_csi(predictions, observations, threshold: float = 0.5):
    """Critical Success Index = hits / (hits + misses + false_alarms)"""
    raise NotImplementedError


def compute_fss(predictions, observations, neighborhood_size: int = 5):
    """Fractions Skill Score — spatial verification with displacement tolerance."""
    raise NotImplementedError


def compute_brier_score(predicted_probs, observed_binary):
    """Brier Score = mean((predicted_prob - observed)^2)"""
    raise NotImplementedError


def evaluate_model(model, test_loader, lead_times: list[int] = [1, 2, 3, 4, 5, 6]):
    """
    Full evaluation across all hazards and lead times.
    Returns a nested dict: {hazard: {lead_time: {metric: value}}}
    """
    raise NotImplementedError
