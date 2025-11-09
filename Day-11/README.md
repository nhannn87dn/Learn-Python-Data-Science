# 🐼 **Buổi 11: Pandas Series & DataFrame – Phần 1**


## 🎯 **Mục tiêu buổi học**

* Làm quen với thư viện **Pandas** và vai trò trong phân tích dữ liệu.
* Hiểu hai cấu trúc dữ liệu chính: **Series** và **DataFrame**.
* Thực hành thao tác cơ bản: chọn, lọc, indexing, slicing.


---

## 📘 **1. Giới thiệu Pandas**

### 🔹 Pandas là gì?

> Pandas là thư viện mạnh mẽ của Python giúp **xử lý và phân tích dữ liệu dạng bảng** (giống Excel hoặc SQL).

### 🔹 Đặc điểm:

* Dựa trên NumPy → hiệu năng cao.
* Dữ liệu có **hàng (index)** và **cột (column)**.
* Dễ dàng đọc/ghi file (CSV, Excel, JSON,...).
* Tích hợp tốt với Matplotlib và Seaborn để vẽ biểu đồ.

### 🔹 Cài đặt:

```bash
pip install pandas
```

### 🔹 Import:

```python
import pandas as pd
```

---

## 🧱 **2. Cấu trúc dữ liệu trong Pandas**

Pandas có hai cấu trúc dữ liệu chính:

1. **Series** → 1 chiều (giống mảng có nhãn)
2. **DataFrame** → 2 chiều (giống bảng dữ liệu)

---

## 🧩 **3. Series**

### 🧠 **3.1. Giới thiệu Pandas Series là gì**

**Pandas Series** là **cấu trúc dữ liệu một chiều (1D)** trong Pandas, tương tự như **một cột trong Excel** hoặc **một mảng 1 chiều trong NumPy**, nhưng mạnh mẽ hơn.

✅ Đặc điểm chính:

* Là **một mảng dữ liệu (values)** có **nhãn (index)** tương ứng.
* Hỗ trợ **kiểu dữ liệu hỗn hợp** (int, float, string...).
* Hỗ trợ **vector hóa** như NumPy.
* Có **tích hợp nhiều phương thức xử lý dữ liệu tiện lợi**.

---

### ⚙️ **3.2. Cách tạo Series**

#### 🔹 3.2.1. Tạo từ list

```python
import pandas as pd

s = pd.Series([10, 20, 30, 40])
print(s)
```

📤 **Kết quả:**

```
0    10
1    20
2    30
3    40
dtype: int64
```

➡️ Cột đầu là **index (chỉ số)** mặc định từ `0 → n-1`.

---

#### 🔹 3.2.2. Tạo với index tùy chỉnh

```python
s = pd.Series([10, 20, 30], index=['A', 'B', 'C'])
print(s)
```

📤 Kết quả:

```
A    10
B    20
C    30
dtype: int64
```

---

#### 🔹 3.2.3. Tạo từ dictionary

```python
data = {'a': 100, 'b': 200, 'c': 300}
s = pd.Series(data)
print(s)
```

📤 Kết quả:

```
a    100
b    200
c    300
dtype: int64
```

> 👉 Khóa (`key`) sẽ tự động trở thành **index**.

---

#### 🔹 3.2.4. Tạo từ NumPy array

```python
import numpy as np

arr = np.array([1, 2, 3, 4])
s = pd.Series(arr, index=['A', 'B', 'C', 'D'])
print(s)
```

---

#### 🔹 3.2.5. Tạo với giá trị hằng

```python
s = pd.Series(7, index=['a', 'b', 'c'])
print(s)
```

📤 Kết quả:

```
a    7
b    7
c    7
dtype: int64
```

---

### 🧩 **3.3. Thuộc tính quan trọng của Series**

| Thuộc tính | Ý nghĩa                           |
| ---------- | --------------------------------- |
| `s.values` | Trả về mảng giá trị (NumPy array) |
| `s.index`  | Trả về nhãn index                 |
| `s.dtype`  | Kiểu dữ liệu                      |
| `s.shape`  | Kích thước Series                 |
| `s.size`   | Số phần tử                        |
| `s.name`   | Tên của Series                    |

```python
print(s.values)  # [7 7 7]
print(s.index)   # Index(['a', 'b', 'c'], dtype='object')
print(s.dtype)   # int64
```

---

### 🔍 **3.4. Truy cập dữ liệu trong Series**

#### 🔹 3.4.1. Theo vị trí (giống list/array)

```python
s = pd.Series([10, 20, 30, 40], index=['A', 'B', 'C', 'D'])

print(s[0])      # 10
print(s[:2])     # Lấy 2 phần tử đầu
```

---

#### 🔹 3.4.2. Theo nhãn (index)

```python
print(s['B'])       # 20
print(s[['A', 'D']]) # Lấy nhiều giá trị theo nhãn
```

---

#### 🔹 3.4.3. Dùng `.loc[]` và `.iloc[]`

