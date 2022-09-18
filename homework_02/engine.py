"""
create dataclass `Engine`
"""
class Engine():
    volume = None
    pistons = None
    def __init__(self,volume=None,pistons=None):
        self.volume = volume
        self.pistons = pistons