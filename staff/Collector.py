import csv
import datetime
import os
from os.path import join


class Collector:
    """Class properties. In class properties we add directory we want to scan
    and path to our future database"""

    def __init__(self, directory):
        self.directory = directory
        absolute_path = os.path.dirname(__file__)
        parent_directory = os.path.dirname(absolute_path)
        relative_path = "data\\data.csv"
        self.csv_path = os.path.join(parent_directory, relative_path)

    """Data collection in specified directory. OS module helps us to create nested list of desired info"""

    def get_path(self):
        for root, _, files in os.walk(self.directory):
            for name in files:
                path = join(root, name)
                yield path

    """Now with csv module we are able to create a csv database of all files in directory"""

    def make_database(self, data):
        # Determine all possible keys from the data
        all_keys = set()
        for entry in data:
            all_keys.update(entry.keys())

        # Define a common set of keys for the CSV columns
        csv_columns = [
            "File Name",
            "File Size",
            "File Path",
            "Creation Date",
            "Modification Date",
            "Pages",
            "Title",
            "Author",
            "Subject",
            "Keywords",
            "Width",
            "Height",
            "Format",
            "Mode",
            "Alpha Channel",
            "Orientation",
            "Bits per Channel",
            "Compression",
            "Enhancement",
            "GPS Coordinates",
            "Camera Model",
            "Camera Brand",
            "Date Taken",
        ]

        with open(self.csv_path, "w", newline="", encoding="utf-8") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=csv_columns)
            writer.writeheader()

            for entry in data:
                unified_entry = {
                    key: entry.get(key, None) for key in csv_columns if key != "error"
                }
                writer.writerow(unified_entry)

        print("CSV file 'data.csv' has been created.")

    def get_csv_path(self):
        return self.csv_path

    def updated_db(self):
        time_diff = datetime.datetime.now() - datetime.datetime.fromtimestamp(
            os.path.getmtime(self.csv_path)
        )
        if time_diff.days <= 2:
            return False
        else:
            return True
