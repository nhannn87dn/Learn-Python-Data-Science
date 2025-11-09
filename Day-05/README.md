# 🧩 **Buổi 5: Cấu trúc dữ liệu List, Tuple, Set**

Trong Python, để lưu trữ và xử lý nhiều giá trị cùng lúc, ta sử dụng **các cấu trúc dữ liệu**:
`list`, `tuple`, và `set`.
Mỗi loại có đặc điểm riêng phù hợp với từng mục đích khác nhau.

---

## 🔹 1. **List (Danh sách)**

### 🧠 **Định nghĩa**

`List` là **một tập hợp có thể thay đổi (mutable)**, **có thứ tự (ordered)**, và có thể chứa **nhiều kiểu dữ liệu khác nhau**.

### 💡 **Cú pháp tạo list**

```python
ten_list = [giatri1, giatri2, giatri3]
```

Ví dụ:

```python
fruits = ["apple", "banana", "cherry"]
numbers = [10, 20, 30, 40]
mixed = ["Tom", 25, True, 3.14]
```

---

### ⚙️ **Truy cập phần tử**

Dùng chỉ số (index), bắt đầu từ **0**.

```python
print(fruits[0])     # apple
print(fruits[-1])    # cherry (truy cập từ cuối)
```

---

### ✏️ **Thay đổi phần tử**

```python
fruits[1] = "orange"
print(fruits)   # ['apple', 'orange', 'cherry']
```

---

### ➕ **Thêm phần tử**

| Phương thức         | Chức năng                | Ví dụ                              |
| ------------------- | ------------------------ | ---------------------------------- |
| `append(x)`         | Thêm vào cuối list       | `fruits.append("mango")`           |
| `insert(i, x)`      | Thêm vào vị trí chỉ định | `fruits.insert(1, "grape")`        |
| `extend(list_khac)` | Nối thêm nhiều phần tử   | `fruits.extend(["kiwi", "melon"])` |

---

### ➖ **Xóa phần tử**

| Cách          | Giải thích               | Ví dụ                    |
| ------------- | ------------------------ | ------------------------ |
| `remove(x)`   | Xóa phần tử có giá trị x | `fruits.remove("apple")` |
| `pop(i)`      | Xóa phần tử tại vị trí i | `fruits.pop(1)`          |
| `del list[i]` | Xóa bằng lệnh `del`      | `del fruits[0]`          |
| `clear()`     | Xóa toàn bộ list         | `fruits.clear()`         |

---

### 🔁 **Duyệt list**

```python
for fruit in fruits:
    print(fruit)
```

---

### 🔢 **Các phương thức hữu ích**

| Phương thức            | Mô tả                            |
| ---------------------- | -------------------------------- |
| `len(list)`            | Trả về độ dài danh sách          |
| `list.sort()`          | Sắp xếp tăng dần                 |
| `list.reverse()`       | Đảo ngược danh sách              |
| `max(list), min(list)` | Giá trị lớn/nhỏ nhất (nếu là số) |
| `sum(list)`            | Tổng các phần tử số              |

Ví dụ:

```python
numbers = [5, 2, 8, 1]
numbers.sort()
print(numbers)  # [1, 2, 5, 8]
```

---

### 🧠 **List Comprehension**

Cách viết gọn để tạo list mới.

```python
squares = [x**2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]
```

---

## 🔸 2. **Tuple (Bộ giá trị)**

### 🧠 **Định nghĩa**

`Tuple` là **tập hợp có thứ tự nhưng không thể thay đổi (immutable)**.
Dùng khi dữ liệu **không cần sửa đổi**.

### 💡 **Cú pháp**

```python
ten_tuple = (giatri1, giatri2, giatri3)
```

Ví dụ:

```python
info = ("Alice", 20, "Female")
```

Nếu chỉ có **1 phần tử**, phải thêm dấu `,`:

```python
single = (5,)   # đúng
```

---

### ⚙️ **Truy cập phần tử**

```python
print(info[0])   # Alice
print(info[-1])  # Female
```

---

### 🧩 **Không thể thay đổi**

```python
info[1] = 25   # ❌ lỗi: TypeError
```

---

### 🔁 **Duyệt tuple**

```python
for item in info:
    print(item)
```

---

### 🧠 **Ứng dụng tuple**

* Dùng cho dữ liệu cố định (VD: ngày tháng, toạ độ,...)
* Có thể dùng làm **key trong dictionary** (vì bất biến)

Ví dụ:

```python
coordinates = (10.5, 20.3)
```

---

## 🔹 3. **Set (Tập hợp)**

### 🧠 **Định nghĩa**

`Set` là **tập hợp không có thứ tự (unordered)** và **không chứa phần tử trùng lặp**.

### 💡 **Cú pháp**

```python
ten_set = {giatri1, giatri2, giatri3}
```

Ví dụ:

```python
colors = {"red", "green", "blue"}
```

---

### ⚙️ **Đặc điểm**

* Không thể truy cập bằng chỉ số.
* Không có phần tử trùng nhau.

```python
nums = {1, 2, 2, 3}
print(nums)   # {1, 2, 3}
```

---

### ➕ **Thêm phần tử**

```python
colors.add("yellow")
```

### ➖ **Xóa phần tử**

```python
colors.remove("red")
colors.discard("pink")   # không báo lỗi nếu không có phần tử
```

---

### 🔢 **Phép toán trên set**

| Toán tử                            | Mô tả             | Ví dụ                     |        |                  |
| ---------------------------------- | ----------------- | ------------------------- | ------ | ---------------- |
| `                                  | `hoặc`.union()`   | Hợp                       | `{1,2} | {2,3}`→`{1,2,3}` |
| `&` hoặc `.intersection()`         | Giao              | `{1,2} & {2,3}` → `{2}`   |        |                  |
| `-` hoặc `.difference()`           | Hiệu              | `{1,2,3} - {2}` → `{1,3}` |        |                  |
| `^` hoặc `.symmetric_difference()` | Phần tử khác nhau | `{1,2} ^ {2,3}` → `{1,3}` |        |                  |

---

### 🔁 **Duyệt set**

```python
for color in colors:
    print(color)
```

---

## 🧪 **Thực hành gợi ý**

1. Nhập danh sách điểm thi của học viên và tính điểm trung bình.
2. Lưu trữ danh sách môn học bằng tuple (vì không đổi).
3. Tạo tập hợp các tên học viên, loại bỏ trùng lặp.

---

### ✅ **Tổng kết so sánh**

| Đặc điểm      | List  | Tuple | Set   |
| ------------- | ----- | ----- | ----- |
| Có thứ tự     | ✅     | ✅     | ❌     |
| Thay đổi được | ✅     | ❌     | ✅     |
| Phần tử trùng | ✅     | ✅     | ❌     |
| Cú pháp       | `[ ]` | `( )` | `{ }` |
