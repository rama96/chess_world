import warnings
from pathlib import Path
import os
import pandas as pd

warnings.simplefilter(action="ignore", category=FutureWarning)
# The intention is to remove this warning:
#
# /env/lib/python3.8/site-packages/pandas/core/frame.py:1482: FutureWarning: Using short name for 'orient' is deprecated. Only the options: ('dict', list, 'series', 'split', 'records', 'index') will be used in a future version. Use one of the above to silence this warning.
#  warnings.warn(

warnings.simplefilter(action="ignore", category=pd.errors.PerformanceWarning)
# your performance may suffer as PyTables will pickle object types that it cannot


env = os.getenv("chess_world_ENV", "production").lower()
if env.lower() != "production":
    print(f"\n***** ENVIROMENT: {env.upper()} *****")


def create_directory_if_not_exists(path: Path) -> None:
    if not path.is_dir():
        try:
            path.mkdir()
        except Exception as e:
            print(e)


DIR_PACKAGE = Path(__file__).resolve().parent  # ../chess_world/chess_world
DIR_BASE = DIR_PACKAGE.parent  # ../chess_world/

# ../chess_world/DATA
DIR_DATA = DIR_BASE.joinpath("DATA")

# ../chess_world/DATA/LOG
DIR_LOG = DIR_DATA.joinpath("LOG")

# ../chess_world/DATA/RECOMMENDATIONS
DIR_RECOMMENDATIONS = DIR_DATA.joinpath("RECOMMENDATIONS")

# ../chess_world/DATA/UPLOAD
DIR_UPLOAD = DIR_DATA.joinpath("UPLOAD")

# ../chess_world/DATA/REPORTING
DIR_REPORTING = DIR_DATA.joinpath("REPORTING")

# ../chess_world/DATA/DEBUG
DIR_DEBUG = DIR_DATA.joinpath("DEBUG")


create_directory_if_not_exists(DIR_LOG)
create_directory_if_not_exists(DIR_DATA)
create_directory_if_not_exists(DIR_RECOMMENDATIONS)
create_directory_if_not_exists(DIR_UPLOAD)
create_directory_if_not_exists(DIR_REPORTING)
create_directory_if_not_exists(DIR_DEBUG)


name = "chess_world"


pd.set_option("display.max_columns", 500)
pd.set_option("display.width", 1000)
pd.set_option("display.max_colwidth", 25)
pd.options.display.float_format = "{:.2f}".format
pd.options.mode.chained_assignment = None


import os


