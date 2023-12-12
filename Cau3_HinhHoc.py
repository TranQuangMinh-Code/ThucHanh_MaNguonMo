from tkinter import *

def calculate_rectangle():
    length = float(length_entry.get())
    width = float(width_entry.get())
    area = length * width
    perimeter = 2 * (length + width)
    result_label.config(text="Diện tích: %.2f   Chu vi: %.2f" % (area, perimeter))

def calculate_square():
    side = float(side_entry.get())
    area = side * side
    perimeter = 4 * side
    result_label.config(text="Diện tích: %.2f   Chu vi: %.2f" % (area, perimeter))

def calculate_triangle():
    side1 = float(side1_entry.get())
    side2 = float(side2_entry.get())
    side3 = float(side3_entry.get())
    area = calculate_triangle_area(side1, side2, side3)
    perimeter = side1 + side2 + side3
    result_label.config(text="Diện tích: %.2f   Chu vi: %.2f" % (area, perimeter))

def calculate_triangle_area(side1, side2, side3):
    s = (side1 + side2 + side3) / 2
    area = (s * (s - side1) * (s - side2) * (s - side3)) ** 0.5
    return area

def calculate_circle():
    radius = float(radius_entry.get())
    area = 3.14159 * radius * radius
    perimeter = 2 * 3.14159 * radius
    result_label.config(text="Diện tích: %.2f   Chu vi: %.2f" % (area, perimeter))

root = Tk()
root.title("Hỗ trợ học tập - Hình học")

# Giao diện cho hình chữ nhật
rectangle_label = Label(root, text="Hình chữ nhật")
length_label = Label(root, text="Chiều dài:")
length_entry = Entry(root)
width_label = Label(root, text="Chiều rộng:")
width_entry = Entry(root)
rectangle_button = Button(root, text="Tính diện tích và chu vi", command=calculate_rectangle)

# Giao diện cho hình vuông
square_label = Label(root, text="Hình vuông")
side_label = Label(root, text="Cạnh:")
side_entry = Entry(root)
square_button = Button(root, text="Tính diện tích và chu vi", command=calculate_square)

# Giao diện cho tam giác
triangle_label = Label(root, text="Tam giác")
side1_label = Label(root, text="Cạnh 1:")
side1_entry = Entry(root)
side2_label = Label(root, text="Cạnh 2:")
side2_entry = Entry(root)
side3_label = Label(root, text="Cạnh 3:")
side3_entry = Entry(root)
triangle_button = Button(root, text="Tính diện tích và chu vi", command=calculate_triangle)

# Giao diện cho hình tròn
circle_label = Label(root, text="Hình tròn")
radius_label = Label(root, text="Bán kính:")
radius_entry = Entry(root)
circle_button = Button(root, text="Tính diện tích và chu vi", command=calculate_circle)

result_label = Label(root, text="Kết quả sẽ được hiển thị ở đây")

# Định vị trí các widget trong giao diện
rectangle_label.pack()
length_label.pack()
length_entry.pack()
width_label.pack()
width_entry.pack()
rectangle_button.pack()

square_label.pack()
side_label.pack()
side_entry.pack()
square_button.pack()

triangle_label.pack()
side1_label.pack()
side1_entry.pack()
side2_label.pack()
side2_entry.pack()
side3_label.pack()
side3_entry.pack()
triangle_button.pack()

circle_label.pack()
radius_label.pack()
radius_entry.pack()
circle_button.pack()

result_label.pack()

root.mainloop()