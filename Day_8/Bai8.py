# LẬP TRÌNH HƯỚNG ĐỐI TƯỢNG (OOP) - TIẾP TỤC

# --------------------------------------------------------------------------------------

# THUỘC TÍNH CỦA ĐỐI TƯỢNG (Instance variables):

# class Student: 
# # constructor 
#     def __init__(self, name, age): 
# 	# Instance variable 
#         self.name = name 
#         self.age = age
 
# # create first object 
# s1 = Student("Jessa", 20) 
# # access instance variable 
# print('Object 1') 
# print('Name:', s1.name) 
# print('Age:', s1.age) 
# # create second object 
# s2= Student("Kelly", 10) 
# # access instance variable 
# print('Object 2') 
# print('Name:', s2.name) 
# print('Age:', s2.age)

# --------------------------------------------------------------------------------------

# THAY ĐỔI GIÁ TRỊ CỦA Instance Var:

# class Student: 
# 	# constructor 
# 	def __init__(self, name, age): 
# 		# Instance variable 
# 		self.name = name 
# 		self.age = age 

# # create object 
# stud = Student("Jessa", 20) 
# print('Before') 
# print('Name:', stud.name, 'Age:', stud.age) 
# # modify instance variable 
# stud.name = 'Emma' 
# stud.age = 15 
# print('After') 
# print('Name:',stud.name,'Age:', stud.age)

# --------------------------------------------------------------------------------------

# PHƯƠNG THỨC (Methods):

class Parrot:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sing(self, song):
        return "{} sings {}".format(self.name, song)
    
    def dance(self):
        return "{} is now dancing".format(self.name)

blu = Parrot("Blu", 10)
print(blu.sing("Happy"))
print(blu.dance())

# --------------------------------------------------------------------------------------

