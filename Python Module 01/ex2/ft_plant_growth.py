#!/usr/bin/env python3


class Plant:
    def __init__(self, name: str, height: float, days: int) -> None:
        self.name = name
        self.height = height
        self.days = days
        self.growth_rate: float = 0.8

    def grow(self) -> None:
        self.height = round(self.height + self.growth_rate, 1)

    def age(self) -> None:
        self.days += 1

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.days} days old")


if __name__ == "__main__":
    plant = Plant("Rose", 25.0, 30)  # name, height, days

    print("=== Garden Plant Growth ===")
    plant.show()

    initial_height = plant.height

    for day in range(1, 8):
        plant.grow()
        plant.age()
        print(f"=== Day {day} ===")
        plant.show()

    growth = round(plant.height - initial_height, 1)
    print(f"Growth this week: {growth}cm")
