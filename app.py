import datetime
import os
import sqlite3

from flask import Flask, render_template

from staff.Collector import Collector

app = Flask(__name__)
directory = "C:/stakan"
a = Collector(directory)
db_path = a.get_sqlite_path()


@app.route("/")
def index():
    last_indexed_time = datetime.datetime.fromtimestamp(
        os.path.getmtime(db_path)
    ).strftime("%Y-%m-%d %H:%M:%S")

    total_files_count = count_files(db_path)

    return render_template(
        "index.html",
        last_indexed_time=last_indexed_time,
        total_files_count=total_files_count,
    )


@app.route("/extensions_statistics")
def extensions_statistics():
    if a.updated_db():
        return "Update database!"

    connection = sqlite3.connect(db_path)
    query = """
        SELECT SUBSTR(file_name, INSTR(file_name, '.') + 1) AS extension, COUNT(*) 
        FROM metadata 
        GROUP BY extension 
        ORDER BY COUNT(*) DESC 
    """
    result = connection.execute(query).fetchall()
    connection.close()

    return render_template("extensions_statistics.html", statistics=result)


@app.route("/top_10_size_statistics")
def top_10_size_statistics():
    if a.updated_db():
        return "Update database!"

    connection = sqlite3.connect(db_path)
    query = "SELECT * FROM metadata ORDER BY file_size DESC LIMIT 10"
    result = connection.execute(query).fetchall()
    connection.close()

    return render_template("top_10_size_statistics.html", statistics=result)


def count_files(path):
    connection = sqlite3.connect(path)
    query = "SELECT COUNT(*) FROM metadata"
    result = connection.execute(query).fetchone()[0]
    connection.close()
    return result


if __name__ == "__main__":
    app.run(debug=True)
