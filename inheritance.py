# inheritance/ single heritance
class Car:
    @staticmethod
    def start():
     print("car started")
    
    @staticmethod
    def stop():
       print("car stopped")

class ToyotaCar(Car):
   def __init__(self,name):
      self.name=name

car1=ToyotaCar("fortuner")
car2=ToyotaCar("prius")
print(car1.name) # fortuner


# example 2
class Car:
    @staticmethod
    def start():
     print("car started")
    
    @staticmethod
    def stop():
       print("car stopped")

class ToyotaCar(Car):
   def __init__(self,name):
      self.name=name

car1=ToyotaCar("fortuner")
car2=ToyotaCar("prius")
print(car1.name)  # fortuner
print(car1.start())  # car started


# multilevel inheritance
class Car:
   @staticmethod
   def start():
      print("car started")

   @staticmethod
   def stop():
      print("car stopped")

class ToyotaCar(Car):
   def __init__(self,brand):
      self.brand=brand

class Fortuner(ToyotaCar):
   def __init__(self, type):
      self.type=type

car1=Fortuner("diesel")
car1.start() # car started

# multiple inheritance

class A:
   varA="welcome to class A"
class B:
   varB="welcome to class B"
class C(A,B):
   varC="welcome to class C"
c1=C()
print(c1.varC)
print(c1.varB)
print(c1.varA)
   
'''welcome to class C
   welcome to class B
   welcome to class A
'''


   