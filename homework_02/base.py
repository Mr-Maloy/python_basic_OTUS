from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    """
    Это общий класс для транспортных средств
    """
    started = False
    weight = 0
    fuel = 0
    fuel_consumption = 0

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if self.started is False:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError("No fuel to use vehicle!")

    def move(self, distance):
        if self.fuel // self.fuel_consumption < distance:
            raise NotEnoughFuel("Not enough fuel to go so far")
        else:
            self.fuel -= distance * self.fuel_consumption

# Комментарий для Pull Request