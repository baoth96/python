# BÀI TẬP VỀ NHÀ:

# ĐỀ BÀI 03 TRONG FILE HÌNH 02:

# GIẢI:

# with open("inp.txt", "r") as f:
#     num = f.readlines()
#     n = num[0]
#     k = [int(i) for i in (num[1].split(" "))]
#     list = []
#     for i in range(len(k)):
#         if int(n) == k[i]:
#             list.append(i)
#             lst = " ".join(str(i) for i in list)

# with open("out.txt", "w") as f:
#     f.write(lst)

# ------------------------------------------------------------------------------

# ĐỀ BÀI 04 TRONG FILE HÌNH 02:

# GIẢI:

# with open("inp.txt", "r") as f:
#     num = f.read()
#     list = [int(i) for i in num.split(" ")]
#     list.reverse()
#     lst = " ".join(str(i) for i in list)

# with open("out.txt", "w") as f:
#     f.write(lst)

# ------------------------------------------------------------------------------

# ĐỀ BÀI 05 TRONG FILE HÌNH 03:

# GIẢI:

# def fibonaci(n):
#     f0 = 0
#     f1 = 1
#     fn = 1

#     for i in range(1, n):
#         f0 = f1
#         f1 = fn
#         fn = f0 + f1
#     return fn

# lst = ""
# with open("inp.txt", "r") as f:
#     n = f.read()
#     for i in range(0, (int(n)+1)):
#         if int(fibonaci(i)) <= int(n):
#             lst = lst + str(fibonaci(i)) + " "

# with open("out.txt", "w") as f:
#     f.write(lst)


n = 13

lst = [1, 1]
for i in range(2, n):
    lst.append(lst[i-1] + lst[i-2])
print(lst[0:lst.index(n)+1])
