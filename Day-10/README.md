# 🧮 **Buổi 10: NumPy cơ bản – Phần 2**


## 🧩 **1. Ôn lại phần trước**

### 🔹 NumPy là thư viện giúp:

* Tạo và thao tác trên **mảng n chiều (ndarray)**.
* Tính toán nhanh hơn nhiều so với list.
* Dễ dàng kết hợp với Pandas, Matplotlib.

### 🔹 Cách import:

```python
import numpy as np
```

---

## 🔗 **11. Join mảng**

### 11.1. Khái niệm

> **Join (hoặc concatenate)** là quá trình **ghép nhiều mảng lại với nhau** theo **chiều (axis)** mà bạn chỉ định.
> Tất cả các mảng phải có **số chiều tương thích** nhau.

---

### 11.2. Các hàm dùng để join mảng

| Hàm                | Mô tả                                       |
| ------------------ | ------------------------------------------- |
| `np.concatenate()` | Hàm tổng quát nhất để nối mảng              |
| `np.stack()`       | Nối mảng **thêm chiều mới**                 |
| `np.hstack()`      | Nối theo **chiều ngang (columns)**          |
| `np.vstack()`      | Nối theo **chiều dọc (rows)**               |
| `np.dstack()`      | Nối theo **chiều sâu (depth)**, tạo mảng 3D |

---

### 11.3. Dùng `np.concatenate()`

➤ Cú pháp:

```python
np.concatenate((a1, a2, ...), axis=0)
```

➤ Ví dụ:

```python
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

joined = np.concatenate((a, b))
print(joined)
```

📤 Kết quả:

```
[1 2 3 4 5 6]
```

---

➤ Với mảng 2 chiều:

```python
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])

# Nối theo hàng (axis=0)
print(np.concatenate((a, b), axis=0))

# Nối theo cột (axis=1)
print(np.concatenate((a, a), axis=1))
```

📤 Kết quả:

```
[[1 2]
 [3 4]
 [5 6]]

[[1 2 1 2]
 [3 4 3 4]]
```

---

### 11.4. Dùng `np.stack()`

`stack()` **tạo thêm một chiều mới** (khác với concatenate).

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

stacked = np.stack((a, b), axis=0)
print(stacked)
```

📤 Kết quả:

```
[[1 2 3]
 [4 5 6]]
```

🧠 So sánh nhanh:

* `concatenate` nối **trên cùng chiều**
* `stack` nối **thêm một chiều mới**

---

### 11.5. Dùng `np.vstack()` và `np.hstack()`

➤ Nối theo hàng (vertical stack)

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

v = np.vstack((a, b))
print(v)
```

📤 Kết quả:

```
[[1 2 3]
 [4 5 6]]
```

---

➤ Nối theo cột (horizontal stack)

```python
h = np.hstack((a, b))
print(h)
```

📤 Kết quả:

```
[1 2 3 4 5 6]
```

Với mảng 2D:

```python
a = np.array([[1], [2], [3]])
b = np.array([[4], [5], [6]])

print(np.hstack((a, b)))
```

📤 Kết quả:

```
[[1 4]
 [2 5]
 [3 6]]
```

---

### 11.6. Dùng `np.dstack()` (depth stack)

Ghép các mảng theo **chiều sâu** → tạo mảng 3D.

```python
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

print(np.dstack((a, b)))
```

📤 Kết quả:

```
[[[1 5]
  [2 6]]

 [[3 7]
  [4 8]]]
```

🧩 Nghĩa là mỗi “lớp” (layer) chứa dữ liệu tương ứng từ từng mảng.

---

### 11.7. Lưu ý quan trọng

| Điều kiện                                             | Giải thích                                                 |
| ----------------------------------------------------- | ---------------------------------------------------------- |
| Các mảng phải có cùng **số chiều**                    | Ví dụ: không thể nối mảng 1D với 2D                        |
| Kích thước ở các trục khác `axis` phải **giống nhau** | Ví dụ: nếu nối theo hàng (`axis=0`), số cột phải bằng nhau |

