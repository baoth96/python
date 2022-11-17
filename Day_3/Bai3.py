# HỌC VỀ HÀM def:

# BÀI TẬP 1:
# Viết chương trình nhập một số n. Chọn chức năng a hoặc b để tính:
# a. Tính ước của n
# b. Tính tổng 1/n-1 + 1/n-2 + 1/n-3 + ... + 1/n-(n-1)
# Nếu không chọn 1 trong 2 chức năng thì mời chọn lại, chọn một số bất kỳ để thoát chương tình.

# GIẢI BÀI TẬP 1:

# def tinh_uoc(n):
#     for i in range(1, n+1):
#         if (n % i == 0):
#             print(i)

# def tinh_tong(n):
#     s = 0
#     for i in range(1, n):
#         s = s + 1/(n-i)
#     print(s)

# chon = 0
# while (chon != 3):
#     print("1. Tim uoc")
#     print("2. Tinh tong")
#     print("3. Thoat")
#     chon = int(input("Moi ban chon chuc nang"))
#     if (chon == 1):
#         so = int(input("Moi ban nhap so"))
#         tinh_uoc(so)
#     elif(chon == 2):
#         so = int(input("Moi ban nhap so"))
#         tinh_tong(so)
#     else:
#         print("Nhap so khong hop le")

#------------------------------------------------------------------------------------

# HỌC VỀ DANH SÁCH list

# # Tạo list
# my_list = []
# my_list = [1, "2, 3.4, True"]
# # In 1 phần tử
# print(my_list[1])
# # Lấy nhiều phần tử
# print(my_list[1:3])
# # Lấy độ dài list
# print(len(my_list))

# # In các phần tử trong danh sách
# # c1
# for i in my_list:
#     print(i)
# # c2
# for i in range(0, len(my_list)):
#     print(my_list[i])

# # Các phương thức thao tác trên list

# # Thao tác trên list

# # Chèn 1 giá trị vào vị trí bất kỳ trong list
# my_list.insert(2, "Nam")
# print(my_list)

# # Chèn vào cuối
# my_list.append(13)
# print(my_list)

# # Xóa theo giá trị
# my_list.remove("Nam")
# print(my_list)

# # Xóa theo vị trí
# del my_list[2]
# print(my_list)

# # Sắp xếp tăng dần
# my_list2 = [1, 3, 3, 5, 7]
# my_list2.sort()
# print(my_list2)

# # Đảo chuỗi
# my_list2.reverse()
# print(my_list2)

# # Chuyển list thành chuỗi
# my_list2 = ["1", "3", "4", "7", "9"]
# s = ",".join(my_list2)
# print(s)

# # Chuyển chuỗi thành list
# s2 = s.split(",")
# print(s2)

#---------------------------------------------------------------------------------

# BÀI TẬP 2:

# diem = [10, 9.5, 7]

# # Tính điểm trung bình cộng
# tong = 0
# for i in diem:
#    tong = tong + i
# print(tong)

# # Nếu điểm thêm vào > 5 thì thêm vào vị trí bất kỳ
# them_diem = float(input("Nhập điểm: "))
# if them_diem > 5:
#     diem.insert(2, them_diem)
#     print(diem)

#---------------------------------------------------------------------------

# BÀI TẬP VỀ NHÀ 1:

# Cho 1 danh sách các số  
# num = [1, 9, 5, 6, 9, 0, 2, 3]
# a. Nhập vào số n, kiểm tra nếu n có trong danh sách thì in ra vị trí cuối cùng của n trong danh sách
# Vd: Nhập n = 9: in ra 4
# b. Nhâp vào số k, in ra danh sách các số lớn hơn k có trong list num
# Vd: Nhập k = 3: in ra [5, 6, 9, 9]

# GIẢI:

num = [1, 9, 5, 6, 9, 0, 2, 3]

# # Câu a:
num2 = []
n = int(input("Nhập n: "))
for i in range(0, len(num)):
    if n == num[i]:
        num2.append(i)
print(num2[-1])

# Câu b:
# k = int(input("Nhập k: "))
# num3 = []
# for i in num:
#     if i > k:
#         num3.append(i)

# num3.sort()
# print(num3)


#-----------------------------------------------------------------------------------

# BÀI TẬP VỀ NHÀ 2:

# Cho nums = [2, 7, 11, 15]
# target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# GIẢI:

# nums = [2, 7, 11, 15]
# nums4 = []
# k = int(input("Nhập: "))

# for i in range(0, len(nums)):
#     for j in range(i, len(nums)):
#         if (nums[i] + nums[j] == k and i != j):
#             nums4.append(i)
#             nums4.append(j)
# print(nums4)
