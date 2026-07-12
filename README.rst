A repository for testing data used in the MTH5 project.

Includes:

- NIMS [.bin] 
- ZEN [.z3d]
- Metronix (from https://cloud.geo-metronix.de/s/WCiDGispeeiQS9G?dir=/small_example)
  - ATSS files
- Phoenix sample data
  - MTU-5C [.td_]
  - MTUA [ .ts, .tbl]
- LEMI
  - LEMI 424 [.txt]
  - LEMI 423 [.b423]
- MiniSEED + StationXML [.mseed, .xml]
- USGS ASCII [.ascii]

Installation
-------------------------------

.. code-block::

  # Install in development mode (recommended for testing)
  pip install -e .

  # Install with development dependencies
  pip install -e ".[dev]"

  # Install from repository directly
  pip install git+https://github.com/kujaku11/mth5_test_data.git

How To Add Data
----------------------

The suggested way to add data is to pull or fork the repository, add your data, push, then create a pull request.

1. Clone the repository or fork

.. code-block::  

  git clone https://github.com/IAGA-DVI-DataStandards/mth5_test_data.git

2. Add your data 

- Identify the data you want to add.  Please keep the data small (<50 MB).
- Create a zip file called "{my_data_type}_test_data.zip"
- Create a new folder in `mth5_test_data/mth5_test_data/{new_folder_data_type}`
- Place the zip file in the new folder `mth5_test_data/mth5_test_data/{new_folder_data_type}/{my_data_type}_test_data.zip`

3. Commit Changes

When you commit a change include a complete message in the commit like "Adding new data {my_data} that includes an edge case of x..."

`git commit -a -m "Adding new data {my_data} that includes an edge case of x..."`

4. Add path the `__init__.py`

Add 

.. code-block:: python

  # Add path for you new data
  NEWDATA_TEST_DATA_DIR = MTH5_TEST_DATA_DIR / "new_data_type"

  # add to the __all__ to import directly
  __all__ = [
      ...
      "NEWDATA_TEST_DATA"
  ]

  # add path to the dictionary so it can be found by the methods.
  DATA_PATH_DICT = {
      ...
      "new_data_type": NEWDATA_TEST_DATA_DIR,
  }

5. Push Commits

Push to either your fork or repository

6. Create a Pull Request

Use the tools on the git web page to create a Pull Request
Add some information into the pull request about what kind of data is being added and why it should be added.
The admin of the repository will then review and approve the merge.








