from dataclasses import dataclass


@dataclass
class Cat:
    name: str = "Murzik"

    def sound(self):
        print(f"{self.name}: Мяу Мяу...")


if __name__ == "__main__":
    d = Cat("Findus")
    d.sound()
else:
    print(f"hdef.py >> {__name__}")
