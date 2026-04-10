from dataclasses import dataclass

@dataclass(order=True)
class Investor:
    name: str
    age: int
    cash: float
    hobbies: str


i1 = Investor("Jerri ", 45, 23000,'golf')
i2 = Investor("Johnny ", 45, 2000, 'craps')

print(i1)
print(i2)