"""
StormSight — Multi-Task Training Loop

Trains the shared backbone + multi-task heads jointly.

TODO:
- [ ] Implement multi-task loss (weighted sum of per-head losses)
- [ ] Implement class-balanced / focal loss for rare events
- [ ] Add lead-time-specific evaluation during training
- [ ] Implement time-separated validation (no temporal leakage)
- [ ] Checkpoint best model by CSI score
- [ ] WandB / TensorBoard logging
"""

import torch
import torch.nn as nn
from pathlib import Path


def train(config_path: str = "configs/training_config.json"):
    """Main training entry point."""
    # TODO: Implement training loop
    # 1. Load config
    # 2. Create dataset with time-separated train/val split
    # 3. Initialize model
    # 4. Define multi-task loss
    # 5. Training loop with evaluation at each epoch
    # 6. Save best checkpoint
    raise NotImplementedError("Implement training loop")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Train StormSight model")
    parser.add_argument("--config", default="configs/training_config.json")
    args = parser.parse_args()
    train(args.config)
