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
    def is_valid_data(args, args_value):
        if args_value > 0:
            return True
        else:
            raise ValueError(f"Invalid value for {args}")