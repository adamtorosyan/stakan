import datetime
import os
import sqlite3
import tkinter as tk
from tkinter import messagebox

from staff.Collector import Collector


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Stakan file statistics")
        self.directory = "C:/stakan"
        self.a = Collector(self.directory)
        self.db_path = self.a.get_sqlite_path()

        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        self.menu_bar.add_command(
            label="Статистика по расширениям", command=self.show_extensions_statistics
        )

        self.menu_bar.add_command(
            label="Статистика ТОП-10 по размеру",
            command=self.show_top_10_size_statistics,
        )

        total_files_label = tk.Label(root, text=f"Всего файлов: {self.count_files()}")
        total_files_label.pack()

        last_indexed_label = tk.Label(
            root, text=f"Дата последней индексации: {self.last_indexed_time()}"
        )
        last_indexed_label.pack()

    def show_extensions_statistics(self):
        if self.a.updated_db():
            messagebox.showinfo("Update Database", "Необходимо обновить базу данных.")
            return

        connection = sqlite3.connect(self.db_path)
        query = """
            SELECT SUBSTR(file_name, INSTR(file_name, '.') + 1) AS extension, COUNT(*) 
            FROM metadata 
            GROUP BY extension 
            ORDER BY COUNT(*) DESC 
        """
        result = connection.execute(query).fetchall()
        connection.close()

        self.show_statistics(result, "Статистика по расширениям")

    def show_top_10_size_statistics(self):
        if self.a.updated_db():
            messagebox.showinfo("Update Database", "Необходимо обновить базу данных.")
            return

        connection = sqlite3.connect(self.db_path)
        query = "SELECT * FROM metadata ORDER BY file_size DESC LIMIT 10"
        result = connection.execute(query).fetchall()
        connection.close()

        self.show_statistics(result, "Статистика ТОП-10 по размеру")

    def show_statistics(self, data, title):
        statistics_window = tk.Toplevel(self.root)
        statistics_window.title(title)

        listbox = tk.Listbox(statistics_window, width=40, height=15)
        listbox.pack()

        for item in data:
            listbox.insert(tk.END, f"{item[0]}: {item[1]}")

    def count_files(self):
        connection = sqlite3.connect(self.db_path)
        query = "SELECT COUNT(*) FROM metadata"
        result = connection.execute(query).fetchone()[0]
        connection.close()
        return result

    def last_indexed_time(self):
        last_indexed_time = datetime.datetime.fromtimestamp(
            os.path.getmtime(self.db_path)
        ).strftime("%Y-%m-%d %H:%M:%S")
        return last_indexed_time


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
