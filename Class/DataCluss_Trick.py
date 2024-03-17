# https://docs.python.org/3/library/dataclasses.html#class-variables

from dataclasses import dataclass, field

@dataclass
class InventoryItem:
    name: str
    unit_price: float
    quantity_on_hand: int = 0
    # sizes: list[str] = field(default=['medium'], init=False)
    sizes: list[str] = field(default_factory=list)

    def total_coast(self) -> float:
        return self.unit_price * self.quantity_on_hand

# print(help(InventoryItem))
x = InventoryItem('Boc', 5.5)
print(x.__repr__())
