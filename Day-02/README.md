# 🧠 **Buổi 2: Biến & Kiểu dữ liệu**


## 1️⃣ Khái niệm về **biến (variable)**

**Biến** là một “tên” dùng để **lưu trữ dữ liệu** trong bộ nhớ máy tính.
Hiểu đơn giản: Biến giống như một “hộp” có nhãn, bạn có thể đặt một giá trị vào hộp đó và dùng lại sau này.

### 🧩 Cú pháp khai báo biến trong Python:

```python
ten_bien = gia_tri
```

> ✅ Python **tự động nhận biết kiểu dữ liệu**, bạn không cần khai báo kiểu trước như các ngôn ngữ C, Java.

### 💡 Ví dụ:

```python
name = "Tom"
age = 20
height = 1.75
is_student = True
```

### 🔤 Quy tắc đặt tên biến:

* Tên biến chỉ bao gồm **chữ cái, số và dấu gạch dưới** `_`.
* **Không được bắt đầu bằng số**.
* **Phân biệt chữ hoa và chữ thường** (`Name` khác `name`).
* Không được trùng với **từ khóa** của Python (như `if`, `for`, `class`, …).

### 💬 Ví dụ tên hợp lệ và không hợp lệ:

```python
# ✅ Hợp lệ
ten = "An"
so_tuoi = 25
diem_trung_binh = 8.5
is_active = True

# ❌ Không hợp lệ
2so = 5          # bắt đầu bằng số
ten-hoc-sinh = "Nam"   # có dấu gạch ngang
for = "abc"      # trùng từ khóa
```

---

## 2️⃣ **Kiểu dữ liệu cơ bản trong Python**

Python có nhiều kiểu dữ liệu, nhưng phổ biến nhất cho người mới là:

| Kiểu dữ liệu | Ví dụ giá trị         | Giải thích                  |
| ------------ | --------------------- | --------------------------- |
| `int`        | `10`, `-5`, `0`       | Số nguyên                   |
| `float`      | `3.14`, `-0.5`        | Số thực (có phần thập phân) |
| `str`        | `"Hello"`, `'Python'` | Chuỗi ký tự                 |
| `bool`       | `True`, `False`       | Kiểu logic (đúng / sai)     |

---

### 🔹 Ví dụ minh họa:

```python
a = 10           # int
b = 3.5          # float
c = "Xin chào"   # str
d = True         # bool

print(type(a))
print(type(b))
print(type(c))
print(type(d))
```

### 📤 Kết quả:

```
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
```

---

## 3️⃣ **Ép kiểu dữ liệu (Type Casting)**

Khi cần chuyển đổi dữ liệu từ kiểu này sang kiểu khác, ta dùng các hàm sau:

| Hàm       | Chuyển sang kiểu |
| --------- | ---------------- |
| `int()`   | Số nguyên        |
| `float()` | Số thực          |
| `str()`   | Chuỗi            |
| `bool()`  | Boolean          |

### 🔸 Ví dụ:

```python
x = 3.14
y = int(x)      # chuyển float sang int → 3
z = str(y)      # chuyển int sang chuỗi → "3"

print(x, y, z)
```

### 💬 Lưu ý:

* Ép kiểu sai có thể gây lỗi:

```python
int("abc")  # ❌ Lỗi vì không thể chuyển chữ thành số
```

---

## 4️⃣ **Nhập và xuất dữ liệu**

### 🧭 Xuất dữ liệu – `print()`

```python
print("Xin chào Python!")
print("Tôi tên là", name)
```

> Hàm `print()` có thể in nhiều giá trị, cách nhau bằng dấu `,`.

### 💡 Ví dụ:

```python
ten = "Lan"
tuoi = 18
print("Tên:", ten, "- Tuổi:", tuoi)
```

📤 **Kết quả:**

```
Tên: Lan - Tuổi: 18
```

---

### 🧭 Nhập dữ liệu – `input()`

Hàm `input()` cho phép người dùng nhập dữ liệu từ bàn phím, và **luôn trả về kiểu chuỗi (`str`)**.

