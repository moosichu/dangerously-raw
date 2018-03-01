import assign_cars as ac
import sort_rides as sr

def solve(list_of_cars, list_of_rides, sim_steps):
    # Currently a stub
    available_cars = {}
    for car in list_of_cars:
        available_cars[car.id] = car

    sorted_rides = sr.sort_rides(list_of_rides)
    for t in range(0, sim_steps):
        assignments = ac.assign_cars(
            available_cars = available_cars,
            sorted_rides = sorted_rides,
            t = t
        )

        for assignment in assignments:
            # TODO: Remove cars from available cars list
            # TODO: add cars to cars in flight
            # TODO: use the simulator
            # TODO: add the rides to the result
            pass

    return {
        0: [0, 2, 6],   # car 0 does rides 0, 2 and 6
        1: [1, 3, 4, 5] # car 1 does rides 1, 3, 4 and 5
    }