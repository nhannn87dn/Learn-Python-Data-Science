# Hướng dẫn nhanh — Sử dụng module `os` trong Python (vài phương thức phổ biến)


## 1 Import

```python
import os
```

---

## 2 Thông tin hệ và môi trường

* `os.name` — tên kiểu hệ (ví dụ `'posix'` cho Linux/macOS, `'nt'` cho Windows).
* `os.environ` — dict-like chứa biến môi trường.
* `os.getenv('VAR', default=None)` — lấy biến môi trường an toàn.

```python
print(os.name)                # 'posix' hoặc 'nt'
print(os.getenv('HOME'))      # thư mục home (Unix) hoặc None
print(os.environ.get('PATH')) # PATH
```

> Lưu ý: thay đổi `os.environ['VAR'] = 'value'` chỉ ảnh hưởng trong tiến trình hiện tại.

---

## 3 Làm việc với thư mục hiện tại

* `os.getcwd()` — lấy current working directory.
* `os.chdir(path)` — thay đổi current working directory.

```python
cwd = os.getcwd()
print("Current:", cwd)

os.chdir('/tmp')  # ví dụ trên Linux/macOS
print("Now:", os.getcwd())
```

---

## 4 Tạo / xóa thư mục

* `os.mkdir(path)` — tạo 1 thư mục (sẽ lỗi nếu thư mục cha không tồn tại).
* `os.makedirs(path, exist_ok=False)` — tạo thư mục nhiều cấp; `exist_ok=True` để không lỗi nếu đã tồn tại.
* `os.rmdir(path)` — xóa thư mục rỗng.
* `shutil.rmtree(path)` — xóa thư mục có nội dung (dùng `import shutil`).

```python
import shutil

os.makedirs('data/2025/logs', exist_ok=True)
# xóa rỗng:
os.rmdir('data/2025/logs')  # chỉ khi rỗng
# xóa cả cây thư mục:
shutil.rmtree('data')       # cẩn thận!
```

---

## 5 Liệt kê file / thư mục

* `os.listdir(path='.')` — trả list tên (file + thư mục) trong đường dẫn.
* `os.scandir(path)` — trả iterator với thông tin file (fast).
* `os.walk(top)` — duyệt cây thư mục (tốt để tìm mọi file con).

```python
for name in os.listdir('.'):
    print(name)

# dùng scandir để phân biệt file/dir nhanh:
with os.scandir('.') as it:
    for entry in it:
        print(entry.name, 'is_file=', entry.is_file(), 'is_dir=', entry.is_dir())

# walk:
for dirpath, dirnames, filenames in os.walk('.'):
    print(dirpath, 'contains', len(filenames), 'files')
```

---

## 6 Kiểm tra tồn tại / loại file

* `os.path.exists(path)` — tồn tại (file hoặc thư mục).
* `os.path.isfile(path)` — là file.
* `os.path.isdir(path)` — là thư mục.
* `os.path.getsize(path)` — kích thước (byte).
* `os.path.abspath(path)` — đường dẫn tuyệt đối.
* `os.path.join(a, b, ...)` — nối đường dẫn an toàn (cross-platform).
* `os.path.splitext(path)` — tách tên và phần mở rộng.

```python
p = 'example.txt'
print(os.path.exists(p))
print(os.path.isfile(p))
print(os.path.abspath(p))
name, ext = os.path.splitext(p)
print(name, ext)
full = os.path.join('/home/user', 'docs', 'file.txt')
```

---

## 7 Đổi tên và xóa file

* `os.rename(src, dst)` — đổi tên (hoặc di chuyển).
* `os.remove(path)` hoặc `os.unlink(path)` — xóa file.

```python
if os.path.exists('old.txt'):
    os.rename('old.txt', 'new.txt')

if os.path.isfile('new.txt'):
    os.remove('new.txt')
```

---

## 8 Thông tin file (metadata)

* `os.stat(path)` — trả `os.stat_result`, gồm kích thước, thời gian sửa, mode (permission), v.v.

```python
st = os.stat('somefile.txt')
print("Size:", st.st_size)
print("Modified:", st.st_mtime)  # epoch seconds; dùng datetime để chuyển đổi
```

---

## 9 Duyệt và lọc file ví dụ — lấy tất cả `.py` trong thư mục (không đệ quy)

```python
py_files = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith('.py')]
print(py_files)
```

Với đệ quy dùng `os.walk`:

```python
py_files = []
for dirpath, _, filenames in os.walk('src'):
    for fn in filenames:
        if fn.endswith('.py'):
            py_files.append(os.path.join(dirpath, fn))
```

---

## 10 Thực thi lệnh hệ thống (ghi nhớ: `subprocess` thường an toàn hơn)

* `os.system(cmd)` — đơn giản, trả code thoát; không an toàn cho dữ liệu nhập không tin cậy.
* Khuyến nghị dùng `subprocess.run([...])` cho tuỳ chọn an toàn và kiểm soát đầu ra.

```python
import os
os.system('echo Hello from os.system')

# tốt hơn:
import subprocess
subprocess.run(['echo', 'Hello from subprocess'], check=True)
```

---

## Mẹo & lưu ý

* Dùng `os.path.join` thay vì nối chuỗi thủ công để giữ tương thích Windows/Linux.
* Tránh dùng `os.system` với dữ liệu từ user (nguy cơ injection). Dùng `subprocess` với list args.
* `os` thao tác file hệ thống — luôn kiểm tra `exists()` trước khi xóa/đổi tên.
* Với thao tác xóa cây thư mục dùng `shutil.rmtree` rất mạnh — cẩn thận.
* `pathlib` (Python 3.4+) cung cấp API hướng đối tượng cho đường dẫn và thường dễ dùng hơn `os.path`. (Ví dụ: `from pathlib import Path`)

---

## Tóm tắt mẫu nhanh (snippet tổng hợp)

```python
import os

# in cwd và liệt kê
print("CWD:", os.getcwd())
print(os.listdir('.'))

# tạo thư mục an toàn
os.makedirs('out/reports', exist_ok=True)

# tạo file thử
p = os.path.join('out', 'reports', 'readme.txt')
with open(p, 'w', encoding='utf-8') as f:
    f.write("Hello\n")

# check và in info
if os.path.exists(p):
    print("File size:", os.path.getsize(p))
    print("Absolute path:", os.path.abspath(p))

# xóa file
os.remove(p)
```

---
