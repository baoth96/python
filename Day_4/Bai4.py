# BÀI 1:
# Nhập vào một email, in ra tên của email đó
# Ví dụ: input: thaihoangbao112@gmail.com
#        output: thaihoangbao112

# GIẢI:

# email = input("Nhap email: ")
# a = email.index("@", 0, len(email))

# print(email[0:a])

#------------------------------------------------------------------------------

# BÀI 2:
# Nhập vào một chuỗi (vừa chuỗi vừa số), tính tổng các số có trong chuỗi.

# GIẢI:

# day = input("")
# tong = 0
# for i in day:
#     if(ord(i) >48) and (ord(i) <= 57): #Bảng mã Ascii
#         tong = tong + int(i)
# print(tong)

#------------------------------------------------------------------------------

# BÀI 3:
# Nhập vào một chuỗi, in ra số lần xuất hiện của nguyên âm u, e, o
# Ví dụ: input: yeu em khong
#        output: u: 1, e: 2, o: 1

# GIẢI:

# a = "yeu em khong"
# b = ["e", "u", "o"]

# for i in range(0, len(b)):
#     dem = 0
#     for j in range(0, len(a)):
#         if b[i] == a[j]:
#             dem = dem + 1
#     print(b[i], ":", dem)

#-------------------------------------------------------------------------------

# BÀI 4:
# Cho chuỗi car = {"brand": "BMW", "year": 2018, "color": "red"}
# input: year
# output: 2018

# GIẢI:

# car = {"brand": "BMW", "year": 2018, "color": "red"}
# n = input("")
# print(car.get(n))

#-------------------------------------------------------------------------------

# BÀI TẬP VỀ NHÀ:
# Nhập vào một chuỗi, kiểm tra chuỗi đó có phải đối xứng hay ko?
# Ví dụ: abba là đối xứng, abab là ko đối xứng

# GIẢI:

# Cách 1:
# def chuoi_doi_xung(chuoi):
#     if chuoi[::-1] == chuoi:
#         print(chuoi, "là chuỗi đối xứng")
#     else:
#         print(chuoi, "là chuỗi không đối xứng")

# chuoi = input("Nhập vào chuỗi: ")
# chuoi_doi_xung(chuoi)

# Cách 2:
# def Xau_doi_xung(str):
#     """
#     :param str: string
#     :return: True if symmetrical, False if not symmetrical
#     """

#     if str[::-1] == str:
#         return True
#     return False

# str = input("Nhap vao xau bat ky: ")
# if Xau_doi_xung(str) is True:
#     print("Xau tren doi xung!")
# else:
#     print("Xau tren khong doi xung!")

#-------------------------------------------------------------------------------

# BÀI TẬP VỀ NHÀ:
# Đề bài 02 trong file ảnh

# GIẢI:

# list = []

# def nhan_vien(n):
#     for i in range(0, n):
#         ten = input("Nhập tên nhân viên: ")
#         list.append(ten)
#     print(list)

# def hien_thi_list(ten):
#     for i in list:
#         print(i)

# def vi_tri_nhan_vien(ten):
#     tim = list.index(str(ten), 0, len(list))
#     tim = tim + 1
#     print("Vị trí nhân viên:", tim)

# def xoa_nhan_vien(ten):
#     list.remove(ten)
#     print(list)

# chon = 0
# while chon != 5:
#     print("1: Nhập thông tin nhân viên")
#     print("2: Hiển thị thông tin")
#     print("3: Tìm kiếm nhân viên")
#     print("4: Xóa nhân viên")
#     print("5: Thoát chương trình")
#     chon = int(input("Mời chọn chức năng: "))
#     if chon == 1:
#         n = int(input("Nhập số lượng nhân viên: "))
#         nhan_vien(n)
#     elif chon == 2:
#         ten = ""
#         hien_thi_list(ten)
#     elif chon == 3:
#         ten = input("Nhập tên nhân viên cần tìm: ")
#         vi_tri_nhan_vien(ten)
#     elif chon == 4:
#         ten = input("Nhập tên nhân viên cần xóa: ")
#         xoa_nhan_vien(ten)
#     else:
#         print("Kết thúc, thoát chương trình.")

#-------------------------------------------------------------------------------

# BÀI TẬP VỀ NHÀ:
# Đề bài 03 trong file ảnh

# GIẢI:

list = []
list_1 = []
list_2 = []
n = int(input("Mời nhập vào n: "))
if 0 <= n <= 20:
    for i in range(1, n+1):
        so = int((input("Mời nhập số: ")))
        list.append(so)
        chuoi = ", ".join([str(j) for j in list])
    print("Chuỗi ban đầu là:", chuoi)
    
    for i in range(0, len(list)):
        k = list[i]
        if int(k) % 2 == 0:
            list_1.append(k)
            list_1.sort()
            chuoi_1 = ", ".join([str(j) for j in list_1])
    print("Chuỗi sau khi sắp xếp tăng dần các số chắn là:", chuoi_1)

    for i in range(0, len(list)):
        # k = list[i]
        if int(list[i]) % 2 != 0:
            list_2.append(list[i])
            list_2.sort()
            list_2.reverse()
            chuoi_2 = ", ".join([str(j) for j in list_2])
    print("Chuỗi sau khi sắp xếp giảm dần các số lẻ là:", chuoi_2)