---

### 11.8. Ví dụ tổng hợp

```python
import numpy as np

a = np.arange(1, 7).reshape(2, 3)
b = np.arange(7, 13).reshape(2, 3)

print("a:\n", a)
print("b:\n", b)
print("\nconcatenate axis=0:\n", np.concatenate((a, b), axis=0))
print("\nconcatenate axis=1:\n", np.concatenate((a, b), axis=1))
print("\nstack axis=0:\n", np.stack((a, b), axis=0))
```

📤 Kết quả:

```
a:
 [[1 2 3]
  [4 5 6]]
b:
 [[ 7  8  9]
  [10 11 12]]

concatenate axis=0:
 [[ 1  2  3]
  [ 4  5  6]
  [ 7  8  9]
  [10 11 12]]

concatenate axis=1:
 [[ 1  2  3  7  8  9]
  [ 4  5  6 10 11 12]]

stack axis=0:
 [[[ 1  2  3]
   [ 4  5  6]]

  [[ 7  8  9]
   [10 11 12]]]
```

---


## ✂️ **12.Tách mảng (Split arrays) trong NumPy**


### 12.1. Khái niệm

> **Split** là thao tác chia một mảng lớn thành **nhiều mảng con**.
> NumPy cung cấp nhiều hàm khác nhau để tách mảng theo chiều **hàng**, **cột**, hoặc **chiều sâu**.

---

### 12.2. Các hàm tách mảng phổ biến

| Hàm                | Mô tả                                                             | Tách theo              |
| ------------------ | ----------------------------------------------------------------- | ---------------------- |
| `np.split()`       | Hàm cơ bản nhất để tách mảng                                      | Trục chỉ định (`axis`) |
| `np.array_split()` | Giống `split()` nhưng **linh hoạt hơn** (cho phép chia không đều) | Trục chỉ định          |
| `np.hsplit()`      | Tách theo **chiều ngang (columns)**                               | Trục 1                 |
| `np.vsplit()`      | Tách theo **chiều dọc (rows)**                                    | Trục 0                 |
| `np.dsplit()`      | Tách theo **chiều sâu (depth)**                                   | Trục 2                 |

---

### 12.3. Dùng `np.split()`

➤ Cú pháp:

```python
np.split(array, indices_or_sections, axis=0)
```

* `array`: mảng cần tách
* `indices_or_sections`:

  * Nếu là **số nguyên N** → chia mảng thành N phần bằng nhau
  * Nếu là **danh sách các chỉ số** → tách tại các vị trí đó
* `axis`: trục tách (0 = hàng, 1 = cột)

---

➤ Ví dụ 1: Chia đều mảng 1 chiều

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
result = np.split(arr, 3)
print(result)
```

📤 Kết quả:

```
[array([1, 2]), array([3, 4]), array([5, 6])]
```

➡️ Mảng `[1,2,3,4,5,6]` được chia thành 3 phần bằng nhau.

---

Nếu chia không đều sẽ lỗi:

```python
# ❌ Sẽ lỗi vì 7 không chia hết cho 3
arr = np.array([1, 2, 3, 4, 5, 6, 7])
np.split(arr, 3)
```

📛 Lỗi:

```
ValueError: array split does not result in an equal division
```

---

### 12.4. Dùng `np.array_split()` (chia linh hoạt hơn)

```python
arr = np.array([1, 2, 3, 4, 5, 6, 7])
result = np.array_split(arr, 3)
print(result)
```

📤 Kết quả:

```
[array([1, 2, 3]),
 array([4, 5]),
 array([6, 7])]
```

✅ Không lỗi dù không chia đều!

---

### 12.5. Tách mảng 2 chiều theo hàng và cột

```python
arr = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8]
])

# Tách theo cột (axis=1)
cols = np.split(arr, 2, axis=1)
print("Tách theo cột:", cols)

