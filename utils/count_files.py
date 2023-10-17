import sys

import pandas as pd

sys.path = ["C:/stakan"] + sys.path

from staff.Collector import Collector

directory = "c:/"
a = Collector(directory)
path = a.get_csv_path()


def count_files(path):
    if a.updated_db():
        return "Update database!"
    else:
        df = pd.read_csv(path)
        return f"Amount of files on computer: {len(df)}"


print(count_files(path))
