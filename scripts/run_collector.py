import sys

sys.path = ["C:/stakan"] + sys.path
from filesmeta.CommonMinion import CommonMinion
from filesmeta.DocMinion import DocMinion
from filesmeta.GRU import Gru
from filesmeta.ImgMinion import ImgMinion
from filesmeta.PdfMinion import PDFMinion
from staff.Collector import Collector


def process_and_create_database(directory):
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
    metadata = g.process_files(file_paths)

    c.make_database(metadata)


def main():
    directory = "C:/Users/WarSa/OneDrive/Рабочий стол/www.msu.ru"
    process_and_create_database(directory)


if __name__ == "__main__":
    main()
