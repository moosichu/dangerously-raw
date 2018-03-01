class Car:
    def __init__(self, id, x, y):
      self.id = id
      self.x = x
      self.y = y
    def __repr__(self):
      return str(self)
    def __str__(self):
        return "id:" + str(self.id) + "; position: (" + str(self.x) + "," + str(self.y) + ")\n"


def get_car_list(num_cars):
  result = []
  for car_id in range(0, num_cars):
    car = Car(car_id, 0, 0)
    result.append(car)
  return result
