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

# class Parrot:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def sing(self, song):
#         return "{} sings {}".format(self.name, song)
    
#     def dance(self):
#         return "{} is now dancing".format(self.name)

# blu = Parrot("Blu", 10)
# print(blu.sing("Happy"))
# print(blu.dance())

# --------------------------------------------------------------------------------------

# PHƯƠNG THỨC LỚP (Class methods):

# class Student:
#     school_name = "ABC School"
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def show(self):
#         print("Student:", self.name, self.age, Student.school_name)

#     def change_age(self, new_age):
#         self.age = new_age

#     @classmethod
#     def change_school_name(cls, new_name):
#         cls.school_name = new_name

# s1 = Student("Harry", 12)
# s1.show()
# s1.change_age(15)
# s1.show()
# Student.change_school_name("XYZ School")
# s1.show()

# --------------------------------------------------------------------------------------

# THỪA KẾ (Inheritance):

# class Bird:
#     def __init__(self):
#         print("Bird is ready")

#     def whoisthis(self):
#         print("Bird")

#     def swim(self):
#         print("Swim faster")

# class Penguin(Bird):
#     def __init__(self):
#         super().__init__()
#         print("Penguin is ready")

#     def whoisthis(self):
#         print("Penguin")

#     def run(self):
#         print("Run faster")

# peggy = Penguin()
# peggy.whoisthis()
# peggy.swim()
# peggy.run()

# --------------------------------------------------------------------------------------

# ĐƠN THỪA KẾ:

# class Vehicle: 
# 	def Vehicle_info(self): 
# 		print('Inside Vehicle class') 

# class Car(Vehicle): 
# 	def car_info(self): 
# 		print('Inside Car class') 

# car = Car() 
# car.Vehicle_info() 
# car.car_info()

# --------------------------------------------------------------------------------------

# ĐA THỪA KẾ:

# class Father():
#     def Driving(self):
#         print("Enjoys Driving")

# class Mother():
#     def Cooking(self):
#         print("Enjoys Cooking")

# class Child(Father, Mother):
#     def Playing(self):
#         print("Child Loves Playing")

# c = Child()
# c.Driving()
# c.Cooking()
# c.Playing()

# --------------------------------------------------------------------------------------

# THỪA KẾ NHIỀU CẤP:

# class Animal:
#     def speak(self):
#         print("Animal Speaking")

# class Dog(Animal):
#     def bark(self):
#         print("dog barking")

# class DogChild(Dog):
#     def eat(self):
#         print("Eating bread...")

# d = DogChild()
# d.bark()
# d.speak()
# d.eat()

# --------------------------------------------------------------------------------------

# THỪA KẾ (Hybrid Inheritance):

# class Vehicle: 
# 	def info(self): 
# 		print("This is Vehicle") 

# class Car(Vehicle): 
# 	def car_info(self, name): 
# 		print("Car name is:", name) 

# class Truck(Vehicle): 
# 	def truck_info(self, name): 
# 		print("Truck name is:", name) 

# obj1 = Car() 
# obj1.info() 
# obj1.car_info('BMW') 
# obj2 = Truck() 
# obj2.info() 
# obj2.truck_info('Ford')

# --------------------------------------------------------------------------------------

# THỪA KẾ (super() function):

# class Company:
#     def company_name(self):
#         return "Google"

# class Employee (Company):
#     def info(self):
#         c_name = super().company_name()
#         print("Jessa works at", c_name)

# emp = Employee()
# emp.info()

# --------------------------------------------------------------------------------------

# TÍNH GHI ĐÈ (Overriding):

# class Vehicle: 
# 	def max_speed(self): 
# 		print("max speed is 100 Km/Hour")

# class Car(Vehicle): 
# 	def max_speed(self): 
# 		print("max speed is 200 Km/Hour")

# car = Car() 
# car.max_speed()

# --------------------------------------------------------------------------------------

# TÍNH NẠP CHỒNG (Overloading): Phương thức cùng tên nhưng khác tham số, gọi là overloading

# VÍ DỤ 1:

# def addition(a, b): 
# 	c = a + b 
# 	print(c) 

# def addition(a, b, c): 
# 	d = a + b + c 
# 	print(d) 

# addition(3, 7, 5)


# VÍ DỤ 2:

# class Shape:
#     def area(self, a, b=0):
#         if b > 0:
#             print("Area of Rectangle is:", a * b)
#         else:
#             print("Area of Square is:", a **2)

# s = Shape()
# s.area(4)
# s.area(4, 5)

# --------------------------------------------------------------------------------------

# Access Modifiers in Python:

# 01: Private Member:

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.__salary = salary

# emp = Employee("Jessa", 10000)
# print("Name:", emp.name)
# print("Salary:", emp._Employee__salary)


# 02: Protected Member:

# class Company:
# 	def __init__(self): 
# 		self._project = "NLP" 

# class Employee(Company):
# 	def __init__(self, name): 
# 		self.name = name 
# 		Company.__init__(self) 
	
# 	def show(self): 
# 		print("Employee name :", self.name) 
# 		print("Working on project :", self._project) 

# c = Employee("Jessa") 
# c.show() 
# print('Project:', c._project)

# --------------------------------------------------------------------------------------

# Getter & Setter:

# class Student: 
# 	def __init__(self, name, age): 
# 		self.name = name # private member 
# 		self.__age = age 
	 
# 	def get_age(self): # getter method
# 		return self.__age 
	
# 	def set_age(self, age): # setter method 
# 		if age >= 15:
# 			self.__age = age
# 		else:
# 			Raise ("Error") 

# stud = Student('Jessa', 14) 
# # retrieving age using getter 
# print('Name:', stud.name, stud.get_age()) 
# # changing age using setter 
# stud.set_age(16) 
# # retrieving age using getter 
# print('Name:', stud.name, stud.get_age())

# --------------------------------------------------------------------------------------

# TÍNH ĐA HÌNH (Polymorphism):

class Ferrari: 
	def fuel_type(self): 
		print("Petrol") 
	
	def max_speed(self): 
		print("Max speed 350") 

class BMW: 
	def fuel_type(self): 
		print("Diesel") 
	def max_speed(self): 
		print("Max speed is 240") 

ferrari = Ferrari() 
bmw = BMW() 
# iterate objects of same type 
for car in (ferrari, bmw): 
	# call methods without checking class of object 
	car.fuel_type() 
	car.max_speed()
