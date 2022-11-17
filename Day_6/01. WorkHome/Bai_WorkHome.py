# BÀI TẬP VỀ NHÀ:

# BÀI 1:

# Đề Bài 01 Trong File Word:
# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.

# Example 1:
# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

ls = []
lst = [1, 2, 3, 4]
for i in lst:
    ls.append(sum(lst[0:i]))
print(ls)

# ls = []
# tong = 0
# for i in range(0, len(lst)):
#     tong = tong + lst[i]
#     ls.append(tong)

# print(lst)

# GIẢI:

# with open("inp.txt", "r") as f:
#     nums = f.read()
#     lst = [int(i) for i in nums.split(" ")]


# ----------------------------------------------------------------------------

# BÀI 2:
# Đề Bài 02 Trong File Word:
# Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
# Return the array in the form [x1,y1,x2,y2,...,xn,yn].

# Example 1:
# Input: nums = [2,5,1,3,4,7], n = 3
# Output: [2,3,5,4,1,7]
# Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].
nums = [2, 5, 1, 3, 4, 7]

lst = []
for i in range(0, len(nums)-3):
    lst.append(nums[i])
    lst.append(nums[i+3])

print(lst)

# GIẢI:

# with open("inp.txt", "r") as f:
#     nums = f.read()
#     lst = [int(i) for i in nums.split(" ")]

# a = int(len(lst)/2)
# list_1 = []
# list_2 = []

# for i in range(0, a):
#     list_1.append(lst[i])

# for i in range(a, len(lst)):
#     list_2.append(lst[i])

# list_3 = ""
# for i in range(0, a):
#     list_3 = list_3 + str(list_1[i]) + " " + str(list_2[i]) + " "
#     lst_3 = list_3.split()
# print(lst_3)
