from car import Car

# Take a list of cars in flight of the form (car, ride, has_picked_up)
# where has_picked_up indicates whether we have picked up the person from the start 
# return list of cars in flight in t + 1 and the list of newly available cars

def perform_time_step(t, cars_in_flight):
  newly_available_cars = []
  updated_cars_in_flight = []

  for (car, ride, has_picked_up) in cars_in_flight:
    # change pick up status if possible
    if car.position == (ride["start_col"], ride["start_row"]) and t >= ride["earliest_start"]:
      has_picked_up = True

    # Figure out where we're heading next
    next_destination = (ride["start_col"], ride["start_row"]) if has_picked_up else (ride["end_col"], ride["end_row"])

    # make a move towards thing
    if car.position[0] < next_destination[0]: #move right on x axis
      car.position = (car.position[0] + 1, car.position[1])
    elif car.position[0] > next_destination[0]: #move left on x axis
      car.position = (car.position[0] - 1, car.position[1])
    elif car.position[1] < next_destination[1]: #move up on y axis
      car.position = (car.position[0], car.position[1] + 1)
    elif car.position[1] > next_destination[1]: #move down on y axis
      car.position = (car.position[0], car.position[1] - 1)

    # If we are at the end of the ride, free up the car
    if car.position == new_car.destination and has_picked_up: #car has arrived
      newly_available_cars.append(car)
    else: #car is still in flight
      updated_cars_in_flight.append((car, ride, has_picked_up))

  return (updated_cars_in_flight, newly_available_cars)
