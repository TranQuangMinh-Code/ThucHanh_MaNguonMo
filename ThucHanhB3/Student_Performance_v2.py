import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from tkinter import messagebox

# Đọc dữ liệu từ file CSV
data = pd.read_csv('Student_Performance.csv')

# Chia dữ liệu thành dữ liệu đào tạo và dữ liệu kiểm tra
X = data[['Hours Studied', 'Previous Scores', 'Extracurricular Activities', 'Sleep Hours', 'Sample Question Papers Practiced']]
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
result_message = f"Mean Absolute Error: {mae}\nMean Squared Error: {mse}\nRoot Mean Squared Error: {rmse}\nCoefficients: {coefficients}"
messagebox.showinfo("Kết Quả Đánh Giá Mô Hình", result_message)
