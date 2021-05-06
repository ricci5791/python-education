"""Module which contains class hierarchy for different variants of transport"""
import random


class MovableObject:
    """Class which contains methods for object that can move or be moved"""

    def __init__(self):
        self.coords = [0., 0.]
        self.velocity = 0.

    def move(self, new_coords: list[float, float]):
        """Method which accepts list of 2 coords and set it to a instance
        :param new_coords:"""
        self.coords = new_coords

    def change_speed(self, new_speed: float):
        """Method which accepts float number(speed) and set it to a instance
        :param new_speed:"""
        self.velocity = new_speed

    def __str__(self):
        return f"Object coords: {self.coords}, velocity: {self.velocity}\n"


class Transport(MovableObject):
    """Class that represents basic implementation for vehicle"""
    transport_list = list()

    def __new__(cls, *args, **kwargs):
        instance = super(Transport, cls).__new__(cls)
        cls.transport_list.append(instance)
        return instance

    def __init__(self):
        super().__init__()
        self._is_start_engine = False
        self._transport_mass = 1.
        self.payload_mass = 0
        self.max_speed = 100

    def start_engine(self):
        """Starts transport engine"""
        self._is_start_engine = True

    def move(self, new_coords: list[float, float]):
        """Moves transport if engine ignited
        :param new_coords:"""
        if not self._is_start_engine:
            print("Firstly you need to ignite your engine!")
            return
        self.coords = new_coords

    def add_payload(self, payload_mass):
        """Add payload to a transport
        :param payload_mass:"""
        self.payload_mass = payload_mass

    def unload_payload(self, payload_mass):
        """Unload payload from a transport. Can be unloaded fractionally
        :param payload_mass:"""
        if payload_mass > self.payload_mass:
            print(f"You can't unload {payload_mass}. It's too much!")
            return
        self.payload_mass -= payload_mass

    @staticmethod
    def show_transport_list():
        """Print out list of all created instances of class
        and it's derivatives"""
        print(f"List of instances: {Transport.transport_list}")

    def __str__(self):
        return super().__str__() + \
               f"With payload mass: {self.payload_mass}; " \
               f"with{'' if self._is_start_engine else ' not'} ignited engine\n"


class Aircraft(Transport):
    """Represents vehicle that can fly
    :param max_payload: Max carried weight"""

    def __init__(self, max_payload=5000):
        super().__init__()
        self.max_payload = max_payload

    def airport_distance(self) -> tuple[float, float]:
        """Add distance from the aircraft to a random airport"""
        return self.coords[0] - random.randint(1, 100), \
               self.coords[1] - random.randint(1, 100)

    def add_payload(self, payload_mass):
        """Add payload to a aircraft with some checks
        :param payload_mass:"""
        if payload_mass > self.max_payload:
            print(f"Too much of payload. Max is {self.max_payload}")

    def __str__(self):
        return super().__str__() + f"Max payload is {self.max_payload}"


class Tanker(Transport):
    """Represents ship that can carry petroleum
    :param name: Name of ship
    :param max_route_length: Max path length without refuel
    """

    def __init__(self, name, max_route_length=1000):
        super().__init__()
        self.name = name
        self.max_route_length = max_route_length

    def make_sound(self):
        """Makes sounds :)"""
        print(f"Piiiiip from {self.name}!")

    def __str__(self):
        return super().__str__() + \
               f"Can carry {self.payload_mass} barrels of petroleum"


class Bus(Transport):
    """Represents city bus with basic function to make stop
    :param max_passengers: Max count of being boarded
    """

    def __init__(self, max_passengers):
        super().__init__()
        self.max_passengers = max_passengers
        self.passengers = 0

    def make_stop(self, passengers_diff):
        """Add given passengers to a bus
        :param passengers_diff:"""
        if self.passengers + passengers_diff > self.max_passengers:
            print("Too many passengers on board. Take less of them!")
            return
        self.passengers += passengers_diff

    def get_passengers_count(self):
        """Return passengers count boarded"""
        return self.passengers

    def __str__(self):
        return super().__str__() + \
               f"Passengers: {self.passengers} out of {self.max_passengers}"


class Subway(Transport):
    """Subway class that can append/pop wagons,
     accepts wagon count and width of railway
     :param wagon_count:
     :param railway_width:
     """

    def __init__(self, wagon_count=5, railway_width=1460):
        super().__init__()
        self.railway_width = railway_width
        self.wagon_count = wagon_count

    def append_wagons(self, wagon_count):
        """Append wagon to a train
        :param wagon_count:"""
        self.wagon_count += wagon_count

    def pop_wagons(self, wagon_count):
        """Pop wagon from a train
        :param wagon_count:"""
        if wagon_count > self.wagon_count:
            print("Too many to pop!")
            return
        self.wagon_count -= wagon_count

    def get_railway_width(self):
        """Return standard railway path width"""
        return self.railway_width

    def __str__(self):
        return super().__str__() + \
               f"Can run on {self.railway_width} rails width " \
               f"with {self.wagon_count} wagons"


if __name__ == "__main__":
    aircraft = Aircraft(2500)
    subway = Subway(7)
    bus = Bus(50)
    tanker = Tanker("Susan")

    print("\nAircraft functionality")
    print(f"Nearest airfield is {aircraft.airport_distance()}")
    aircraft.move([2, 3])
    aircraft.start_engine()
    aircraft.move([2, 3])

    print("\nSubway functionality")
    print("Popping 6 wagons from the subway")
    subway.pop_wagons(6)

    print("Popping another 6 wagons from the subway")
    subway.pop_wagons(6)

    print("\nSubway rail width:" + str(subway.get_railway_width()))

    print("\nBus functionality")
    print(f"Passengers before stop: {bus.passengers}")
    bus.make_stop(5)
    print(f"Passengers after stop: {bus.passengers}")

    print("\nTanker functionality")
    tanker.make_sound()
    print("Adding 500 barrels of payload")
    tanker.add_payload(500)
    print(tanker)

    aircraft.show_transport_list()
