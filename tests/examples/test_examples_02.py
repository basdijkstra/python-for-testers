from objects import robust_car
import pytest


def test_car_error_raised():
    with pytest.raises(ValueError):
        my_car = robust_car.Car("Ducati", "Monster", 2019)


def test_car_error_message():
    with pytest.raises(ValueError) as ve:
        my_car = robust_car.Car("Ducati", "Monster", 2019)
    assert str(ve.value) == "Ducati does not make cars!"
