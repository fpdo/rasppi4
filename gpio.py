class GPIO_Handler:
    def __init__(self, gpio: int, mode: str = "io"):
        self._io = gpio
        self._mode = mode
        self._value = None
        self._direction = None
        self._period = None
        self._duty_cycle = None
        self._enable = None

        self._gpio_path = "/sys/class/gpio"
        if (self._mode == "pwm"):
            self._pwm_path = "/sys/class/pwm/pwmchip0"

        self._init_io()

    @property
    def direction(self):
        try:
            with open(f"{self._gpio_path}/gpio{self._io}/direction", "r") as direction:
                self._direction = direction.read()
                return self._value
        except Exception as e:
            print(f"Error while reading GPIO{self._io} direction: {str(e)}")
        return None

    @property
    def value(self):
        try:
            with open(f"{self._gpio_path}/gpio{self._io}/value", "r") as value:
                self._value = int(value.read())
                return self._value
        except Exception as e:
            print(f"Error while reading GPIO{self._io} value: {str(e)}")
        return None

    @property
    def period(self):
        try:
            with open(f"{self._pwm_path}/pwm0/period", "r") as period:
                self._period = int(period.read())
                return self._period
        except Exception as e:
            print(f"Error while reading GPIO{self._io} period: {str(e)}")
        return None

    @property
    def duty_cycle(self):
        try:
            with open(f"{self._pwm_path}/pwm0/duty_cycle", "r") as duty_cycle:
                self._duty_cycle = int(duty_cycle.read())
                return self._duty_cycle
        except Exception as e:
            print(f"Error while reading GPIO{self._io} duty cycle: {str(e)}")
        return None

    @property
    def enable(self):
        try:
            with open(f"{self._pwm_path}/pwm0/enable", "r") as enable:
                self._enable = int(enable.read())
                return self._enable
        except Exception as e:
            print(f"Error while reading GPIO{self._io} enable: {str(e)}")

    @direction.setter
    def direction(self, new_direction: str = "out"):
        if (new_direction not in ["in", "out"]):
            print(
                f"Error setting {new_direction}, only valid options are: 'in', 'out'")
            return 1

        try:
            with open(f"{self._gpio_path}/gpio{self._io}/direction", "w") as direction:
                direction.write(new_direction)
            print(f"GPIO{self._io} direction set to {new_direction}")
            self._direction = new_direction
        except Exception as e:
            print(f"Error setting {new_direction}: {str(e)}")
        return 0

    @value.setter
    def value(self, new_value: int = 0):
        if (new_value not in [0, 1]):
            print(
                f"Error setting {new_value}, only valid options are: '0', '1'")
            return 1
        elif (self._direction != "out"):
            print(f"Error setting {new_value}, can only set value for outputs")
            return 1

        try:
            with open(f"{self._gpio_path}/gpio{self._io}/value", "w") as direction:
                direction.write(str(new_value))
            print(f"GPIO{self._io} value set to {new_value}")
            self._value = new_value
        except Exception as e:
            print(f"Error setting {new_value}: {str(e)}")

        return 0

    @period.setter
    def period(self, new_value: int = 0):
        new_value_ns = new_value * 1e6
        try:
            with open(f"{self._pwm_path}/pwm0/period", "w") as period:
                period.write(str(new_value_ns))
                print(f"GPIO{self._io} PWM period set to {new_value}ms")
                self._period = new_value
        except Exception as e:
            print(f"Error while setting GPIO{self._io} period: {str(e)}")
            return 1
        return 0

    @duty_cycle.setter
    def duty_cycle(self, new_value: int = 0):
        new_value /= 100
        new_value *= self._period
        try:
            with open(f"{self._pwm_path}/pwm0/duty_cycle", "w") as duty_cycle:
                duty_cycle.write(str(new_value))
                print(
                    f"GPIO{self._io} PWM duty cycle set to {new_value}/{self._period}%")
                self._duty_cycle = new_value
        except Exception as e:
            print(f"Error while setting GPIO{self._io} duty cycle: {str(e)}")
            return 1
        return 0

    @enable.setter
    def enable(self, new_value: int = 0):
        try:
            with open(f"{self._pwm_path}/pwm0/enable", "w") as enable:
                enable.write(str(new_value))
                print(f"GPIO{self._io} Enable set to {new_value}")
        except Exception as e:
            print(f"Error while setting GPIO{self._io} enable: {str(e)}")
            return 1
        return 0

    def deinit(self):
        try:
            with open(f"{self._gpio_path}/unexport", "w") as unexport:
                unexport.write(str(self._io))
                if (self._mode == "pwm"):
                    with open(f"{self._pwm_path}/unexport", "w") as pwm_unexport:
                        pwm_unexport.write(str(0))

            print(f"GPIO{self._io} unexported")
        except Exception as e:
            print(f"Error while unexporting IO: {str(e)}")

    # Private methods
    def _init_io(self):
        try:
            with open(f"{self._gpio_path}/export", "w") as export:
                export.write(str(self._io))
                if (self._mode == "pwm"):
                    with open(f"{self._pwm_path}/export", "w") as pwm_export:
                        pwm_export.write(str(0))
            print(f"GPIO{self._io} exported")
        except Exception as e:
            print(f"Error while exporting IO: {str(e)}")
