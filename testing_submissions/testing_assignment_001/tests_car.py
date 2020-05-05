import pytest
from car import Car

@pytest.mark.parametrize("max_speed, acceleration, tyre_friction",[
    (-10,10,3), (0, 7, 2)
])
def test_for_invalid_max_speed_when_negative_or_zero_max_speed_is_given(max_speed, acceleration, tyre_friction):
    
    # Act
    with pytest.raises(Exception) as e:
        Car(color="blue",acceleration=acceleration, max_speed=max_speed, tyre_friction=tyre_friction)
        
    # Assert
    assert str(e.value) == "Invalid value for max_speed"


@pytest.mark.parametrize("max_speed, acceleration, tyre_friction",[
    (10,-10,3), (4, 0, 5)
])
def test_for_invalid_acceleration_when_negative_or_zero_acceleration_is_given(max_speed, acceleration, tyre_friction):
    #Act
    with pytest.raises(Exception) as e:
        Car(color="blue",acceleration=acceleration, max_speed=max_speed, tyre_friction=tyre_friction)
        
    #Assert
    assert str(e.value) == "Invalid value for acceleration"


@pytest.mark.parametrize("max_speed, acceleration, tyre_friction",[
    (10,10,-3), (90, 7, 0)
])
def test_for_invalid_tyre_friction_when_negative_or_zero_tyre_friction_is_given(max_speed, acceleration, tyre_friction):
    #Act
    with pytest.raises(Exception) as e:
        Car(color="blue",acceleration=acceleration, max_speed=max_speed, tyre_friction=tyre_friction)
        
    #Assert
    assert str(e.value) == "Invalid value for tyre_friction"


@pytest.fixture
def car():
    car_obj = Car(max_speed=50, acceleration=10, tyre_friction=8)
    return car_obj

def test_car_start_engine_before_engine_starts(car):
    # Arrange
    FALSE = False
    
    # Assert
    assert car.is_engine_started is FALSE

def test_car_start_engine_when_engine_already_started(car, capsys):
    # Arrange
    IF_ENGINE_STARTS_RETURNS_TRUE = True
    MSG_FROM_CAR = "Stop the engine to start_engine\n"
    
    # Act
    car.start_engine()
    car.start_engine()
    output = capsys.readouterr()
    
    # Assert
    assert car.is_engine_started is IF_ENGINE_STARTS_RETURNS_TRUE
    assert output.out == MSG_FROM_CAR

def test_for_stop_engine_when_car_engine_not_in_start(car, capsys):
    # Arrange
    MSG_FROM_CAR = "Start the engine to stop_engine\n"
    
    # Act
    car.stop_engine()
    output = capsys.readouterr()
    
    # Assert
    assert output.out == MSG_FROM_CAR

def test_stop_engine_when_car_engine_is_started(car):
    # Arrange
    RETURNS_FALSE = False
    
    # Act
    car.start_engine()
    car.stop_engine()
    
    # Assert
    assert car.is_engine_started is RETURNS_FALSE

def test_car_accelerate_when_engine_stopped(car, capsys):
    # Arrange
    MSG_FROM_CAR = "Start the engine to accelerate\n"
    
    # Act
    car.accelerate()
    output = capsys.readouterr()
    
    # Assert
    assert output.out  == MSG_FROM_CAR

def test_car_apply_breaks_when_engine_stopped(car, capsys):
    # Arrange
    MSG_FROM_CAR = "Start the engine to apply_breaks\n"
    
    # Act
    car.apply_brakes()
    output = capsys.readouterr()
    
    # Assert
    assert output.out == MSG_FROM_CAR

def test_car_sound_horn_when_engine_stopped(car, capsys):
    # Arrange
    MSG_FROM_CAR = "Start the engine to sound_horn\n"
    
    # Act
    car.sound_horn()
    output = capsys.readouterr()
    
    # Assert
    assert output.out == MSG_FROM_CAR

def test_stop_engine_when_engine_stopped(car, capsys):
    # Arrange
    MSG_FROM_CAR = "Start the engine to stop_engine\n"
    
    # Act
    car.stop_engine()
    output = capsys.readouterr()
    
    # Assert
    assert output.out == MSG_FROM_CAR

def test_start_engine_when_start_engine_method_is_applied_on_car(car):
    # Arrange
    RETURNS_TRUE = True
    
    # Act
    car.start_engine()
    
    # Assert
    assert car.is_engine_started is RETURNS_TRUE

