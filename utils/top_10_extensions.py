import sqlite3
import sys

sys.path = ["C:/stakan"] + sys.path
from staff.Collector import Collector

directory = "c:/"
a = Collector(directory)
db_path = a.get_sqlite_path()


def show_top_ex(path):
    if a.updated_db():
        return "Update database!"
    else:
        connection = sqlite3.connect(path)
        query = """
            SELECT SUBSTR(file_name, INSTR(file_name, '.') + 1) AS extension, COUNT(*) 
            FROM metadata 
            GROUP BY extension 
            ORDER BY COUNT(*) DESC 
            LIMIT 10
        """
        result = connection.execute(query).fetchall()
        connection.close()
        return result


for i, (extension, count) in enumerate(show_top_ex(db_path)):  # type: ignore
    print(f"{i + 1}) Extension {extension} in an amount of {count} pieces")
