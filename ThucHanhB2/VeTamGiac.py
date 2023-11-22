import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt

def draw_triangle():
    a = float(entry_a.get())
    b = float(entry_b.get())
    c = float(entry_c.get())

    # Kiểm tra tính hợp lệ của 3 cạnh tam giác
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        result_label.config(text="Tam giác không hợp lệ!")
        return

    # Tính toán tọa độ các đỉnh tam giác
    A = np.array([0, 0])
    B = np.array([c, 0])
    cos_angle = (c**2 + a**2 - b**2) / (2 * a * c)
    sin_angle = np.sqrt(1 - cos_angle**2)
    height = a * sin_angle
    C = np.array([a * cos_angle, height])

    # Tính chu vi và diện tích tam giác
    perimeter = a + b + c
    s = perimeter / 2  # Nửa chu vi
    area = np.sqrt(s * (s - a) * (s - b) * (s - c))

    # Vẽ tam giác
    plt.figure()
    plt.gca().set_aspect('equal', adjustable='box')
    plt.plot([A[0], B[0]], [A[1], B[1]], 'b-')
    plt.plot([B[0], C[0]], [B[1], C[1]], 'b-')
    plt.plot([C[0], A[0]], [C[1], A[1]], 'b-')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Vẽ tam giác')

    # Hiển thị chu vi và diện tích trên biểu đồ
    plt.text(0.5 * (A[0] + B[0]), -1.0, f"Chu vi: {perimeter:.2f}", ha='center', va='top')
    plt.text(0.5 * (A[0] + B[0]), -1.3, f"Diện tích: {area:.2f}", ha='center', va='top')

    plt.grid(True)
    plt.show()

# Tạo cửa sổ giao diện tkinter
window = tk.Tk()
window.title("Vẽ tam giác")
window.geometry("200x200")

# Tạo các thành phần giao diện
label_a = tk.Label(window, text="Cạnh a:")
label_a.pack()
entry_a = tk.Entry(window)
entry_a.pack()

label_b = tk.Label(window, text="Cạnh b:")
label_b.pack()
entry_b = tk.Entry(window)
entry_b.pack()

label_c = tk.Label(window, text="Cạnh c:")
label_c.pack()
entry_c = tk.Entry(window)
entry_c.pack()

draw_button = tk.Button(window, text="Vẽ tam giác", command=draw_triangle)
draw_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

# Chạy giao diện tkinter
window.mainloop()