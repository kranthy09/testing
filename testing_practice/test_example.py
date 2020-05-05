import pytest
from example import check_email_format
from car_v2 import Car


def test_check_email_format_with_invalid_email_raise_exception():
    
    #Arrange
    email_to_check = "badememail.com"
    
    #Act
    with pytest.raises(Exception) as e:
        check_email_format(email_to_check)
    
    assert str(e.value) == "Invalid email format"


@pytest.mark.parametrize("max_speed, acceleration, tyre_friction, current_speed", [
    (130,10,3,7),(20,3,10,0)
])
def test_apply_break_when_car_is_in_motion(max_speed, acceleration, tyre_friction, current_speed):
    
    car = Car(color="Red", max_speed=max_speed, acceleration=acceleration, tyre_friction=tyre_friction)
    car.start_engine()
    car.accelerate()
    car.apply_brakes()

    assert car.current_speed == current_speed


def test_accelerate_more_than_max_speed_limit(car):
    
    #Act
    car.start_engine()
    car.accelerate()
    car.accelerate()
    car.accelerate()
    car.accelerate()
    car.accelerate()
    
    #Assert
    assert car.current_speed == 30


def test_apply_break_when_tyre_friction_is_greater_than_current_speed(car):
    
    #Act
    car.start_engine()
    car.accelerate()
    car.accelerate()
    car.apply_brakes()
    car.apply_brakes()
    car.apply_brakes()
    car.apply_brakes()
    car.apply_brakes()
    car.apply_brakes()
    car.apply_brakes()
    car.apply_brakes()
    car.apply_brakes()
    car.apply_brakes()
    
    #Assert
    assert car.current_speed == 0