# OOPs

# 1) class  : blupreint of an object.
# 2) object : instance of a class
# 3) self
# 4) constructer
# 5) inharitance
# 6) Abstraction
# 7) Encapsulation
# 8) Polymorphism


# OOPs : 

# class xyz:
#     def mthd1(self):
#         print("i am from class xyz")
    
#     def mthd2(self):
#         print("i am method 2")
        
# obj = xyz()
# obj.mthd2()
# obj.mthd1()



# 4) constructer : __init__


# class xyz:
#     def __init__(self, a, b):
#         # print("hlo seriiiiii")
#         self.name = a
#         self.age = b
    
#     def car(self):
#         print(f"username is {self.name} and age is {self.age}")

# obj = xyz("kriss", 20)
# obj.car()

# xy = xyz("moris", 30)
# xy.car()


# constuercter : __init__

class cls1:
    def __init__(self, x, y, z):
        print("heyyyyyyyyyyyy")
        self.a = x
        self.b = y
        self.c = z
        
    def sumthis(self):
        print(self.a + self.b + self.c)
        
obj = cls1(10, 20, 30)
obj.sumthis()

obj1 = cls1(1, 2, 3)
obj1.sumthis()

