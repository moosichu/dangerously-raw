from car import Car

#Will take a list of cars in flight of the form (car_id, current_position, destination_position)
#Will make one step in time, move the cars along and return a tuple with the next cars in flight and the cars which are now available
def move_cars(cars_in_flight): 
  return_cars_in_flight = []
  return_cars_free = []
  for car in cars_in_flight:
    new_car = Car()
    new_car.destination = car.destination
    new_car.id = car.id
    if car.position[0] < car.destination[0]: #move right on x axis
      new_car.position = (car.position[0] + 1, car.position[1])
    elif car.position[0] > car.destination[0]: #move left on x axis
      new_car.position = (car.position[0] - 1, car.position[1])
    elif car.position[1] < car.destination[1]: #move up on y axis
      new_car.position = (car.position[0], car.position[1] + 1)
    elif car.position[1] > car.destination[1]: #move down on y axis
      new_car.position = (car.position[0], car.position[1] - 1)
    if new_car.position == new_car.destination: #car has arrived
      return_cars_free.append(new_car)
    else: #car is still in flight
      return_cars_in_flight.append(new_car)
  return(return_cars_in_flight, return_cars_free)
