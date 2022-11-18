# LẬP TRÌNH HƯỚNG ĐỐI TƯỢNG (OOP)

# BÀI TẬP 1:
# You are making a video game! The given code declares a Player class, with its
# attributes and an intro() method.
# Complete the code to take the name and level from user input, create a Player project
# with the corresponding values and call the intro() method of that object.

# Sample input: Tony
#               12
# Sample output: Tony (Level 12)

# GIẢI:

# class Player:
#     def __init__(self, name, level):
#         self.name = name
#         self.level = level

#     def intro(self):
#         return self.name + " (Level " + str(self.level) + ")"

# tony = Player("Tony", 12)
# print(tony.intro())

# ---------------------------------------------------------------------------------

# BÀI TẬP 2:
# You are making a drawing application, which has a Shape base class.
# The given code defines a Rectangle class, creates a Rectangle objects and calls
# its area() and perimeter() methods.
# Do the following to complete the program:
# 1. Inherit the Rectangle class from Shape
# 2. Define the perimeter() method in the Rectangle class, printing the perimeter of the Rectangle.

# GIẢI:

# class Shape:
#     def __init__(self, dai, rong):
#         self.dai = dai
#         self.rong = rong

#     def area(self):
#         return self.dai * self.rong
    
# class Rectangle(Shape):
#     def perimeter(self):
#         return (self.dai + self.rong) * 2

# dai = Rectangle(5, 6)
# print(dai.perimeter())
# print(dai.area())

# ---------------------------------------------------------------------------------

# BÀI TẬP VỀ NHÀ:

#                                   Projec OOP
#                               Quản lý nhân viên

# 1. Tạo class có tên Nhân viên
# 2. Tạo một biến thuộc lớp để lưu trữ nhân viên
# 3. Viết hàm thêm thông tin nhân viên
# 4. Viết hàm cập nhật thông tin nhân viên
# 5. Viết hàm xoá nhân viên
# 6. Viết hàm hiển thị thông tin nhân viên
# 7. Tạo đối tượng thuộc lớp nhân viên
# 8. Tạo menu chức năng của chương trình

# GIẢI:

class Nhanvien:
    nhanviens = []

    def add_nv(self):
        n = int(input("Nhập số lượng nhân viên: "))
        for i in range(n):
            ten = input("Nhập tên nhân viên: ")
            self.nhanviens.append(ten)

    def hien_thi(self):
        return self.nhanviens

    def update_nv(self):
        ten_cu = input("Nhập tên nhân viên cũ: ")
        ten_moi = input("Nhập tên nhân viên mới: ")
        return self.nhanviens

    def xoa_nv(self):
        ten = input("Nhập tên nhân viên cần xóa: ")
        self.nhanviens.remove(ten)
        return self.nhanviens

nv_obj = Nhanvien()

chon = 0
while chon != 5:
    print("1. Thêm nhân viên")
    print("2. Hiển thị nhân viên")
    print("3. Cập nhật nhân viên")
    print("4. Xóa nhân viên")
    print("5. Thoát chương trình")

    chon = int(input("Mời chọn chức năng: "))
    if chon == 1:
        nv_obj.add_nv()
    elif chon == 2:
        print(nv_obj.hien_thi())
    elif chon == 3:
        print(nv_obj.update_nv())
    elif chon == 4:
        print(nv_obj.xoa_nv())
    else:
        print("Kết thúc, thoát chương trình")