# a = float(input("Nhap vao a: "))
# print(a)


# x = 10 
# y = 12 
# # Output: x > y is False 
# print('x > y is',x>y) 
# # Output: x < y is True 
# print('x < y is',x<y) 
# # Output: x == y is False 
# print('x == y is',x==y) 
# # Output: x != y is True 
# print('x != y is',x!=y) 
# # Output: x >= y is False 
# print('x >= y is',x>=y) 
# # Output: x <= y is True 
# print('x <= y is',x<=y) 


# x1 = 5 
# y1 = 5 
# x2 = 'Hello' 
# y2 = 'Hello' 
# x3 = [1,2,3] 
# y3 = [1,2,3] 
# # Output: False 
# print(x1 is not y1) 
# # Output: True 
# print(x2 is y2) 
# # Output: False 
# print(x3 is y3) 


# x = 'Hello world' 
# y = {1:'a',2:'b'} 
# # Output: True 
# print('H' in x)  
# # Output: True 
# print(1 in y) 
# # Output: False 
# print('a' in y) 


# a = 2
# b = 2.0
# tich = a * b
# print(tich)


# chieu_cao = float(input("Nhap chieu cao: "))
# can_nang = float(input("Nhap can nang: "))

# BMI = can_nang / (chieu_cao **2)

# print("Chi so BMI: ", round(BMI, 2))

# if (BMI < 18.5):
#     print("Underweight")
# elif (18.5 <= BMI <= 24.9):
#     print("Normal")
# elif (25 <= BMI <= 29.9):
#     print("Overweight")
# elif (30 <= BMI <= 34.9):
#     print("Obese")
# else:
#     print("Extreamly Obese")


# x = int(input("Nhap vao so bat ky: "))
# if (x % 2 == 0):
#     print("So chan")
# else:
#     print("So le")


# BAI TAP VE NHA - BUOI 1
# Viết chương trình nhập vào tháng, nhập vào năm và in ra tháng đó có bao nhiêu ngày
# Lưu ý: Năm nhuận thì tháng 2 có 29 ngày

thang = int(input("Nhap vao thang: "))
nam = int(input("Nhap vao nam: "))

if (thang in {1, 3, 5, 7, 8, 10, 12}):
    print("Thang nay co 31 ngay")
elif (thang == 2):
    if (nam % 4 == 0 and nam % 100 != 0):
        print("Thang nay co 29 ngay")
    else:
        print("Thang nay co 28 ngay")
else:
    print("Thang nay co 30 ngay")
