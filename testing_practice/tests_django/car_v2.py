class Car:
    
    def __init__(self,max_speed, acceleration, tyre_friction, color = None):
        self._color = color
        self.is_valid_data("max_speed", max_speed)
        self.is_valid_data("acceleration", acceleration)
        self.is_valid_data("tyre_friction", tyre_friction)
        
        self._acceleration = acceleration
        self._tyre_friction = tyre_friction
        self._max_speed = max_speed
        self._is_engine_started = False
        self._current_speed = 0
    
    def start_engine(self):
        if self._is_engine_started:
            print("Stop the engine to start_engine")
        else:
            self._is_engine_started = True
    def accelerate(self):
        if self._is_engine_started:
            self._current_speed += self._acceleration
            if self._current_speed > self._max_speed:
                self._current_speed = self._max_speed
        else:
            print("Start the engine to accelerate")
    def apply_brakes(self):
        if self._is_engine_started:
            self._current_speed -= self._tyre_friction
            if self._current_speed <= 0:
                self._current_speed = 0
        else:
            print("Start the engine to apply_breaks")
    def sound_horn(self):
        if self._is_engine_started:
            print("Beep Beep")
        else:
            print("Start the engine to sound_horn")
    def stop_engine(self):
        if self._is_engine_started:
            self._is_engine_started = False
        else:
            print("Start the engine to stop_engine")
    
    @property
    def max_speed(self):
        return self._max_speed
    @property
    def acceleration(self):
        return self._acceleration
    @property
    def tyre_friction(self):
        return self._tyre_friction
    @property
    def color(self):
        return self._color
    @property
    def is_engine_started(self):
        return self._is_engine_started
    @property
    def current_speed(self):
        return self._current_speed
    @staticmethod
    def is_valid_data(args, value):
        if value > 0:
            return True
        else:
            raise ValueError(f"Invalid value for {args}")
        
class Truck(Car):
    def __init__(self,max_speed, acceleration, tyre_friction, max_cargo_weight, color=None):
        super().__init__(max_speed, acceleration, tyre_friction, color)
        self.is_valid_data("max_cargo_weight", max_cargo_weight)
        self._max_cargo_weight = max_cargo_weight
        self._weight_in_cargo = 0
    def sound_horn(self):
        if self._is_engine_started:
            print("Honk Honk")
        else:
            print("Start the engine to sound_horn")
    def load(self, cargo_weight):
        self.is_valid_data("cargo_weight", cargo_weight)
        if self._current_speed:
            print("Cannot load cargo during motion")
        else:
            self._weight_in_cargo += cargo_weight
            if self._weight_in_cargo > self._max_cargo_weight:
                print(f"Cannot load cargo more than max limit: {self._max_cargo_weight}")
                self._weight_in_cargo -= cargo_weight
    def unload(self, cargo_weight):
        self.is_valid_data("cargo_weight", cargo_weight)
        if self._current_speed:
            print("Cannot unload cargo during motion")
        else:
            self._weight_in_cargo -= cargo_weight
            if self._weight_in_cargo < 0:
                print(f"Cannot unload cargo less than min limit: {0}")
                self._weight_in_cargo += cargo_weight
    @property
    def max_cargo_weight(self):
        return self._max_cargo_weight
    @property
    def weight_in_cargo(self):
        return self._weight_in_cargo

class RaceCar(Car):
    def __init__(self, max_speed, acceleration, tyre_friction, color = None):
        super().__init__(max_speed, acceleration, tyre_friction,color)
        self._nitro = 0
    def accelerate(self):
        import math
        super().accelerate()
        if self._nitro:
            self._current_speed += math.ceil(self._acceleration * 0.3)
            self._nitro -= 10
            if self._current_speed > self._max_speed:
                self._current_speed = self._max_speed
    def apply_brakes(self):
        if self._current_speed > (0.5 * self._max_speed):
            self._nitro += 10
        super().apply_brakes()
    def sound_horn(self):
        if self._is_engine_started:
            print("Peep Peep\nBeep Beep")
        else:
            print("Start the engine to sound_horn")
    @property
    def nitro(self):
        return self._nitro