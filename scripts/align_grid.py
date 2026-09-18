"""
Spatiotemporal alignment to unified grid.

Brings together datasets with different:
- spatial resolutions
- coordinate systems
- timestamps / update frequencies
- file formats

Pipeline:
  INSAT → HDF/NetCDF processing → Reprojection → Temporal alignment
  + IMDAA + QPE + DEM → Unified spatial grid → Training dataset

TODO:
- [ ] Define target grid (resolution, bounds, projection)
- [ ] Implement spatial regridding for each data source
- [ ] Implement temporal interpolation / alignment
- [ ] Handle missing data
- [ ] Output unified [C, H, W] tensors per timestep
"""

raise NotImplementedError("Implement grid alignment pipeline")