| Cú pháp        | Ý nghĩa                  |
| -------------- | ------------------------ |
| `s.loc[label]` | Truy cập theo **nhãn**   |
| `s.iloc[pos]`  | Truy cập theo **vị trí** |

```python
print(s.loc['C'])   # 30
print(s.iloc[2])    # 30
```

---

### 🧮 **3.5. Toán tử và thao tác trên Series**

Pandas Series hỗ trợ **toán tử vector hóa** (giống NumPy):

```python
a = pd.Series([10, 20, 30])
b = pd.Series([1, 2, 3])

print(a + b)     # [11, 22, 33]
print(a * 2)     # [20, 40, 60]
print(a / b)     # [10, 10, 10]
```

> ⚠️ Nếu index không trùng, Pandas sẽ **tự căn chỉnh theo index** (alignment):

```python
a = pd.Series([10, 20, 30], index=['x', 'y', 'z'])
b = pd.Series([1, 2, 3], index=['y', 'z', 'w'])

print(a + b)
```

📤 Kết quả:

```
w     NaN
x     NaN
y    21.0
z    32.0
dtype: float64
```

---

### 🔢 **3.6. Một số phương thức thao tác phổ biến**

| Phương thức      | Mô tả                        |
| ---------------- | ---------------------------- |
| `head(n)`        | Lấy n phần tử đầu            |
| `tail(n)`        | Lấy n phần tử cuối           |
| `sum()`          | Tổng giá trị                 |
| `mean()`         | Trung bình                   |
| `max() / min()`  | Giá trị lớn/nhỏ nhất         |
| `sort_values()`  | Sắp xếp theo giá trị         |
| `sort_index()`   | Sắp xếp theo index           |
| `unique()`       | Lấy giá trị duy nhất         |
| `value_counts()` | Đếm tần suất giá trị         |
| `apply(func)`    | Áp dụng hàm cho từng phần tử |

---

📌 Ví dụ:

```python
s = pd.Series([10, 20, 30, 40, 20])

print(s.mean())          # 24.0
print(s.value_counts())  # 20:2, 10:1, 30:1, 40:1
print(s.apply(lambda x: x*2))
```

---

### 🔄 **3.7. Kiểm tra và xử lý dữ liệu thiếu**

```python
s = pd.Series([1, 2, None, 4])

print(s.isnull())      # [False False True False]
print(s.notnull())     # [ True  True False  True]
print(s.fillna(0))     # Điền giá trị 0 vào chỗ NaN
print(s.dropna())      # Loại bỏ giá trị NaN
```

---

### 🧾 **3.8. Kết hợp Series**

Bạn có thể **cộng, ghép nối (concat), hoặc biến đổi** nhiều Series với nhau.

```python
s1 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
s2 = pd.Series([4, 5, 6], index=['d', 'e', 'f'])

s3 = pd.concat([s1, s2])
print(s3)
```

📤 Kết quả:

```
a    1
b    2
c    3
d    4
e    5
f    6
dtype: int64
```


---

## 🧮 **4. Pandas DataFrame**

### 🧠 **4.1. DataFrame là gì?**

**DataFrame** là một cấu trúc dữ liệu **2 chiều (2D)** trong **Pandas**, tương tự như **bảng dữ liệu** trong Excel hoặc **bảng trong cơ sở dữ liệu**.
Mỗi cột có thể chứa **kiểu dữ liệu khác nhau** (số, chuỗi, boolean, ngày tháng,...).

👉 Cấu trúc cơ bản:

```
DataFrame = hàng (rows) + cột (columns)
```

Ví dụ trực quan:

| Name    | Age | City     |
| ------- | --- | -------- |
| Alice   | 25  | New York |
| Bob     | 30  | London   |
| Charlie | 22  | Tokyo    |

---

### ⚙️ **4.2. Cách tạo DataFrame**

#### 🔹 Tạo từ dictionary

```python
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 22],
    'City': ['New York', 'London', 'Tokyo']
}

df = pd.DataFrame(data)
print(df)
```

#### 🔹 Tạo từ list của list

```python
data = [
    ['Alice', 25, 'New York'],
    ['Bob', 30, 'London'],
    ['Charlie', 22, 'Tokyo']
]
df = pd.DataFrame(data, columns=['Name', 'Age', 'City'])
```

#### 🔹 Tạo từ dictionary các Series

```python
s1 = pd.Series([25, 30, 22])
s2 = pd.Series(['New York', 'London', 'Tokyo'])
df = pd.DataFrame({'Age': s1, 'City': s2})
```

---

### 🔍 **4.3. Truy xuất dữ liệu trong DataFrame**

#### 🔹 Lấy cột

```python
df['Name']          # trả về một Series
df[['Name', 'City']] # trả về DataFrame con
```

#### 🔹 Lấy hàng theo chỉ số

```python
df.iloc[0]   # Hàng đầu tiên (index = 0)
df.iloc[1:3] # Từ hàng 1 đến 2
```

#### 🔹 Lấy hàng theo nhãn (index label)

```python
df.loc[0]          # truy cập theo nhãn (mặc định là số)
df.loc[0, 'Name']  # lấy giá trị cụ thể
```

