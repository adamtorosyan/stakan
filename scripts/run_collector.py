import os
import sys

sys.path = ["C:/stakan"] + sys.path
from staff.Collector import Collector


def main():
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(project_root)
    collector = Collector(directory="c:/")
    collector.make_database()


if __name__ == "__main__":
    main()
