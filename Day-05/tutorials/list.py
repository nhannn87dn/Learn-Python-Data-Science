# myList = ['apple', 123, 'apple', "kiwi", "melon"]
# myList[1] = 'wdw'
# print(myList, type(myList))
# Try cập phần tử dựa vào index
#print(myList[1])
#print(myList[1:3])

# Kiểm tra sự tồn tại của phẩn tử trong list
# if "orange" in myList:
#     print("có")

# có thể định nghĩa 1 list rỗng chưa có phần tử nào
# emList = []
# emList.append("1") # thêm phần tử vào cuối list
# emList.append(True)
# emList.insert(1, '2') # chèn phần tử vào vị trí chỉ định
# print(emList)

# Xoá phần tử ra khỏi list

# emList.pop(2) # xoá phần tử có index = 2
# print(emList)

# emList.remove('2') # xoá phần tự cụ thể
# print(emList)
# emList.clear() # xoá all phần tử của list
# print(emList)
# # xoá luôn list ( list đó sẽ ko tồn tại nữa)
# del emList
# print(emList) # báo lỗi ko tồn tại


# lặp qua list
# mylist = ["apple", "banana", "kiwi"]
# m = mylist.reverse()
# print(m)
 
# for x in mylist:
#     print(x)


# Cập nhật giá trị của phần tử trong list

mylist = ["apple", "banana", "kiwi"]
mylist[0] = 'melon'
print(mylist)