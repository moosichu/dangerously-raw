

def read_data(file_name):
    with open(file_name) as file:
        first_line = file.readline().split()
        rides = []
        line = file.readline()
        ride_id = 0
        while line != "":
            ride_info = line.split()
            rides.append({
                "start_row":       ride_info[0],
                "start_col":       ride_info[1],
                "fin_row":         ride_info[2],
                "fin_col":         ride_info[3],
                "earliest_start":  ride_info[4],
                "latest_finish":   ride_info[5],
                "ride_id": ride_id
            })
            line = file.readline()
            ride_id = ride_id + 1

        result = {
            "num_rows":   first_line[0],
            "num_cols":   first_line[1],
            "num_vehs":   first_line[2],
            "num_rides":  first_line[3],
            "ride_bonus": first_line[4],
            "sim_steps":  first_line[5],
            "rides":      rides
        }

    return result


if __name__ == "__main__":
    data = read_data("input/a_example.in")
    print(data)
