# 🐼 **Buổi 12: Pandas – Phần 2: Lọc & Tổng hợp dữ liệu**

## 🎯 **Mục tiêu buổi học**

* Cách đọc dữ liệu từ **JSON, file CSV, Excel**.
* Nắm vững kỹ thuật **lọc dữ liệu nâng cao** bằng `query()` và **boolean mask**.
* Biết cách **nhóm dữ liệu (`groupby`)**, tính toán tổng hợp (`aggregate`).
* Làm quen với **sắp xếp dữ liệu (`sort_values`, `sort_index`)**.

---

## Dữ liệu sử dụng: `sales_data.csv`

> **File**: `data/sales_data.csv`  
> **Số dòng**: 77 đơn hàng  
> **Thời gian**: Từ 05/01/2024 đến 20/12/2024  
> **Quốc gia**: Vietnam, Thailand, Indonesia, Malaysia, Singapore  
> **Sản phẩm**: Laptop, Phone, Tablet, Monitor, Desk, Chair, Sofa  
> **Kênh bán**: Online / Offline

### Cấu trúc cột

| Cột            | Kiểu dữ liệu | Mô tả |
|----------------|--------------|-------|
| `OrderID`      | int          | Mã đơn hàng |
| `Date`         | date         | Ngày đặt hàng |
| `Country`      | str          | Quốc gia |
| `Product`      | str          | Tên sản phẩm |
| `Category`     | str          | Loại: Electronics / Furniture |
| `Quantity`     | int          | Số lượng |
| `UnitPrice`    | float        | Giá đơn vị |
| `Sales`        | float        | Doanh thu = Quantity × UnitPrice |
| `Profit`       | float        | Lợi nhuận |
| `SalesChannel` | str          | Kênh bán: Online / Offline |

---

## 📘 **1. Cách đọc dữ liệu từ các nguồn**

### 🔹 Đọc file CSV

```python
import pandas as pd

# Đọc file [sales_data.csv]
df = pd.read_csv('./data/sales_data.csv')
print(df.head())
```

### 🔹 Đọc file JSON

```python
import pandas as pd

# Đọc file JSON
df = pd.read_json('./data/sales_data.json')
print(df.head())
```

### 🔹 Đọc file Excel

```python
import pandas as pd

# Đọc file Excel
df = pd.read_excel('./data/sales_data.xlsx')
print(df.head())
```

---

## 🔍 **2. Lọc dữ liệu bằng Boolean Mask**

Boolean mask là cách tạo **biểu thức điều kiện trả về True/False** để lọc dòng dữ liệu.

### 🔹 Ví dụ 1: Lọc các đơn hàng của "Vietnam"

```python
vietnam_orders = df[df['Country'] == 'Vietnam']
print(vietnam_orders)
```

### 🔹 Ví dụ 2: Lọc với điều kiện kết hợp

```python
df_classA_math = df[(df['Category'] == 'Furniture') & (df['SalesChannel'] == 'Online')]
print(df_classA_math)
```

### 🔹 Ví dụ 3: Lọc điểm nằm trong một danh sách

```python
df_selected = df[df['Quantity'].isin(['2', '10'])]
```

> 💡 `isin()` rất hữu ích khi muốn lọc nhiều giá trị cùng lúc.

---

## 🧩 **3. Lọc dữ liệu bằng `query()`**

Phương thức `query()` cho phép lọc dữ liệu **giống cú pháp SQL**, giúp code ngắn gọn hơn.

### 🔹 Ví dụ 1

```python
df.query("Quantity > 8")
```

### 🔹 Ví dụ 2

```python
df.query("Category == 'Furniture' and SalesChannel == 'Online'")
```

### 🔹 Ví dụ 3: Dùng biến trong query

```python
min_quantity = 8
df.query("Quantity >= @min_quantity")
```

> 💡 Dấu `@` dùng để gọi biến Python bên ngoài.

---

## 📊 **4. Nhóm dữ liệu với `groupby()`**

`groupby()` dùng để **gom nhóm dữ liệu theo cột** và **tính toán tổng hợp** (như trung bình, tổng, đếm,...).

### 🔹 Cú pháp

```python
df.groupby('column_name')
```

### 🔹 Ví dụ 1: Tính điểm trung bình theo Country

```python
avg_country = df.groupby('Country')['Sales'].mean()
print(avg_country)
```

---

### 🔹 Ví dụ 2: Tính trung bình theo Country và Category

```python
avg_country_cate = df.groupby(['Country', 'Category'])['Sales'].mean()
print(avg_country_cate)
```


---

### 🔹 Ví dụ 3: Đếm số lượng bán ra của kênh theo từng quốc gia

```python
count_channel = df.groupby('Country')['SalesChannel'].count()
print(count_channel)
```

---

## 🔢 **5. Tổng hợp với `aggregate()`**

Hàm `agg()` (hoặc `aggregate()`) cho phép áp dụng **nhiều phép tính cùng lúc**.

### 🔹 Ví dụ

```python
stats = df.groupby('Country')['Sales'].agg(['mean', 'max', 'min', 'count'])
print(stats)
```

---

### 🔹 Nhiều phép tính khác nhau cho mỗi cột

```python
df.groupby('Country').agg({
    'Sales': ['mean', 'max'],
    'SalesChannel': 'count'
})
```

---

## 📈 **6. Sắp xếp dữ liệu (`sort_values`, `sort_index`)**

### 🔹 Sắp xếp theo giá trị

```python
df.sort_values('Sales', ascending=False)
```

### 🔹 Sắp xếp theo nhiều cột

```python
df.sort_values(['Country', 'Sales'], ascending=[True, False])
```

### 🔹 Sắp xếp theo index

```python
df.sort_index()
```

---

## 💻 **7. Thực hành**

### 🧩 **Bài 1:**

Dựa vào data set `./data/sales_data.csv` hãy thực hiện các yêu cầu phân tích sau:

1. Tìm các đơn hàng của “Vietnam” có lợi nhuận > 500*
1. Lấy danh sách sản phẩm thuộc “Electronics” có giá > 1000
1. Tính tổng doanh số theo “Country” và “Category”
1. Tính tổng `Sales`, trung bình `Profit`, đếm `OrderID`
1. Sắp xếp danh sách quốc gia theo tổng doanh số giảm dần
1. Tính tổng doang số tháng 1
1. Tính tổng doang số kênh `Online` và `Offline` cả năm

---

