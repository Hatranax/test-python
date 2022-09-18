from abc import ABC

#import sys
#sys.path.insert(0,'c:\\Users\\Anastasiya\\HelloWorld\\test-python')

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
           raise NotEnoughFuel
        else:
            self.fuel -= distance*self.fuel_consumption


    
