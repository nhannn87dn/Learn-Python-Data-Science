str = "Hello, World!"
print(str[0])
# xác định độ dài của chuỗi
print(len(str))

# Cắt chuỗi:
# Ví dụ muốn lấy cụm từ: lo
print(str[3:5])
print(str[:5])
print(str[2:])

m = '$120000'
number = m[1:]
print(number)

# thay thế kí tự trong chuỗi
print(m.replace('$', ''))

# convert to Upper CASE
print(str.upper())
# Tách chuỗi
print(str.split(','))


# Bỏ khoảng trắng đầu và cuối chuỗi
a = " Hello, World! "
print(a.strip())


# Nối chuỗi:
firstName = 'Nguyen'
lastName = 'Ngoc Nhan'

fullName = firstName + ' ' +  lastName
print(fullName)

age = 38
name = 'John'
text  = 'Xin chao. Toi la {}. Toi nam nay {} tuoi'
#print(text + age)
print(text.format(name, age))


quantity = 2
price = 49.95
txt = "Mua {0} cái bánh hết {1} đô la. Em tôi ăn hết {0} cái bánh"
print(txt.format(quantity, price))

txt2 = f"Mua {quantity} cái bánh hết {price} đô la. Em tôi ăn hết {quantity} cái bánh"
print(txt2)


print("Dòng 1\n\tDòng 2") 