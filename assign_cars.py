import sort_rides as sr

# Takes a list of cars and a ride and returns the closest car
# cars must be a non-empty array
def closest_car(cars, ride, t):
  closest_car = sorted(cars, key=lambda car: sr.get_distance(ride["start_col"], ride["start_row"], car.x, car.y))[0]
  # Check that the car can make it to the ride in time
  # i.e. The car can make it to the start point before the latest start time
  if sr.get_distance(ride["start_col"], ride["start_row"], closest_car.x, closest_car.y) + t > ride["latest_finish"] - sr.get_ride_length(ride):
    return None
  else:
    return closest_car


def get_new_sorted_rides(sorted_rides, num_rides_removed):
  new_sorted_rides = []
  ride_number = 0
  return sorted_rides[num_rides_removed:]

# At a single time step
# Given all the available cars
# And all the sorted rides
# sorted_rides should be sorted by last possible start time (i.e. finish time - distance)
# Return a map from car_id to ride_id
# available_cars is a map from car_id to car
def assign_cars(available_cars, sorted_rides, t):
  assignments = {}
  num_rides_removed = 0
  new_sorted_rides = []
  for ride in sorted_rides:
    # Make sure we still have cars
    if not available_cars:
      return assignments, get_new_sorted_rides(sorted_rides, num_rides_removed)
    # Get the closest car
    cc = closest_car(available_cars.values(), ride, t)
    if cc == None:
      num_rides_removed = num_rides_removed + 1
      continue
    # Make the assignment and remove the car from available cars
    assignments[cc.id] = (available_cars[cc.id], ride["ride_id"])
    del(available_cars[cc.id])
    num_rides_removed = num_rides_removed + 1


  return assignments, []