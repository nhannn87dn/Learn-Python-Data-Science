#print(4 => 4)


    
# try:
#     x = 5
#     y = 2
#     print( x / y)
    
#     m = [1,3]
#     print(m[2])
    
# except ZeroDivisionError:
#     print('Ko the chia mot so cho 0')
# except IndexError:
#     print('Index ko ton tai')
    
def divide(x, y):
    try:
        result = x / y
        
    except ZeroDivisionError:
        print("Không thể chia cho 0")
    else:
        print("Kết quả là: ", result)
    finally:
        print("Đã thực hiện xong lệnh")
        
#divide(5,0)

# x = input("Nhap vao mot gia tri so: ")
# print(type(x))
# if not x.isnumeric():
#  # dùng raise để ném lỗi.
#   raise TypeError("Only integers are allowed")
# if not type(int(x)) is int:
#     raise TypeError("Only integers are allowed")

# NHập vào một số > 5
try:
    n = int(input('Nhap vao so > 5: '))
    if n < 5:
        raise Exception("Vui long nhap vao mot so lon hon 5")
except Exception as e:
    print('Co loi xay ra: ', e)