"""
Download DEM (Digital Elevation Model) data.

Source: SRTM (Shuttle Radar Topography Mission)
Resolution: 30m or 90m

TODO:
- [ ] Download SRTM tiles for India
- [ ] Compute slope and drainage density layers
- [ ] Resample to match model grid
- [ ] Save to data/dem/
"""

import argparse
from pathlib import Path


def download_dem(region: str = "india", output_dir: str = "../data/dem"):
    """Download and process DEM data."""
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    raise NotImplementedError("Implement DEM download")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download DEM data")
    parser.add_argument("--region", default="india")
    parser.add_argument("--output", default="../data/dem")
    args = parser.parse_args()
    download_dem(args.region, args.output)
