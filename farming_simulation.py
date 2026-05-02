import time
import random


class Tractor:
    def __init__(self, fuel=100, efficiency=1.0):
        self.fuel = fuel
        self.efficiency = efficiency

    def use(self):
        if self.fuel <= 0:
            print("Tractor is out of fuel.")
            return False
        self.fuel -= random.randint(5, 15)
        print(f"Tractor used. Fuel left: {self.fuel}")
        return True


class Field:
    def __init__(self):
        self.state = "empty"

    def plant(self):
        if self.state == "empty":
            self.state = "planted"
            print("Seeds planted.")
        else:
            print("Field is not ready for planting.")

    def grow(self):
        if self.state == "planted":
            self.state = "growing"
            print("Crops are growing...")
        else:
            print("Nothing to grow.")

    def harvest(self):
        if self.state == "growing":
            self.state = "empty"
            yield_amount = random.randint(50, 150)
            print(f"Harvest completed. Yield: {yield_amount}")
        else:
            print("Nothing to harvest.")


def simulate():
    tractor = Tractor()
    field = Field()

    print("Farming Simulation Started\n")

    field.plant()
    time.sleep(1)

    if tractor.use():
        field.grow()
    time.sleep(1)

    if tractor.use():
        field.harvest()

    print("\nSimulation Ended")


if __name__ == "__main__":
    simulate()