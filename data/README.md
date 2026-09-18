# StormSight Data Pipeline

## Directory Structure

- `raw/` — Downloaded satellite/reanalysis files (gitignored, large)
- `interim/` — Intermediate processing outputs (gitignored)
- `processed/` — Final training-ready tensors (tracked if small enough)
- `ground_truth/` — Labelled severe weather event catalog
- `dem/` — Digital elevation model, slope, basin/drainage layers
- `event_manifest.csv` — Master manifest linking events to data files

## Data Sources

| Source | Download Script | Format | Size Estimate |
|---|---|---|---|
| INSAT-3D/3DR/3DS | `scripts/download_insat.py` | HDF5 / NetCDF | ~50 GB |
| IMDAA Reanalysis | `scripts/download_imdaa.py` | GRIB2 / NetCDF | ~30 GB |
| MOSDAC QPE | `scripts/download_qpe.py` | NetCDF | ~10 GB |
| SRTM DEM | `scripts/download_dem.py` | GeoTIFF | ~2 GB |
| IMD Event Records | Manual curation | CSV | <1 MB |
