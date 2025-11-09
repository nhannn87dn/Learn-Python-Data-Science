# ⚙️ **Buổi 7: Exception Handling & File I/O**

Nội dung chính:

* Cách **xử lý lỗi (Exception Handling)** để chương trình không bị dừng đột ngột.
* Cách **đọc / ghi file** trong Python (file text, CSV).
* Thực hành đọc dữ liệu điểm học sinh, tính trung bình và ghi kết quả ra file.

---

## 🧩 **1. Exception Handling (Xử lý ngoại lệ)**

### 🧠 **Định nghĩa**

> **Exception (ngoại lệ)** là lỗi xảy ra khi chương trình đang chạy, ví dụ: chia cho 0, truy cập phần tử không tồn tại, đọc file không có, v.v.

Nếu không xử lý, chương trình sẽ **bị dừng**.
Ta dùng **khối `try-except`** để **bắt và xử lý lỗi**.

---

### 💡 **Cú pháp cơ bản**

```python
try:
    # đoạn code có thể gây lỗi
except:
    # xử lý khi lỗi xảy ra
```

**Ví dụ:**

```python
try:
    x = int(input("Nhập số chia: "))
    result = 10 / x
    print(result)
except:
    print("Đã xảy ra lỗi! Không thể chia cho 0 hoặc nhập sai kiểu dữ liệu.")
```

---

### 🧱 **Bắt lỗi cụ thể**

Ta có thể bắt **từng loại lỗi riêng biệt**:

```python
try:
    x = int(input("Nhập số chia: "))
    result = 10 / x
except ValueError:
    print("Lỗi: Bạn phải nhập số!")
except ZeroDivisionError:
    print("Lỗi: Không thể chia cho 0!")
```

---

### ⚙️ **`else` và `finally` trong xử lý lỗi**

| Khối      | Mục đích                                                                       |
| --------- | ------------------------------------------------------------------------------ |
| `else`    | Chạy khi **không có lỗi xảy ra**                                               |
| `finally` | Luôn chạy **dù có lỗi hay không** (thường để đóng file, giải phóng tài nguyên) |

**Ví dụ:**

```python
try:
    x = int(input("Nhập số: "))
    print(10 / x)
except ZeroDivisionError:
    print("Không thể chia cho 0.")
else:
    print("Không có lỗi xảy ra.")
finally:
    print("Kết thúc chương trình.")
```

---

### 🚨 **Tự phát sinh lỗi (`raise`)**

Dùng khi muốn **chủ động báo lỗi**.

```python
def kiem_tra_tuoi(age):
    if age < 0:
        raise ValueError("Tuổi không thể âm!")
    print(f"Tuổi của bạn là: {age}")

kiem_tra_tuoi(-5)  # Gây lỗi ValueError
```

---

## 📂 **2. File I/O (Đọc & ghi file)**

### 🧠 **Định nghĩa**

File I/O (Input/Output) là thao tác **đọc dữ liệu từ file** và **ghi dữ liệu vào file**.

---

### 💡 **Mở file trong Python**

Sử dụng hàm `open()`

```python
f = open("ten_file.txt", "mode", encoding="utf-8")
```

| Mode   | Chức năng                        |
| ------ | -------------------------------- |
| `'r'`  | Đọc file (mặc định)              |
| `'w'`  | Ghi mới (xóa dữ liệu cũ)         |
| `'a'`  | Ghi thêm vào cuối file           |
| `'r+'` | Đọc và ghi                       |
| `'x'`  | Tạo file mới, lỗi nếu đã tồn tại |

---

### 📖 **Đọc file text**

**Ví dụ file:** `data.txt`

```
Alice
Bob
Charlie
```

**Cách đọc:**

```python
f = open("data.txt", "r", encoding="utf-8")

# Cách 1: Đọc toàn bộ nội dung
content = f.read()
print(content)

# Cách 2: Đọc từng dòng
for line in f:
    print(line.strip())

f.close()  # đừng quên đóng file!
```

---

### ✏️ **Ghi file text**

```python
f = open("output.txt", "w", encoding="utf-8")
f.write("Xin chào!\n")
f.write("Đây là dòng thứ hai.")
f.close()
```

---

### ✅ **Sử dụng `with open()` (an toàn hơn)**

Cú pháp này **tự động đóng file** sau khi dùng xong.

```python
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Dòng 1\n")
    f.write("Dòng 2\n")
```

---

## 🧾 **3. Làm việc với file CSV (Comma Separated Values)**

File CSV là **dạng bảng dữ liệu** ngăn cách bởi dấu phẩy `,`.

**Ví dụ:** `students.csv`

```
name,math,english
Alice,8,7
Bob,9,8
Charlie,6,5
```

---

### 📥 **Đọc file CSV**

Sử dụng module `csv` của Python:

```python
import csv

with open("students.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```

Kết quả:

```
['name', 'math', 'english']
['Alice', '8', '7']
['Bob', '9', '8']
['Charlie', '6', '5']
```

---

### 📤 **Ghi file CSV**

```python
import csv

students = [
    ["name", "math", "english"],
    ["Alice", 8, 7],
    ["Bob", 9, 8],
]

with open("students.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(students)
```

---

### 🧠 **Ứng dụng dictionary với CSV**

```python
import csv

with open("students.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["name"], "-", row["math"])
```

---

## 🧪 **4. Thực hành gợi ý**

### 🧭 **Bài 1:**

Tạo file `students.txt` chứa tên học sinh.
Viết chương trình đọc và in từng dòng ra màn hình.

---

### 🧭 **Bài 2:**

Đọc file `scores.csv` chứa tên và điểm 3 môn, tính điểm trung bình cho từng học sinh và ghi kết quả ra file `results.csv`.

**Input (scores.csv):**

```
name,math,english,science
Alice,8,7,9
Bob,6,8,7
```

**Output (results.csv):**

```
name,average
Alice,8.0
Bob,7.0
```

**Gợi ý:**

```python
import csv

with open("scores.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    results = []
    for row in reader:
        avg = (int(row["math"]) + int(row["english"]) + int(row["science"])) / 3
        results.append({"name": row["name"], "average": round(avg, 1)})

with open("results.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "average"])
    writer.writeheader()
    writer.writerows(results)
```

---

### 🧭 **Bài 3:**

Viết chương trình yêu cầu người dùng nhập tên file.
Nếu file không tồn tại, **bắt lỗi `FileNotFoundError`** và thông báo cho người dùng.

---

## ✅ **Tổng kết**

| Khái niệm        | Chức năng                     | Ví dụ                             |
| ---------------- | ----------------------------- | --------------------------------- |
| `try/except`     | Bắt và xử lý lỗi              | `try: ... except:`                |
| `finally`        | Luôn chạy dù có lỗi hay không | Dùng để đóng file                 |
| `raise`          | Tự phát sinh lỗi              | `raise ValueError("Sai dữ liệu")` |
| `open()`         | Mở file để đọc/ghi            | `open("data.txt", "r")`           |
| `csv.reader`     | Đọc file CSV                  | `csv.reader(file)`                |
| `csv.DictReader` | Đọc CSV thành dict            | `row["name"]`                     |
