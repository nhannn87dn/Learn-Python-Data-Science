# 🧠 **Buổi 9: Giới thiệu Data Science & Thư viện**

---

## 🎯 **Mục tiêu buổi học**

* Hiểu khái niệm cơ bản về **Data Science** và vai trò của Python.
* Làm quen các **thư viện quan trọng** trong phân tích dữ liệu: NumPy, Pandas, Matplotlib, Seaborn.
* Làm việc trên **Jupyter Notebook**.
* Nắm cú pháp cơ bản của **NumPy phần 1**: tạo và thao tác với mảng (array).

---

## 🧩 **1. Giới thiệu về Data Science**

### 🔹 Data Science là gì?

> **Data Science (Khoa học dữ liệu)** là lĩnh vực kết hợp giữa **lập trình, thống kê, và trực quan hóa** để trích xuất thông tin và hiểu biết từ dữ liệu.

### 🔹 Quy trình cơ bản trong Data Science

1. **Thu thập dữ liệu** (Collect)
2. **Tiền xử lý dữ liệu** (Clean)
3. **Phân tích & mô hình hóa** (Analyze / Model)
4. **Trực quan hóa & trình bày kết quả** (Visualize / Report)

---

## 📦 **2. Các thư viện phổ biến trong Data Science**

| Thư viện       | Vai trò                                             | Ví dụ sử dụng             |
| -------------- | --------------------------------------------------- | ------------------------- |
| **NumPy**      | Xử lý mảng số học nhanh, thay thế list thông thường | `np.array([1, 2, 3])`     |
| **Pandas**     | Làm việc với dữ liệu dạng bảng (Excel, CSV)         | `pd.read_csv('data.csv')` |
| **Matplotlib** | Vẽ biểu đồ, đồ thị                                  | `plt.plot(x, y)`          |
| **Seaborn**    | Thư viện vẽ biểu đồ nâng cao, đẹp hơn Matplotlib    | `sns.barplot(data=df)`    |

---

## 🧩 **3. Tạo môi trường ảo cho dự án**

Giả sử bạn đang ở trong thư mục dự án:

```bash
cd path/to/your/project
```

**Bước 1: Tạo môi trường ảo**


```bash
python -m venv venv
```

Lệnh này sẽ tạo thư mục con `venv/` trong dự án, chứa bản sao riêng của Python và pip.
Toàn bộ package cài vào đây **chỉ có hiệu lực trong dự án này**.

---

**Bước 2: Kích hoạt môi trường ảo**

🔹 Windows (CMD hoặc PowerShell)

```bash
venv\Scripts\activate
```

🔹 macOS / Linux

```bash
source venv/bin/activate
```

Khi kích hoạt xong, bạn sẽ thấy prompt thay đổi, ví dụ:

```
(venv) C:\Users\Tomy\project>
```

---

**Bước 3: Cài đặt package (chỉ cho dự án)**

Giờ bạn có thể cài bất kỳ package nào — ví dụ `pandas`:

```bash
pip install pandas
```

Package này sẽ được lưu trong `venv/lib/.../site-packages` của **dự án**,
không ảnh hưởng đến các thư mục khác hoặc hệ thống.

---

**Lưu danh sách package (tùy chọn)**

Để người khác (hoặc bạn sau này) có thể cài lại toàn bộ package:

```bash
pip freeze > requirements.txt
```

Khi cần cài lại:

```bash
pip install -r requirements.txt
```

---

**Thoát khỏi môi trường ảo**

Sau khi làm việc xong:

```bash
deactivate
```

---

## ⚙️ **3. Công cụ làm việc**

### 🔹 3.1 Jupyter Notebook

```bash
pip install notebook
```

Chạy Notebook:

```bash
jupyter notebook
```

Truy cập tại địa chỉ: `http://localhost:8888`

Một số thao tác cơ bản:

* **Shift + Enter:** chạy cell hiện tại.
* **Esc + A/B:** thêm cell phía trên/dưới.
* **Markdown cell:** ghi chú lý thuyết, tiêu đề.
* **Code cell:** viết và chạy lệnh Python.

### 🔹 3.2 Bộ Kit Anaconda Navigator

Download tại link: <https://www.anaconda.com/download>

