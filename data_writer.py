

def write_data(data, file_name):
    with open(file_name, "w") as file:
        for car_id, ride_ids in data.items():
            num_rides = len(ride_ids)
            # We want the first number to be the number of rides a given car does
            line = "{}".format(num_rides)
            # Give the ids of the rides the car does
            for ride in ride_ids:
                line += " {}".format(ride)
            line += "\n"
            file.write(line)



if __name__ == "__main__":
    write_data({
        0: [0, 2, 6],   # car 0 does rides 0, 2 and 6
        1: [1, 3, 4, 5] # car 1 does rides 1, 3, 4 and 5
    }, "output/test.out")