```python
ten = input("Nhập tên của bạn: ")
print("Xin chào", ten)
```

📤 Kết quả:

```
Nhập tên của bạn: An
Xin chào An
```

Ví dụ về Nhiều input một lần:

```python
animal = input("What is your favorite animal:")
color = input("What is your favorite color:")
number = input("What is your favorite number:")
print(animal, color, number)
```


### 🧮 Muốn nhập số → cần ép kiểu:


> 🧩 **Lưu ý:** `input()` **luôn trả về kiểu chuỗi (`str`)**
> Nếu bạn muốn dùng làm số, phải **ép kiểu**.


```python
tuoi = int(input("Nhập tuổi: "))
print("Năm sau bạn sẽ", tuoi + 1, "tuổi")
```

---

## 5️⃣ **Toán tử số học**

| Toán tử | Ý nghĩa              | Ví dụ    | Kết quả |
| ------- | -------------------- | -------- | ------- |
| `+`     | Cộng                 | `5 + 2`  | `7`     |
| `-`     | Trừ                  | `5 - 2`  | `3`     |
| `*`     | Nhân                 | `5 * 2`  | `10`    |
| `/`     | Chia                 | `5 / 2`  | `2.5`   |
| `//`    | Chia lấy phần nguyên | `5 // 2` | `2`     |
| `%`     | Chia lấy dư          | `5 % 2`  | `1`     |
| `**`    | Lũy thừa             | `2 ** 3` | `8`     |

### 💡 Ví dụ:

```python
a = 10
b = 3
print(a + b)   # 13
print(a / b)   # 3.3333
print(a // b)  # 3
print(a ** b)  # 1000
```

---

## 6️⃣ **Chuỗi và các phương thức xử lý chuỗi**

### 📍 Tạo chuỗi:

```python
s1 = 'Hello'
s2 = "Python"
s3 = """Chuỗi
nhiều dòng"""
```

### 📍 Nối chuỗi:

```python
name = "An"
message = "Xin chào " + name
print(message)
```

### 📍 Lặp chuỗi:

```python
print("Hi! " * 3)
# Kết quả: Hi! Hi! Hi!
```

### 📍 Truy cập ký tự:

```python
text = "Python"
print(text[0])    # P
print(text[-1])   # n (ký tự cuối)
```

### 📍 Một số phương thức thông dụng:

| Phương thức       | Chức năng                 | Ví dụ                                       |
| ----------------- | ------------------------- | ------------------------------------------- |
| `len(s)`          | Độ dài chuỗi              | `len("Python")` → `6`                       |
| `s.upper()`       | Viết hoa                  | `"abc".upper()` → `"ABC"`                   |
| `s.lower()`       | Viết thường               | `"HELLO".lower()` → `"hello"`               |
| `s.title()`       | Viết hoa chữ cái đầu      | `"xin chao".title()` → `"Xin Chao"`         |
| `s.strip()`       | Xóa khoảng trắng đầu/cuối | `"  hi ".strip()` → `"hi"`                  |
| `s.replace(a, b)` | Thay thế                  | `"python".replace("py", "my")` → `"mython"` |
| `s.split()`       | Tách chuỗi thành list     | `"a,b,c".split(",")` → `["a", "b", "c"]`    |

---

## 7️⃣ **Thực hành mini: nhập thông tin và tính toán**

### 🔹 Bài tập 1: Nhập và in thông tin

```python
name = input("Nhập tên của bạn: ")
age = int(input("Nhập tuổi của bạn: "))

print("Xin chào", name + "!")
print("Năm sau bạn sẽ", age + 1, "tuổi.")
```

### 🔹 Bài tập 2: Tính chu vi và diện tích hình chữ nhật

```python
width = float(input("Nhập chiều rộng: "))
height = float(input("Nhập chiều cao: "))

chu_vi = 2 * (width + height)
dien_tich = width * height

print("Chu vi:", chu_vi)
print("Diện tích:", dien_tich)
```

---
