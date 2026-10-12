# class is a blueprint , an object is a real thing built from blueprint.
# self always the first paramet , self refers to the specific object using the method

class Students:
    def __init__(self, name , age):
        self.name= name
        self.age = age

    def greet( self):
        print(f"Hello , I am {self.name}")  

s1 = Students('Ali', 20)
s1. greet()          


class Car:

    def __init__(self , brand_name , year):
        self.brand_name = brand_name
        self.year = year


    def des(self):
        print(f" The brand name of the car is {self.brand_name} and the year is {self.year}")   


s2= Car('BMW' , '2000')
s2.des()

# task 2
class Car:

    def __init__(self , brand_name , year):
        self.brand_name = brand_name
        self.year = year


    def des(self):
        print(f" The brand name of the car is {self.brand_name} and the year is {self.year}")   

s2= Car('BMW' , '2000')
s2.des()
s3= Car('Toyota' , '2002')
s2.des()

# instance vs class variables and methods

class Students:
    school = 'Netsol'
    def __init__(self, name):
        self.name = name
s1 = Students('Ali')
s2 = Students('Sara')
print(s1.school , s2.school)

print(s2.name)



# task 1
class Employee:
    company = 'Netsol' 
    def __init__(self, name):
             self.name = name  

s4 = Employee('Sara')
print(s4.company)    


# task 2 
# if employee is printing on the terminal then it is mean that class contain that variable
class Employee:
    company = 'Netsol' 
    def __init__(self, name):
             self.name = name  

s4 = Employee('Sara')
s5 = Employee('Ali')
s6 = Employee('Nida')

print(s4.company , s5.company , s6.company)
# print(s4.company)   
# print(s5.company) 
# print(s6.company)  

# constructor and destructor
class Students:
     def __init__(self , name):
          self.name = name
          print(f"{self.name} created")
     def __del__(self):
          print(f"{self.name} destroyed")
               
s1 = Students('Ali')
del s1        



# task 1
class Book:
     def __init__(self , name):
          self.name = name
          print(f"{self.name} Book added")
     def __del__(self):
          print(f"{self.name} Book removed")
# task 2               
s1 = Book('Self imporvement')
del s1        


# inheritance
# it lets a clss (child) reuse code from another class(parent)
# multilevel a->b->c each level inherits from the one above



class Animals:
     def eat(self):
          print('Eating')
# single inheritance          
class Dog(Animals):  
     def bark(self):
          print('barking')


d = Dog()
d.eat()
d.bark()    


# task 1
class Vehical:
    def start(self):
         print('It is parent class')


class Car(Vehical):
     def honk(self):
          print('It is an object')
                   
        
d = Car()
d.honk()

# task 2
class Shape:
     def color(self):
          print('it is shape class')

class Circle(Shape):
     def diameter(self):
          print('it is 1st inherited class')

class Square(Shape):
     def size(self):
          print('it is 2nd inherited class')  

d1 = Shape()
d1.color()
d1.diameter()
d1.size()



# multiple inheritance 
class Camera():
     def working(self):
          print("Camera")

class Phone():
     def working(self):
          print("Phone")

class Smartphone(Camera , Phone):
     pass 

Smartphone().working()
# Smartphone.__mro__


# access specifier and name mangling
class Bankaccount():
     def __init__(self , holder):
          self.holder= holder
          self._pin = 123
          self.__password = 'secret'

ob1 = Bankaccount("Mamoona")
print(ob1.holder)      
# print(ob1.pin)  error      

# inner class, association, aggregation  composition
# task 1
class Engine():
     def start(self):
          print("engine start")

class Car():
     def __init__(self):
          self.engine = Engine()

     def drive(self):
          self.engine.start()      

Car().drive()         


# task 2
class Book():
     def name(self):
          print("what is your book name")

class Library():
      def __init__(self):
           self.book = Book()

      def info(self):
           self.book.name()
               
Library.info()

# polymorphism

# task 1
class Square:
     def area(self):
          print('square area')

class Circle:
     def area(self):
          print('circle area')   

for shape in [Circle() , Square()]  
shape.area()      

# task2 

# magic/ dunder function 
# task 1
class Product:
     def __init__(self , name , price):
          self.name = name
          self.price = price

     def __str__(self):
          print(f"Check the info: {self.name} and {self.price} ")

p = Product("ALML" , 3000)
print(p)          

# task 2

class Item:

    def __init__(self):
        self.items = ["Apple", "Banana", "Mango", "Orange"]

    def __len__(self):
        return len(self.items)


i = Item()
# len look for __len__ function 
print(len(i)) 


# dynamic polymorphism
# task 1
class Employee:
     def pay(self):
          print("it is an employee parent class")

class Manager(Employee):
     def pay(self):
          print("it is an manager child class")     

# task 2
job =[Employee() , Manager()]
for e in job:
     e.pay()               


# abtract method and clasees , data classes , keyword arguments


