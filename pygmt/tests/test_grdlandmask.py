"""
Test pygmt.grdlandmask.
"""

from pathlib import Path

import pytest
import xarray as xr
from pygmt import grdlandmask
from pygmt.enums import GridRegistration, GridType
from pygmt.exceptions import GMTInvalidInput
from pygmt.helpers import GMTTempFile


@pytest.fixture(scope="module", name="expected_grid")
def fixture_expected_grid():
    """
    Load the expected grdlandmask grid result.
    """
    return xr.DataArray(
        data=[
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0, 0.0, 1.0],
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 1.0, 1.0, 0.0, 0.0],
        ],
        coords={
            "lon": [125.0, 126.0, 127.0, 128.0, 129.0, 130.0],
            "lat": [30.0, 31.0, 32.0, 33.0, 34.0, 35.0],
        },
        dims=["lat", "lon"],
    )


def test_grdlandmask_outgrid(expected_grid):
    """
    Creates a grid land mask with an outgrid argument.
    """
    with GMTTempFile(suffix=".nc") as tmpfile:
        result = grdlandmask(outgrid=tmpfile.name, spacing=1, region=[125, 130, 30, 35])
        assert result is None  # return value is None
        assert Path(tmpfile.name).stat().st_size > 0  # check that outgrid exists
        temp_grid = xr.load_dataarray(tmpfile.name, engine="gmt", raster_kind="grid")
        xr.testing.assert_allclose(a=temp_grid, b=expected_grid)


@pytest.mark.benchmark
def test_grdlandmask_no_outgrid(expected_grid):
    """
    Test grdlandmask with no set outgrid.
    """
    result = grdlandmask(spacing=1, region=[125, 130, 30, 35], cores=2)
    # check information of the output grid
    assert isinstance(result, xr.DataArray)
    assert result.gmt.gtype == GridType.GEOGRAPHIC
    assert result.gmt.registration == GridRegistration.GRIDLINE
    # check information of the output grid
    xr.testing.assert_allclose(a=result, b=expected_grid)


def test_grdlandmask_fails():
    """
    Check that grdlandmask fails correctly when region and spacing are not given.
    """
    with pytest.raises(GMTInvalidInput):
        grdlandmask()
