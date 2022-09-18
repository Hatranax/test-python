"""
create dataclass `Engine`
"""

from dataclasses import dataclass


@dataclass
class Engine:
    volume : int
    pistons : int
    #def __init__(self,volume=None,pistons=None):
    #    self.volume = volume
    #    self.pistons = pistons