"""Module which contains class hierarchy for different variants of transport"""


class MovableObject:
    """Class which contains methods for object that can move or be moved"""

    def __init__(self):
        self.coords = [0., 0.]
        self.velocity = 0.

    def move(self, new_coords: list[float, float]):
        """Method which accepts list of 2 coords and set it to a instance"""
        self.coords = new_coords

    def change_speed(self, new_speed: float):
        """Method which accepts float number(speed) and set it to a instance"""
        self.velocity = new_speed

    def __str__(self):
        return f"Object coords: {self.coords},\n" \
               f"Object velocity: {self.velocity}\n"


class Transport(MovableObject):
    """Class that represents basic implementation for vehicle"""

    def __init__(self):
        super().__init__()
        self.is_start_engine = False
        self.transport_mass = 1.
        self.payload_mass = 0
        self.max_speed = 100

    def start_engine(self):
        """Starts transport engine"""
        self.is_start_engine = True

    def move(self, new_coords: list[float, float]):
        """Moves transport if engine ignited"""
        if not self.is_start_engine:
            print("Firstly you need to ignite your engine!")
            return
        self.coords = new_coords

    def add_payload(self, payload_mass):
        """Add payload to a transport"""
        self.payload_mass = payload_mass

    def unload_payload(self, payload_mass):
        """Unload payload from a transport. Can be unloaded fractionally"""
        if payload_mass > self.payload_mass:
            print(f"You can't unload {payload_mass}. It's too much!")
            return
        self.payload_mass -= payload_mass

    def __str__(self):
        return super().__str__() + \
               f"With payload mass: {self.payload_mass} and" \
               f" with{'' if self.is_start_engine else ' not'} ignited engine"


if __name__ == "__main__":
    trans = Transport()
    print(trans)
    trans.start_engine()
    print(trans)
