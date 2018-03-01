import assign_cars as ac
import sort_rides as sr

def solve(list_of_cars, list_of_rides, sim_steps):
    # Currently a stub
    available_cars = {}
    cars_int_flight = []
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

        for car_id, (car, ride_id) in assignments.items():
            rides = result["rides"]
            fin_row = rides[ride_id]["fin_row"]
            fin_col = rides[ride_id]["fin_col"]
            car.destination = (fin_col, fin_row)
            result[car_id].append(ride_id)
            cars_int_flight.append(car, ride_id, False)
            pass

    # TODO: use the simulator

    return result