### 🔹 3.3 Google Colab

Link: <https://colab.research.google.com/>

---

## 🧮 **4. Làm quen với NumPy**

### 🔹 Cài đặt NumPy

```bash
pip install numpy
```

### 🔹 Import thư viện

```python
import numpy as np
```

---

## 🧱 **5. Tạo mảng NumPy**

NumPy cung cấp đối tượng **ndarray** – mảng n chiều (n-dimensional array).

### 🔸 Tạo mảng từ list Python

```python
import numpy as np

arr = np.array([1, 2, 3, 4])
print(arr)
# 👉 [1 2 3 4]
```

### 🔸 Mảng 2 chiều

```python
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2)
```

### 🔸 Các hàm tạo mảng nhanh

```python
np.zeros((2, 3))   # Mảng 2x3 toàn số 0
np.ones((3, 2))    # Mảng 3x2 toàn số 1
np.arange(0, 10, 2)  # [0, 2, 4, 6, 8]
np.linspace(0, 1, 5) # [0.  0.25 0.5 0.75 1.]
```

---

## ⚙️ **6. Truy cập và cắt mảng (Indexing & Slicing)**

### 6.1 Truy cập dựa vào Index

```python
arr = np.array([10, 20, 30, 40, 50])
print(arr[0])      # 10
print(arr[-1])     # 50
```

Với mảng 2 chiều:

```python
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(matrix[0, 1])  # 2
print(matrix[:, 2])  # [3 6]
```

### 6.2 Cắt mảng - Slicing

Cú pháp chung `[start:end:step]`


| Thành phần | Ý nghĩa                                                  | Ghi chú                     |
| ---------- | -------------------------------------------------------- | --------------------------- |
| `start`    | Chỉ số bắt đầu (index đầu tiên được lấy)                 | Mặc định là `0`             |
| `end`      | Chỉ số kết thúc (đến nhưng **không bao gồm** vị trí này) | Mặc định là độ dài của mảng |
| `step`     | Bước nhảy (khoảng cách giữa các phần tử được lấy)        | Mặc định là `1`             |

---

#### 🔍 Ví dụ cơ bản

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60])
print(arr[1:4])      # Lấy từ index 1 đến 3 → [20 30 40]
print(arr[:3])       # Bỏ qua start → [10 20 30]
print(arr[2:])       # Bỏ qua end → [30 40 50 60]
print(arr[::2])      # step = 2 → [10 30 50]
print(arr[::-1])     # step = -1 → đảo ngược mảng → [60 50 40 30 20 10]
```

---

####  Slicing trên mảng 2 chiều

Với mảng 2D, bạn có thể cắt theo **hàng** và **cột** cùng lúc:

```python
matrix = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])

# Cú pháp: array[hàng_start:hàng_end, cột_start:cột_end]
print(matrix[0:2, 1:3])
```

📤 Kết quả:

```
[[2 3]
 [6 7]]
```

➡️ nghĩa là:

* Lấy hàng 0 → 1
* Lấy cột 1 → 2

---

#### Dùng step để cắt theo hàng và cột

```python
print(matrix[::2, ::2])  # Lấy cách 2 hàng và 2 cột
```

📤 Kết quả:

```
[[ 1  3]
 [ 9 11]]
```

---

####  Ghi nhớ nhanh

| Cú pháp         | Ý nghĩa                     |
| --------------- | --------------------------- |
| `arr[a:b]`      | Lấy từ a → b-1              |
| `arr[a:]`       | Từ a đến hết                |
| `arr[:b]`       | Từ đầu đến b-1              |
| `arr[::n]`      | Cách n phần tử              |
| `arr[::-1]`     | Đảo ngược mảng              |
| `arr[m:n, p:q]` | Lấy m→n-1 hàng và p→q-1 cột |


---



## 🧠 **7. Data Types trong NumPy**

### 7.1 Kiểu dữ liệu là gì?

Trong **NumPy**, mỗi mảng (`ndarray`) chỉ chứa **một kiểu dữ liệu duy nhất** cho tất cả phần tử (khác với list trong Python có thể chứa nhiều loại).

### 7.2 Kiểm tra kiểu dữ liệu trong NumPy

```python
import numpy as np

