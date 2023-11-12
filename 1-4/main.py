# 1).

class Animal:
    def __init__(self, sound):
        self.sound = sound

    def make_sound(self):
        pass


class Cat(Animal):
    def make_sound(self):
        print(self.sound)


class Dog(Animal):
    def make_sound(self):
        print(self.sound)


class Fish(Animal):
    def make_sound(self):
        print(self.sound)


cat = Cat("Miau")
dog = Dog("Gaw")
fish = Fish("Fish sound")

cat.make_sound()
dog.make_sound()
fish.make_sound()


# 2).

class Shape:
    def __init__(self):
        pass

    def area(self):
        pass


class Circle(Shape):
    def __init__(self, r):
        super().__init__()
        self.r = r

    def area(self):
        return 3.14 * self.r ** 2


class Square(Shape):
    def __init__(self, a):
        super().__init__()
        self.a = a

    def area(self):
        return self.a ** 2


class Rectangle(Shape):
    def __init__(self, a, b):
        super().__init__()
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b


circle = Circle(5)
square = Square(6)
rectangle = Rectangle(7, 8)

print(circle.area())
print(square.area())
print(rectangle.area())


# 3).

class ObjectList:
    def __init__(self, list):
        self.list = list
        pass

    def print_info(self):
        for marks in self.list:
            print(f"{type(marks)}")
            print(f"Attributes - \n\t - {marks}\n\n")


list = ObjectList([3, "hello", [1, 2, 3], {'a': 1, 'b': 2}, (4, 5, 6)])
list.print_info()


# 4).

class Building:
    def __init__(self, name, address, count_of_floor):
        self.name = name
        self.address = address
        self.count_of_floor = count_of_floor

    def description(self):
        print(f"Name: {self.name}")
        print(f"Address: {self.address}")
        print(f"Count of floor: {self.count_of_floor}\n\n\n")


class School(Building):
    def description(self):
        super().description()


class Hospital(Building):
    def description(self):
        super().description()


class Museum(Building):
    def description(self):
        super().description()


print("SCHOOL")
school = Building("Дом на Набережной", "Набережная Кутузова, 14", 3)
school.description()

print("HOSPITAL")
hospital = Building("Резиденция на Лесной", "Лесная улица, 24", 1)
hospital.description()

print("MUSEUM")
museum = Building("Элегантный особняк", "Проспект Мира, 109", 10)
museum.description()
