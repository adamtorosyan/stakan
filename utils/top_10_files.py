import sys

import pandas as pd

sys.path = ["C:/stakan"] + sys.path
from staff.Collector import Collector

directory = "c:/"
a = Collector(directory)
path = a.get_csv_path()


def top_10_files(path):
    if a.updated_db():
        return "Update database!"
    else:
        df = pd.read_csv(path)
        top_10 = df.nlargest(10, "File Size")
        return top_10


def show_top_10_files(path):
    if a.updated_db():
        yield "Update database!"
    else:
        file_info = top_10_files(path)
        for i, (_, row) in enumerate(file_info.iterrows()):  # type: ignore
            yield (f'{i+1}) File "{row["File Name"]}": size {row["File Size"]} bytes')


for file in show_top_10_files(path):
    print(file)