# Tách theo hàng (axis=0)
rows = np.split(arr, 2, axis=0)
print("Tách theo hàng:", rows)
```

📤 Kết quả:

```
Tách theo cột: [array([[1, 2],
                       [5, 6]]),
                array([[3, 4],
                       [7, 8]])]

Tách theo hàng: [array([[1, 2, 3, 4]]),
                 array([[5, 6, 7, 8]])]
```

---

### 12.6. Tách theo chỉ số cụ thể

```python
arr = np.array([10, 20, 30, 40, 50, 60])
result = np.split(arr, [2, 5])
print(result)
```

📤 Kết quả:

```
[array([10, 20]),
 array([30, 40, 50]),
 array([60])]
```

🧩 Nghĩa là:

* Tách tại vị trí index 2 và 5 → tạo 3 phần: `[0–1]`, `[2–4]`, `[5–end]`.

---

### 12.7. Dùng `np.hsplit()`, `np.vsplit()`, `np.dsplit()`

➤ `hsplit()` — tách theo **chiều ngang** (cột):

```python
arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8]])

print(np.hsplit(arr, 2))
```

📤 Kết quả:

```
[array([[1, 2],
        [5, 6]]),
 array([[3, 4],
        [7, 8]])]
```

---

➤ `vsplit()` — tách theo **chiều dọc** (hàng):

```python
print(np.vsplit(arr, 2))
```

📤 Kết quả:

```
[array([[1, 2, 3, 4]]),
 array([[5, 6, 7, 8]])]
```

---

➤ `dsplit()` — tách theo **chiều sâu (3D)**

```python
arr = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])

print(np.dsplit(arr, 2))
```

📤 Kết quả:

```
[array([[[1],
         [3]],
        [[5],
         [7]]]),
 array([[[2],
         [4]],
        [[6],
         [8]]])]
```

---

### 12.8. So sánh nhanh

| Hàm                | Tách theo         | Linh hoạt (chia không đều)? | Dùng cho           |
| ------------------ | ----------------- | --------------------------- | ------------------ |
| `np.split()`       | Trục (axis)       | ❌ Không                     | Khi chia đều       |
| `np.array_split()` | Trục (axis)       | ✅ Có                        | Khi không chia đều |
| `np.hsplit()`      | Cột (columns)     | ❌ Không                     | Mảng ≥ 2D          |
| `np.vsplit()`      | Hàng (rows)       | ❌ Không                     | Mảng ≥ 2D          |
| `np.dsplit()`      | Chiều sâu (depth) | ❌ Không                     | Mảng 3D            |

---

### 12.9. Ví dụ tổng hợp

```python
import numpy as np

arr = np.arange(1, 13).reshape(3, 4)
print("Mảng gốc:\n", arr)

print("\nSplit theo cột:")
print(np.hsplit(arr, 2))

print("\nSplit theo hàng:")
print(np.vsplit(arr, 3))

print("\nArray split không đều:")
print(np.array_split(arr, 4, axis=1))
```

---


## 🔍 **13. Tìm kiếm phần tử trong mảng (Searching Arrays) – NumPy**

Trong **NumPy**, việc **tìm kiếm phần tử** (hoặc **chỉ số của phần tử**) trong mảng là thao tác rất phổ biến khi bạn muốn **lọc dữ liệu** hoặc **xác định vị trí** các giá trị thỏa mãn điều kiện nào đó.

---

### 13.1. **Hàm `np.where()`**

Hàm `numpy.where()` trả về **chỉ số** (index) của các phần tử trong mảng **thỏa mãn điều kiện cho trước**.

 ✅ Cú pháp:

```python
np.where(điều_kiện)
```

Ví dụ:

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

# Tìm vị trí các phần tử lớn hơn 25
result = np.where(arr > 25)

print(result)
```

📤 Kết quả:

```
(array([2, 3, 4], dtype=int64),)
```

🔹 Nghĩa là: các phần tử ở **vị trí 2, 3, 4** (tức là 30, 40, 50) thỏa mãn điều kiện `arr > 25`.

