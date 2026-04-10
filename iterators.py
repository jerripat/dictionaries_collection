import random

class Dice:
    def __init__(self, rolls):
        self.rolls = rolls
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.rolls:
            self.count += 1
            return random.randint(1, 6)
        else:
            raise StopIteration

dice = Dice(3)
for die in dice:
    print(die)

#as list comprehension
die = [die for die in Dice(3)]
print(die)
d1,d2,d3 = die
print(f"Sum: {d1+d2+d3}")
print(d1,d2,d3)