import assign_cars as ac
import sort_rides as sr
import simulator as sim

def solve(list_of_cars, list_of_rides, sim_steps):
    # Currently a stub
    available_cars = {}
    cars_in_flight = []
    result = {}
    for car in list_of_cars:
        available_cars[car.id] = car
        result[car.id] = []

    sorted_rides = sr.sort_rides(list_of_rides)
    for t in range(0, sim_steps):
        # print("timestep: " + str(t))
        # print("  cars:")
        # for car in available_cars.values():
        #     print("    {}".format(car.id))

        # print("  sorted_rides:")
        # print(sorted_rides)

        assignments, sorted_rides = ac.assign_cars(
            available_cars = available_cars,
            sorted_rides = sorted_rides,
            t = t
        )

        for car_id, (car, ride_id) in assignments.items():
            fin_row = list_of_rides[ride_id]["fin_row"]
            fin_col = list_of_rides[ride_id]["fin_col"]
            result[car_id].append(ride_id)
            cars_in_flight.append((car, list_of_rides[ride_id], False))

        cars_in_flight, newly_available_cars = sim.perform_time_step(
            t, cars_in_flight
        )

        # for car, ride, is_available in cars_in_flight:
        #     if car.id in available_cars.keys():
        #         available_cars[car.id] = car

        # Add the newly_available_cars to list of available cars
        for available_car in newly_available_cars:
            available_cars[available_car.id] = available_car

        if sorted_rides == []:
            break

    return result