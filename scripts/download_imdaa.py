"""
Download IMDAA reanalysis data.

Variables: temperature, humidity, wind, geopotential, pressure profiles
Source: NCMRWF / collaborating agencies

TODO:
- [ ] Implement IMDAA data access
- [ ] Download relevant pressure-level variables
- [ ] Save to data/raw/imdaa/
"""

import argparse
from pathlib import Path


def download_imdaa(start_date: str, end_date: str, output_dir: str = "../data/raw/imdaa"):
    """Download IMDAA reanalysis data."""
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    # TODO: Implement
    raise NotImplementedError("Implement IMDAA download")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download IMDAA reanalysis data")
    parser.add_argument("--start", required=True)
    parser.add_argument("--end", required=True)
    parser.add_argument("--output", default="../data/raw/imdaa")
    args = parser.parse_args()
    download_imdaa(args.start, args.end, args.output)
