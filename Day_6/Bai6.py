# HỌC VỀ FILES.CSV:

# import csv
# data = [
#     {"id":"7575", "sdt":"567457", "email":"abc@gmail.com"},
#     {"id":"7586", "sdt":"567457", "email":"abc@gmail.com"}
# ]

# def read():
#     with open ("khach_hang.csv", "r") as f:
#         reader = csv.DictReader(f)
#         for i in reader:
#             print(i["ten"])

# def write(data):
#     with open("data.csv", "w") as f:
#         write = csv.DictWriter(f, fieldnames=["id", "sdt", "email"])
#         write.writeheader()
#         write.writerows(data)

# write(data)
# read()

# -------------------------------------------------------------------------------

# BÀI TẬP CSV:
# Tập tin inp.csv chứa chiều dài và chiều rộng của hình chữ nhật (nằm trên một dòng), 
# anh/chị hãy viết chương trình Python thực hiện:
# 1. Đọc các giá trị trong file inp.csv => chiều dài và chiều rộng
# 2. Viết hàm chuviCN, dientichCN để tính chu vi và diện tích hình chữ nhật
# có tham số là cạnh chiều dài và chiều rộng
# 3. Gọi hàm và tính kết quả, sau đó ghi kết quả vào file out.csv

# GIẢI:

import csv

def dientich(a, b):
    return a * b

def chuvi(a, b):
    return (a + b) * 2

def read():
    data = []
    with open("inp.csv", "r") as f:
        reader = csv.DictReader(f)
        dt = {}
        for i in reader:
            dt["dientich"] = str(dientich(int(i["chieudai"]), int(i["chieurong"])))
            dt["chuvi"] = str(chuvi(int(i["chieudai"]), int(i["chieurong"])))
            data.append(dt)
    return data

ls = read()

def write(ls):
    with open("out.csv", "w") as f:
        write = csv.DictWriter(f, fieldnames=["dientich", "chuvi"])
        write.writeheader()
        write.writerows(ls)

write(ls)
read()

# -------------------------------------------------------------------------------
