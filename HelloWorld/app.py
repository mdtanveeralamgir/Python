#CLASSES
"""
class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}")


opel = Person("Opel")
opel.talk()

"""

"""
class Point: #pascal naming convension: 'EmailClient'
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self):
        print('move')

    def draw(self):
        print('draw')


point1 = Point(10, 20)
point1.move()
print(point1.x)

"""
#INHERITANCE
class Mammal:
    def walk(self):
        print('walk')
class Dog(Mammal):
    pass #A class cannot be empty. if nothing needs to add we need to tell 'pass'

class Cat(Mammal):
    def eat(self):
        print('eating')

dog = Dog()
dog.walk()
