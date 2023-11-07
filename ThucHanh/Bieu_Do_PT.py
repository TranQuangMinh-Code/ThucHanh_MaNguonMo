import tkinter as tk
from tkinter import Entry, Label, Button, Text, Scrollbar, messagebox
import numpy as np
from sympy import *
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def tinh_integral():
    try:
        phuong_trinh = phuong_trinh_entry.get()
        x = symbols('x')
        integral = integrate(phuong_trinh, x)
        ket_qua_integral.delete(1.0, tk.END)
        ket_qua_integral.insert(tk.END, str(integral))
    except Exception as e:
        messagebox.showerror('Lỗi', f'Có lỗi xảy ra: {str(e)}')

def ve_bieu_do():
    try:
        phuong_trinh = phuong_trinh_entry.get()
        x = symbols('x')
        f = lambdify(x, phuong_trinh, 'numpy')
        x_values = np.linspace(-10, 10, 400)
        y_values = f(x_values)

        fig = Figure(figsize=(5, 4), dpi=100)
        ax = fig.add_subplot(111)
        ax.plot(x_values, y_values)
        ax.set_xlabel('x')
        ax.set_ylabel('f(x)')
        ax.set_title('Biểu đồ hàm số')

        canvas = FigureCanvasTkAgg(fig, master=app)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack()
    except Exception as e:
        messagebox.showerror('Lỗi', f'Có lỗi xảy ra: {str(e)}')

app = tk.Tk()
app.title("Phần mềm Giải Tích")

phuong_trinh_label = Label(app, text="Nhập phương trình (ví dụ: x**2 + 3*x - 2):")
phuong_trinh_label.pack()

phuong_trinh_entry = Entry(app)
phuong_trinh_entry.pack()

tinh_button = Button(app, text="Tính Integral", command=tinh_integral)
tinh_button.pack()

ket_qua_integral_label = Label(app, text="Kết quả tích phân:")
ket_qua_integral_label.pack()

ket_qua_integral = Text(app, height=5, width=40)
ket_qua_integral.pack()

ve_button = Button(app, text="Vẽ biểu đồ", command=ve_bieu_do)
ve_button.pack()

app.mainloop()
