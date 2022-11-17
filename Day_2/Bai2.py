# number = int(input("Nhap vao mot so: "))
# sum = 0


# for i in range(2, number):
#     if i % 2 == 0:
#         sum += i
# print(sum)


# n = 5
# for i in range(5):
#     for j in range(5-i):
#         print("", end=" ")
#     for k in range(i+1):
#         print("*", end=" ")
#     print("")


# n = int(input("Nhap vao n: "))

# while n > 0:
#     s = 0
#     for i in range(1, n+1):
#         s = s + 1/i
#         print("Tong la", round(s, 2))
#         n = int(input("Nhap vao n: "))


# n = int(input("Nhap vao n: "))
# i = 1
# dem = 0

# while i <= n:
#     if (i % 2 == 0):
#         dem = dem +1
#     i = i + 1
# print("Dem bao nhieu so chan:", dem)


# n = int(input("Nhap vao n: "))
# dem = 0

# for i in range(1, n+1):
#     if (i % 2 == 0):
#         dem = dem +1
# print("Dem bao nhieu so chan:", dem)


# BÀI TẬP VỀ NHÀ:
# 1. Viết chương trình khi chạy chương trình yêu cầu nhập số N, sử dụng vòng lặp (for, while) để:
#     a> In ra các số từ 1..n, số lẻ từ 1..n, số chẵn từ 1..n
#     b> Tính tổng các số từ 1..n
#     c> Tính tổng các số lẻ 1..n
#     d> Tính tổng các số chẵn 1..n
#     e> Đếm có bao nhiêu số chẵn
#     f> Đếm có bao nhiêu số lẻ

# GIẢI:
# a> In ra các số từ 1..n, số lẻ từ 1..n, số chẵn từ 1..n
# a.1> In ra các số từ 1..n

# n = int(input("Nhap n: "))
# for i in range(0, n):
#     i = i + 1
#     print(i, end=" ")

# a.2> số chẵn từ 1..n

# n = int(input("Nhap n: "))
# for i in range(0, n):
#     i = i + 1
#     if (i % 2 == 0):
#         print(i, end=" ")

# a.3> số lẻ từ 1..n

# n = int(input("Nhap n: "))
# for i in range(0, n):
#     i = i + 1
#     if (i % 2 != 0):
#         print(i, end=" ")

# b> Tính tổng các số từ 1..n

# n = int(input("Nhap n: "))
# i = 0
# sum = 0   
# while i < n:
#     i = i + 1
#     sum = sum + i
# print("Tong la:", sum)

# c> Tính tổng các số lẻ 1..n

# n = int(input("Nhap n: "))
# i = 0
# sum = 0
# while i < n:
#     i = i + 1
#     if (i % 2 != 0):
#         sum = sum + i
# print("Tong so le la:", sum)

# d> Tính tổng các số chẵn 1..n

# n = int(input("Nhap n: "))
# i = 0
# sum = 0
# while i < n:
#     i = i + 1
#     if (i % 2 == 0):
#         sum = sum + i
# print("Tong so chan la:", sum)

# f> Đếm có bao nhiêu số lẻ

# n = int(input("Nhap n: "))
# i = 0
# dem = 0
# while i < n:
#     i = i + 1
#     if (i % 2 != 0):
#         dem = dem + 1
# print("Dem bao nhieu so le:", dem)


# BÀI TẬP VỀ NHÀ:
# 2. Nhập vào một số không âm, hỏi có bao nhiêu bước để trả nó về 0.
# Nếu số hiện tại là số chắn, bạn có thể chia 2 nó, ngược lại, nếu là số lẻ thì bạn trừ đi 1.

n = int(input("Nhap n: "))
dem = 0

while n != 0:
    if (n % 2 == 0):
        n = n/2
    else:
        n = n -1
    dem = dem + 1
print("Steps:", dem)