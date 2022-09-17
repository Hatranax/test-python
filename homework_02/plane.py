"""
создайте класс `Plane`, наследник `Vehicle`
"""

from base import Vehicle
from exceptions import CargoOverload

class Plane (Vehicle):
    cargo = 0
    max_cargo = 0

    def __init__(self,m_c):
        max_cargo = m_c
    
    def load_cargo(cargo_added):
        if cargo+cargo_added > max_cargo:
            raise CargoOverload('Too much cargo!')
        else:
            cargo += cargo_added

    def remove_all_cargo():
        a = cargo
        cargo = 0
        return a

