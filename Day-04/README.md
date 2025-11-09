# 🧠 **Buổi 4: Vòng lặp**

Vòng lặp dùng để **lặp lại một khối lệnh nhiều lần** mà không cần viết lại cùng một đoạn code.
Python có 2 loại vòng lặp chính:

* `for` – dùng khi **biết trước số lần lặp**
* `while` – dùng khi **chưa biết trước số lần lặp**, chỉ dừng khi điều kiện sai


---

## 1️⃣ **Hàm `range()` trong Python**

`range()` là hàm **tạo ra một dãy số nguyên** — thường được dùng trong **vòng lặp `for`**.

### 🔹 Cú pháp:

```python
range(stop)
range(start, stop)
range(start, stop, step)
```

| Tham số | Ý nghĩa                              |
| ------- | ------------------------------------ |
| `start` | Giá trị bắt đầu (mặc định là 0)      |
| `stop`  | Giá trị kết thúc **(không bao gồm)** |
| `step`  | Bước nhảy (mặc định là 1)            |

### 💡 Ví dụ:

```python
print(list(range(5)))         # [0, 1, 2, 3, 4]
print(list(range(2, 6)))      # [2, 3, 4, 5]
print(list(range(1, 10, 2)))  # [1, 3, 5, 7, 9]
```

> ⚠️ Ghi nhớ: `range()` **không bao gồm giá trị stop**.
> Ví dụ `range(1, 5)` → 1, 2, 3, 4

---

## 2️⃣ **Vòng lặp `for`**

### 🔹 Cú pháp:

```python
for biến in dãy:
    # khối lệnh được lặp
```

Vòng lặp `for` sẽ **duyệt qua từng phần tử** trong dãy (list, chuỗi, hoặc `range`).

### 💡 Ví dụ 1: Duyệt dãy số với `range()`

```python
for i in range(5):
    print("Lần lặp:", i)
```

📤 Kết quả:

```
Lần lặp: 0
Lần lặp: 1
Lần lặp: 2
Lần lặp: 3
Lần lặp: 4
```

---

### 💡 Ví dụ 2: Duyệt danh sách

```python
names = ["An", "Bình", "Chi"]
for name in names:
    print("Xin chào", name)
```

📤 Kết quả:

```
Xin chào An  
Xin chào Bình  
Xin chào Chi
```

---

### 💡 Ví dụ 3: Tính tổng từ 1 đến n

```python
n = int(input("Nhập n: "))
tong = 0

for i in range(1, n + 1):
    tong += i

print("Tổng từ 1 đến", n, "là:", tong)
```

---

## 3️⃣ **Vòng lặp `while`**

Vòng lặp `while` dùng khi **chưa biết trước số lần lặp**, và **chạy cho đến khi điều kiện sai**.

### 🔹 Cú pháp:

```python
while điều_kiện:
    # khối lệnh
```

### 💡 Ví dụ 1:

```python
i = 1
while i <= 5:
    print("Giá trị i =", i)
    i += 1
```

📤 Kết quả:

```
Giá trị i = 1  
Giá trị i = 2  
Giá trị i = 3  
Giá trị i = 4  
Giá trị i = 5
```

---

### 💡 Ví dụ 2: Tính tổng với `while`

```python
n = int(input("Nhập n: "))
tong = 0
i = 1

while i <= n:
    tong += i
    i += 1

print("Tổng từ 1 đến", n, "là:", tong)
```

---

## 4️⃣ **Lệnh điều khiển vòng lặp**

### 🔸 `break` — dừng vòng lặp ngay lập tức

```python
for i in range(1, 10):
    if i == 5:
        break
    print(i)
```

📤 Kết quả:

```
1
2
3
4
```

---

### 🔸 `continue` — bỏ qua vòng lặp hiện tại, sang lần kế tiếp

```python
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
```

📤 Kết quả:

```
1
2
4
5
```

---

### 🔸 `else` trong vòng lặp

Câu lệnh `else` sẽ chạy **khi vòng lặp kết thúc bình thường (không bị break)**.

```python
for i in range(3):
    print("Lần lặp", i)
else:
    print("Hoàn tất vòng lặp.")
```

📤 Kết quả:

```
Lần lặp 0
Lần lặp 1
Lần lặp 2
Hoàn tất vòng lặp.
```

Nếu có `break`, phần `else` **không được thực hiện**:

```python
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("Hoàn tất!")  # Không in
```

---

## 5️⃣ **Kết hợp điều kiện trong vòng lặp**

Bạn có thể dùng `if` trong vòng lặp để lọc dữ liệu hoặc thực hiện hành động có điều kiện.

### 💡 Ví dụ: In các số chẵn từ 1 đến 10

```python
for i in range(1, 11):
    if i % 2 == 0:
        print(i)
```

📤 Kết quả:

```
2
4
6
8
10
```

---

## 6️⃣ **Thực hành tổng hợp**

### 🔹 Bài 1: Tính tổng các số lẻ từ 1 đến n

```python
n = int(input("Nhập n: "))
tong = 0

for i in range(1, n + 1):
    if i % 2 != 0:
        tong += i

print("Tổng các số lẻ từ 1 đến", n, "là:", tong)
```

---

### 🔹 Bài 2: Kiểm tra số nguyên tố

```python
n = int(input("Nhập số n: "))

if n < 2:
    print(n, "không phải là số nguyên tố.")
else:
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            print(n, "không phải là số nguyên tố.")
            break
    else:
        print(n, "là số nguyên tố.")
```

---

### 🔹 Bài 3: Tìm giá trị lớn nhất trong danh sách

```python
numbers = [3, 7, 1, 9, 4, 8]
max_num = numbers[0]

for num in numbers:
    if num > max_num:
        max_num = num

print("Giá trị lớn nhất là:", max_num)
```

---

### 🔹 Bài 4: Đếm số phần tử thỏa điều kiện

```python
numbers = [1, 5, 8, 3, 10, 7]
count = 0

for n in numbers:
    if n > 5:
        count += 1

print("Có", count, "số lớn hơn 5 trong danh sách.")
```
