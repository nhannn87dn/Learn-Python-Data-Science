Tuyệt vời 👏 Dưới đây là **bộ câu hỏi ôn tập + mini quiz trắc nghiệm cuối buổi 8** — giúp học viên tự kiểm tra toàn bộ kiến thức Python cơ bản (từ buổi 1–8).

---

# 🧠 **Ôn tập & Mini Quiz – Python Cơ bản (Buổi 8)**

---

## 🧩 **Phần 1: Câu hỏi lý thuyết ngắn**

1. Python là ngôn ngữ **biên dịch** hay **thông dịch**?
2. Biến trong Python có cần khai báo kiểu dữ liệu trước không?
3. Kết quả của biểu thức `3 + 5 * 2` là bao nhiêu?
4. Toán tử `==` khác gì với `=`?
5. Lệnh `input()` trong Python dùng để làm gì?
6. Từ khóa nào dùng để bắt lỗi trong Python?
7. Sự khác nhau giữa `list` và `tuple` là gì?
8. Phép toán `setA & setB` có nghĩa là gì?
9. Trong hàm, `*args` và `**kwargs` dùng để làm gì?
10. Khi mở file bằng `open("data.txt", "w")`, nếu file chưa tồn tại, chuyện gì xảy ra?

---

## 💡 **Phần 2: Trắc nghiệm chọn đáp án đúng**

### 1️⃣

Kết quả của đoạn code sau là gì?

```python
x = 5
y = 2
print(x // y)
```

A. 2.5
B. 2
C. 3
D. 5

✅ **Đáp án:** B → `//` là chia lấy phần nguyên.

---

### 2️⃣

Câu lệnh nào tạo được một **tuple** hợp lệ?
A. `numbers = (1, 2, 3)`
B. `numbers = [1, 2, 3]`
C. `numbers = {1, 2, 3}`
D. `numbers = tuple[1, 2, 3]`

✅ **Đáp án:** A

---

### 3️⃣

Kết quả của đoạn code:

```python
for i in range(2, 5):
    print(i, end=" ")
```

A. `1 2 3 4 5`
B. `2 3 4`
C. `2 3 4 5`
D. `3 4 5`

✅ **Đáp án:** B → `range(2, 5)` tạo dãy từ 2 đến 4.

---

### 4️⃣

Lệnh nào dùng để dừng vòng lặp sớm?
A. `stop`
B. `exit`
C. `break`
D. `continue`

✅ **Đáp án:** C

---

### 5️⃣

Kết quả của đoạn code:

```python
scores = [7, 8, 9]
print(sum(scores)/len(scores))
```

A. 7
B. 8
C. 9
D. Lỗi

✅ **Đáp án:** B → Trung bình = (7+8+9)/3 = 8.0

---

### 6️⃣

Trong Python, `dict` lưu trữ dữ liệu dưới dạng:
A. Danh sách các giá trị
B. Cặp khóa–giá trị
C. Các phần tử không trùng lặp
D. Bộ dữ liệu bất biến

✅ **Đáp án:** B

---

### 7️⃣

Kết quả của:

```python
def add(a, b=3):
    return a + b

print(add(2))
```

A. 5
B. 3
C. Lỗi
D. 2

✅ **Đáp án:** A → Tham số mặc định `b=3`.

---

### 8️⃣

Lệnh nào dùng để bắt lỗi khi chia cho 0?

```python
x = 10
y = 0
____:
    print(x / y)
except ZeroDivisionError:
    print("Lỗi chia cho 0")
```

A. `try`
B. `if`
C. `catch`
D. `raise`

✅ **Đáp án:** A

---

### 9️⃣

Hàm nào trong module `math` trả về căn bậc hai của số?
A. `sqrt()`
B. `pow()`
C. `root()`
D. `square()`

✅ **Đáp án:** A

---

### 🔟

Giả sử có cấu trúc sau:

```
project/
│
├── utils/
│   ├── __init__.py
│   └── helper.py
└── main.py
```

Muốn gọi hàm `hello()` trong `helper.py`, ta viết:

```python
from utils.helper import hello
```

✅ **Đúng** hay ❌ **Sai**?

✅ **Đúng**

---

## 🧠 **Phần 3: Thực hành nhỏ**

### 1️⃣ Viết hàm `calculate_average(scores)` nhận danh sách điểm và trả về điểm trung bình.

Ví dụ:

```python
print(calculate_average([7, 8, 9]))  # 👉 8.0
```

### 2️⃣ Viết chương trình đọc file `students.txt` (mỗi dòng chứa “tên, điểm”)

👉 Tính điểm trung bình của từng học sinh và ghi ra file `result.txt`.

### 3️⃣ Tạo module `converter.py` chứa:

* `km_to_miles(km)`
* `c_to_f(celsius)`

Sau đó import và dùng trong `main.py`.

---

## 🏁 **Gợi ý ôn tập trước buổi nâng cao**

* Ôn lại cú pháp định nghĩa hàm (`def`), `return`.
* Hiểu rõ `for`, `while`, và cách kết hợp với `range()`.
* Luyện tập nhiều về `list`, `dict`, `set`.
* Đọc/ghi file thật với dữ liệu thực tế (ví dụ danh sách sinh viên).
* Thử tự tách code ra nhiều module nhỏ.

