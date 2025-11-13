
#  5 + 3 = 8
#  7 + 8  = ? 

# định nghĩa 1 hàm trong python
# def sum(a, b):
#     return a + b
 
# # cách gọi hàm
# r = sum(2, 6)
# print(r)

# hàm ko có tham số
# def hello():
#     print('Xin chao')
    
# hello()


# def cal(a, b, pt="+"):
#     if pt == '+':
#         print(a+ b)
#     elif pt == '-':
#         print(a - b)

# cal(5,2, '-')


# Phạm vi toàn cục

# x = 2
# def myFunction():
#     global x
#     x = 3
#     print(x) #
# # kết thúc khối của hàm
# myFunction()
# print(x)

# def sayHello(name):
#     print(f"Chào {name}")
# sayHello('Tuan')
# # chuyển thành lambda

# s = lambda name: f"Chào {name}"
# print(s('KHoa'))

# *args trong function

#print(1,34,5,6,7,True)

def console(*args):
    print(args)
    
console(1, True, None, [1,2])


def my_function(**myvar):
  print("Type:", type(myvar))
  print("Name:", myvar["name"])
  print("Age:", myvar["age"])
  print("All data:", myvar)

my_function(name = "Tobias", age = 30, city = "Bergen")