"""
StormSight — Event-Window Dataset

Constructs temporal sequences around confirmed severe weather events.
Includes hard-negative sampling for events where conditions were favorable
but no severe weather materialized.

TODO:
- [ ] Implement event-window extraction (T-6h to T+1h around each event)
- [ ] Load multi-source tensors (satellite, atmospheric, QPE, terrain)
- [ ] Implement hard-negative sampling strategy
- [ ] Handle missing data / temporal gaps
- [ ] Class-balanced sampling for rare events
"""

import torch
from torch.utils.data import Dataset
from pathlib import Path
from typing import Optional


class StormSightDataset(Dataset):
    """
    Event-centered severe weather dataset.

    Each sample is a temporal sequence of multi-modal observations
    around a confirmed or hard-negative weather event.

    Args:
        manifest_path: Path to event_manifest.csv
        data_dir: Root directory for processed tensors
        sequence_length: Number of timesteps per sample (default: 6)
        lead_times: List of lead times to predict (hours)
        include_hard_negatives: Whether to include hard-negative samples
    """

    def __init__(
        self,
        manifest_path: str,
        data_dir: str,
        sequence_length: int = 6,
        lead_times: list[int] = [1, 2, 3, 4, 5, 6],
        include_hard_negatives: bool = True,
    ):
        self.data_dir = Path(data_dir)
        self.sequence_length = sequence_length
        self.lead_times = lead_times

        # TODO: Load manifest and build index
        raise NotImplementedError("Implement dataset loading")

    def __len__(self):
        raise NotImplementedError

    def __getitem__(self, idx):
        """
        Returns:
            dict with keys:
                - 'atmospheric': [T, C_atm, H, W] — satellite + reanalysis sequence
                - 'terrain': [C_terrain, H, W] — static DEM/slope/basin
                - 'targets': dict of [H, W] probability maps per hazard per lead time
                - 'metadata': event info (timestamp, location, event_type)
        """
        raise NotImplementedError
