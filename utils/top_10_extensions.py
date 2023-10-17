import sys
from collections import Counter
from os.path import splitext

sys.path = ["C:/stakan"] + sys.path
import pandas as pd
from staff.Collector import Collector

directory = "c:/"
a = Collector(directory)
path = a.get_csv_path()


def show_top_ex(path):
    if a.updated_db():
        return "Update database!"
    else:
        df = pd.read_csv(path)
        extensions = df["File Path"].apply(
            lambda x: x.split(".")[-1] if "." in x else "absent"
        )
        top = extensions.value_counts().head(10)
        return top


for i, (extension, count) in enumerate(show_top_ex(path).items()):  # type: ignore
    print(f"{i + 1}) Extension {extension} in an amount of {count} pieces")
