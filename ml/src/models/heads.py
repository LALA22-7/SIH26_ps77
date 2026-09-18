"""
StormSight — Multi-Task Prediction Heads

Separate heads for each hazard in the cascade:
  - Thunderstorm probability (dense spatial map)
  - Cloudburst probability (dense spatial map)
  - Flash-flood probability (dense spatial map, terrain-conditioned)

TODO:
- [ ] Implement ThunderstormHead
- [ ] Implement CloudburstHead
- [ ] Implement FlashFloodHead (with DEM/terrain conditioning input)
- [ ] Ensure all heads accept shared backbone output
"""

import torch
import torch.nn as nn


class ThunderstormHead(nn.Module):
    """Predicts thunderstorm probability map from shared backbone features."""

    def __init__(self, in_channels: int):
        super().__init__()
        # TODO: Implement prediction head
        # Output: [B, 1, H, W] probability map
        raise NotImplementedError

    def forward(self, shared_features):
        raise NotImplementedError


class CloudburstHead(nn.Module):
    """Predicts cloudburst probability map from shared backbone features."""

    def __init__(self, in_channels: int):
        super().__init__()
        # TODO: Implement prediction head
        raise NotImplementedError

    def forward(self, shared_features):
        raise NotImplementedError


class FlashFloodHead(nn.Module):
    """
    Predicts flash-flood probability map.
    Conditioned on terrain (DEM, slope, basin) in addition to backbone features.
    """

    def __init__(self, in_channels: int, terrain_channels: int = 3):
        super().__init__()
        # TODO: Implement terrain-conditioned prediction head
        # Inputs: shared_features + terrain_features (elevation, slope, drainage)
        raise NotImplementedError

    def forward(self, shared_features, terrain_features):
        raise NotImplementedError


class StormSightMultiTask(nn.Module):
    """
    Full multi-task model combining backbone + all heads.

    Input: [B, T, C, H, W] atmospheric sequence + [B, C_terrain, H, W] terrain
    Output: dict of probability maps for each hazard
    """

    def __init__(self, config: dict):
        super().__init__()
        # TODO: Wire backbone + heads together
        raise NotImplementedError

    def forward(self, atmospheric_sequence, terrain_features):
        raise NotImplementedError
