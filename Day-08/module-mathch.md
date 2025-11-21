# 🧮 **Module `math` trong Python**

---

## 1️⃣ Giới thiệu

Module **`math`** cung cấp các hàm **toán học cơ bản và nâng cao** (như lượng giác, lũy thừa, logarit, làm tròn, v.v.) — được viết bằng C nên **rất nhanh và chính xác**.

🔹 Import module:

```python
import math
```

---

## 2️⃣ Các hằng số toán học

| Hằng số    | Ý nghĩa                                | Ví dụ                  |
| ---------- | -------------------------------------- | ---------------------- |
| `math.pi`  | Số π (3.1415926535...)                 | `math.pi * r**2`       |
| `math.e`   | Cơ số tự nhiên (2.71828...)            | `math.exp(1)`          |
| `math.inf` | Vô cực (`∞`)                           | `math.isinf(math.inf)` |
| `math.nan` | Giá trị “không phải số” (Not a Number) | `math.isnan(math.nan)` |

```python
import math

print(math.pi)   # 3.141592653589793
print(math.e)    # 2.718281828459045
```

---

## 3️⃣ Hàm làm tròn & trị tuyệt đối

| Hàm             | Mô tả                                   | Ví dụ                 |
| --------------- | --------------------------------------- | --------------------- |
| `math.ceil(x)`  | Làm tròn lên                            | `math.ceil(4.2) → 5`  |
| `math.floor(x)` | Làm tròn xuống                          | `math.floor(4.8) → 4` |
| `math.trunc(x)` | Bỏ phần thập phân                       | `math.trunc(4.9) → 4` |
| `math.fabs(x)`  | Trị tuyệt đối (trả float)               | `math.fabs(-5) → 5.0` |
| `round(x)`      | (Hàm built-in Python) Làm tròn gần nhất | `round(4.6) → 5`      |

```python
print(math.ceil(3.2))   # 4
print(math.floor(3.9))  # 3
print(math.trunc(-2.7)) # -2
print(math.fabs(-10))   # 10.0
```

---

## 4️⃣ Hàm mũ, căn, và logarit

| Hàm                   | Ý nghĩa                       | Ví dụ                    |
| --------------------- | ----------------------------- | ------------------------ |
| `math.pow(x, y)`      | x^y (trả float)               | `math.pow(2, 3) → 8.0`   |
| `math.sqrt(x)`        | √x                            | `math.sqrt(25) → 5.0`    |
| `math.exp(x)`         | e^x                           | `math.exp(1) → 2.71828`  |
| `math.log(x[, base])` | log cơ số `base` (mặc định e) | `math.log(8, 2) → 3.0`   |
| `math.log10(x)`       | log cơ số 10                  | `math.log10(1000) → 3.0` |
| `math.log2(x)`        | log cơ số 2                   | `math.log2(8) → 3.0`     |

```python
print(math.pow(2, 5))   # 32.0
print(math.sqrt(16))    # 4.0
print(math.exp(2))      # 7.38905609893065
print(math.log(8, 2))   # 3.0
print(math.log10(100))  # 2.0
```

---

## 5️⃣ Hàm lượng giác

| Hàm               | Ý nghĩa                | Ví dụ                           |
| ----------------- | ---------------------- | ------------------------------- |
| `math.sin(x)`     | sin(x) (radian)        | `math.sin(math.pi/2)` → 1.0     |
| `math.cos(x)`     | cos(x)                 | `math.cos(0)` → 1.0             |
| `math.tan(x)`     | tan(x)                 | `math.tan(math.pi/4)` → 1.0     |
| `math.asin(x)`    | arcsin(x) (trả radian) | `math.asin(1)` → π/2            |
| `math.acos(x)`    | arccos(x)              | `math.acos(0)` → π/2            |
| `math.atan(x)`    | arctan(x)              | `math.atan(1)` → π/4            |
| `math.degrees(x)` | đổi radian → độ        | `math.degrees(math.pi)` → 180.0 |
| `math.radians(x)` | đổi độ → radian        | `math.radians(180)` → π         |

```python
angle = math.radians(30)
print(math.sin(angle))          # 0.5
print(math.degrees(math.pi/4))  # 45.0
```

---

## 6️⃣ Hàm tổ hợp, giai thừa, và gcd

