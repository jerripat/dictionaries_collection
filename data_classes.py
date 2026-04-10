from dataclasses import dataclass


@dataclass(order=True, frozen=True)
class Person:
    name: str
    age: int
    friends: list[str]


bob: Person = Person("Bob", 30, ["Alice", "Charlie"])
print(bob)
jerri: Person = Person("Jerri", 25, ["Bob", "Alice"])
mario: Person = Person("Mario", 35, [])

people: list[Person] = [bob, jerri, mario]
people.sort()

for person in people:
    print(person)

@dataclass(order=True, frozen=True)
class Rectangle:
    width: float
    height: float

    @property
    def area(self) -> float:
        return self.width * self.height

    @property
    def perimeter(self) -> float:
        return 2 * (self.width + self.height)

    def describe(self) -> None:
        print(f"Rectangle with width {self.width} and height {self.height}")
        print(f"Area: {self.area}")
        print(f"Perimeter: {self.perimeter}")

rect1: Rectangle = Rectangle(5.0, 3.0)
rect1.describe()