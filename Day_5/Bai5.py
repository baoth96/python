# BÀI TẬP VỀ TUPLE:

# contacts = [('James', 42), ('Amy', 24), ('Join', 31), ('Amanda', 63), ('Bob', 18)]
# name = input("Nhap ten: ")
# for i in range(0, len(contacts)):
#     if name == contacts[i][0]:
#         print(name, "is", contacts[i][1])

# --------------------------------------------------------------------------------

# HỌC VỀ FILES:

# with open("test.txt", encoding="utf-8") as f:
#     print(f.read())

# with open("out.txt", "w", encoding="utf-8") as f:
#     f.write("Trung\n")
#     f.write("Đông\n")

# with open("out.txt", "a", encoding="utf-8") as f:
#     f.write("Tây\n")

# with open("out.txt", "r", encoding="utf-8") as f:
#     lines = f.readlines()
#     for line in lines:
#         print(line, end="")

# --------------------------------------------------------------------------------

# BÀI TẬP VỀ FILES:

# BÀI 1:
# Tập tin inp.txt chứa chiều dài và chiều rộng của hình chữ nhật (nằm trên một dòng),
# anh/chị hãy viết chương trình Python thực hiện:
# 1. Đọc các giá trị trong file inp.txt => chiều dài và chiều rộng
# 2. Viết hàm chuviCN, dientichCN để tính chu vi và diện tích hình chữ nhật
# có tham số là cạnh chiều dài và chiều rộng
# 3. Gọi hàm và tính kết quả, sau đó ghi kết quả vào file out.txt

# GIẢI:

# def chu_vi(a, b):
#     return (a+b)*2

# def dien_tich(a,b):
#     return a*b

# with open("test.txt", "r") as f:
#     ct = f.read()
#     lst = [int(i) for i in ct.split(" ")]
#     cv = chu_vi(lst[0], lst[1])
#     dt = dien_tich(lst[0], lst[1])

# with open("out.txt", "w") as f:
#     f.write(str(cv) + "\n")
#     f.write(str(dt))

# --------------------------------------------------------------------------------

# BÀI 2:
# Từ file test.txt gồm nhiều dòng khác nhau
# Lấy nội dung trong file test.txt và xuất ra file out.txt các chữ cái đầu.
# Ví dụ: test.txt: Thai hoang Bao
#                  Tran thi Thanh Thi
#          out.txt: Thb
#                   TtTT

#GIẢI:

# list = []

# def xu_ly(str_film):
#     ls = str_film.split(" ")
#     s = ""
#     for i in ls:
#         s = s +i[0]
#     return s

# with open("test.txt") as f:
#     lines = f.readlines()
#     for i in lines:
#         vt = xu_ly(i)
#         list.append(vt)

# with open("out.txt", "w") as f:
#     for i in list:
#         f.write(i + "\n")
        
# --------------------------------------------------------------------------------

# BÀI TẬP VỀ NHÀ:

# BÀI 1:
# 1. Yêu cầu nhập n (số học sinh trong lớp)
# Nhập tên của từng học sinh
# Lưu vào file
# 2. Đọc và in ra tên học sinh của lớp

# GIẢI:

# list = []
# n = int(input("Số học sinh trong lớp: "))

# for i in range(0, n):
#     ten = input("Nhập tên: ")
#     list.append(ten)

# with open("out.txt", "w") as f:
#     for i in list:
#         f.write(i + "\n")

# with open("out.txt", "r") as f:
#     print(f.read())

# --------------------------------------------------------------------------------

# BÀI 2:
# Đề bài 02 trong file ảnh

# GIẢI:

# list = []

# with open("test.txt", "r") as f:
#     n = f.read()
#     for i in range(1, int(n)+1):
#         if (int(n) % i == 0 and int(n) != i):
#             list.append(i)
#     sum = 0
#     for i in range(0, len(list)):
#         sum = sum + list[i]

# with open("out.txt", "w") as f:
#     if int(n) == sum:
#         f.write("YES")
#     if int(n) != sum:
#         f.write("NO")

# --------------------------------------------------------------------------------

# BÀI 3:
# Đề bài 01 trong file ảnh

# GIẢI:

# fi = open("test.txt")
# fo = open("out.txt", "w")
# num = fi.readlines()

# n = num[0]
# ln = [int(i) for i in (num[1].split(" "))]
# tong = 0
# st = ""

# for i in range(len(ln)):
#     if (int(n) % ln[i] == 0):
#         tong = tong + ln[i]
#         st = st + str(ln[i]) + " "

# fo.write(st + "\n")
# fo.write(str(tong))

# fo.close()
# fi.close()


with open("test.txt", "r") as f:
    num = f.readlines()
    n = num[0]
    m = [int(i) for i in (num[1].split(" "))]
    st = ""
    sum = 0
    for i in range(len(m)):
        if int(n) % m[i] == 0:
            st = st + str(m[i]) +" "
            sum = sum + m[i]

with open("out.txt", "w") as f:
    f.write(st + "\n")
    f.write(str(sum))