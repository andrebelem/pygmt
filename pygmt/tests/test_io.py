"""
Test input/output (I/O) utilities.
"""

import numpy as np
import pytest
import xarray as xr
from pygmt.enums import GridRegistration, GridType
from pygmt.helpers import GMTTempFile
from pygmt.io import load_dataarray

pytest.importorskip("netCDF4")


# TODO(PyGMT>=0.20.0): Remove test_io_load_dataarray
def test_io_load_dataarray():
    """
    Check that load_dataarray works to read a netCDF grid with GMTDataArrayAccessor
    information loaded.
    """
    with GMTTempFile(suffix=".nc") as tmpfile:
        rng = np.random.default_rng()
        grid = xr.DataArray(
            data=rng.random((2, 2)), coords=[[0.1, 0.2], [0.3, 0.4]], dims=("x", "y")
        )
        grid.to_netcdf(tmpfile.name)

        with pytest.warns(FutureWarning):
            dataarray = load_dataarray(tmpfile.name)

        assert dataarray.gmt.gtype == GridType.CARTESIAN
        assert dataarray.gmt.registration == GridRegistration.PIXEL
        # this would fail if we used xr.open_dataarray instead of load_dataarray
        dataarray.to_netcdf(tmpfile.name)


def test_io_load_dataarray_cache():
    """
    Check that load_dataarray fails when the cache argument is used.
    """
    with pytest.raises(TypeError):
        _ = load_dataarray("somefile.nc", cache=True)
