import assign_cars as ac
import sort_rides as sr

def solve(list_of_cars, list_of_rides, sim_steps):
    # Currently a stub
    available_cars = {}
    result = {}
    for car in list_of_cars:
        available_cars[car.id] = car
        result[car.id] = []

    sorted_rides = sr.sort_rides(list_of_rides)
    for t in range(0, sim_steps):
        assignments = ac.assign_cars(
            available_cars = available_cars,
            sorted_rides = sorted_rides,
            t = t
        )

        for car_id, ride_id in assignments.items():
            # TODO: add cars to cars in flight
            result[car_id].append(ride_id)
            pass

    # TODO: use the simulator

    return result