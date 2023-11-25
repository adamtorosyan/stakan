import csv
import datetime
import json
import os
import sqlite3
from os.path import join


class Collector:
    def __init__(self, directory):
        self.directory = directory
        absolute_path = os.path.dirname(__file__)
        parent_directory = os.path.dirname(absolute_path)
        relative_path = "data\\data.db"
        self.sqlite_path = os.path.join(parent_directory, relative_path)

    def get_path(self):
        for root, _, files in os.walk(self.directory):
            for name in files:
                path = join(root, name)
                yield path

    def make_database(self, data):
        connection = sqlite3.connect(self.sqlite_path)
        cursor = connection.cursor()

        # Create a table
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS metadata (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                file_name TEXT,
                file_size INTEGER,
                file_path TEXT,
                creation_date TEXT,
                modification_date TEXT,
                pages INTEGER,
                title TEXT,
                author TEXT,
                subject TEXT,
                keywords TEXT,
                width INTEGER,
                height INTEGER,
                format TEXT,
                mode TEXT,
                channels TEXT,  -- Changed to TEXT
                bit_depth INTEGER,
                compression TEXT,
                icc_profile TEXT,
                orientation TEXT,
                exif_data TEXT,
                error TEXT
            )
        """
        )

        # Insert data into the table
        for entry in data:
            # Convert the 'channels' list to a JSON-formatted string
            entry["Channels"] = json.dumps(entry.get("Channels"))

            cursor.execute(
                """
                INSERT INTO metadata (
                    file_name, file_size, file_path, creation_date, modification_date, pages,
                    title, author, subject, keywords, width, height, format, mode,
                    channels, bit_depth, compression, icc_profile, orientation, exif_data, error
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
                (
                    entry.get("File Name"),
                    entry.get("File Size"),
                    entry.get("File Path"),
                    entry.get("Creation Date"),
                    entry.get("Modification Date"),
                    entry.get("Pages"),
                    entry.get("Title"),
                    entry.get("Author"),
                    entry.get("Subject"),
                    entry.get("Keywords"),
                    entry.get("Width"),
                    entry.get("Height"),
                    entry.get("Format"),
                    entry.get("Mode"),
                    entry.get("Channels"),
                    entry.get("Bit Depth"),
                    entry.get("Compression"),
                    entry.get("ICC Profile"),
                    entry.get("Orientation"),
                    entry.get("EXIF Data"),
                    entry.get("error"),
                ),
            )

        connection.commit()
        connection.close()

        print("SQLite database 'data.db' has been created and populated.")

    def get_sqlite_path(self):
        return self.sqlite_path

    def updated_db(self):
        time_diff = datetime.datetime.now() - datetime.datetime.fromtimestamp(
            os.path.getmtime(self.sqlite_path)
        )
        if time_diff.days <= 2:
            return False
        else:
            return True
