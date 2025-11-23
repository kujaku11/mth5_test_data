"""
allows the path to this repo to be imported, for example:
>>> from mth5_test_data.util import MTH5_TEST_DATA_DIR
>>> MTH5_TEST_DATA_DIR
PosixPath('/home/kkappler/.cache/iris_mt/mth5_test_data')
"""

import inspect
import pathlib
import zipfile

import mth5_test_data

init_file = inspect.getfile(mth5_test_data)
MTH5_TEST_DATA_DIR = pathlib.Path(init_file).parent

NIMS_TEST_DATA_DIR = MTH5_TEST_DATA_DIR / "nims"
ZEN_TEST_DATA_DIR = MTH5_TEST_DATA_DIR / "zen"
PHOENIX_TEST_DATA_DIR = MTH5_TEST_DATA_DIR / "phoenix"
METRONIX_TEST_DATA_DIR = MTH5_TEST_DATA_DIR / "metronix"
ASCII_TEST_DATA_DIR = MTH5_TEST_DATA_DIR / "usgs_ascii"

__all__ = [
    "MTH5_TEST_DATA_DIR",
    "NIMS_TEST_DATA_DIR",
    "ZEN_TEST_DATA_DIR",
    "PHOENIX_TEST_DATA_DIR",
    "METRONIX_TEST_DATA_DIR",
    "ASCII_TEST_DATA_DIR",
]

DATA_PATH_DICT = {
    "nims": NIMS_TEST_DATA_DIR,
    "zen": ZEN_TEST_DATA_DIR,
    "phoenix": PHOENIX_TEST_DATA_DIR,
    "metronix": METRONIX_TEST_DATA_DIR,
    "usgs_ascii": ASCII_TEST_DATA_DIR,
}


def get_zip_file(instrument: str) -> pathlib.Path:
    """
    Get the path to the mth5 test data zip file for a given instrument.

    Parameters
    ----------
    instrument : str
        Name of the instrument (e.g., 'nims', 'zen', 'phoenix', 'metronix').

    Returns
    -------
    pathlib.Path
        Path to the zip file for the specified instrument.
    """
    instrument = instrument.lower()
    zip_file_name = f"{instrument}_test_data.zip"
    if instrument in DATA_PATH_DICT:
        data_path = DATA_PATH_DICT[instrument]
    else:
        raise ValueError(
            f"Instrument '{instrument}' not found in test data directories."
        )
    zip_file_path = data_path / zip_file_name
    if zip_file_path.exists():
        return zip_file_path
    else:
        raise FileNotFoundError(f"Zip file for instrument '{instrument}' not found.")


def unzip_file(
    zip_path: str | pathlib.Path, extract_to: str | pathlib.Path | None = None
) -> pathlib.Path:
    """
    Unzip a zip file to a specified directory.

    Parameters
    ----------
    zip_path : str or pathlib.Path
        Path to the zip file to be extracted.
    extract_to : str or pathlib.Path
        Directory where the contents will be extracted.

    Returns
    -------
    pathlib.Path
        Path to the directory where files were extracted.
    """

    if extract_to is None:
        extract_to = pathlib.Path(zip_path).parent
    else:
        extract_to = pathlib.Path(extract_to)

    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(extract_to)

    return extract_to


def is_unzipped(
    zip_path: str | pathlib.Path, extract_to: str | pathlib.Path | None = None
) -> bool:
    """
    Check if a zip file has already been unzipped to a specified directory.

    Parameters
    ----------
    zip_path : str or pathlib.Path
        Path to the zip file.
    extract_to : str or pathlib.Path
        Directory where the contents would be extracted.

    Returns
    -------
    bool
        True if the contents have already been extracted, False otherwise.
    """

    zip_path = pathlib.Path(zip_path)
    if zip_path.suffix != ".zip":
        raise ValueError(f"The file {zip_path} is not a zip file.")
    if extract_to is None:
        extract_to = zip_path.parent
    else:
        extract_to = pathlib.Path(extract_to)

    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        for member in zip_ref.namelist():
            member_path = extract_to / member
            if not member_path.exists():
                return False
    return True


def get_test_data_path(instrument: str) -> pathlib.Path:
    """
    Get the path to the mth5 test data directory.

    Returns
    -------
    pathlib.Path
        Path to the mth5 test data directory.
    """
    zip_file_path = get_zip_file(instrument)
    if not is_unzipped(zip_file_path):
        return unzip_file(zip_file_path)
    else:
        return DATA_PATH_DICT[instrument.lower()]
