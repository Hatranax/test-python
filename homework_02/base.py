from abc import ABC

from homework_02.exceptions import LowFuelError, NotEnoughFuel

class Vehicle(ABC):
    weight : int
    started = False
    fuel : int
    fuel_consumption : int
    
    def __init__(self,Vweight,Vfuel,Vfuel_consumption):
        self.weight = Vweight
        self.fuel = Vfuel
        self.fuel_consumption = Vfuel_consumption

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError('There is no juice in fuel tank!')

    def move(self,distance):
        if distance*self.fuel_consumption > self.fuel:
           raise NotEnoughFuel('Not enough fuel!')
        else:
            self.fuel -= distance*self.fuel_consumption


    