def test_car_current_speed_is_zero_with_no_acceleration_and_when_engine_is_started(car):
    # Arrange
    no_acceleration_current_speed_is_zero = 0
    
    # Act
    car.start_engine()
    
    # Assert
    assert car.current_speed == no_acceleration_current_speed_is_zero

def test_for_apply_breaks_when_car_is_in_motion(car):
    # Arrange
    current_speed_when_accelerated_and_applied_breaks = 2
    
    #Act
    car.start_engine()
    car.accelerate()
    car.apply_brakes()
    
    #Assert
    assert car.current_speed == current_speed_when_accelerated_and_applied_breaks

def test_apply_breaks_when_car_is_at_rest_and_engine_is_started(car):
    # Arrange
    current_speed_when_no_accelerate_is_applied = 0
    
    #Act
    car.start_engine()
    car.apply_brakes()
    #Assert
    assert car.current_speed == current_speed_when_no_accelerate_is_applied

def test_apply_breaks_when_current_speed_is_less_than_tyre_friction_and_engine_is_in_start(car):
    # Arrange
    current_speed_when_multiple_times_applied_breaks = 0
    
    # Act
    car.start_engine()
    car.accelerate()
    car.apply_brakes()
    car.apply_brakes()
    
    # Assert
    assert car.current_speed == current_speed_when_multiple_times_applied_breaks

def test_sound_horn_when_car_engine_started(car, capsys):
    # Arrange
    horn_sound = "Beep Beep\n"
    returns_true_if_engine_started = True
    
    #Act
    car.start_engine()
    car.sound_horn()
    output = capsys.readouterr()
    
    #Assert
    assert car.is_engine_started is returns_true_if_engine_started
    assert output.out == horn_sound

def  test_accelerate_when_car_is_engine_is_started(car):
    # Arrange
    returns_true_if_engine_started = True
    current_speed_when_accelerated = 10
    # Act
    car.start_engine()
    car.accelerate()
    
    # Assert
    assert car.is_engine_started is returns_true_if_engine_started
    assert car.current_speed == current_speed_when_accelerated

def test_accelerate_when_current_speed_reaches_max_speed_limit_when_engine_is_started(car):
    # Arrange
    current_speed_when_max_limit_speed_reached = 50
    
    # Act
    car.start_engine()
    car.accelerate()
    car.accelerate()
    car.accelerate()
    car.accelerate()
    car.accelerate()
    car.accelerate()
    car.accelerate()
    car.accelerate()
    
    # Assert
    assert car.current_speed == current_speed_when_max_limit_speed_reached

def test_instance_of_car_created_with_attribute_values_given(car):
    # Arrange
    max_speed_attribute = 50
    acceleration_attribute = 10
    tyre_friction_attribute = 8
    current_speed_by_default_zero = 0
    
    # Assert
    assert car.max_speed == max_speed_attribute
    
    # Assert
    assert car.acceleration == acceleration_attribute
    
    # Assert
    assert car.tyre_friction == tyre_friction_attribute
    
    # Assert
    assert car.current_speed == current_speed_by_default_zero


def test_valid_max_speed_for_car_object(car):
    # Arrange
    retuns_true_for_valid_data = True
    
    # Assert
    assert car.is_valid_data("max_speed", car.max_speed) is 

def test_valid_acceleration_for_car_object(car):
    # Arrange
    retuns_true_for_valid_data = True
    
    # Assert
    assert car.is_valid_data("acceleration", car.acceleration) is retuns_true_for_valid_data

def test_valid_tyre_friction_for_car_object(car):
    # Arrange
    retuns_true_for_valid_data = True
    
    # Assert
    assert car.is_valid_data("tyre_friction", car.tyre_friction) is retuns_true_for_valid_data

def test_car_current_speed_with_start_engine_accelerated_and_engine_stopped_returns_current_speed_with_repective_acceleration(car):
    
    # Arrange
    current_speed_when_accelerated = 10
    returns_true_if_engine_stopped = False
    car.start_engine()
    car.accelerate()
    
    # Act
    car.stop_engine()
    
    # Assert
    assert car.is_engine_started is returns_true_if_engine_stopped
    assert car.current_speed == current_speed_when_accelerated
    