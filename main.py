import data_reader as dr
import data_writer as dw


filenames = [
	"a_example",
	"b_should_be_easy",
	"c_no_hurry",
	"d_metropolis",
	"e_high_bonus"
]

for filename in filenames:
	input_data = dr.read_data("input/" + filename + ".in")
	# output_data = solve(input_data) # pipeline here
	
	dw.write_data(output_data, "out/" + filename + ".out")


if __name__ == "__main__":
    print("We are dangerously raw!!!!")
    data = data_reader.read_data("input/a_example.in")
    print(data)