"""
создайте класс `Car`, наследник `Vehicle`
"""
from base import Vehicle

class Car(Vehicle):
    engine = None

    def set_engine(self,Vengine):
        self.engine = Vengine