arr = np.array([1, 2, 3])
print(arr.dtype)  # int64 (hoặc int32 tùy hệ thống)
```

### 7.3. Các kiểu dữ liệu phổ biến trong NumPy

| Kiểu dữ liệu                          | Mô tả                   | Ví dụ                                    |
| ------------------------------------- | ----------------------- | ---------------------------------------- |
| `int8`, `int16`, `int32`, `int64`     | Số nguyên (8–64 bit)    | `np.array([1, 2], dtype=np.int32)`       |
| `uint8`, `uint16`, `uint32`, `uint64` | Số nguyên không dấu     | `np.array([1, 2], dtype=np.uint8)`       |
| `float16`, `float32`, `float64`       | Số thực dấu chấm động   | `np.array([1.2, 3.4], dtype=np.float32)` |
| `complex64`, `complex128`             | Số phức                 | `np.array([1+2j, 3+4j])`                 |
| `bool_`                               | Boolean (True/False)    | `np.array([True, False])`                |
| `str_`, `unicode_`                    | Chuỗi                   | `np.array(["A", "B"])`                   |
| `object_`                             | Đối tượng Python bất kỳ | `np.array([1, "A", True], dtype=object)` |

### 7.4. Ép kiểu dữ liệu (Type Casting)

#### ✴️ Khi tạo mảng:

```python
arr = np.array([1, 2, 3], dtype=float)
print(arr)        # [1. 2. 3.]
print(arr.dtype)  # float64
```

#### ✴️ Khi muốn đổi kiểu:

```python
arr = np.array([1.1, 2.2, 3.3])
new_arr = arr.astype(int)
print(new_arr)        # [1 2 3]
print(new_arr.dtype)  # int64
```

---


### 7.5.Một số thuộc tính của mảng

```python
arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr.shape)   
# (2, 3) Mảng 2 chiều
# Chiều thứ 1 có 2 phần tử, chiều thứ 2 có 3 phần tử
print(arr.ndim)    
# 2 (số chiều)
print(arr.size)    
# 6 (số phần tử)
print(arr.dtype)   
# kiểu dữ liệu (int64)
```

---


## ➕ **8. Toán tử và thao tác trên mảng**

### ⚙️ **8.1. Giới thiệu**

**NumPy** hỗ trợ rất nhiều **toán tử và thao tác vector hóa** (vectorized operations) giúp tính toán nhanh hơn nhiều so với việc dùng vòng lặp trong Python.
Thay vì phải lặp từng phần tử, NumPy thực hiện **các phép toán song song** trên toàn bộ mảng.

---

### ⚙️ **8.2. Các phép toán số học cơ bản**

Các phép toán cơ bản như cộng, trừ, nhân, chia… có thể thực hiện **trực tiếp giữa các mảng** cùng kích thước hoặc giữa mảng và một số (broadcasting).

Ví dụ:

```python
import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])

print(a + b)   # [11 22 33 44]
print(a - b)   # [-9 -18 -27 -36]
print(a * b)   # [10 40 90 160]
print(b / a)   # [10. 10. 10. 10.]
print(a ** 2)  # [ 1  4  9 16]
```

---

### ⚙️ **8.3. Broadcasting (tự mở rộng kích thước)**


> **Broadcasting** cho phép NumPy thực hiện phép toán giữa các mảng có **kích thước khác nhau**, bằng cách **tự mở rộng** mảng nhỏ hơn cho phù hợp.

Ví dụ:

```python
a = np.array([1, 2, 3])
b = 2
print(a + b)
# 👉 [3 4 5]
```

Ở đây, `b` được "broadcast" thành `[2, 2, 2]`.


Với mảng 2 chiều:

```python
A = np.array([[1, 2, 3],
              [4, 5, 6]])
B = np.array([10, 20, 30])

print(A + B)
# 👉 [[11 22 33]
#      [14 25 36]]
```

---


**Quy tắc broadcast**

* Nếu hai mảng có số chiều khác nhau → thêm chiều 1 vào mảng nhỏ hơn.
* Nếu kích thước không khớp, NumPy sẽ cố mở rộng chiều có kích thước 1.
* Nếu vẫn không khớp → báo lỗi.

---

### ⚙️ **8.4. Các toán tử so sánh**

NumPy cho phép **so sánh từng phần tử** giữa hai mảng và trả về mảng Boolean.

```python
a = np.array([1, 2, 3, 4])
b = np.array([1, 0, 3, 5])

