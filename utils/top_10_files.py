import sqlite3
import sys

import pandas as pd

sys.path = ["C:/stakan"] + sys.path
from staff.Collector import Collector

directory = "c:/"
a = Collector(directory)
db_path = a.get_sqlite_path()


def show_top_10_files(path):
    if a.updated_db():
        yield "Update database!"
    else:
        connection = sqlite3.connect(path)
        query = "SELECT * FROM metadata ORDER BY file_size DESC LIMIT 10"
        result = connection.execute(query).fetchall()
        connection.close()
        for i, row in enumerate(result):  # type: ignore
            yield (f'{i+1}) File "{row[1]}": size {row[2]} bytes')


for file in show_top_10_files(db_path):
    print(file)