---

### 13.2. **Hàm `np.searchsorted()`**

Hàm `searchsorted()` dùng để **tìm vị trí** mà một phần tử nên được **chèn vào** trong mảng **đã sắp xếp**, sao cho mảng vẫn **giữ nguyên thứ tự tăng dần**.

Cú pháp:

```python
np.searchsorted(array, value)
```

Ví dụ:

```python
arr = np.array([10, 20, 30, 40, 50])

x = np.searchsorted(arr, 35)
print(x)
```

Kết quả:

```
3
```

🔹 Nghĩa là: nếu chèn **35** vào vị trí **3**, mảng sẽ vẫn được sắp xếp theo thứ tự tăng dần.

---

### 13.3. **Kết hợp điều kiện trong `where()`**

Bạn có thể kết hợp nhiều điều kiện bằng **toán tử logic** (`&`, `|`).

Ví dụ:

```python
arr = np.array([5, 10, 15, 20, 25, 30])

# Tìm phần tử lớn hơn 10 và nhỏ hơn 25
result = np.where((arr > 10) & (arr < 25))

print(result)
print(arr[result])
```

Kết quả:

```
(array([2, 3], dtype=int64),)
[15 20]
```

---

### 13.4. **Tìm giá trị cụ thể bằng so sánh**

Bạn có thể tìm **chỉ số** của giá trị cụ thể.

Ví dụ:

```python
arr = np.array([1, 2, 3, 4, 2, 5, 2])
indices = np.where(arr == 2)
print(indices)
```

Kết quả:

```
(array([1, 4, 6], dtype=int64),)
```

---

### 13.5. **Lọc dữ liệu bằng điều kiện (Boolean Indexing)**

Thay vì chỉ lấy chỉ số, bạn có thể **lọc giá trị trực tiếp**.

Ví dụ:

```python
arr = np.array([10, 20, 30, 40, 50])

filtered = arr[arr > 25]
print(filtered)
```

Kết quả:

```
[30 40 50]
```

---

## 🔢 **14 Sắp xếp mảng (Sorting Arrays)**

Trong **NumPy**, việc **sắp xếp (sorting)** dữ liệu là thao tác thường xuyên khi xử lý và phân tích dữ liệu. NumPy cung cấp các **hàm sắp xếp nhanh, hiệu quả**, hoạt động tốt trên cả mảng 1D và nhiều chiều.

---

### 14.1. **Hàm `np.sort()`**

Hàm `numpy.sort()` **trả về một bản sao đã sắp xếp** của mảng (không thay đổi mảng gốc).

Cú pháp:

```python
np.sort(array, axis=-1, kind=None)
```

| Tham số | Ý nghĩa                                                             |
| ------- | ------------------------------------------------------------------- |
| `array` | Mảng cần sắp xếp                                                    |
| `axis`  | Trục sắp xếp (0: cột, 1: hàng, -1: mặc định là cuối cùng)           |
| `kind`  | Thuật toán sắp xếp (`quicksort`, `mergesort`, `heapsort`, `stable`) |

---

Ví dụ 1 – Sắp xếp mảng 1 chiều:

```python
import numpy as np

arr = np.array([3, 1, 4, 1, 5, 9])
sorted_arr = np.sort(arr)

print(sorted_arr)
```

Kết quả:

```
[1 1 3 4 5 9]
```

> 🔹 `np.sort()` **không làm thay đổi** mảng gốc `arr`.

---

Ví dụ 2 – Sắp xếp mảng 2 chiều theo hàng:

```python
arr2d = np.array([[3, 2, 1],
                  [6, 5, 4]])

print(np.sort(arr2d, axis=1))
```

Kết quả:

```
[[1 2 3]
 [4 5 6]]
```

> 🔹 `axis=1` → sắp xếp **theo từng hàng**.
> 🔹 Nếu `axis=0` → sắp xếp **theo từng cột**.

---

### 14.2. **Hàm `np.argsort()`**

