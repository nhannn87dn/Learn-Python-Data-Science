# 🧩 **Buổi 6: Dictionary & Function**

Nội dung chính:

* Lưu trữ dữ liệu theo **cặp khóa–giá trị (key–value)** bằng `dictionary`.
* Viết và sử dụng **hàm** để tái sử dụng mã lệnh, truyền tham số, trả về kết quả.
* Làm quen với `*args`, `**kwargs`, và **hàm lambda**.

---

## 🔹 1. **Dictionary (Từ điển)**

### 🧠 **Định nghĩa**

`Dictionary` là **cấu trúc dữ liệu lưu trữ theo cặp key–value**, trong đó:

* `key` là **duy nhất**, không trùng lặp.
* `value` có thể là **bất kỳ kiểu dữ liệu nào**.
* Là **unordered (không có thứ tự cố định)** trong Python 3.6 trở về trước, nhưng từ 3.7 trở đi thì **giữ nguyên thứ tự chèn vào**.

---

### 💡 **Cú pháp**

```python
ten_dict = {
    "key1": "value1",
    "key2": "value2",
}
```

Ví dụ:

```python
student = {
    "name": "Alice",
    "age": 20,
    "grade": "A"
}
```

---

### ⚙️ **Truy cập phần tử**

```python
print(student["name"])       # Alice
print(student.get("age"))    # 20
```

👉 Dùng `.get()` an toàn hơn vì không lỗi nếu key không tồn tại:

```python
print(student.get("address", "Không có dữ liệu"))
```

---

### ✏️ **Thêm / Sửa giá trị**

```python
student["email"] = "alice@gmail.com"   # thêm
student["age"] = 21                    # sửa
```

---

### ➖ **Xóa phần tử**

| Cách            | Giải thích            | Ví dụ                  |
| --------------- | --------------------- | ---------------------- |
| `pop(key)`      | Xóa và trả về giá trị | `student.pop("grade")` |
| `del dict[key]` | Xóa phần tử theo key  | `del student["age"]`   |
| `clear()`       | Xóa toàn bộ           | `student.clear()`      |

---

### 🔁 **Duyệt dictionary**

```python
# Duyệt key
for key in student:
    print(key)

# Duyệt value
for value in student.values():
    print(value)

# Duyệt cả key và value
for key, value in student.items():
    print(key, ":", value)
```

---

### 🧠 **Các phương thức hữu ích**

| Phương thức     | Mô tả                          |
| --------------- | ------------------------------ |
| `keys()`        | Lấy danh sách key              |
| `values()`      | Lấy danh sách value            |
| `items()`       | Lấy danh sách cặp (key, value) |
| `update(dict2)` | Gộp dictionary khác            |

Ví dụ:

```python
student.update({"age": 22, "major": "IT"})
```

---

### 💡 **Ứng dụng thực tế**

Lưu dữ liệu có cấu trúc, ví dụ:

```python
students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 90},
    {"name": "Charlie", "score": 78},
]
```

---

## 🔸 2. **Hàm (Function)**

### 🧠 **Định nghĩa**

Hàm là **một khối mã (code block)** có thể **tái sử dụng** nhiều lần.
Giúp chương trình **ngắn gọn**, **dễ đọc**, **dễ bảo trì**.

---

### 💡 **Cú pháp**

```python
def ten_ham(tham_so1, tham_so2, ...):
    # thân hàm
    return gia_tri
```

Ví dụ:

```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))
```

---

### ⚙️ **Tham số và giá trị trả về**

```python
def tinh_tong(a, b):
    return a + b

result = tinh_tong(3, 5)
print(result)   # 8
```

Nếu hàm không có `return`, Python trả về `None`.

---

### 🔁 **Tham số mặc định**

```python
def say_hello(name="User"):
    print(f"Hello, {name}!")

say_hello()        # Hello, User!
say_hello("Tom")   # Hello, Tom!
```

---

## 🌟 **3. `*args` và `**kwargs`**

### 🧩 **`*args` – nhận nhiều tham số không định danh**

Cho phép truyền **số lượng đối số không cố định**.

```python
def tong(*args):
    print(args)         # args là tuple
    return sum(args)

print(tong(1, 2, 3, 4))  # 10
```

---

### 🧩 **`**kwargs` – nhận nhiều tham số có tên**

Lưu dưới dạng **dictionary**.

```python
def thong_tin(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

thong_tin(name="Alice", age=20, city="Hanoi")
```

Kết quả:

```
name: Alice
age: 20
city: Hanoi
```

---

## ⚡ **4. Lambda Function (Hàm ẩn danh)**

### 🧠 **Định nghĩa**

Là **hàm ngắn gọn**, không cần `def`, thường dùng trong biểu thức nhanh.

### 💡 **Cú pháp**

```python
lambda thamso: bieu_thuc
```

Ví dụ:

```python
square = lambda x: x**2
print(square(5))  # 25
```

Ứng dụng với `map()`, `filter()`, `sorted()`:

```python
nums = [1, 2, 3, 4, 5]
doubles = list(map(lambda x: x*2, nums))
print(doubles)  # [2, 4, 6, 8, 10]
```

---

## 🧪 **5. Thực hành gợi ý**

### 🧭 **Bài 1:**

Viết hàm `student_info()` nhận vào dictionary chứa thông tin sinh viên, in ra:

```python
# Input
student = {"name": "Alice", "age": 20, "score": 85}

# Output
Name: Alice
Age: 20
Score: 85
```

---

### 🧭 **Bài 2:**

Viết hàm `tinh_trung_binh(*args)` nhận nhiều điểm thi và trả về điểm trung bình.

---

### 🧭 **Bài 3:**

Viết hàm `loc_hoc_sinh(danh_sach, diem_min)` trả về danh sách học sinh có điểm ≥ `diem_min`.

Ví dụ:

```python
students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 60},
    {"name": "Charlie", "score": 90},
]
```

Kết quả:

```python
loc_hoc_sinh(students, 80)
# [{'name': 'Alice', 'score': 85}, {'name': 'Charlie', 'score': 90}]
```

---

## ✅ **Tổng kết**

| Khái niệm      | Mục đích                  | Cú pháp              |
| -------------- | ------------------------- | -------------------- |
| **Dictionary** | Lưu trữ dữ liệu key–value | `{key: value}`       |
| **Hàm**        | Tổ chức code, tái sử dụng | `def ten_ham(...):`  |
| **`*args`**    | Nhiều tham số không tên   | `def ham(*args):`    |
| **`**kwargs`** | Nhiều tham số có tên      | `def ham(**kwargs):` |
| **Lambda**     | Hàm ngắn gọn, 1 dòng      | `lambda x: x + 1`    |
