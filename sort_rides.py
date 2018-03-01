def get_ride_length(ride):
  return abs(ride.start_row-ride.fin_row) + abs(ride.start_col-ride.fin_col)

def get_latest_possible_start_time(ride):
  return ride.latest_finish - get_ride_length(ride)

# Take in a list of unclaimed rides
# Return the rides sorted by the latest possible start time
def sort_rides(rides)
  return sorted(rides, key=get_latest_possible_start_time)