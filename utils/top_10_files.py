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


def top_10_files(path):
    if updated_db(path):
        return "Update database!"
    else:
        df = pd.read_csv(path)
        top_10 = df.nlargest(10, "Size")
        return top_10


def show_top_10_files(path):
    if updated_db(path):
        return "Update database!"
    else:
        file_info = top_10_files(path)
        for i, (index, row) in enumerate(file_info.iterrows()):
            print(f'{i+1}) File "{row["Name"]}": size {row["Size"]} bytes')


show_top_10_files(path)
