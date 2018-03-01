class Car:
    id = 0
    x = 0
    y = 0
    def __repr__(self):
      return str(self)
    def __str__(self):
        return "id:" + str(self.id) + "; position: (" + str(self.x) + "," + str(self.y) + ")\n"


def get_car_list(num_cars):
  result = []
  for car_id in range(0, num_cars):
    car = Car()
    car.id = car_id
    result.append(Car())
  return result
