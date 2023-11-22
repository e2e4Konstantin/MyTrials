from dataclasses import dataclass


@dataclass
class Dog:
    name: str = "Palkan"

    def sound(self):
        print(f"{self.name}: Гав Гав")


if __name__ == "__main__":
    d = Dog("Grom")
    d.sound()
else:
    print(f"defines.py >> {__name__}")
