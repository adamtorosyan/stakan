import datetime
import os
import sys

import pandas as pd

sys.path = ["C:/stakan"] + sys.path

from staff.Collector import Collector

directory = "c:/"
a = Collector(directory)
path = a.get_csv_path()


def updated_db(path):
    time_diff = datetime.datetime.fromtimestamp(
        os.path.getmtime(path)
    ) - datetime.datetime.fromtimestamp(os.path.getctime(path))
    if time_diff.days <= 2:
        return False
    else:
        return True


def count_files(path):
    if updated_db(path):
        return "Update database!"
    else:
        df = pd.read_csv(path)
        return f"Amount of file on computer: {len(df)}"


print(count_files(path))
