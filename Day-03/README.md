# 🧠 **Buổi 3: Toán tử Logic & Cấu trúc điều khiển**

---

## 1️⃣ **Toán tử so sánh (Comparison Operators)**

Toán tử so sánh được dùng để **so sánh hai giá trị** và **trả về kết quả kiểu `bool`** (`True` hoặc `False`).

| Toán tử | Ý nghĩa           | Ví dụ    | Kết quả |
| ------- | ----------------- | -------- | ------- |
| `==`    | Bằng              | `5 == 5` | `True`  |
| `!=`    | Khác              | `5 != 3` | `True`  |
| `>`     | Lớn hơn           | `7 > 2`  | `True`  |
| `<`     | Nhỏ hơn           | `4 < 1`  | `False` |
| `>=`    | Lớn hơn hoặc bằng | `5 >= 5` | `True`  |
| `<=`    | Nhỏ hơn hoặc bằng | `6 <= 3` | `False` |

### 💡 Ví dụ:

```python
a = 10
b = 20

print(a == b)   # False
print(a != b)   # True
print(a < b)    # True
print(a >= 5)   # True
```

---

## 2️⃣ **Toán tử logic (Logical Operators)**

Dùng để **kết hợp nhiều điều kiện** trong câu lệnh `if`.

| Toán tử | Ý nghĩa                                 | Ví dụ                  | Kết quả |
| ------- | --------------------------------------- | ---------------------- | ------- |
| `and`   | Đúng khi **cả hai** điều kiện đều đúng  | `(a > 5) and (a < 10)` | `True`  |
| `or`    | Đúng khi **ít nhất một** điều kiện đúng | `(a > 10) or (a == 5)` | `False` |
| `not`   | Phủ định kết quả logic                  | `not(a > 5)`           | `False` |

### 💡 Ví dụ:

```python
x = 7
print(x > 5 and x < 10)   # True
print(x > 10 or x == 7)   # True
print(not(x == 7))        # False
```

---

## 3️⃣ **Cấu trúc điều khiển rẽ nhánh (if - elif - else)**

### 🧩 Cấu trúc `if` cơ bản:

```python
if điều_kiện:
    # khối lệnh nếu điều kiện đúng
```

### 💡 Ví dụ:

```python
age = 18
if age >= 18:
    print("Bạn đã đủ 18 tuổi.")
```

---

### 🧩 Cấu trúc `if - else`:

```python
if điều_kiện:
    # khối lệnh nếu đúng
else:
    # khối lệnh nếu sai
```

### 💡 Ví dụ:

```python
n = int(input("Nhập số: "))

if n % 2 == 0:
    print("Đây là số chẵn.")
else:
    print("Đây là số lẻ.")
```

---

### 🧩 Cấu trúc `if - elif - else` (nhiều nhánh):

Dùng khi có **nhiều trường hợp cần kiểm tra**.

```python
if điều_kiện_1:
    # nếu điều kiện 1 đúng
elif điều_kiện_2:
    # nếu điều kiện 1 sai và điều kiện 2 đúng
else:
    # nếu tất cả điều kiện đều sai
```

### 💡 Ví dụ:

```python
score = float(input("Nhập điểm trung bình: "))

if score >= 8.0:
    print("Xếp loại Giỏi")
elif score >= 6.5:
    print("Xếp loại Khá")
elif score >= 5.0:
    print("Xếp loại Trung bình")
else:
    print("Xếp loại Yếu")
```

---

## 4️⃣ **Cấu trúc lồng nhau (Nested if)**

Một `if` có thể được đặt **bên trong** một `if` khác để kiểm tra điều kiện chi tiết hơn.

### 💡 Ví dụ:

```python
age = int(input("Nhập tuổi của bạn: "))

if age >= 18:
    citizen = input("Bạn có phải công dân Việt Nam không (y/n)? ")
    if citizen == "y":
        print("Bạn đủ điều kiện bầu cử.")
    else:
        print("Bạn chưa đủ điều kiện bầu cử.")
else:
    print("Bạn chưa đủ 18 tuổi.")
```

---

## 5️⃣ **Toán tử gán rút gọn (Augmented Assignment)**

| Toán tử | Ý nghĩa     | Ví dụ                            |
| ------- | ----------- | -------------------------------- |
| `+=`    | Cộng và gán | `x += 1` tương đương `x = x + 1` |
| `-=`    | Trừ và gán  | `x -= 2` tương đương `x = x - 2` |
| `*=`    | Nhân và gán | `x *= 3` tương đương `x = x * 3` |
| `/=`    | Chia và gán | `x /= 2` tương đương `x = x / 2` |

### 💡 Ví dụ:

```python
x = 10
x += 5
print(x)  # 15
```

---

## 6️⃣ **Thực hành tổng hợp**

### 🔹 Bài 1: Chương trình tính điểm & xếp loại

```python
name = input("Nhập tên học sinh: ")
score = float(input("Nhập điểm trung bình: "))

if score >= 8.0:
    grade = "Giỏi"
elif score >= 6.5:
    grade = "Khá"
elif score >= 5.0:
    grade = "Trung bình"
else:
    grade = "Yếu"

print("Học sinh:", name)
print("Điểm trung bình:", score)
print("Xếp loại:", grade)
```

---

### 🔹 Bài 2: Tính chiết khấu đơn hàng

```python
total = float(input("Nhập tổng giá trị đơn hàng (VNĐ): "))

if total >= 1000000:
    discount = 0.2     # 20%
elif total >= 500000:
    discount = 0.1     # 10%
elif total >= 200000:
    discount = 0.05    # 5%
else:
    discount = 0

final_price = total * (1 - discount)

print("Chiết khấu:", discount * 100, "%")
print("Số tiền phải trả:", final_price, "VNĐ")
```

---

### 🔹 Bài 3: Kiểm tra điều kiện tam giác

```python
a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))

if a + b > c and a + c > b and b + c > a:
    print("Ba cạnh tạo thành tam giác.")
else:
    print("Không phải tam giác.")
```
