import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import csv

class CSVViewerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CSV Viewer")
        self.root.geometry("850x600")
        # Tạo Treeview để hiển thị dữ liệu
        self.tree = ttk.Treeview(self.root)
        self.tree["columns"] = ("#0", "Column 1", "Column 2", "Column 3","Column 4","Column 5")
        self.tree.column("#0", width=0, stretch=tk.NO)  # Ẩn cột đầu tiên
        self.tree.column("Column 1", anchor=tk.W, width=100)
        self.tree.column("Column 2", anchor=tk.W, width=100)
        self.tree.column("Column 3", anchor=tk.W, width=100)
        self.tree.column("Column 4", anchor=tk.W, width=100)
        self.tree.column("Column 5", anchor=tk.W, width=100)
        self.tree.pack(expand=tk.YES, fill=tk.BOTH, side="top", pady=10)

        # Button để chọn file CSV
        self.select_button = tk.Button(self.root, text="Chọn File CSV", command=self.load_csv)
        self.select_button.pack(pady=10)

    def load_csv(self):
        # Mở hộp thoại để chọn file CSV
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])

        # Kiểm tra xem người dùng đã chọn một file chưa
        if file_path:
            # Đọc dữ liệu từ file CSV
            data = self.read_csv(file_path)

            # Hiển thị dữ liệu lên Treeview
            self.display_data(data)

    def read_csv(self, file_path):
        data = []

        with open(file_path, "r") as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                data.append(row)

        return data

    def display_data(self, data):
        # Xóa dữ liệu cũ trong Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Hiển thị dữ liệu lên Treeview
        for row in data:
            self.tree.insert("", tk.END, values=row)

if __name__ == "__main__":
    root = tk.Tk()
    app = CSVViewerApp(root)
    root.mainloop()
