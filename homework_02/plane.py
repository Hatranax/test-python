"""
создайте класс `Plane`, наследник `Vehicle`
"""

from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload





class Plane (Vehicle):
    cargo = 0
    max_cargo = 0

    def __init__(self,Vweight,VFuel,Vfuel_consumption,Vmax_cargo):
        super().__init__(Vweight,VFuel,Vfuel_consumption)
        self.max_cargo = Vmax_cargo
    
    def load_cargo(self,cargo_added):
        if self.cargo+cargo_added > self.max_cargo:
            raise CargoOverload('Too much cargo!')
        else:
            self.cargo += cargo_added

    def remove_all_cargo(self):
        a = self.cargo
        self.cargo = 0
        return a

