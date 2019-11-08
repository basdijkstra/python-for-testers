from objects import car
import pytest

test_data = [
    ("Lamborghini", "Countach", 1988, False),
    ("Maserati", "Ghibli", 2018, True),
    ("Ford", "Focus", 2015, True)
]


@pytest.mark.parametrize("make, model, year, is_recent", test_data)
def test_is_car_recent(make, model, year, is_recent):
    my_car = car.Car(make, model, year)
    assert my_car.is_a_recent_car() == is_recent


# def test_is_my_lamborghini_recent():
#     my_car = car.Car("Lamborghini", "Countach", 1988)
#     assert my_car.is_a_recent_car() is False
#
#
# def test_is_my_maserati_recent():
#     my_car = car.Car("Maserati", "Ghibli", 2018)
#     assert my_car.is_a_recent_car() is True
#
#
# def test_is_my_ford_recent():
#     my_car = car.Car("Ford", "Focus", 2015)
#     assert my_car.is_a_recent_car() is True