print(a == b)  # [ True False  True False]
print(a > b)   # [False  True False False]
print(a != b)  # [False  True False  True]
```

Ta có thể dùng kết quả này để **lọc dữ liệu** (filtering).

---

### ⚙️ **8.5. Các hàm toán học thông dụng**

NumPy cung cấp rất nhiều **hàm vector hóa** áp dụng trực tiếp lên toàn mảng:

| Nhóm              | Hàm ví dụ        | Mô tả                           |
| ----------------- | ---------------- | ------------------------------- |
| Căn bậc hai       | `np.sqrt(a)`     | Căn bậc hai                     |
| Lũy thừa          | `np.power(a, 2)` | Bình phương từng phần tử        |
| Logarit           | `np.log(a)`      | Log tự nhiên                    |
| Sin/Cos/Tan       | `np.sin(a)`      | Các hàm lượng giác              |
| Làm tròn          | `np.round(a)`    | Làm tròn đến số nguyên gần nhất |
| Giá trị tuyệt đối | `np.abs(a)`      | Trị tuyệt đối                   |

Ví dụ:

```python
a = np.array([1, 4, 9, 16])

print(np.sqrt(a))   # [1. 2. 3. 4.]
print(np.log(a))    # [0.   1.39 2.19 2.77]
print(np.sin(a))    # [0.84 -0.76 0.41 -0.29]
```

---

### ⚙️ **8.6. Thao tác logic trên mảng**

Ta có thể kết hợp các điều kiện logic để lọc dữ liệu:

```python
a = np.array([10, 20, 30, 40, 50])

print(a[(a > 20) & (a < 50)])  # [30 40]
print(a[(a == 10) | (a == 50)]) # [10 50]
```

---

### ⚙️ **8.7. Hàm thao tác phần tử**

| Hàm                 | Mô tả                                |
| ------------------- | ------------------------------------ |
| `np.add(a, b)`      | Cộng phần tử tương ứng               |
| `np.subtract(a, b)` | Trừ phần tử tương ứng                |
| `np.multiply(a, b)` | Nhân phần tử tương ứng               |
| `np.divide(a, b)`   | Chia phần tử tương ứng               |
| `np.exp(a)`         | e^a                                  |
| `np.maximum(a, b)`  | Lấy giá trị lớn hơn giữa hai phần tử |
| `np.minimum(a, b)`  | Lấy giá trị nhỏ hơn giữa hai phần tử |

Ví dụ:

```python
a = np.array([1, 2, 3])
b = np.array([2, 2, 0])

print(np.maximum(a, b))  # [2 2 3]
print(np.minimum(a, b))  # [1 2 0]
```

---

### ⚙️ **8.8. Toán tử ma trận**

Khi làm việc với mảng 2D, NumPy cung cấp **toán tử ma trận**:

```python
A = np.array([[1, 2],
              [3, 4]])
B = np.array([[5, 6],
              [7, 8]])

print(A @ B)         # Tích ma trận
print(np.dot(A, B))  # Cách khác tương đương
print(A.T)           # Ma trận chuyển vị
```

Kết quả:

```
[[19 22]
 [43 50]]
[[19 22]
 [43 50]]
[[1 3]
 [2 4]]
```

---

### ⚙️ **8.9. Thống kê cơ bản trên mảng**

| Hàm            | Ý nghĩa          |
| -------------- | ---------------- |
| `np.sum(a)`    | Tổng các phần tử |
| `np.mean(a)`   | Trung bình       |
| `np.median(a)` | Trung vị         |
| `np.std(a)`    | Độ lệch chuẩn    |
| `np.var(a)`    | Phương sai       |
| `np.max(a)`    | Giá trị lớn nhất |
| `np.min(a)`    | Giá trị nhỏ nhất |

Ví dụ:

```python
a = np.array([1, 2, 3, 4, 5])

