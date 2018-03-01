import data_reader as dr
import data_writer as dw
import car
import solver

filenames = [
    "a_example"
    # "b_should_be_easy",
    # "c_no_hurry",
    # "d_metropolis",
    # "e_high_bonus"
]


if __name__ == "__main__":
    for filename in filenames:
        print("operating on {}".format(filename))
        input_data = dr.read_data("input/" + filename + ".in")
        list_of_cars = car.get_car_list(input_data["num_vehs"]) # takes number of cars and returns list of cars of that size
        output_data = solver.solve(
            list_of_cars = list_of_cars,
            list_of_rides = input_data["rides"],
            sim_steps = input_data["sim_steps"]
        )
        dw.write_data(output_data, "output/" + filename + ".out")
