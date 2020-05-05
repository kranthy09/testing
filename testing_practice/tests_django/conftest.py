import pytest


@pytest.fixture
def car():
    from car_v2 import Car
    
    car_obj = Car(color='Red', max_speed=30, acceleration=10, tyre_friction=3)
    
    return car_obj