print(np.mean(a))  # 3.0
print(np.std(a))   # 1.4142
print(np.max(a))   # 5
```

---

## 🔁 **9. Thay đổi hình dạng mảng (Reshape)**


###  9.1. Khái niệm

**Reshape** nghĩa là **thay đổi hình dạng (shape)** của mảng mà **không làm thay đổi dữ liệu bên trong**.

👉 Dữ liệu (các phần tử) vẫn giữ nguyên thứ tự, chỉ thay đổi **số chiều** và **số phần tử mỗi chiều**.

---

###  9.2. Cú pháp

```python
numpy.reshape(a, newshape)
```

hoặc dùng **phương thức của mảng**:

```python
a.reshape(newshape)
```

* `a`: mảng cần thay đổi hình dạng
* `newshape`: tuple biểu thị hình dạng mới (ví dụ `(rows, cols)`)

---

###  9.3. Ví dụ cơ bản

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
reshaped = arr.reshape(2, 3)

print("Mảng gốc:", arr)
print("Mảng mới:\n", reshaped)
```

📤 Kết quả:

```
Mảng gốc: [1 2 3 4 5 6]
Mảng mới:
 [[1 2 3]
  [4 5 6]]
```

🧩 Giải thích:

* Mảng ban đầu có **6 phần tử**
* Sau khi reshape thành `(2, 3)` → 2 hàng, 3 cột
  ✅ Tổng phần tử vẫn là **6 = 2 × 3**

---

###  9.4. Quy tắc bắt buộc

Tổng số phần tử **trước và sau khi reshape phải bằng nhau**.

```python
arr = np.array([1, 2, 3, 4, 5, 6])
arr.reshape(4, 2)  # ❌ Lỗi! 6 phần tử không thể reshape thành 8
```

###  9.5. Dùng `-1` để tự động tính kích thước

NumPy cho phép bạn dùng `-1` để **tự động suy ra kích thước còn lại**:

```python
arr = np.array([1, 2, 3, 4, 5, 6])
print(arr.reshape(3, -1))  # 3 hàng, NumPy tự tính cột
```

📤 Kết quả:

```
[[1 2]
 [3 4]
 [5 6]]
```

🧠 NumPy hiểu rằng 6 phần tử chia cho 3 hàng → 2 cột.

---

###  9.6. Reshape mảng nhiều chiều

```python
matrix = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8]
])

reshaped = matrix.reshape(4, 2)
print(reshaped)
```

📤 Kết quả:

```
[[1 2]
 [3 4]
 [5 6]
 [7 8]]
```

---

###  9.7. Reshape sang 3 chiều

```python
arr = np.arange(12)  # [0, 1, 2, ..., 11]
reshaped = arr.reshape(2, 3, 2)
print(reshaped)
```

📤 Kết quả:

```
[[[ 0  1]
  [ 2  3]
  [ 4  5]]

 [[ 6  7]
  [ 8  9]
  [10 11]]]
```

🧩 Nghĩa là:

* 2 “khối” (block)
* Mỗi khối có 3 hàng, 2 cột

---

###  9.8. Dạng “flatten” (ngược lại với reshape)

Nếu bạn muốn **chuyển mảng nhiều chiều → 1 chiều**, dùng:

```python
arr = np.array([[1, 2], [3, 4], [5, 6]])
flat = arr.reshape(-1)
# hoặc arr.flatten()
print(flat)  # [1 2 3 4 5 6]
```

---


## 🧮 **10. Một số phép toán thống kê**

NumPy cung cấp **nhiều hàm thống kê mạnh mẽ** giúp bạn dễ dàng **phân tích dữ liệu**, **tóm tắt thông tin**, và **chuẩn bị cho xử lý Data Science / Machine Learning**.
Các phép toán này được **tối ưu hóa**, **chạy rất nhanh** và **hoạt động trên cả mảng nhiều chiều**.

---

🧩 1. **Tổng – `np.sum()`**

Tính **tổng các phần tử** trong mảng.

