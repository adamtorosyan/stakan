import csv
import datetime
import os
from os.path import getsize, join


class Collector:
    """Class properties. In class properties we add directory we want to scan
    and path to our future database"""

    def __init__(self, directory):
        self.directory = directory
        absolute_path = os.path.dirname(__file__)
        parent_directory = os.path.dirname(absolute_path)
        relative_path = "data\data.csv"
        self.csv_path = os.path.join(parent_directory, relative_path)

    """Data collection in specified directopry. OS midule helps us to create nested list of desired info"""

    def get_info(self):
        data_info = []

        for root, _, files in os.walk(self.directory):
            for name in files:
                size = getsize(join(root, name))
                path = join(root, name)
                creation_date = str(
                    datetime.datetime.fromtimestamp(os.path.getctime(path))
                )
                modification_date = str(
                    datetime.datetime.fromtimestamp(os.path.getmtime(path))
                )

                data_info.append([name, size, path, creation_date, modification_date])

        return data_info

    """Now with csv module we are able to create a csv database of all files in directory"""

    def make_database(self):
        myFile = open(self.csv_path, "w", newline="", encoding="utf-8")
        writer = csv.writer(myFile)
        writer.writerow(["Name", "Size", "Path", "Creation_date", "Modification_date"])
        for data_list in self.get_info():
            writer.writerow(data_list)
        myFile.close()

    def get_csv_path(self):
        return self.csv_path


directory = "c:/"
a = Collector(directory)
print(a.get_csv_path())
a.make_database()
