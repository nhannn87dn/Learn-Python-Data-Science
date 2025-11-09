# 🧩 **Buổi 1: Giới thiệu & Môi trường lập trình Python**

---

## 🎯 Mục tiêu buổi học

Sau buổi này, bạn sẽ:

* Hiểu **Python là gì** và **vì sao nên học Python**.
* Cài đặt và thiết lập **môi trường lập trình** (Python, pip, VSCode hoặc Jupyter Notebook).
* Biết cách **chạy chương trình Python** cơ bản.
* Sử dụng được các lệnh cơ bản `print()` và `input()`.
* Viết chương trình đầu tiên: **nhập tên, tuổi và in lời chào**.

---

## 🧠 1. Giới thiệu về Python

### 1.1 Python là gì?

**Python** là một ngôn ngữ lập trình **bậc cao, thông dịch, đa năng và dễ học**.
Nó được tạo ra vào năm **1991** bởi **Guido van Rossum** với triết lý “*Simple is better than complex*”.

Python được sử dụng trong rất nhiều lĩnh vực:

* 🌐 **Lập trình web:** Django, Flask
* 📊 **Phân tích dữ liệu & AI:** Pandas, NumPy, TensorFlow, scikit-learn
* 🧩 **Tự động hóa (Automation):** viết script quản lý hệ thống
* 🔬 **Khoa học, thống kê, tài chính:** xử lý và phân tích dữ liệu lớn
* 🎮 **Phát triển game:** Pygame

> ✅ Python được đánh giá là ngôn ngữ **phổ biến nhất thế giới** (theo TIOBE Index, StackOverflow Survey).

---

### 1.2 Ưu điểm của Python

| Ưu điểm                   | Giải thích                               |
| ------------------------- | ---------------------------------------- |
| **Dễ học, dễ đọc**        | Cú pháp gần giống ngôn ngữ tự nhiên      |
| **Cộng đồng lớn**         | Nhiều thư viện, tài liệu hỗ trợ          |
| **Đa năng**               | Dùng cho web, data, AI, game, automation |
| **Miễn phí, mã nguồn mở** | Dễ cài đặt, hỗ trợ mọi hệ điều hành      |

---

### 1.3 Nhược điểm

| Nhược điểm                           | Ghi chú                                          |
| ------------------------------------ | ------------------------------------------------ |
| Chạy chậm hơn C/Java                 | Do Python là ngôn ngữ thông dịch                 |
| Không phù hợp cho app mobile native  | Không phổ biến cho Android/iOS                   |
| Quản lý bộ nhớ tự động, ít kiểm soát | Đôi khi tốn tài nguyên hơn các ngôn ngữ thấp cấp |

---

### 1.4 Vì sao nên học Python đầu tiên?