🧠 Ví dụ:

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
total = np.sum(arr)
print(total)
```

📤 Kết quả:

```
15
```

> 🔹 Bạn có thể chỉ định **trục (axis)** để tính tổng theo hàng hoặc cột.

```python
arr2d = np.array([[1, 2], [3, 4]])
print(np.sum(arr2d, axis=0))  # Tổng theo cột → [4, 6]
print(np.sum(arr2d, axis=1))  # Tổng theo hàng → [3, 7]
```

---

🧩 2. **Trung bình – `np.mean()`**

Tính **giá trị trung bình (mean)** của các phần tử.

🧠 Ví dụ:

```python
arr = np.array([10, 20, 30, 40])
print(np.mean(arr))
```

📤 Kết quả:

```
25.0
```

---

🧩 3. **Trung vị – `np.median()`**

Tính **giá trị trung vị** (median — giá trị nằm giữa sau khi sắp xếp).

🧠 Ví dụ:

```python
arr = np.array([1, 3, 5, 7, 9])
print(np.median(arr))
```

📤 Kết quả:

```
5.0
```

---

🧩 4. **Độ lệch chuẩn – `np.std()`**

Độ lệch chuẩn (standard deviation) cho biết **mức độ phân tán** của dữ liệu so với giá trị trung bình.

🧠 Ví dụ:

```python
arr = np.array([10, 20, 30, 40, 50])
print(np.std(arr))
```

📤 Kết quả:

```
14.142135623730951
```

> 🔹 Độ lệch chuẩn càng nhỏ → dữ liệu càng tập trung quanh giá trị trung bình.
> 🔹 Độ lệch chuẩn càng lớn → dữ liệu càng phân tán.

---

🧩 5. **Phương sai – `np.var()`**

Phương sai (variance) là **bình phương của độ lệch chuẩn**.
Nó đo lường **độ phân tán của dữ liệu**.

🧠 Ví dụ:

```python
arr = np.array([10, 20, 30, 40, 50])
print(np.var(arr))
```

📤 Kết quả:

```
200.0
```

> 🔹 `np.var(arr)` = (std)^2

---

🧩 6. **Giá trị lớn nhất và nhỏ nhất**

| Hàm              | Mô tả                               |
| ---------------- | ----------------------------------- |
| `np.max(arr)`    | Lấy giá trị lớn nhất                |
| `np.min(arr)`    | Lấy giá trị nhỏ nhất                |
| `np.argmax(arr)` | Lấy **chỉ số** của giá trị lớn nhất |
| `np.argmin(arr)` | Lấy **chỉ số** của giá trị nhỏ nhất |

🧠 Ví dụ:

```python
arr = np.array([5, 7, 2, 9, 4])

print(np.max(arr))     # 9
print(np.min(arr))     # 2
print(np.argmax(arr))  # 3
print(np.argmin(arr))  # 2
```

---

🧩 7. **Tích – `np.prod()`**

Tính **tích của tất cả phần tử** trong mảng.

```python
arr = np.array([1, 2, 3, 4])
print(np.prod(arr))  # 24
```

---

🧩 8. **Tích lũy – `np.cumsum()` và `np.cumprod()`**

| Hàm            | Mô tả              |
| -------------- | ------------------ |
| `np.cumsum()`  | Tính tổng lũy tiến |
| `np.cumprod()` | Tính tích lũy tiến |

🧠 Ví dụ:

```python
arr = np.array([1, 2, 3, 4])

print(np.cumsum(arr))  # [ 1  3  6 10]
print(np.cumprod(arr)) # [ 1  2  6 24]
```

---

🧩 9. **Tính trung bình, min, max theo trục (axis)**

Khi làm việc với mảng 2D, bạn có thể chỉ định `axis`.

🧠 Ví dụ:

```python
arr2d = np.array([[10, 20, 30],
                  [40, 50, 60]])

print(np.mean(arr2d, axis=0))  # Trung bình theo cột
print(np.mean(arr2d, axis=1))  # Trung bình theo hàng
```

📤 Kết quả:

```
[25. 35. 45.]
[20. 50.]
```

---

🧩 10. **Tóm tắt nhanh bằng `np.ptp()` và `np.percentile()`**

| Hàm                     | Mô tả                         |
| ----------------------- | ----------------------------- |
| `np.ptp(arr)`           | Khoảng biến thiên (max - min) |
| `np.percentile(arr, p)` | Giá trị tại phân vị thứ *p*   |

🧠 Ví dụ:

```python
arr = np.array([10, 20, 30, 40, 50])

print(np.ptp(arr))          # 40
print(np.percentile(arr, 50))  # Trung vị (50th percentile) = 30
```


