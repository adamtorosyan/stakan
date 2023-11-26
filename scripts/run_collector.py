import sys

sys.path = ["C:/stakan"] + sys.path
import concurrent.futures
import time

from filesmeta.CommonMinion import CommonMinion
from filesmeta.DocMinion import DocMinion
from filesmeta.GRU import Gru
from filesmeta.ImgMinion import ImgMinion
from filesmeta.PdfMinion import PDFMinion
from staff.Collector import Collector


def process_and_create_database_parallel(directory):
    c = Collector(directory)

    g = Gru()
    m1 = ImgMinion()
    m2 = PDFMinion()
    m3 = DocMinion()
    m4 = CommonMinion()
    g.add_minion(m1)
    g.add_minion(m2)
    g.add_minion(m3)
    g.add_minion(m4)

    file_paths = c.get_path()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        metadata = list(executor.map(g.process_file, file_paths))

    c.make_database(metadata)


def main_parallel():
    directory = r"C:\Users\WarSa\OneDrive\Рабочий стол\www.msu.ru"
    start_time = time.time()
    process_and_create_database_parallel(directory)
    elapsed_time = time.time() - start_time
    print(f"Elapsed Time: {elapsed_time} seconds")


if __name__ == "__main__":
    main_parallel()