* Cú pháp đơn giản, giúp bạn **tập trung vào tư duy lập trình** hơn là cú pháp phức tạp.
* Dễ chuyển sang các ngôn ngữ khác sau này (JavaScript, C#, Java...).
* Là nền tảng quan trọng để học **Khoa học dữ liệu (Data Science)**, **AI**, **Machine Learning**.

---

## 🧰 2. Cài đặt môi trường lập trình

### 2.1 Cài đặt Python

* Truy cập: [https://www.python.org/downloads/](https://www.python.org/downloads/)
* Chọn **Python 3.x** mới nhất → cài đặt.
* ✅ Nhớ tick **“Add Python to PATH”** khi cài (rất quan trọng).

Sau khi cài, mở Terminal (hoặc Command Prompt) gõ:

```bash
python --version
```

Kết quả hiển thị:

```
Python 3.12.x
```

---

### 2.2 Kiểm tra và cài pip

`pip` là trình quản lý thư viện trong Python (giống npm trong Node.js).
Kiểm tra:

```bash
pip --version
```

Cài mới hoặc nâng cấp:

```bash
python -m ensurepip --upgrade
```

---

### 2.3 Cài Visual Studio Code (VSCode)

1. Tải tại: [https://code.visualstudio.com/](https://code.visualstudio.com/)
2. Cài extension **Python (Microsoft)**
3. Tạo file mới `main.py`, nhập:

   ```python
   print("Hello, Python!")
   ```

4. Chạy code: Nhấn **Run ▶** hoặc `Ctrl + F5`.

---


## 💻 3. Chạy chương trình Python

### 3.1 Cách 1 — Chạy file `.py`

Tạo file `hello.py`:

```python
print("Hello, Python!")
```

Chạy trong Terminal:

```bash
python hello.py
```

Kết quả:

```
Hello, Python!
```

---

### 3.2 Cách 2 — Dùng Interactive Shell

Gõ `python` trong terminal, bạn sẽ thấy dấu nhắc `>>>`

```bash
>>> 2 + 3
5
>>> print("Xin chào!")
Xin chào!
```

Thoát shell: gõ `exit()` hoặc `Ctrl + Z` (Windows), `Ctrl + D` (Mac/Linux).

---

## 🪄 4. Làm quen với cú pháp cơ bản

### 4.1 Lệnh `print()`

Lệnh `print()` trong Python dùng để **xuất** (display/output) một giá trị ra màn hình (console) — thường là một chuỗi văn bản hoặc một biến. Ví dụ cơ bản:

```python
print("Hello World!")
```

Kết quả sẽ là:

```
Hello World!
```

Ứng dụng rất phổ biến: khi ta muốn xem dữ liệu, debug, hoặc hiển thị kết quả chương trình.

---

**Cách sử dụng `print()` để in văn bản**

* Bạn có thể gọi `print()` nhiều lần, mỗi lần sẽ tự động xuống dòng mới sau khi in (mặc định). 

  ```python
  print("Hello World!")
  print("I am learning Python.")
  print("It is awesome!")
  ```

  Kết quả sẽ là ba dòng riêng biệt.
* Văn bản phải được đặt trong dấu nháy kép `"` hoặc nháy đơn `'`. Ví dụ:

  ```python
  print("This will work!")
  print('This will also work!')
  ```

  
* Nếu quên dấu nháy, sẽ gây lỗi cú pháp (SyntaxError). Ví dụ:

  ```python
  print(This will cause an error)
  ```

  Sẽ báo lỗi `SyntaxError: invalid syntax.` 

---

**Tùy chỉnh việc xuống dòng – tham số `end`**

Mặc định, `print()` sau mỗi lần in sẽ đưa con trỏ xuống dòng mới. Nhưng nếu muốn **tiếp tục in trên cùng một dòng**, bạn có thể dùng tham số `end`. Ví dụ:

```python
print("Hello World!", end=" ")
print("I will print on the same line.")
```

Kết quả sẽ là:

```
Hello World! I will print on the same line.
```

Lưu ý: ở ví dụ dùng `end=" "` — có thêm một dấu cách để kết quả đẹp hơn. 

---

**Những lưu ý quan trọng khi sử dụng `print()`**

* Phải đặt chuỗi trong dấu nháy đơn `'...'` hoặc nháy kép `"..."`. Nếu không, Python sẽ hiểu bạn muốn in một biến hoặc tên không hợp lệ.
* Khi in nhiều phần tử (ví dụ biến và chuỗi), bạn có thể truyền nhiều tham số vào `print()`, Python sẽ tự thêm dấu cách giữa các phần tử. Ví dụ:

  ```python
  name = "Alice"
  print("Hello", name, "!")
  ```

  Kết quả: `Hello Alice !`

---


### 4.3 Comment trong Python

**Comment** (chú thích) là phần **ghi chú trong mã nguồn** mà **Python sẽ bỏ qua khi chạy chương trình**.
→ Chúng **không ảnh hưởng đến kết quả** của chương trình, chỉ giúp **con người đọc hiểu dễ hơn**.

💡 *Hiểu đơn giản:* comment là lời nhắn dành cho bạn hoặc người khác đọc code sau này.

Ví dụ:

```python
# Đây là một comment
print("Hello, Python!")  # In ra màn hình
```

Kết quả khi chạy:

```
Hello, Python!
```

👉 Dòng bắt đầu bằng `#` sẽ bị Python **bỏ qua hoàn toàn**.

**Cú pháp comment trong Python**

🔹 Comment một dòng (Single-line comment)

Dùng ký tự **`#`** để bắt đầu comment.
Mọi thứ sau dấu `#` sẽ được coi là comment.

Ví dụ:

```python
# Đây là dòng chú thích
x = 5  # Gán giá trị 5 cho biến x
print(x)
```

🔹 Comment nhiều dòng (Multi-line comment)

Python **không có cú pháp riêng** cho comment nhiều dòng như C hay Java (`/* ... */`).
Nhưng có 2 cách làm phổ biến:

**Cách 1: Dùng nhiều dấu `#` liên tiếp**

```python
# Đây là comment dòng 1
# Đây là comment dòng 2
# Đây là comment dòng 3
```

**Cách 2: Dùng chuỗi nhiều dòng (`''' ... '''` hoặc `""" ... """`)**

Python cho phép bạn dùng **chuỗi nhiều dòng** (multi-line string) như một dạng chú thích tạm — thường đặt ở đầu file, đầu hàm, hoặc lớp để mô tả chức năng.

Ví dụ:

```python
"""
Chương trình này in ra lời chào.
Được viết bởi: Tomy
Ngày: 29/10/2025
"""
print("Xin chào!")
```

➡️ Dù thực chất Python coi đây là **chuỗi**, nhưng nếu không gán nó cho biến nào thì nó **không ảnh hưởng đến chương trình**, nên được dùng như comment.

---

## 🧩 5. Bài tập thực hành

Xem link:

## 🧩 6. Hướng dẫn sử dụng Công cụ


### 6.1 Giới thiệu Jupyter Notebook

Jupyter là môi trường chạy code dạng **cell**, rất phổ biến trong Data Science.
Cài đặt:

```bash
pip install jupyterlab
```

Chạy:

```bash
jupyter lab
```

→ Trình duyệt sẽ mở giao diện trực quan, nơi bạn có thể chạy từng dòng code riêng biệt.

---


### 6.21 Jupyter Extention VSCode

Tìm `Jupyter` sau đó cài đặt

### 6.3 Giới thiệu Google Colab

**Google Colab (Colaboratory)** là một môi trường **lập trình Python trực tuyến miễn phí**, do **Google cung cấp**, cho phép bạn:

* Viết và chạy code Python **ngay trên trình duyệt**, **không cần cài đặt gì cả**.
* Sử dụng **máy chủ của Google (CPU, GPU, TPU)** để xử lý dữ liệu hoặc chạy mô hình AI.
* Lưu, chia sẻ, và cộng tác dễ dàng qua **Google Drive** (giống như Google Docs).

> ✅ **Tóm lại:** Colab là “**Jupyter Notebook chạy trên mây**”, giúp bạn học và thực hành Python ở bất cứ đâu.

### Bước 1️⃣ – Truy cập trang Colab

👉 Mở: [https://colab.research.google.com](https://colab.research.google.com)

Nếu bạn đã đăng nhập tài khoản Google, giao diện sẽ hiện lên như sau:

> “Welcome to Colaboratory”
> → Chọn **New Notebook** (hoặc **Tệp → Sổ tay mới / New Notebook**)

---

### Bước 2️⃣ – Làm quen giao diện

| Khu vực                | Chức năng                      |
| ---------------------- | ------------------------------ |
| **Ô code (Code cell)** | Nơi bạn viết code Python       |
| **Ô text (Text cell)** | Viết ghi chú, mô tả, markdown  |
| **Thanh công cụ**      | Chạy code, thêm cell, lưu file |
| **Kết quả thực thi**   | Hiển thị ngay bên dưới ô code  |

> 💡 **Tip:** Nhấn `Shift + Enter` để chạy ô code.

---

### Bước 3️⃣ – Viết chương trình đầu tiên

Thử viết vào một ô code:

```python
print("Hello from Google Colab!")
```

Nhấn `Shift + Enter`
→ Colab sẽ chạy code và hiển thị kết quả ngay bên dưới.

---

### Bước 4️⃣ – Lưu & chia sẻ notebook

* Notebook sẽ được lưu **tự động vào Google Drive** của bạn (trong thư mục *Colab Notebooks*).
* Để đổi tên file: nhấn vào tiêu đề (ví dụ “Untitled0.ipynb”).
* Để chia sẻ: chọn **Share → nhập email người nhận → chọn quyền xem/chỉnh sửa**.

---

## 🔗 Tài liệu tham khảo

* Trang chủ Python: [https://www.python.org/](https://www.python.org/)
* W3Schools Python: [https://www.w3schools.com/python/](https://www.w3schools.com/python/)
* JupyterLab: [https://jupyter.org/](https://jupyter.org/)
