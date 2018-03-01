def get_distance(row1,col1,row2,col2):
  return abs(row1-row2) + abs(col1-col2)

def get_ride_length(ride):
  return get_distance(ride["start_row"], ride["fin_row"], ride["start_col"], ride["fin_col"])

def get_latest_possible_start_time(ride):
  return ride["latest_finish"] - get_ride_length(ride)

# Take in a list of unclaimed rides
# Return the rides sorted by the latest possible start time
def sort_rides(rides):
  return sorted(rides, key=get_latest_possible_start_time)