Hàm `argsort()` **không sắp xếp giá trị**, mà **trả về chỉ số** của các phần tử **theo thứ tự tăng dần**.

Ví dụ:

```python
arr = np.array([40, 10, 20])
indices = np.argsort(arr)

print(indices)
print(arr[indices])
```

Kết quả:

```
[1 2 0]
[10 20 40]
```

> 🔹 Dùng `arr[indices]` để truy cập phần tử theo thứ tự đã sắp xếp.

---

### 14.3. **Sắp xếp theo kiểu giảm dần**

NumPy không có tham số `reverse=True` như Python, nhưng ta có thể đảo ngược kết quả:

Ví dụ:

```python
arr = np.array([5, 2, 9, 1])
sorted_desc = np.sort(arr)[::-1]
print(sorted_desc)
```

Kết quả:

```
[9 5 2 1]
```

---

### 14.4. **Sắp xếp với điều kiện (theo giá trị cột)**

Khi có mảng 2D, ta có thể sắp xếp theo giá trị của một **cột cụ thể**.

Ví dụ:

```python
arr = np.array([[1, 3],
                [2, 1],
                [3, 2]])

# Sắp xếp theo cột thứ 2 (chỉ số 1)
sorted_by_col = arr[arr[:, 1].argsort()]
print(sorted_by_col)
```

Kết quả:

```
[[2 1]
 [3 2]
 [1 3]]
```

---

### 14.5. **Hàm `np.ndarray.sort()`**

Khác với `np.sort()`, hàm **`array.sort()` sẽ sắp xếp trực tiếp trên mảng gốc**.

Ví dụ:

```python
arr = np.array([3, 1, 2])
arr.sort()
print(arr)
```

Kết quả:

```
[1 2 3]
```

> 🔹 Không trả về mảng mới, mà **thay đổi dữ liệu gốc**.

---

### 14.6. **Sắp xếp theo kiểu ổn định (Stable Sort)**

Khi có các phần tử bằng nhau, bạn có thể dùng `kind='stable'` để **giữ nguyên thứ tự gốc** của các phần tử bằng nhau.

Ví dụ:

```python
arr = np.array([2, 1, 2, 1])
print(np.sort(arr, kind='stable'))
```

Kết quả:

```
[1 1 2 2]
```

---



## 🧹 **15 Lọc mảng (Filtering Arrays)**

Trong **NumPy**, “**filtering**” (lọc mảng) là quá trình **chọn ra các phần tử thỏa mãn điều kiện** từ một mảng có sẵn.
Cách này **nhanh hơn nhiều so với vòng lặp `for` trong Python** nhờ khả năng xử lý vector hóa (vectorized operations).

---

### 15.1. **Khái niệm cơ bản**

Bạn có thể lọc dữ liệu bằng **mảng boolean** — tức là mảng chứa các giá trị `True`/`False`.
Các phần tử tương ứng với `True` sẽ được **giữ lại**, `False` sẽ bị **loại bỏ**.

---

Ví dụ cơ bản:

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

# Tạo mảng điều kiện
filter_arr = arr > 25

print(filter_arr)
```

Kết quả:

```
[False False  True  True  True]
```

> 🔹 Đây là **mảng Boolean** — kết quả của phép so sánh từng phần tử trong `arr`.

---

### 15.2. **Lọc mảng bằng điều kiện**

Bạn có thể áp dụng mảng Boolean trực tiếp để lấy ra các phần tử tương ứng.

Ví dụ:

```python
arr = np.array([10, 20, 30, 40, 50])

# Lấy ra phần tử > 25
filtered = arr[arr > 25]

print(filtered)
```

Kết quả:

```
[30 40 50]
```

---

### 15.3. **Kết hợp nhiều điều kiện**

Sử dụng **toán tử logic** `&` (AND), `|` (OR), và `~` (NOT).
⚠️ Lưu ý: Khi kết hợp điều kiện, bạn **phải đặt chúng trong ngoặc tròn `( )`**.

Ví dụ:

```python
arr = np.array([5, 10, 15, 20, 25, 30])

