from objects import car

def test_car_info():
    my_car = car.Car("Ford", "Focus", 2019)
    assert my_car.get_info() == "This is a 2019 Ford Focus"

def test_car_year():
    my_car = car.Car("Ford", "Focus", 2019)
    assert my_car.year > 2018