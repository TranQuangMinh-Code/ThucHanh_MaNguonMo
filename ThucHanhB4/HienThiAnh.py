import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

# Hàm để mở ảnh từ máy tính
def open_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        # Hiển thị ảnh đã mở
        img = Image.open(file_path)
        img.thumbnail((400, 400))  # Để hiển thị ảnh nhỏ hơn
        img = ImageTk.PhotoImage(img)
        image_label.config(image=img)
        image_label.image = img

# Tạo cửa sổ Tkinter
root = tk.Tk()
root.title("Hiển thị ảnh")

# Nút để mở ảnh từ máy tính
open_image_button = tk.Button(root, text="Browse", command=open_image)
open_image_button.pack()

# Nhãn và hình ảnh để hiển thị ảnh đã mở
image_label = tk.Label(root)
image_label.pack()

# Biến lưu trữ đường dẫn ảnh đã chọn
selected_image_path = None

root.mainloop()