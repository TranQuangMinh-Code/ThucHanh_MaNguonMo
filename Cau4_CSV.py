import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import csv
import matplotlib.pyplot as plt


class CSVViewerApp:
    def __init__(self, root):
        # Thiết lập cửa sổ
        self.root = root
        self.root.title("CSV Viewer")
        self.root.geometry("1000x400")  # Kích thước cửa sổ lớn hơn
        # Tạo Treeview để hiển thị dữ liệu
        self.tree = ttk.Treeview(self.root, show="headings")
        column_names = ["Mã lớp", "Số SV", "Loại A+", "Loại A", "Loại B+", "Loại B", "Loại C+", "Loại C",
                        "Loại D+", "Loại D", "Loại F", "L1", "L2", "TX1", "TX2", "Cuối kỳ"]
        self.tree["columns"] = tuple(range(1, 19))  # Số cột tương ứng với số cột trong file CSV
        self.tree.heading("#1", text="STT")  # Đặt tên cột 1 là "STT"
        for col, col_name in zip(range(2, 19), column_names):
            self.tree.heading(col, text=col_name)
            self.tree.column(col, width=50)
        # Hiển thị dữ liệu theo số lượng dòng
        self.tree.pack(expand=tk.YES, fill=tk.BOTH, side="top", pady=10)
        # Button để chọn file CSV
        self.select_button = tk.Button(self.root, text="Chọn File CSV", command=self.load_csv)
        self.select_button.pack(pady=10)
        # Button để hiển thị biểu đồ
        self.plot_button = tk.Button(self.root, text="Hiển thị biểu đồ", command=self.plot_chart)
        self.plot_button.pack(pady=10)

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
            self.tree.insert("", tk.END, values=(i + 1,) + tuple(row[1:]))

    def plot_chart(self):
        # Lấy dữ liệu từ Treeview
        data = []
        for child in self.tree.get_children():
            values = self.tree.item(child)["values"]
            data.append(values[2:11])  # Lấy các giá trị từ cột "Loại A+" đến "Loại F"

        # Tính toán số lượng sinh viên đạt từng loại điểm của mỗi mã lớp
        class_stats = {}
        for row in data:
            class_code = row[0]
            if class_code not in class_stats:
                class_stats[class_code] = [0] * 10  # Khởi tạo danh sách số lượng điểm là 0
            for i, count in enumerate(row[1:]):
                class_stats[class_code][i] += int(count)

        # Chuẩn bị dữ liệu cho biểu đồ
        labels = ["A+", "A", "B+", "B", "C+", "C", "D+", "D", "F"]
        class_codes = sorted(class_stats.keys())
        counts = [[class_stats[class_code][i] for class_code in class_codes] for i in range(9)]

        # Tạo biểu đồ cột
        fig, ax = plt.subplots()
        width = 0.1  # Độ rộng của mỗi cột
        x = range(len(class_codes))
        for i, count in enumerate(counts):
            ax.bar([xi + i * width for xi in x], count, width, label=labels[i])

        # Đặt tên cho trục x và trục y
        ax.set_xlabel("Mã lớp")
        ax.set_ylabel("Số lượng sinh viên")

        # Đặt tên cho các nhóm cột
        ax.set_xticks([xi + 4 * width for xi in x])
        ax.set_xticklabels(class_codes)

        # Hiển thị chú thích
        ax.legend()

        # Hiển thị biểu đồ
        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = CSVViewerApp(root)
    root.mainloop()