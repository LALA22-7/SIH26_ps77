"""
Baseline 2: XGBoost / Random Forest with Engineered Features

Uses physics-guided engineered features for non-deep-learning baseline.
Purpose: interpretable baseline to compare against deep models.

Feature set:
- IWV, ΔIWV
- CAPE, CIN
- Convergence, Shear
- CTT, ΔCTT
- Rainfall intensity
- Terrain slope, elevation

TODO:
- [ ] Implement feature extraction pipeline
- [ ] Train XGBoost classifier per hazard
- [ ] Train Random Forest as alternative
- [ ] Evaluate and compare with deep models
"""


def train_xgboost_baseline(features, targets, hazard_type: str):
    """Train XGBoost model for a specific hazard type."""
    raise NotImplementedError


def train_random_forest_baseline(features, targets, hazard_type: str):
    """Train Random Forest model for a specific hazard type."""
    raise NotImplementedError
