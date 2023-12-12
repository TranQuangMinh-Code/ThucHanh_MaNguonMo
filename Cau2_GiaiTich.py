import tkinter as tk
from tkinter import Entry, Label, Button, Frame, messagebox
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt


class QuadraticEquationSolverApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Giải PTB2: Ax^2 + Bx + C = 0")
        self.root.geometry("350x150")

        self.equation_frame = Frame(root)
        self.equation_frame.pack(pady=20)

        self.a_label = Label(self.equation_frame, text="A:")
        self.a_label.pack(side=tk.LEFT, padx=10)

        self.a_entry = Entry(self.equation_frame, width=10)
        self.a_entry.pack(side=tk.LEFT)

        self.b_label = Label(self.equation_frame, text="B:")
        self.b_label.pack(side=tk.LEFT, padx=10)

        self.b_entry = Entry(self.equation_frame, width=10)
        self.b_entry.pack(side=tk.LEFT)

        self.c_label = Label(self.equation_frame, text="C:")
        self.c_label.pack(side=tk.LEFT, padx=10)

        self.c_entry = Entry(self.equation_frame, width=10)
        self.c_entry.pack(side=tk.LEFT)

        self.solve_button = Button(root, text="Giải và Vẽ", command=self.solve_and_plot)
        self.solve_button.pack()

        self.result_label = Label(root, text="")
        self.result_label.pack(pady=10)

    def solve_and_plot(self):
        A = float(self.a_entry.get())
        B = float(self.b_entry.get())
        C = float(self.c_entry.get())

        x = np.linspace(-10, 10, 400)
        y = A * x ** 2 + B * x + C

        plt.plot(x, y)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title(f'Biểu đồ của phương trình: {A}*x^2 + {B}*x + {C}')
        plt.grid()
        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)

        if A == 0:
            if B == 0:
                if C == 0:
                    self.result_label.config(text="Vô số nghiệm")
                else:
                    self.result_label.config(text="Không có nghiệm")
            else:
                x_solution = -C / B
                self.result_label.config(text=f"Nghiệm duy nhất: x = {x_solution}")
        else:
            discriminant = B ** 2 - 4 * A * C
            if discriminant > 0:
                x1 = (-B + np.sqrt(discriminant)) / (2 * A)
                x2 = (-B - np.sqrt(discriminant)) / (2 * A)
                self.result_label.config(text=f"Hai nghiệm phân biệt: x1 = {x1}, x2 = {x2}")
            elif discriminant == 0:
                x_solution = -B / (2 * A)
                self.result_label.config(text=f"Nghiệm kép: x = {x_solution}")
            else:
                self.result_label.config(text="Phương trình không có nghiệm thực")

        plt.show()


if __name__ == "__main__":
    root = tk.Tk()
    app = QuadraticEquationSolverApp(root)
    root.mainloop()