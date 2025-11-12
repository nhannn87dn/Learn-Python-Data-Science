weather = 'rain'
x = 123
# Nếu trời mưa thì tôi được ở nhà
# TH 1: Cú pháp ngắn với if
# if weather == 'rain' and x == 1:
#    print('Ở nhà')
#    print('abc')

#TH 2: Cú pháp đầy đủ với if
level = 'VIP'
orderAmount = 500
# Vd: Nếu mà level của khách hàng = VIP và hoá đơn mua hàng tối thiểu 500 
# thì được chiết khấu 10%
# Còn lại thì không.
if level == 'VIP':
    #print('discount 10')
    if orderAmount >= 500:
        print('discount 10')
else:
    print('ko dc chiet khau')

# TH 3: if if else
dtb = 7.5
# Nếu mà dtb >= 9 thì --> Xuất sắc
# Nếu dtb >= 8 và < 9 --> Giỏi
# Nếu dtb > 6.5 và < 8 thì Khá
# Nếu dtb > 5 và < 6.5 thì Trung Bình
# Còn lại là Yếu
if dtb >= 9:
    print('Xuat Sac')
elif dtb >= 8 and dtb < 9:
    print('Gioi')
elif dtb >= 6.5 and dtb < 8:
    print('Kha')
elif dtb >= 5 and dtb < 6.5:
    print('Kha')
else:
    print('Yeu')
    
    
c = 12
if c > 1:
    pass