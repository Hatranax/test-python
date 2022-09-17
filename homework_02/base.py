from abc import ABC
from email.errors import StartBoundaryNotFoundDefect


class Vehicle(ABC):
    weight = 0
    started = False
    fuel = 0
    fuel_consumption = 0
    
    def __init__(self,w,f,f_c):
        weight = w
        fuel = f
        fuel_consumption_= f_c
