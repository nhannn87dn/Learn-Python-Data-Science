# 🎨 **Buổi 14: Trực quan hoá dữ liệu (Data Visualization)**

## 🎯 **Mục tiêu buổi học**

* Hiểu vai trò của **trực quan hoá dữ liệu** trong phân tích dữ liệu.
* Làm quen với hai thư viện phổ biến: **Matplotlib** và **Seaborn**.
* Biết cách tạo và tùy chỉnh các biểu đồ cơ bản và nâng cao.
* Thực hành trực quan hóa dữ liệu doanh thu hoặc điểm số học sinh.

---

## 🧠 **1. Giới thiệu về trực quan hoá dữ liệu**

> “A picture is worth a thousand words” — Một biểu đồ có thể giúp bạn nhìn ra xu hướng, mối quan hệ, hay bất thường mà con số không thể hiện rõ.

**Hai thư viện chính:**

* **Matplotlib:** Thư viện cơ bản, mạnh mẽ, tùy biến cao.
* **Seaborn:** Xây dựng dựa trên Matplotlib, dễ dùng hơn, có giao diện đẹp và nhiều biểu đồ thống kê.

---

## 📊 **2. Matplotlib cơ bản**


`Matplotlib` là thư viện nền tảng của Python cho vẽ đồ thị 2D.
Nó có 2 phong cách chính:

* **Pyplot style**: dễ dùng, giống như cách bạn vẽ trong MATLAB.
* **Object-oriented (OO) style**: dùng khi bạn cần nhiều biểu đồ phức tạp trong cùng 1 figure.

Cài đặt:

```bash
pip install matplotlib
```

Import:

```python
import matplotlib.pyplot as plt
```

---

### 🔹 **1. Cấu trúc cơ bản**

```python
import matplotlib.pyplot as plt

# Dữ liệu mẫu
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 15]

# Biểu đồ đường (Line chart)
plt.plot(x, y)
plt.title("Doanh thu theo tháng")
plt.xlabel("Tháng")
plt.ylabel("Doanh thu (triệu)")
plt.show()
```

### 📈 **2. Biểu đồ đường (Line Chart)**

Dùng để thể hiện **xu hướng** theo thời gian.

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 15, 13, 20, 18]

plt.plot(x, y, color='blue', linestyle='--', marker='o', linewidth=2, label='Doanh thu')
plt.title("Biểu đồ Doanh thu theo Tháng", fontsize=14)
plt.xlabel("Tháng")
plt.ylabel("Doanh thu (triệu đồng)")
plt.grid(True)
plt.legend()
plt.show()
```

🔍 **Giải thích:**

* `color`: màu đường (`'red'`, `'blue'`, `'#00FF00'`, v.v.)
* `linestyle`: kiểu đường (`'-'`, `'--'`, `'-.'`, `':'`)
* `marker`: ký hiệu tại mỗi điểm (`'o'`, `'s'`, `'^'`, v.v.)
* `linewidth`: độ dày của đường
* `label`: tên hiển thị trong chú thích (legend)

---

### 📊 **3. Biểu đồ cột (Bar Chart)**

Dùng để so sánh các nhóm dữ liệu rời rạc.

```python
labels = ['A', 'B', 'C', 'D']
values = [23, 45, 12, 36]

plt.bar(labels, values, color='orange', width=0.6, edgecolor='black')
plt.title("Doanh số theo Nhóm sản phẩm")
plt.xlabel("Nhóm sản phẩm")
plt.ylabel("Doanh số")
plt.show()
```

🔹 **Biểu đồ cột ngang:**

```python
plt.barh(labels, values, color='teal')
plt.title("Doanh số theo Nhóm sản phẩm (ngang)")
plt.show()
```

---

### 🔵 **4. Biểu đồ phân tán (Scatter Plot)**

Dùng để thể hiện **mối quan hệ giữa hai biến số**.

```python
import numpy as np

x = np.random.rand(50)
y = np.random.rand(50)

plt.scatter(x, y, color='purple', s=80, alpha=0.7, edgecolor='black')
plt.title("Biểu đồ phân tán")
plt.xlabel("Chiều cao")
plt.ylabel("Cân nặng")
plt.show()
```

**Giải thích:**

* `s`: kích thước điểm
* `alpha`: độ trong suốt (0 → trong suốt, 1 → đậm)
* `edgecolor`: màu viền của marker

---

### 🥧 **5. Biểu đồ tròn (Pie Chart)**

Dùng để biểu diễn **tỷ lệ phần trăm**.

```python
sizes = [40, 25, 20, 15]
labels = ['A', 'B', 'C', 'D']
colors = ['gold', 'lightcoral', 'lightgreen', 'skyblue']

plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90, shadow=True)
plt.title("Thị phần sản phẩm")
plt.show()
```

**Tuỳ chọn phổ biến:**

* `autopct='%1.1f%%'`: hiển thị phần trăm.
* `startangle`: góc bắt đầu (90 giúp xoay biểu đồ cho đẹp hơn).
* `shadow=True`: tạo bóng.

---

### ⚙️ **6. Tuỳ chỉnh biểu đồ nâng cao**

🔸 Kích thước biểu đồ

```python
plt.figure(figsize=(8, 5))
```

🔸 Thêm nhiều biểu đồ trong 1 figure (Subplots)

```python
x = [1, 2, 3, 4, 5]
y1 = [10, 15, 20, 25, 30]
y2 = [30, 25, 20, 15, 10]

plt.subplot(1, 2, 1)  # 1 hàng, 2 cột, vị trí 1
plt.plot(x, y1, color='blue')
plt.title("Biểu đồ 1")

plt.subplot(1, 2, 2)  # 1 hàng, 2 cột, vị trí 2
plt.plot(x, y2, color='red')
plt.title("Biểu đồ 2")

plt.tight_layout()
plt.show()
```

🔸 Lưu biểu đồ ra file ảnh

```python
plt.savefig('chart.png', dpi=300, bbox_inches='tight')
```

---

### 🎨 **8. Một số mẹo làm biểu đồ đẹp hơn**

| Tính năng         | Hàm / Tham số                           | Gợi ý                    |
| ----------------- | --------------------------------------- | ------------------------ |
| Màu sắc           | `color='#FF5733'`                       | Dùng mã HEX hoặc tên màu |
| Phông chữ         | `plt.rcParams['font.family'] = 'Arial'` | Đặt font mặc định        |
| Kích thước figure | `plt.figure(figsize=(10,6))`            | Dễ đọc hơn               |
| Nền biểu đồ       | `plt.style.use('seaborn')`              | Dùng style có sẵn        |
| Ghi chú           | `plt.text(x, y, "Ghi chú")`             | Ghi chú giá trị          |
| Chú thích         | `plt.legend()`                          | Hiển thị tên đường       |


Xem thêm tại: https://www.w3schools.com/python/matplotlib_markers.asp

---


## 🧠 **1. Giới thiệu về Seaborn**

### 🔹 Seaborn là gì?

**Seaborn** là thư viện trực quan hoá dữ liệu mạnh mẽ, xây dựng dựa trên **Matplotlib** và tích hợp chặt chẽ với **Pandas**.
Nó giúp bạn tạo biểu đồ **đẹp, hiện đại, và dễ dàng** hơn nhiều so với Matplotlib thuần.

> 👉 Nói cách khác: *Matplotlib là công cụ vẽ, còn Seaborn là “người thiết kế” làm cho biểu đồ trở nên chuyên nghiệp.*

---

## 💡 **2. Ưu điểm của Seaborn**

| Đặc điểm         | Seaborn                                         | Matplotlib                     |
| ---------------- | ----------------------------------------------- | ------------------------------ |
| Giao diện        | Cao cấp, thân thiện                             | Cần nhiều cấu hình thủ công    |
| Dữ liệu          | Làm việc trực tiếp với `DataFrame`              | Thường phải truyền list/array  |
| Mặc định         | Biểu đồ có sẵn style, palette màu đẹp           | Biểu đồ cơ bản, phải chỉnh tay |
| Biểu đồ thống kê | Có sẵn nhiều loại (boxplot, violin, heatmap...) | Cần tự vẽ hoặc tính toán       |

---

## ⚙️ **3. Cài đặt và import**

### 🔸 Cài đặt

```bash
pip install seaborn
```

### 🔸 Import

```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
```

---

## 🧩 **4. Dữ liệu mẫu có sẵn**

Seaborn cung cấp một số **dataset mẫu** để thực hành nhanh:

```python
sns.get_dataset_names()  # Liệt kê các bộ dữ liệu mẫu
```

Ví dụ: `"tips"`, `"iris"`, `"penguins"`, `"flights"`.

```python
df = sns.load_dataset("tips")
df.head()
```

Kết quả:

| total_bill | tip  | sex    | smoker | day | time   | size |
| ---------- | ---- | ------ | ------ | --- | ------ | ---- |
| 16.99      | 1.01 | Female | No     | Sun | Dinner | 2    |
| 10.34      | 1.66 | Male   | No     | Sun | Dinner | 3    |
| ...        | ...  | ...    | ...    | ... | ...    | ...  |

---

## 📊 **5. Các loại biểu đồ phổ biến trong Seaborn**

---

### 🔹 **1. Biểu đồ phân tán (Scatter plot)** – `sns.scatterplot()`

Thể hiện mối quan hệ giữa 2 biến số (giống như biểu đồ scatter của Matplotlib, nhưng dễ tùy chỉnh hơn).

```python
sns.scatterplot(data=df, x="total_bill", y="tip", hue="sex", style="smoker")
plt.title("Mối quan hệ giữa hoá đơn và tiền tip")
plt.show()
```

**Giải thích:**

* `hue`: tô màu theo giới tính.
* `style`: ký hiệu điểm theo nhóm.
* `size`: kích thước điểm theo giá trị khác.

---

### 🔹 **2. Biểu đồ cột (Bar plot)** – `sns.barplot()`

Hiển thị giá trị trung bình của một biến theo nhóm.

```python
sns.barplot(data=df, x="day", y="total_bill", hue="sex", ci=None)
plt.title("Doanh thu trung bình theo ngày và giới tính")
plt.show()
```

**Giải thích:**

* `ci=None`: tắt hiển thị khoảng tin cậy (confidence interval).

---

### 🔹 **3. Biểu đồ hộp (Boxplot)** – `sns.boxplot()`

Dùng để xem **phân bố dữ liệu** và **phát hiện outlier**.

```python
sns.boxplot(data=df, x="day", y="total_bill", hue="sex")
plt.title("Phân bố hoá đơn theo ngày và giới tính")
plt.show()
```

---

### 🔹 **4. Biểu đồ violin (Violin plot)** – `sns.violinplot()`

Tương tự boxplot nhưng thể hiện thêm **mật độ xác suất**.

```python
sns.violinplot(data=df, x="day", y="total_bill", inner="quartile", hue="sex", split=True)
plt.title("Phân bố hoá đơn chi tiết theo giới tính")
plt.show()
```

---

### 🔹 **5. Biểu đồ histogram / KDE** – `sns.histplot()` / `sns.kdeplot()`

#### Histogram

```python
sns.histplot(data=df, x="total_bill", bins=20, kde=True, color="skyblue")
plt.title("Phân bố giá trị hoá đơn")
plt.show()
```

#### KDE (mật độ xác suất)

```python
sns.kdeplot(data=df, x="total_bill", fill=True)
plt.title("Phân bố mật độ xác suất")
plt.show()
```

---

### 🔹 **6. Biểu đồ ma trận tương quan (Heatmap)**

Hiển thị mối tương quan giữa các biến số.

```python
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Ma trận tương quan giữa các biến số")
plt.show()
```

---

###🔹 **7. Biểu đồ cặp (Pairplot)**

Hiển thị mối quan hệ giữa **tất cả các biến số** trong DataFrame.

```python
iris = sns.load_dataset("iris")
sns.pairplot(iris, hue="species")
plt.suptitle("Phân bố dữ liệu Iris", y=1.02)
plt.show()
```

---

### 🔹 **8. Biểu đồ đếm (Countplot)**

Hiển thị số lượng bản ghi trong từng nhóm.

```python
sns.countplot(data=df, x="day", hue="sex")
plt.title("Số lượng khách theo ngày và giới tính")
plt.show()
```

---

## 🎨 **6. Tùy chỉnh giao diện Seaborn**

Seaborn có các theme (chủ đề) và palette màu rất đẹp.

### 🔸 Theme

```python
sns.set_style("whitegrid")  # Các lựa chọn: "dark", "white", "darkgrid", "whitegrid", "ticks"
```

### 🔸 Palette (bảng màu)

```python
sns.set_palette("pastel")    # pastel, deep, bright, dark, colorblind
sns.color_palette("coolwarm", as_cmap=True)
```

### 🔸 Kích thước figure

```python
plt.figure(figsize=(8,5))
```
