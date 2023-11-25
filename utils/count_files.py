import sqlite3
import sys

import pandas as pd

sys.path = ["C:/stakan"] + sys.path
from staff.Collector import Collector

directory = "c:/"
a = Collector(directory)
db_path = a.get_sqlite_path()


def count_files(path):
    if a.updated_db():
        return "Update database!"
    else:
        connection = sqlite3.connect(path)
        query = "SELECT COUNT(*) FROM metadata"
        result = connection.execute(query).fetchone()[0]
        connection.close()
        return f"Amount of files on computer: {result}"


print(count_files(db_path))
