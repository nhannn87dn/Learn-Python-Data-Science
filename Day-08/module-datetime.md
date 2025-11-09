# 🕒 **Module `datetime` trong Python**

---

## 1️⃣ Giới thiệu

Module **`datetime`** giúp làm việc với **ngày (date)**, **giờ (time)** và **thời điểm (datetime)** trong Python.
Bạn có thể:

* Lấy thời gian hiện tại
* Cộng/trừ ngày giờ
* Định dạng ngày giờ thành chuỗi (string)
* Chuyển chuỗi về dạng `datetime`

👉 Import cơ bản:

```python
import datetime
```

---

## 2️⃣ Các lớp chính trong `datetime`

| Lớp                  | Mô tả                                                 |
| -------------------- | ----------------------------------------------------- |
| `datetime.date`      | Đại diện cho ngày (năm, tháng, ngày)                  |
| `datetime.time`      | Đại diện cho thời gian (giờ, phút, giây, microsecond) |
| `datetime.datetime`  | Kết hợp cả ngày và giờ                                |
| `datetime.timedelta` | Hiệu hoặc khoảng cách giữa hai thời điểm              |
| `datetime.timezone`  | Đại diện cho múi giờ                                  |

---

## 3️⃣ Lớp `date` — làm việc với ngày

### 🔹 Tạo đối tượng `date`

```python
from datetime import date

d1 = date(2025, 10, 30)
print(d1)             # 2025-10-30

today = date.today()
print(today)          # ngày hiện tại (vd: 2025-10-30)
```

### 🔹 Các thuộc tính của `date`

```python
print(today.year)   # 2025
print(today.month)  # 10
print(today.day)    # 30
```

### 🔹 Phương thức tiện ích

```python
print(today.weekday())    # 0=Monday, 6=Sunday
print(today.isoformat())  # '2025-10-30'
print(today.isoCalendar())# tuple (year, week_num, weekday)
```

---

## 4️⃣ Lớp `time` — làm việc với giờ

### 🔹 Tạo đối tượng `time`

```python
from datetime import time

t1 = time(14, 30, 15)
print(t1)  # 14:30:15
```

### 🔹 Các thuộc tính

```python
print(t1.hour)   # 14
print(t1.minute) # 30
print(t1.second) # 15
```

---

## 5️⃣ Lớp `datetime` — kết hợp ngày & giờ

### 🔹 Tạo `datetime` cụ thể

```python
from datetime import datetime

dt = datetime(2025, 10, 30, 9, 15, 0)
print(dt)  # 2025-10-30 09:15:00
```

### 🔹 Lấy thời điểm hiện tại

```python
now = datetime.now()
print("Now:", now)

utc_now = datetime.utcnow()
print("UTC:", utc_now)
```

### 🔹 Truy xuất thành phần

```python
print(now.year, now.month, now.day)
print(now.hour, now.minute, now.second)
```

---

## 6️⃣ Định dạng và chuyển đổi (format ↔ parse)

### 🔹 Định dạng (`datetime → string`)

Dùng `strftime(format)`

```python
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted)  # "2025-10-30 09:15:00"
```

| Ký hiệu | Ý nghĩa          | Ví dụ    |
| ------- | ---------------- | -------- |
| `%Y`    | Năm (4 chữ số)   | 2025     |
| `%y`    | Năm (2 chữ số)   | 25       |
| `%m`    | Tháng (01–12)    | 10       |
| `%d`    | Ngày (01–31)     | 30       |
| `%H`    | Giờ (00–23)      | 09       |
| `%M`    | Phút             | 15       |
| `%S`    | Giây             | 00       |
| `%A`    | Tên thứ          | Thursday |
| `%a`    | Tên thứ viết tắt | Thu      |
| `%B`    | Tên tháng        | October  |

### 🔹 Phân tích chuỗi (`string → datetime`)

Dùng `strptime(string, format)`

```python
text = "2025-10-30 09:15:00"
dt2 = datetime.strptime(text, "%Y-%m-%d %H:%M:%S")
print(dt2)
```

---

## 7️⃣ Lớp `timedelta` — cộng / trừ ngày giờ

