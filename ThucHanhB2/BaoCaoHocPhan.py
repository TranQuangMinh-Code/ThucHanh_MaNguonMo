import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import csv

class CSVViewerApp:
    def __init__(self, root):
        # Thiết lập cửa sổ
        self.root = root
        self.root.title("CSV Viewer")
        self.root.geometry("1200x400")
        # Tạo Treeview để hiển thị dữ liệu
        self.tree = ttk.Treeview(self.root, show="headings")
        column_names = ["Mã lớp", "Số SV", "Loại A+", "Loại A", "Loại B+", "Loại B", "Loại C+", "Loại C",
                        "Loại D+", "Loại D", "Loại F", "L1", "L2", "TX1", "TX2", "Cuối kỳ"]
        self.tree["columns"] = tuple(range(1, 18))  # Số cột tương ứng với số cột trong file CSV
        self.tree.heading("#1", text="STT")  # Đặt tên cột 1 là "STT"
        for col, col_name in zip(range(2, 18), column_names):
            self.tree.heading(col, text=col_name)
            self.tree.column(col, width=80)
        # Hiển thị dữ liệu theo số lượng dòng
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
        with open(file_path, "r", encoding="utf-8-sig") as file:
            csv_reader = csv.reader(file, delimiter=";")
            headers = next(csv_reader)  # Lấy tiêu đề từ dòng đầu tiên
            for row in csv_reader:
                data.append(row)
        return data

    def display_data(self, data):
        # Xóa dữ liệu cũ trong Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)
        # Hiển thị dữ liệu lên Treeview
        for i, row in enumerate(data):  # Dùng enumerate để có thể lấy được số thứ tự
            self.tree.insert("", tk.END, values=(i+1,) + tuple(row[1:]))

if __name__ == "__main__":
    root = tk.Tk()
    app = CSVViewerApp(root)
    root.mainloop()
