# import math as m

# print(m.ceil(1.4))

# print(sum((1,2,35)))

from datetime import date, time, datetime, timedelta

# chi tiết thời gian hiện tại
now = datetime.now()
print("Now:", now)


print(now.year, now.month, now.day)
print(now.hour, now.minute, now.second)

# Định dạng format thời gian
formatted = now.strftime("%d-%m-%Y %H:%M:%S")
print(formatted)

# format 
text = "2025-10-30 09:15:00"
dt2 = datetime.strptime(text, "%Y-%m-%d %H:%M:%S")
print(dt2)

# t1 = time(14, 30, 15)
# print(t1)

# thời gian hiện tại
# today = date.today()
# print(today)
# # in ra năm hiện tại
# print(today.year)
# # in ra tháng hiện tại
# print(today.month)
# print(today.day)
# print(today.weekday())

# tạo đối tượng thời gian từ ngày cụ thể
# d1 = date(1985, 10, 30)
# print(d1)