### 🔹 Tạo `timedelta`

```python
from datetime import timedelta

delta = timedelta(days=7, hours=3)
print(delta)  # 7 days, 3:00:00
```

### 🔹 Cộng / trừ với datetime hoặc date

```python
now = datetime.now()
print("Now:", now)

future = now + timedelta(days=7)
past = now - timedelta(hours=5)

print("Future:", future)
print("Past:", past)
```

### 🔹 Hiệu giữa hai ngày

```python
d1 = datetime(2025, 10, 30)
d2 = datetime(2025, 11, 15)
diff = d2 - d1
print(diff.days)  # 16
```

---

## 8️⃣ Lớp `timezone` — xử lý múi giờ (nâng cao)

```python
from datetime import timezone, timedelta, datetime

vn_tz = timezone(timedelta(hours=7))  # UTC+7 (Việt Nam)
now_utc = datetime.now(timezone.utc)
now_vn = now_utc.astimezone(vn_tz)

print("UTC:", now_utc)
print("VN:", now_vn)
```

---

## 9️⃣ Một số ví dụ thực tế

### 🧩 Ví dụ 1: Tính tuổi

```python
from datetime import date

birth = date(2000, 5, 20)
today = date.today()
age = today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))
print("Tuổi:", age)
```

---

### 🧩 Ví dụ 2: In ngày thứ Hai kế tiếp

```python
from datetime import date, timedelta

today = date.today()
days_until_monday = (7 - today.weekday()) % 7
next_monday = today + timedelta(days=days_until_monday)
print("Thứ Hai kế tiếp:", next_monday)
```

---

### 🧩 Ví dụ 3: So sánh thời gian

```python
from datetime import datetime

t1 = datetime(2025, 10, 30, 8, 0)
t2 = datetime(2025, 10, 30, 10, 0)

if t2 > t1:
    print("t2 sau t1")
```

---

### 🧩 Ví dụ 4: Đếm ngược đến một ngày đặc biệt

```python
from datetime import date

today = date.today()
new_year = date(today.year + 1, 1, 1)
remain = (new_year - today).days

print(f"Còn {remain} ngày nữa đến Tết Dương Lịch 🎉")
```

---

## 🔟 Tóm tắt các nhóm hàm / lớp quan trọng

| Nhóm               | Hàm / Lớp                                             | Mô tả                             |
| ------------------ | ----------------------------------------------------- | --------------------------------- |
| Ngày               | `date.today()`, `date(year,month,day)`                | Làm việc với ngày                 |
| Giờ                | `time(hour,minute,second)`                            | Làm việc với giờ                  |
| Ngày + giờ         | `datetime.now()`, `datetime.strptime()`, `strftime()` | Kết hợp đầy đủ                    |
| Hiệu / khoảng cách | `timedelta(days, hours, ...)`                         | Cộng / trừ ngày giờ               |
| Múi giờ            | `timezone(timedelta(hours=+X))`                       | Quản lý múi giờ                   |
| Format             | `strftime`, `strptime`                                | Chuyển đổi giữa chuỗi và datetime |

---

## 📘 Mẹo nhỏ

* Dùng `datetime.now()` cho local time, `datetime.utcnow()` cho giờ quốc tế.
* Dùng `timedelta` thay vì tự cộng số ngày/tháng.
* Khi làm việc với API hoặc cơ sở dữ liệu quốc tế → luôn chuẩn hóa về **UTC**.
* Dùng `isoformat()` để xuất chuỗi ISO 8601 (`2025-10-30T09:15:00`).

---

## 🔹 Ví dụ tổng hợp

```python
from datetime import datetime, timedelta, timezone

# Lấy giờ hiện tại
now = datetime.now()

# Định dạng
print(now.strftime("Hôm nay là %A, ngày %d/%m/%Y - %H:%M:%S"))

# Sau 3 ngày
future = now + timedelta(days=3)
print("Sau 3 ngày:", future.strftime("%d/%m/%Y %H:%M"))

# Múi giờ Việt Nam
vn = timezone(timedelta(hours=7))
print("Giờ Việt Nam:", datetime.now(vn))
```

