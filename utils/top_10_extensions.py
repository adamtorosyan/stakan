import datetime
import os
import sys
from collections import Counter
from os.path import splitext

sys.path = ["C:/stakan"] + sys.path
import pandas as pd
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


def get_ex(path):
    if updated_db(path):
        return "Update database!"
    else:
        df = pd.read_csv(path)
        extensions = []
        for i in df["Path"]:
            ex = splitext(i)[1]
            if not ex:
                extensions.append(None)
            else:
                if ex.startswith("."):
                    extensions.append(ex[1:])
        return extensions


def count_ex(path):
    if updated_db(path):
        return "Update database!"
    else:
        extensions = get_ex(path)
        top = Counter(extensions).most_common(10)
        return top


def show_top_ex(path):
    if updated_db(path):
        return "Update database!"
    else:
        top = count_ex(path)
        for i in range(len(top)):
            print(f"{i+1}) Extension {top[i][0]} in an amount of {top[i][1]} pieces")


show_top_ex(path)