---

### 🧮 **4.4. Các thao tác phổ biến**

#### 🔹 Thêm cột mới

```python
df['Country'] = ['USA', 'UK', 'Japan']
```

#### 🔹 Xoá cột hoặc hàng

```python
df.drop('Age', axis=1, inplace=True)  # xóa cột
df.drop(1, axis=0, inplace=True)      # xóa hàng có index = 1
```

#### 🔹 Lọc dữ liệu (Filter)

```python
df[df['Age'] > 23]         # lọc hàng có Age > 23
df[df['City'] == 'Tokyo']  # lọc theo giá trị chuỗi
```

#### 🔹 Sắp xếp dữ liệu

```python
df.sort_values(by='Age', ascending=False)
```

#### 🔹 Thống kê nhanh

```python
df.describe()  # tính trung bình, min, max, std, ...
df.info()      # thông tin cấu trúc dữ liệu
df.shape       # (số hàng, số cột)
```

---

### 🧰 **4.5. Xử lý dữ liệu bị thiếu (NaN)**

```python
df.isnull()         # kiểm tra giá trị thiếu
df.dropna()         # loại bỏ hàng có giá trị NaN
df.fillna(0)        # thay giá trị NaN bằng 0
```

---

### 🔗 **4.6. Gộp & nối dữ liệu**

#### 🔹 Nối theo chiều dọc (concat)

```python
df_new = pd.concat([df1, df2])
```

#### 🔹 Merge theo cột chung (giống SQL JOIN)

```python
pd.merge(df1, df2, on='id', how='inner')
```

---

### 📈 **4.7. Một số thao tác hữu ích khác**

```python
df['Age'].mean()       # Trung bình tuổi
df['City'].unique()    # Các giá trị duy nhất
df['City'].value_counts() # Đếm tần suất
df.rename(columns={'Name': 'FullName'}, inplace=True) # đổi tên cột
```

---

### 📊 **4.8. Truy xuất nâng cao**

#### 🔹 Áp dụng hàm cho từng phần tử

```python
df['Age'] = df['Age'].apply(lambda x: x + 1)
```

#### 🔹 Gộp nhóm (Group By)

```python
df.groupby('City')['Age'].mean()
```

---

### 📊 **4.9. Kỹ thuật di chuyển vị trí các cột trong DataFrame**

Giả sử bạn có DataFrame như sau:

```python
import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 22],
    'City': ['New York', 'London', 'Tokyo']
})

print(df)
```

Kết quả:

```
      Name  Age      City
0    Alice   25  New York
1      Bob   30    London
2  Charlie   22     Tokyo
```

---

**1. Cách 1 – Sắp xếp lại bằng danh sách tên cột**

Nếu bạn muốn **di chuyển cột `City` lên đầu**, bạn có thể chỉ định thứ tự cột thủ công:

```python
df = df[['City', 'Name', 'Age']]
print(df)
```

Kết quả:

```
       City     Name  Age
0   New York    Alice   25
1     London      Bob   30
2      Tokyo  Charlie   22
```

---

**2. Cách 2 – Dùng `insert()` để chèn lại cột vào vị trí mong muốn**

Bạn có thể **chèn một cột đã có vào vị trí mới** rồi xóa cột cũ.

Ví dụ: di chuyển cột `City` lên vị trí đầu tiên:

```python
city_col = df.pop('City')      # Lấy và xóa cột City khỏi DataFrame
df.insert(0, 'City', city_col) # Chèn lại cột City vào vị trí đầu (index 0)
print(df)
```

Kết quả giống như trên:

```
       City     Name  Age
0   New York    Alice   25
1     London      Bob   30
2      Tokyo  Charlie   22
```

👉 Ưu điểm:

* Dễ dùng khi chỉ muốn di chuyển **một cột duy nhất**.
* Không cần viết lại toàn bộ danh sách cột.

---

**3. Cách 3 – Sử dụng `reindex()` để sắp xếp lại cột**

Cách này hữu ích khi bạn muốn đảm bảo DataFrame có **thứ tự cột cố định**, có thể áp dụng sau khi merge hoặc đọc từ file.

```python
df = df.reindex(columns=['Age', 'Name', 'City'])
print(df)
```

Kết quả:

```
   Age     Name      City
0   25    Alice  New York
1   30      Bob    London
2   22  Charlie     Tokyo
```

---

### ✅ **Tóm tắt nhanh**

| Chức năng     | Câu lệnh ví dụ             |
| ------------- | -------------------------- |
| Tạo DataFrame | `pd.DataFrame(data)`       |
| Lấy cột       | `df['col']`                |
| Lấy hàng      | `df.loc[i]`, `df.iloc[i]`  |
| Thêm cột      | `df['new'] = ...`          |
| Xóa cột       | `df.drop('col', axis=1)`   |
| Lọc dữ liệu   | `df[df['col'] > 10]`       |
| Sắp xếp       | `df.sort_values(by='col')` |
| Gộp nhóm      | `df.groupby('col')`        |
| Thống kê      | `df.describe()`            |


### ✅ **Thực hành**