# Lọc phần tử lớn hơn 10 và nhỏ hơn 25
filtered = arr[(arr > 10) & (arr < 25)]

print(filtered)
```

Kết quả:

```
[15 20]
```

---

### 15.4. **Tạo filter thủ công (bằng mảng Boolean)**

Bạn cũng có thể tạo một mảng Boolean thủ công để chọn phần tử.

 Ví dụ:

```python
arr = np.array([10, 20, 30, 40])
filter_arr = [True, False, True, False]

filtered = arr[filter_arr]
print(filtered)
```

Kết quả:

```
[10 30]
```

---

### 15.5. **Lọc mảng 2 chiều**

Bạn có thể áp dụng điều kiện trực tiếp lên mảng 2D — kết quả là mảng 1D chứa các phần tử thỏa mãn điều kiện.

Ví dụ:

```python
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

# Lọc phần tử > 3
filtered = arr[arr > 3]
print(filtered)
```

Kết quả:

```
[4 5 6]
```

---

### 15.6. **Kết hợp với `np.where()` để lấy chỉ số**

Nếu bạn cần **vị trí** (index) thay vì **giá trị**, hãy dùng `np.where()`.

Ví dụ:

```python
arr = np.array([3, 6, 9, 12])
indices = np.where(arr > 5)

print(indices)
print(arr[indices])
```

Kết quả:

```
(array([1, 2, 3], dtype=int64),)
[ 6  9 12]
```

---

### 15.7. **Lọc giá trị NaN (thiếu dữ liệu)**

Khi làm việc với dữ liệu thực tế, bạn có thể cần loại bỏ giá trị **NaN (Not a Number)**.

Ví dụ:

```python
arr = np.array([10, np.nan, 20, np.nan, 30])
filtered = arr[~np.isnan(arr)]

print(filtered)
```

Kết quả:

```
[10. 20. 30.]
```

---


## 🔢 **17. Mảng ngẫu nhiên (Random Arrays)**

Tuyệt vời 👏 — Dưới đây là phần **kiến thức chi tiết** về **NumPy Random** và **các phương thức phổ biến**, trình bày theo phong cách dễ hiểu, có ví dụ minh họa rõ ràng — phù hợp để làm **tài liệu học hoặc bài giảng** 👇

---

# 🎲 **NumPy Random – Tạo dữ liệu ngẫu nhiên**

---

### 🧠 **1. Giới thiệu**

**NumPy Random** là **một module con (`numpy.random`)** giúp sinh ra **dữ liệu ngẫu nhiên** để phục vụ cho:

* Mô phỏng dữ liệu (data simulation)
* Thử nghiệm và kiểm thử mô hình
* Sinh dữ liệu cho Machine Learning hoặc Data Science
* Tạo mẫu (sampling) từ các phân phối xác suất khác nhau

Module này cực kỳ hữu ích trong các bài toán về **thống kê, mô phỏng, trí tuệ nhân tạo**, hoặc **xử lý dữ liệu lớn**.

---

### ⚙️ **2. Cách import**

```python
import numpy as np
```

Mọi phương thức trong `numpy.random` có thể truy cập bằng:

```python
np.random.[tên_hàm]()
```

---

### 🎯 **3. Một số phương thức phổ biến**

#### 🔹 3.1. `np.random.rand()`

Tạo mảng chứa **các giá trị ngẫu nhiên trong khoảng [0, 1)** (phân phối **đều**).

```python
a = np.random.rand(3)
b = np.random.rand(2, 3)

