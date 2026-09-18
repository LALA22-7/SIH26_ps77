"""
Download INSAT-3D/3DR/3DS data from MOSDAC.

Channels: TIR1, TIR2, MIR, WV, VIS, SWIR
Source: https://www.mosdac.gov.in

TODO:
- [ ] Implement MOSDAC API authentication
- [ ] Download full-disk imagery for specified date ranges
- [ ] Extract relevant channels
- [ ] Save to data/raw/insat/
"""

import argparse
from pathlib import Path


def download_insat(start_date: str, end_date: str, output_dir: str = "../data/raw/insat"):
    """Download INSAT satellite data from MOSDAC."""
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    # TODO: Implement
    raise NotImplementedError("Implement MOSDAC download")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download INSAT data from MOSDAC")
    parser.add_argument("--start", required=True, help="Start date (YYYY-MM-DD)")
    parser.add_argument("--end", required=True, help="End date (YYYY-MM-DD)")
    parser.add_argument("--output", default="../data/raw/insat")
    args = parser.parse_args()
    download_insat(args.start, args.end, args.output)
