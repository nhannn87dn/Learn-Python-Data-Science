# 🧩 **Buổi 8: Module & Package**

## 🎯 **Mục tiêu buổi học**

* Hiểu khái niệm **module** và **package** trong Python.
* Biết cách **import** và sử dụng **thư viện chuẩn** (built-in modules).
* Biết cách **tạo module riêng** và **tổ chức dự án nhỏ**.
* Ôn tập toàn bộ phần **Python cơ bản (buổi 1–8)**.

---

## 🧱 **1. Module trong Python là gì?**

### 🔹 Định nghĩa:

> **Module** là một tệp (file) chứa mã Python (.py) — có thể là hàm, lớp, hoặc biến — giúp chia nhỏ chương trình lớn thành các phần dễ quản lý hơn.

Ví dụ:

```python
# file: mymodule.py
def say_hello(name):
    print(f"Hello, {name}!")
```

Sử dụng trong file khác:

```python
import mymodule

mymodule.say_hello("Alice")
```

---

## 🧩 **2. Import module**

### ✅ Cú pháp cơ bản:

```python
import module_name
```

Gọi hàm:

```python
module_name.function_name()
```

### 🔹 Import với tên rút gọn (alias):

```python
import math as m
print(m.sqrt(25))
```

### 🔹 Import trực tiếp hàm/lớp:

```python
from math import sqrt, pi
print(sqrt(16))
print(pi)
```

### 🔹 Import tất cả (ít khuyến khích):

```python
from math import *
print(sin(pi/2))
```

---

## 🧮 **3. Một số thư viện chuẩn phổ biến**

| Thư viện   | Chức năng chính                           | Ví dụ                                             |
| ---------- | ----------------------------------------- | ------------------------------------------------- |
| `math`     | Các phép toán học                         | `math.sqrt(9)`, `math.pi`, `math.pow(2,3)`        |
| `os`       | Làm việc với hệ điều hành (thư mục, file) | `os.getcwd()`, `os.listdir()`, `os.mkdir("test")` |
| `datetime` | Làm việc với thời gian và ngày tháng      | `datetime.datetime.now()`                         |

Ví dụ:

```python
import os, math, datetime

print(os.getcwd())                # Đường dẫn hiện tại
print(math.factorial(5))          # 5! = 120
print(datetime.datetime.now())    # Thời gian hiện tại
```

Xem chi tiết cách sử dụng các module:

- [Module Match](./module-mathch.md)
- [Module Datetime](./module-datetime.md)
- [Module OS](./module-os.md)

Danh sách `Built-in Modules`: https://www.w3schools.com/python/python_ref_modules.asp

---

## 📦 **4. Tạo module riêng**

Bạn có thể **tự tạo module** để tái sử dụng code.

Ví dụ:

```
project/
│
├── mymath.py
└── main.py
```

**File: `mymath.py`**

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
```

**File: `main.py`**

```python
import mymath

print(mymath.add(5, 3))
print(mymath.subtract(10, 4))
```

📘 *Khi bạn import, Python sẽ tìm file `mymath.py` trong cùng thư mục hoặc thư viện hệ thống.*

---

## 📁 **5. Package trong Python**

### 🔹 Định nghĩa:

> **Package** là một **thư mục chứa nhiều module**, có file đặc biệt `__init__.py` (có thể rỗng).

Cấu trúc ví dụ:

```
project/
│
├── utils/
│   ├── __init__.py
│   ├── math_utils.py
│   └── string_utils.py
└── main.py
```

**File: `math_utils.py`**

```python
def square(x):
    return x * x
```

**File: `string_utils.py`**

```python
def to_upper(s):
    return s.upper()
```

**File: `main.py`**

```python
from utils.math_utils import square
from utils.string_utils import to_upper

print(square(5))
print(to_upper("hello"))
```

---

## 🧠 **6. Tổ chức dự án nhỏ**

Một dự án Python thường gồm:

```
my_project/
│
├── data/                # Dữ liệu
├── modules/             # Các module tự tạo
│   ├── __init__.py
│   └── helper.py
├── main.py              # File chính
└── requirements.txt     # Danh sách thư viện cần cài
```

**File: modules/helper.py**

```python
def greet(name):
    return f"Xin chào {name}"
```

**File: main.py**

```python
from modules.helper import greet

print(greet("Lan"))
```

---

## 🧩 **7. Ôn tập Python cơ bản (Buổi 1–8)**

| Chủ đề              | Nội dung chính                                 |
| ------------------- | ---------------------------------------------- |
| Biến & Kiểu dữ liệu | `int`, `float`, `str`, `bool`                  |
| Toán tử             | Số học, logic, so sánh                         |
| Cấu trúc điều khiển | `if`, `elif`, `else`                           |
| Vòng lặp            | `for`, `while`, `range`, `break`, `continue`   |
| Cấu trúc dữ liệu    | `list`, `tuple`, `set`, `dict`                 |
| Hàm                 | `def`, `return`, `*args`, `**kwargs`, `lambda` |
| Xử lý ngoại lệ      | `try`, `except`, `finally`, `raise`            |
| File I/O            | `open()`, `read()`, `write()`                  |
| Module & Package    | `import`, `from`, `as`, tổ chức dự án          |

---

## 💻 **8. Bài tập thực hành gợi ý**

1. **Bài 1:**
   Tạo module `math_utils.py` chứa các hàm `add`, `subtract`, `multiply`, `divide`.
   Gọi và sử dụng chúng trong `main.py`.

2. **Bài 2:**
   Tạo package `student/` gồm 2 file:

   * `info.py`: hàm `print_info(name, age)`
   * `score.py`: hàm `average(scores: list)`

   Gọi các hàm trong `main.py`.

3. **Bài 3:**
   Sử dụng các module `math`, `os`, `datetime` để:

   * In ngày giờ hiện tại
   * Tính căn bậc hai một số
   * Hiển thị thư mục hiện tại