print(a)  # [0.23 0.76 0.49]
print(b)
# [[0.44 0.12 0.78]
#  [0.89 0.55 0.30]]
```

---

#### 🔹 3.2. `np.random.randn()`

Sinh giá trị ngẫu nhiên theo **phân phối chuẩn (Gaussian)**, có **mean = 0** và **std = 1**.

```python
a = np.random.randn(5)
print(a)
# [-1.04  0.56  1.32  0.08 -0.67]
```

> 🧩 Dữ liệu sẽ có cả số âm và dương, phân bố xung quanh 0.

---

#### 🔹 3.3. `np.random.randint()`

Sinh số nguyên ngẫu nhiên trong khoảng `[low, high)`.

```python
a = np.random.randint(1, 10, size=5)
print(a)  # [3 7 1 9 5]
```

> Tham số `size` quy định số lượng phần tử muốn tạo.

---

#### 🔹 3.4. `np.random.random()`

Giống `rand()` nhưng **chỉ nhận tham số size dạng tuple**.

```python
a = np.random.random((2, 3))
print(a)
# [[0.12 0.89 0.56]
#  [0.33 0.77 0.21]]
```

---

#### 🔹 3.5. `np.random.choice()`

Chọn **ngẫu nhiên phần tử** từ mảng có sẵn.

```python
items = np.array(['Python', 'Java', 'C++', 'Go'])
print(np.random.choice(items))        # Lấy 1 phần tử
print(np.random.choice(items, 2))     # Lấy 2 phần tử ngẫu nhiên
```

> Có thể thêm `replace=False` để **không chọn trùng**:

```python
np.random.choice(items, 2, replace=False)
```

---

#### 🔹 3.6. `np.random.shuffle()`

**Xáo trộn thứ tự phần tử** trong mảng (thay đổi **trực tiếp** mảng gốc).

```python
arr = np.array([1, 2, 3, 4, 5])
np.random.shuffle(arr)
print(arr)  # [4 2 5 3 1]
```

---

#### 🔹 3.7. `np.random.permutation()`

Tạo **một bản sao** mảng đã được xáo trộn (không làm thay đổi mảng gốc).

```python
arr = np.array([10, 20, 30, 40])
new_arr = np.random.permutation(arr)

print(arr)      # [10 20 30 40]
print(new_arr)  # [30 10 40 20]
```

---

#### 🔹 3.8. `np.random.seed()`

Đặt **hạt giống ngẫu nhiên (random seed)** để **kết quả có thể lặp lại**.

```python
np.random.seed(42)
print(np.random.randint(1, 10, 5))
# Luôn cho ra cùng kết quả mỗi lần chạy
```

> 💡 Dùng khi cần **tái tạo thí nghiệm** hoặc **debug** kết quả ngẫu nhiên.

---

#### 🔹 3.9. Phân phối xác suất nâng cao

NumPy hỗ trợ **nhiều phân phối thống kê** khác nhau:

| Hàm                                  | Mô tả              | Ví dụ                            |
| ------------------------------------ | ------------------ | -------------------------------- |
| `np.random.normal(mean, std, size)`  | Phân phối chuẩn    | `np.random.normal(0, 1, 5)`      |
| `np.random.uniform(low, high, size)` | Phân phối đều      | `np.random.uniform(1, 10, 5)`    |
| `np.random.binomial(n, p, size)`     | Phân phối nhị thức | `np.random.binomial(10, 0.5, 5)` |
| `np.random.poisson(lam, size)`       | Phân phối Poisson  | `np.random.poisson(5, 5)`        |
| `np.random.exponential(scale, size)` | Phân phối mũ       | `np.random.exponential(1, 5)`    |

---

### 📊 **4. Ví dụ tổng hợp**

```python
import numpy as np

# Thiết lập seed
np.random.seed(0)

# Sinh dữ liệu mẫu
ages = np.random.randint(18, 50, size=10)
scores = np.random.normal(70, 10, size=10)

print("Độ tuổi:", ages)
print("Điểm số:", np.round(scores, 2))
```

Kết quả mẫu:

```
Độ tuổi: [41 48 28 34 27 35 46 31 21 44]
Điểm số: [87.64 74.  79.79 92.41 68.68 68.68 59.79 82.41 70.23 83.67]
```

Xem thêm: https://www.w3schools.com/python/numpy/numpy_random.asp

---
