import tkinter as tk
import numpy as np
import pandas as pd
from tkinter import filedialog
from tkinter import ttk
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from tkinter import messagebox
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
        self.predict_button = tk.Button(self.root, text="Dự Đoán và Hiển Thị Kết Quả", command=self.HoiQuyTuyenTinh)
        self.predict_button.pack(pady=10)

    def load_csv(self):
        # Mở hộp thoại để chọn file CSV
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])

        # Kiểm tra xem người dùng đã chọn một file chưa
        if file_path:
            # Đọc dữ liệu từ file CSV
            data = self.read_csv(file_path)

            # Hiển thị dữ liệu lên Treeview
            self.display_data(data)
    def HoiQuyTuyenTinh(self):
        # Đọc dữ liệu từ file CSV
        data = pd.read_csv('Student_Performance.csv')

        # Chia dữ liệu thành dữ liệu đào tạo và dữ liệu kiểm tra
        X = data[['Hours Studied', 'Previous Scores', 'Extracurricular Activities', 'Sleep Hours',
                  'Sample Question Papers Practiced']]
        y = data['Performance Index']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

        # Tạo mô hình hồi quy tuyến tính
        model = LinearRegression()

        # Đào tạo mô hình trên dữ liệu đào tạo
        model.fit(X_train, y_train)

        # Dự đoán trên dữ liệu kiểm tra
        y_pred = model.predict(X_test)

        # Đánh giá mô hình
        mae = metrics.mean_absolute_error(y_test, y_pred)
        mse = metrics.mean_squared_error(y_test, y_pred)
        rmse = np.sqrt(mse)
        coefficients = model.coef_

        # Hiển thị kết quả trong cửa sổ messagebox
        result_message = f"Độ Lệch Trung Bình Tuyệt Đối: {mae}\nĐộ Lệch Bình Phương Trung Bình: {mse}\nĐộ Lệch Chuẩn Bình Phương Gốc: {rmse}\nHệ Số: {coefficients}"
        messagebox.showinfo("Kết Quả Đánh Giá Mô Hình", result_message)

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