| Hàm                 | Ý nghĩa                             | Ví dụ                     |
| ------------------- | ----------------------------------- | ------------------------- |
| `math.factorial(n)` | n! (giai thừa)                      | `math.factorial(5) → 120` |
| `math.comb(n, k)`   | Tổ hợp C(n, k)                      | `math.comb(5, 2) → 10`    |
| `math.perm(n, k)`   | Chỉnh hợp P(n, k)`                  | `math.perm(5, 2) → 20`    |
| `math.gcd(a, b)`    | Ước số chung lớn nhất               | `math.gcd(12, 18) → 6`    |
| `math.lcm(a, b)`    | Bội số chung nhỏ nhất (Python 3.9+) | `math.lcm(4, 6) → 12`     |

```python
print(math.factorial(5))  # 120
print(math.comb(5, 3))    # 10
print(math.perm(5, 3))    # 60
print(math.gcd(12, 18))   # 6
print(math.lcm(4, 6))     # 12
```

---

## 7️⃣ So sánh & xử lý số đặc biệt

| Hàm                   | Mô tả                                | Ví dụ                         |
| --------------------- | ------------------------------------ | ----------------------------- |
| `math.isfinite(x)`    | Kiểm tra không phải `inf` hoặc `nan` | `math.isfinite(5)` → True     |
| `math.isinf(x)`       | Là vô cực?                           | `math.isinf(math.inf)` → True |
| `math.isnan(x)`       | Là “NaN”?                            | `math.isnan(math.nan)` → True |
| `math.copysign(x, y)` | Trả `x` với dấu của `y`              | `math.copysign(3, -1)` → -3.0 |

```python
print(math.isfinite(10))       # True
print(math.isinf(math.inf))    # True
print(math.isnan(math.nan))    # True
print(math.copysign(5, -2))   # -5.0
```

---

## 8️⃣ Các hàm khác hữu ích

| Hàm                   | Mô tả                          | Ví dụ                           |
| --------------------- | ------------------------------ | ------------------------------- |
| `math.fsum(iterable)` | Tổng chính xác cao             | `math.fsum([0.1]*10)` → 1.0     |
| `math.prod(iterable)` | Tích các phần tử               | `math.prod([1,2,3,4]) → 24`     |
| `math.hypot(x, y)`    | Căn(x² + y²) — độ dài vector   | `math.hypot(3, 4)` → 5.0        |
| `math.dist(p, q)`     | Khoảng cách Euclid giữa 2 điểm | `math.dist([0,0], [3,4]) → 5.0` |

```python
points = [(0,0), (3,4)]
print(math.dist(points[0], points[1]))  # 5.0
print(math.hypot(6, 8))                # 10.0
print(math.fsum([0.1]*10))             # 1.0
print(math.prod([2,3,5]))              # 30
```

Hàm `math.fsum()` là hàm cộng chính xác cao dành cho số thực (floating-point) trong module math.
Nó giúp tránh lỗi làm tròn khi cộng nhiều số thập phân.

```python
sum([0.1] * 10)      # Kết quả: 0.9999999999999999
math.fsum([0.1] * 10)  # Kết quả: 1.0
```

---

## 9️⃣ Ví dụ tổng hợp

```python
import math

r = 5
area = math.pi * math.pow(r, 2)
circumference = 2 * math.pi * r
print(f"Bán kính: {r}, Diện tích: {area:.2f}, Chu vi: {circumference:.2f}")

angle = 45
rad = math.radians(angle)
print(f"sin({angle}°) = {math.sin(rad):.2f}")
print(f"log10(1000) = {math.log10(1000)}")
```

---

## 🔟 Tóm tắt nhóm hàm `math`

| Nhóm               | Ví dụ hàm                                 |
| ------------------ | ----------------------------------------- |
| Hằng số            | `pi`, `e`, `inf`, `nan`                   |
| Làm tròn           | `ceil`, `floor`, `trunc`, `fabs`          |
| Mũ & Log           | `pow`, `sqrt`, `log`, `exp`               |
| Lượng giác         | `sin`, `cos`, `tan`, `degrees`, `radians` |
| Giai thừa & Tổ hợp | `factorial`, `comb`, `perm`               |
| Số học             | `gcd`, `lcm`, `copysign`, `fsum`, `prod`  |
| Kiểm tra           | `isfinite`, `isinf`, `isnan`              |

