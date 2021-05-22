"""Module with common use of classes and functions"""
import datetime
from random import choice

import restaurant
import people


def populate_workers():
    """Create managers and cooks list to be used in Restaurant"""
    managers = [people.Manager("Silly", "Seaborn", 12345),
                people.Manager("Sally", "Landborn", 64578),
                people.Manager("Sully", "Spaceborn", 11223)]

    cooks = [people.Cook("Rikky", "Stormfire", 55794),
             people.Cook("Rukky", "Thunderfire", 5542)]
    managers.extend(cooks)

    return managers


rest = restaurant.Restaurant()

rest.hall_dispatcher.workers_list.extend(populate_workers())

rest.hall_dispatcher.add_customer()
print("Making orders")
rest.hall_dispatcher.make_order()
rest.hall_dispatcher.make_order()
rest.hall_dispatcher.make_order()

print("\nGetting transaction history\n")
print(rest.get_transactions_history([
    datetime.datetime(year=2021, month=1, day=1),
    datetime.datetime(year=2022, month=1, day=1)
]))

print("\nGetting statistics\n")
print(rest.get_statistics())

rest.hall_dispatcher.abort_order(
        choice(rest.hall_dispatcher.orders_list).order_id)

print("Suppressing the problem" + str(rest.get_problem().suppress_problem()))

car_order = rest.hall_dispatcher.make_car_order()
print(car_order)
print("Car order was delivered to the car" if car_order.deliver_to_car() else
      "Car order wasn't delivered")
