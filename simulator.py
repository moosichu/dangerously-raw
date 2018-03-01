# #Will take a list of cars in flight of the form (car_id, current_position, destination_position)
# #Will make one step in time, move the cars along and return a tuple with the next cars in flight and the cars which are now available
# def move_cars(cars_in_flight):
#   return_cars_in_flight = []
#   return_cars_free = []
#   for (car_id, (position_x, position_y), (dest_x, dest_y)) in cars_in_flight:
#     new_car = (car_id, (position_x, position_y), (dest_x, dest_y))
#     if position_x < dest_x: #move right on x axis
#       new_car = (car_id, (position_x + 1, position_y), (dest_x, dest_y)
#     elif position_x > dest_x: #move left on x axis
#       new_car = (car_id, (position_x - 1, position_y), (dest_x, dest_y)
#     elif position_y < dest_y: #move up on y axis
#       new_car = (car_id, (position_x, position_y + 1), (dest_x, dest_y)
#     elif position_y > dest_y: #move down on y axis
#       new_car = (car_id, (position_x, position_y - 1), (dest_x, dest_y)
#     if new_car[1][1] == new_car[2][1] &&
#       new_car[1][2] == new_car[2][2]: #car has arrived
#       return_cars_free += new_car
#     else: #car is still in flight
#       return_cars_in_flight += new_car
#   return(return_cars_in_flight, return_cars_free)
