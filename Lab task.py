# =========================================
# 1. Person Class
# =========================================

class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, City: {self.city}")


p1 = Person("Ali", 22, "Lahore")
p1.display()


# =========================================
# 2. Car Class
# =========================================

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display(self):
        print(f"Car: {self.make} {self.model} ({self.year})")


car1 = Car("Toyota", "Corolla", 2020)
car1.display()


# =========================================
# 3. Circle Class
# =========================================

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius * self.radius

    def circumference(self):
        return 2 * 3.14159 * self.radius


circle1 = Circle(5)
print("Circle Area:", circle1.area())
print("Circle Circumference:", circle1.circumference())


# =========================================
# 4. Rectangle Class
# =========================================

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


rect1 = Rectangle(10, 5)
print("Rectangle Area:", rect1.area())
print("Rectangle Perimeter:", rect1.perimeter())


# =========================================
# 5. Student Class
# =========================================

class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def average_marks(self):
        return sum(self.marks) / len(self.marks)


student1 = Student("Sara", 101, [85, 90, 88])
print("Average Marks:", student1.average_marks())


# =========================================
# 6. Book Class
# =========================================

class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def display(self):
        print(f"{self.title} by {self.author} ({self.publication_year})")


book1 = Book("Python Basics", "John Smith", 2023)
book1.display()


# =========================================
# 7. Employee Class
# =========================================

class Employee:
    def __init__(self, name, salary, designation):
        self.name = name
        self.salary = salary
        self.designation = designation

    def display(self):
        print(f"Employee: {self.name}, Designation: {self.designation}, Salary: {self.salary}")


emp1 = Employee("Ahmed", 50000, "Developer")
emp1.display()


# =========================================
# 8. Bank Class
# =========================================

class Bank:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Insufficient balance")

    def display_balance(self):
        print("Current Balance:", self.balance)


account1 = Bank("Ali", "PK001", 10000)
account1.deposit(5000)
account1.withdraw(3000)
account1.display_balance()


# =========================================
# 9. Shape Inheritance
# =========================================

class Shape:
    def area(self):
        pass


class CircleShape(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius * self.radius


class RectangleShape(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


c = CircleShape(4)
r = RectangleShape(6, 3)
t = Triangle(8, 5)

print("Circle Area:", c.area())
print("Rectangle Area:", r.area())
print("Triangle Area:", t.area())


# =========================================
# 10. Animal Inheritance
# =========================================

class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        return "Bark"


class Cat(Animal):
    def sound(self):
        return "Meow"


class Cow(Animal):
    def sound(self):
        return "Moo"


dog = Dog("Buddy")
cat = Cat("Kitty")
cow = Cow("Bella")

print(dog.name, "says", dog.sound())
print(cat.name, "says", cat.sound())
print(cow.name, "says", cow.sound())
