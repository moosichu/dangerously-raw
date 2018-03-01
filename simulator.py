from car import Car

# Take a list of cars in flight of the form (car, ride, has_picked_up)
# where has_picked_up indicates whether we have picked up the person from the start
# return list of cars in flight in t + 1 and the list of newly available cars

def perform_time_step(t, cars_in_flight):
  newly_available_cars = []
  updated_cars_in_flight = []

  for (car, ride, has_picked_up) in cars_in_flight:
    # change pick up status if possible
    if (car.x, car.y) == (ride["start_col"], ride["start_row"]) and t >= ride["earliest_start"]:
      has_picked_up = True

    # Figure out where we're heading next
    next_destination = (ride["start_col"], ride["start_row"]) if has_picked_up else (ride["fin_col"], ride["fin_row"])

    # make a move towards thing
    if car.x < next_destination[0]: #move right on x axis
      car.position = (car.x + 1, car.y)
    elif car.x > next_destination[0]: #move left on x axis
      car.position = (car.x - 1, car.y)
    elif car.y < next_destination[1]: #move up on y axis
      car.position = (car.x, car.y + 1)
    elif car.y > next_destination[1]: #move down on y axis
      car.position = (car.x, car.y - 1)

    # If we are at the end of the ride, free up the car
    if (car.x, car.y) == next_destination and has_picked_up: #car has arrived
      newly_available_cars.append(car)
    else: #car is still in flight
      updated_cars_in_flight.append((car, ride, has_picked_up))

  return (updated_cars_in_flight, newly_available_cars)
