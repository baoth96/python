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
#         return self.name + "Level" + str(self.level)

# tony = Player("Tony", 12)
# print(tony.intro())

# ---------------------------------------------------------------------------------


# class Pet:
#     def __init__(self, name, favorite_food):
#         self.name = name
#         self.favorite_food = favorite_food

#     def eat(self):
#         print("I'm eating" + self.favorite_food)

# class Cat(Pet):  
#     def climb_tree(self):
#         print(self.name, " can climb tree")

# mao_mao = Cat("Mao Mao", "fish")
# mao_mao.eat()
# mao_mao.climb_tree()


class Shape:
    def __init__(self, dai, rong):
        self.dai = dai
        self.rong = rong

    def area(self):
        return self.dai * self.rong
    
class Rectangle(Shape):
    def perimeter(self):
        return (self.dai + self.rong) * 2

dai = Rectangle(5, 6)
print(dai.perimeter())
print(dai.area())