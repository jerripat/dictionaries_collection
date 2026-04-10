from dataclasses import dataclass

@dataclass(order=True)
class Point:
    x: float
    y: float

p1 = Point(2.0, 3.0)
p2 = Point(4.0, 5.0)
print(p1,p2)

print(p1 > p2)

@dataclass(order=True)
class InventoryItem:
    name: str
    price: float
    quantity: int = 0

    def total_cost(self) -> float:
        return self.price * self.quantity

inv1 = InventoryItem("Apple", 1.0, 10)
inv2 = InventoryItem("Orange", 0.5, 20)
print(inv1.price, inv2.quantity)