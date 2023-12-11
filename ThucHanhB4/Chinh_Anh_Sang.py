import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog, ttk
from PIL import Image, ImageTk

# Biến lưu trữ đường dẫn ảnh đã chọn
selected_image_path = None

# Hàm để mở ảnh từ máy tính
def open_image():
    global selected_image_path
    file_path = filedialog.askopenfilename()
    if file_path:
        # Lưu đường dẫn ảnh đã chọn
        selected_image_path = file_path

        # Hiển thị ảnh đã mở
        show_image()

# Hàm để hiển thị ảnh
def show_image():
    global selected_image_path
    if selected_image_path:
        # Đọc ảnh từ đường dẫn
        img = cv2.imread(selected_image_path)

        # Chỉnh độ sáng theo giá trị từ thanh trượt
        brightness_value = brightness_scale.get()
        img = adjust_brightness(img, brightness_value)

        # Chuyển đổi ảnh sang định dạng RGB
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Hiển thị ảnh đã mở
        img_pil = Image.fromarray(img_rgb)
        img_pil.thumbnail((300, 300))  # Để hiển thị ảnh nhỏ hơn
        img_tk = ImageTk.PhotoImage(img_pil)
        image_label.config(image=img_tk)
        image_label.image = img_tk


# Hàm để chỉnh độ sáng của ảnh
def adjust_brightness(image, value):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    hsv[..., 2] = np.clip(hsv[..., 2] * value, 0, 255)
    return cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)


# Tạo cửa sổ Tkinter
root = tk.Tk()
root.geometry("500x450")
root.title("Hiển thị và chỉnh độ sáng ảnh")

# Nút để mở ảnh từ máy tính
open_image_button = tk.Button(root, text="Browse", command=open_image)
open_image_button.pack()

# Nhãn để hiển thị độ sáng
label_brightness = tk.Label(root, text="Brightness:")
label_brightness.pack()

# Thanh trượt để chỉnh độ sáng
brightness_scale = ttk.Scale(root, from_=0.1, to=2.0, orient="horizontal", length=200, command=lambda x: show_image())
brightness_scale.set(1.0)  # Giá trị mặc định là 1.0
brightness_scale.pack()

# Nhãn và hình ảnh để hiển thị ảnh đã mở
image_label = tk.Label(root)
image_label.pack()

# Biến lưu trữ đường dẫn ảnh đã chọn
selected_image_path = None

root.mainloop()
