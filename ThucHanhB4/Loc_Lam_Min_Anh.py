import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def open_image():
    global selected_image_path
    selected_image_path = filedialog.askopenfilename()
    if selected_image_path:
        img = Image.open(selected_image_path)
        img.thumbnail((400, 400))
        img = ImageTk.PhotoImage(img)
        image_label.config(image=img)
        image_label.image = img

def smooth_image():
    global selected_image_path
    if selected_image_path:
        # Đọc ảnh từ đường dẫn
        image = cv2.imread(selected_image_path)

        # Kiểm tra xem ảnh có được đọc thành công không
        if image is not None:
            # Tạo kernel cho filter2D (ví dụ: kernel là bộ lọc trung bình 5x5)
            kernel = np.ones((5, 5), np.float32) / 25
            smoothed_image = cv2.filter2D(image, -1, kernel)

            # Hiển thị ảnh đã làm mịn
            smoothed_img = cv2.cvtColor(smoothed_image, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(smoothed_img)
            img.thumbnail((400, 400))
            img = ImageTk.PhotoImage(img)
            image_label.config(image=img)
            image_label.image = img
        else:
            print("Error: Failed to load the image.")
    else:
        print("Error: No image selected.")


# Tạo cửa sổ Tkinter
root = tk.Tk()
root.title("Hiển thị và Lọc Mịn Ảnh")

# Nút để mở ảnh từ máy tính
open_image_button = tk.Button(root, text="Browse", command=open_image)
open_image_button.pack()

# Nút để làm mịn ảnh
smooth_image_button = tk.Button(root, text="Lọc Mịn Ảnh", command=smooth_image)
smooth_image_button.pack()

# Nhãn và hình ảnh để hiển thị ảnh đã mở hoặc đã làm mịn
image_label = tk.Label(root)
image_label.pack()

# Biến lưu trữ đường dẫn ảnh đã chọn
selected_image_path = None

root.mainloop()
