# 🧹 **Buổi 13: Làm sạch & Thống kê dữ liệu**

## 🎯 **Mục tiêu buổi học**

* Hiểu vai trò của bước **làm sạch dữ liệu (data cleaning)** trong quy trình Data Science.
* Làm quen với các kỹ thuật xử lý **dữ liệu thiếu (missing data)** và **ngoại lệ (outlier)**.
* Sử dụng các hàm thống kê mô tả để hiểu đặc trưng cơ bản của dữ liệu.

---

## 🧠 **1. Giới thiệu về Data Cleaning**

Trước khi phân tích, dữ liệu thực tế thường **không hoàn hảo**:

* Có **giá trị thiếu (NaN, None)**
* Có **giá trị ngoại lệ** (sai lệch lớn)
* Có **dữ liệu trùng lặp hoặc lỗi định dạng**

👉 Làm sạch dữ liệu giúp tăng **độ chính xác** cho mô hình phân tích hoặc Machine Learning.

---

## 🧩 **2. Xử lý dữ liệu thiếu (Missing Values)**

### 🔹 Kiểm tra dữ liệu thiếu

```python
import pandas as pd

df = pd.read_csv("sales.csv")
df.isna().sum()   # Đếm số giá trị NaN theo cột
df.info()         # Xem tổng quan dữ liệu
```

### 🔹 Loại bỏ dữ liệu thiếu

```python
df_clean = df.dropna()               # Xoá mọi hàng có NaN
df_clean = df.dropna(subset=['Price', 'Revenue'])  # Chỉ xoá nếu NaN trong cột nhất định
```

### 🔹 Điền giá trị thay thế (`fillna`)

```python
df['Revenue'].fillna(0, inplace=True)                  # Điền 0
df['Revenue'].fillna(df['Revenue'].mean(), inplace=True) # Điền giá trị trung bình
df['City'].fillna('Unknown', inplace=True)             # Điền chuỗi mặc định
```

---

## ⚠️ **3. Xử lý Outlier (Giá trị ngoại lệ)**

### 🔹 Xác định outlier bằng thống kê

Sử dụng **quy tắc IQR (Interquartile Range)**:

```python
Q1 = df['Revenue'].quantile(0.25)
Q3 = df['Revenue'].quantile(0.75)
IQR = Q3 - Q1
outliers = df[(df['Revenue'] < Q1 - 1.5 * IQR) | (df['Revenue'] > Q3 + 1.5 * IQR)]
```

### 🔹 Loại bỏ hoặc thay thế outlier

```python
df_no_outlier = df[(df['Revenue'] >= Q1 - 1.5 * IQR) & (df['Revenue'] <= Q3 + 1.5 * IQR)]
```

> 💡 **Gợi ý:** Có thể dùng biểu đồ boxplot để trực quan hoá outlier bằng **Seaborn**.

---

## 📊 **4. Thống kê mô tả (Descriptive Statistics)**

### 🔹 Các hàm cơ bản

```python
df['Revenue'].mean()      # Trung bình
df['Revenue'].median()    # Trung vị
df['Revenue'].mode()      # Giá trị thường gặp nhất
df['Revenue'].std()       # Độ lệch chuẩn
```

### 🔹 Tổng hợp thống kê nhanh

```python
df.describe()  # Thống kê nhanh: count, mean, std, min, max, quartiles
```

### 🔹 Thống kê theo nhóm

```python
df.groupby('Region')['Revenue'].mean()
```

---

## 🧪 **5. Thực hành: Phân tích mô tả dữ liệu**

