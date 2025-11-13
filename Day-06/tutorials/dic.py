# # person = {
# #     "name": "John",
# #     "age": 30,
# #     "city": "WDC"
# # }
# # # dùng len để lấy số lượng phần tử có trong dict
# # print(len(person))

# # #1. Truy cập vào phần tử của dict dựa vào key của phần tử 
# # print(person['name']) # ==> John

# # # Lấy danh sách các keys của từ điển
# # print(person.keys()) # trả về một list
# # print(person.values()) # trả về list của các values trong từ điển

# # # lấy danh sách các phần tử trong dict
# # print(person.items())

# # # check sự tồn tại của một key nào đó trong dict
# # if "city" in person:
# #     print('yes')
# # else:
# #     print('no')
    
# # # 2. Thay đổi giá trị của phần tử trong dict

# person = {
#     "name": "John",
#     "age": 30,
#     "city": "WDC"
# }
# # thay đổi city thành New york ?
# person["city"] = 'New York'
# person.update({"age": 40})
# print(person)

# # Thêm phần tử mới vào cho dict
# person['mobile'] = '0988777666'
# print(person)

# # xoá phần tử khỏi dict
# # person.pop("mobile") # xoá một phần tử với key cụ thể
# # print(person)
# # person.clear()
# # print(person)
# # del person
# # print(person)


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# # for k in thisdict:
# #     print(k, thisdict[k]) # k là key của phần tử

# # for v in thisdict.values():
# #     print(v) # v là value của phần tử

# for i in thisdict.items():
#      print(i) # i là phần tử đang lặp qua

myProfile = {
    "id": 1,
    "fullName": "Nguyen va A",
    "kids": {
        "kid_one": {
            "name": "con 1",
            "age": 3
        },
        "kid_two": {
            "name": "con 2",
            "age": 3
        }
    }
}