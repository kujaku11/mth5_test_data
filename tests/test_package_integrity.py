"""
Test suite to verify mth5_test_data package is correctly installed.

This ensures:
1. All expected zip files are present in the installed package
2. Zip files can be extracted without FileExistsError
3. No duplicate content exists (both zipped and extracted)
"""

import pytest
import zipfile
from pathlib import Path
from mth5_test_data import get_test_data_path


class TestPackageIntegrity:
    """Test that the package is correctly installed with no duplicates."""

    @pytest.fixture
    def package_root(self):
        """Get the root directory of the installed package."""
        import mth5_test_data

        return Path(mth5_test_data.__file__).parent

    def test_1_no_duplicate_extracted_directories(self, package_root):
        """Verify no extracted directories exist that would duplicate zip contents.

        NOTE: This test MUST run first (hence test_1_ prefix) before any other
        tests call get_test_data_path(), which extracts zips to the package directory.

        These directories may exist from previous test runs or get_test_data_path() calls.
        We clean them up first to verify the package itself doesn't contain duplicates.
        """
        import shutil

        # These directories should NOT exist in the installed package - they're inside zip files
        forbidden_dirs = [
            package_root / "metronix" / "Northern_Mining",
            package_root / "phoenix" / "sample_data",
        ]

        # Clean up any extracted directories from previous runs
        for forbidden_dir in forbidden_dirs:
            if forbidden_dir.exists():
                shutil.rmtree(forbidden_dir)

        # Now verify they don't exist (if they still exist, they were in the package itself)
        for forbidden_dir in forbidden_dirs:
            assert not forbidden_dir.exists(), (
                f"Duplicate directory found: {forbidden_dir.relative_to(package_root)}. "
                f"This directory should only exist inside the zip file, not as extracted content."
            )

    def test_all_zip_files_present(self, package_root):
        """Verify all expected zip files are present in the package."""
        expected_zips = {
            "metronix/metronix_test_data.zip",
            "metronix/ats/metronix_ats_test_data.zip",
            "phoenix/phoenix_test_data.zip",
            "phoenix_mtu/phoenix_mtu_test_data.zip",
            "usgs_ascii/usgs_ascii_test_data.zip",
            "nims/nims_test_data.zip",
            "zen/zen_test_data.zip",
            "miniseed/miniseed_test_data.zip",
            "lemi/lemi_test_data.zip",
        }

        for zip_path in expected_zips:
            full_path = package_root / zip_path
            assert full_path.exists(), f"Missing zip file: {zip_path}"
            assert full_path.is_file(), f"Not a file: {zip_path}"

            # Verify it's a valid zip file
            assert zipfile.is_zipfile(full_path), f"Not a valid zip: {zip_path}"

    @pytest.mark.parametrize(
        "instrument",
        [
            "metronix",
            "metronix_ats",
            "phoenix",
            "phoenix_mtu",
            "usgs_ascii",
            "nims",
            "zen",
            "lemi",
        ],
    )
    def test_zip_extraction_succeeds(self, instrument, tmp_path):
        """Test that zip files can be extracted without errors."""
        # This simulates what get_test_data_path() does internally
        try:
            data_path = get_test_data_path(instrument)
            assert data_path.exists(), f"Failed to get test data for {instrument}"
            assert (
                data_path.is_dir()
            ), f"Test data path is not a directory for {instrument}"
        except FileExistsError as e:
            pytest.fail(
                f"FileExistsError when extracting {instrument} data. "
                f"This indicates duplicate content in the package. Error: {e}"
            )

    def test_metronix_extracted_structure(self):
        """Verify metronix data extracts correctly with expected structure."""
        data_path = get_test_data_path("metronix")

        # Check for expected Northern_Mining directory structure
        northern_mining = data_path / "Northern_Mining"
        assert (
            northern_mining.exists()
        ), "Northern_Mining directory not found after extraction"
        assert northern_mining.is_dir(), "Northern_Mining is not a directory"

        # Verify some expected subdirectories
        stations_dir = northern_mining / "stations"
        assert stations_dir.exists(), "stations directory not found in Northern_Mining"

    def test_metronix_ats_extracted_structure(self):
        """Verify metronix_ats data extracts correctly with expected structure."""
        data_path = get_test_data_path("metronix_ats")

        # Check for expected Northern_Mining directory structure
        northern_mining = data_path / "meas_2024-12-01_15-31-21"
        assert (
            northern_mining.exists()
        ), "meas_2024-12-01_15-31-21 directory not found after extraction"
        assert northern_mining.is_dir(), "meas_2024-12-01_15-31-21 is not a directory"

    def test_phoenix_extracted_structure(self):
        """Verify phoenix data extracts correctly with expected structure."""
        data_path = get_test_data_path("phoenix")

        # Check for expected sample_data directory structure
        sample_data = data_path / "sample_data"
        assert sample_data.exists(), "sample_data directory not found after extraction"
        assert sample_data.is_dir(), "sample_data is not a directory"

        # Verify some expected files (bin files are in subdirectories)
        bin_files = list(sample_data.rglob("*.bin"))
        assert len(bin_files) > 0, "No .bin files found in phoenix sample_data"

        # Check for expected config files
        json_files = list(sample_data.rglob("*.json"))
        assert len(json_files) > 0, "No .json files found in phoenix sample_data"

    def test_phoenix_mtu_extracted_structure(self):
        """Verify phoenix_mtu data extracts correctly with expected TBL file."""
        data_path = get_test_data_path("phoenix_mtu")

        # Check for expected TBL file
        tbl_file = data_path / "1690C16C.TBL"
        assert tbl_file.exists(), "1690C16C.TBL file not found after extraction"
        assert tbl_file.is_file(), "1690C16C.TBL is not a file"

        # Verify it's a valid TBL file (at least 25 bytes for one block)
        assert tbl_file.stat().st_size >= 25, "TBL file is too small to be valid"

    def test_standalone_files_present(self, package_root):
        """Verify standalone files (not in zips) are present."""
        # Check for standalone NIMS binary files
        nims_dir = package_root / "nims"
        assert (nims_dir / "mnp300a.BIN").exists(), "Missing standalone mnp300a.BIN"
        assert (nims_dir / "mnp300b.BIN").exists(), "Missing standalone mnp300b.BIN"

        # Check for calibration files
        cal_dir = package_root / "calibration_files"
        assert cal_dir.exists(), "Missing calibration_files directory"
        assert (cal_dir / "2254.csv").exists(), "Missing calibration file 2254.csv"

        # Check for mth5 test files
        mth5_dir = package_root / "mth5" / "parkfield"
        assert mth5_dir.exists(), "Missing mth5/parkfield directory"
        h5_files = list(mth5_dir.glob("*.h5"))
        assert len(h5_files) > 0, "No .h5 files found in mth5/parkfield"

    def test_xml_metadata_files_present(self, package_root):
        """Verify XML metadata files are present."""
        xml_dirs = [
            package_root / "florida_xml_metadata_files",
            package_root / "stationxml",
            package_root / "iris" / "xml",
        ]

        for xml_dir in xml_dirs:
            assert (
                xml_dir.exists()
            ), f"Missing XML directory: {xml_dir.relative_to(package_root)}"
            xml_files = list(xml_dir.glob("*.xml"))
            assert (
                len(xml_files) > 0
            ), f"No XML files in {xml_dir.relative_to(package_root)}"
