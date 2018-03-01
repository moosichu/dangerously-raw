from car import Car

def read_data(file_name):
    with open(file_name) as file:
        first_line = file.readline().split()
        rides = []
        line = file.readline()
        ride_id = 0
        while line != "":
            ride_info = line.split()
            rides.append({
                "start_row":       int(ride_info[0]),
                "start_col":       int(ride_info[1]),
                "fin_row":         int(ride_info[2]),
                "fin_col":         int(ride_info[3]),
                "earliest_start":  int(ride_info[4]),
                "latest_finish":   int(ride_info[5]),
                "ride_id": ride_id
            })
            line = file.readline()
            ride_id = ride_id + 1

        result = {
            "num_rows":   int(first_line[0]),
            "num_cols":   int(first_line[1]),
            "num_vehs":   int(first_line[2]),
            "num_rides":  int(first_line[3]),
            "ride_bonus": int(first_line[4]),
            "sim_steps":  int(first_line[5]),
            "rides":      rides
        }
