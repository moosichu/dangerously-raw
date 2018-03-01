

def read_data(file_name):
    return {
        "num_rows": 3,
        "num_cols": 4,
        "num_vehs": 2,
        "num_rides": 3,
        "ride_bonus": 2,
        "sim_steps": 10,
        "rides": [
            {
                "start_row": 0,
                "start_col": 0,
                "fin_row": 1,
                "fin_col": 3,
                "earliest_start": 2,
                "latest_finish": 9
            },
            {
                "start_row": 1,
                "start_col": 2,
                "fin_row": 1,
                "fin_col": 0,
                "earliest_start": 0,
                "latest_finish": 9
            },
            {
                "start_row": 2,
                "start_col": 0,
                "fin_row": 2,
                "fin_col": 2,
                "earliest_start": 0,
                "latest_finish": 9
            }
        ]
    }


if __name__ == "__main__":
    data = read_data("stat")
    print(data)