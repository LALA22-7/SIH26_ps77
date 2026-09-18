"""
Download QPE (Quantitative Precipitation Estimation) data from MOSDAC.

TODO:
- [ ] Implement MOSDAC QPE product download
- [ ] Handle different rainfall estimation products
- [ ] Save to data/raw/qpe/
"""

import argparse
from pathlib import Path


def download_qpe(start_date: str, end_date: str, output_dir: str = "../data/raw/qpe"):
    """Download QPE data."""
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    raise NotImplementedError("Implement QPE download")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download QPE data")
    parser.add_argument("--start", required=True)
    parser.add_argument("--end", required=True)
    parser.add_argument("--output", default="../data/raw/qpe")
    args = parser.parse_args()
    download_qpe(args.start, args.end, args.output)
