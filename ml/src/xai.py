"""
StormSight — Explainable AI Module

Provides operational XAI for severe weather predictions:
- SHAP-style feature attribution
- Saliency / gradient maps for spatial inputs
- Attention visualization
- Temporal contribution plots
- Feature trend visualization

The goal: answer "Why is the model warning here, now?"

TODO:
- [ ] Implement SHAP for tabular/engineered features
- [ ] Implement gradient-based saliency maps for image inputs
- [ ] Implement attention map extraction (if using attention in backbone)
- [ ] Build explanation text generator from attributions
- [ ] Temporal contribution plot (which timestep contributed most)
"""


def explain_prediction(model, sample, method: str = "shap"):
    """
    Generate feature attribution for a single prediction.

    Returns:
        dict with:
            - 'feature_contributions': {feature_name: importance_score}
            - 'spatial_saliency': [H, W] attribution map
            - 'temporal_contributions': [T] per-timestep importance
            - 'explanation_text': human-readable explanation string
    """
    raise NotImplementedError


def generate_explanation_text(feature_contributions: dict) -> str:
    """
    Generate human-readable explanation from feature attributions.

    Example output:
        "Flash-Flood Risk: 82%
         Primary contributing signals:
         - IWV accumulation: High
         - CAPE: Very High
         - CIN: Rapidly decreasing
         - CTT cooling: Strong
         - 3-hour rainfall: Increasing
         - Terrain slope: High"
    """
    raise NotImplementedError
