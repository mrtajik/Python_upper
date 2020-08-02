"""
OOP
"""
#almost everything in Python is an object
#Classes in Python
class Person:
  def __init__(self, name, age): #self instance
    self.name = name
    self.age = age

p1 = Person("Mubin", 35)

print(p1.name)
print(p1.age)

#issubclass() function returns True if the specified object is a subclass of the specified object, otherwise False
class myAge:
  age = 35

class myObj(myAge):
  name = "Mubin"
  age = myAge

x = issubclass(myObj, myAge)
print(x)

#str() and repr() both are used to get a string representation of object.

#str() 
"""
import datetime
now = datetime.datetime.now()
 str(now)
'2019-03-29 01:29:23.211924'
 repr(now)
'datetime.datetime(2019, 3, 29, 1, 29, 23, 211924)'
"""

"""
Inheritance allows us to define a class that inherits all the methods and properties from another class.

Parent class is the class being inherited from, also called base class.

Child class is the class that inherits from another class, also called derived class.
"""
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

z= Person("Mubin", "Satymov")
z.printname()

