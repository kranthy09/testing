from .car import Car

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