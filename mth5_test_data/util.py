"""
allows the path to this repo to be imported, for example:
>>> from mth5_test_data.util import MTH5_TEST_DATA_DIR
>>> MTH5_TEST_DATA_DIR
PosixPath('/home/kkappler/.cache/iris_mt/mth5_test_data')
"""
import inspect
import pathlib

import mth5_test_data

init_file = inspect.getfile(mth5_test_data)
MTH5_TEST_DATA_DIR = pathlib.Path(init_file).parent.parent
