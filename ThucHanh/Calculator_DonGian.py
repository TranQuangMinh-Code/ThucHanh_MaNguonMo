import tkinter as tk


# Hàm tính toán
def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Lỗi")


# Hàm thêm số hoặc phép toán vào biểu thức hiện tại
def add_to_expression(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)


# Hàm xóa kí tự cuối cùng
def delete_last_char():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])


# Hàm reset máy tính
def clear():
    entry.delete(0, tk.END)


# Tạo cửa sổ giao diện
window = tk.Tk()
window.title("Máy Tính Đơn Giản")

# Tạo ô nhập biểu thức
entry = tk.Entry(window, width=30)
entry.grid(row=0, column=0, columnspan=4)

# Tạo các nút số và phép toán
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'AC', 'DEL'
]

row, col = 1, 0
for button in buttons:
    if button == 'AC':
        tk.Button(window, text=button, width=5, height=2, command=clear).grid(row=row, column=col)
    elif button == 'DEL':
        tk.Button(window, text=button, width=5, height=2, command=delete_last_char).grid(row=row, column=col)
    else:
        tk.Button(window, text=button, width=5, height=2,
                  command=lambda b=button: add_to_expression(b) if b != '=' else calculate()).grid(row=row, column=col)

    col += 1
    if col > 3:
        col = 0
        row += 1

# Khởi chạy giao diện
window.mainloop()
