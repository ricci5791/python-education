import transports

aircraft = transports.Aircraft(2500)
subway = transports.Subway(7)
bus = transports.Bus(50)
tanker = transports.Tanker("Susan")

transports.Transport.show_total_distance()

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
tanker.name
tanker.name = "Dilemma"
tanker.name

aircraft.show_transport_list()
transports.Transport.show_total_distance()

print("\n")
print(aircraft.flight_time)

aircraft.flight_time = 5

print(aircraft.flight_time)

movable1 = transports.Transport()
movable2 = transports.Transport()

movable1.move([3, 3])
movable2.move([6, 0])

print(movable1.coords)
print(movable2.coords)

movable3 = movable1 + movable2
movable4 = movable1 - movable2

print(movable3)
print(movable4)
