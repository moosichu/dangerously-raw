def solve(list_of_cars, list_of_rides, sim_steps):
    # Currently a stub
    available_cars = {}
    for car in list_of_cars:
        available_cars[car.id] = car
    for t in range(0, sim_steps):
        pass
    return {
        0: [0, 2, 6],   # car 0 does rides 0, 2 and 6
        1: [1, 3, 4, 5] # car 1 does rides 1, 3, 4 and 5
    }