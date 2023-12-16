class GPIO_Handler:
    def __init__(self, gpio: int):
        self._gpio_path = "/sys/class/gpio"
        self._io = gpio
        self._value = None
        self._direction = None

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

    def deinit(self):
        try:
            with open(f"{self._gpio_path}/unexport", "w") as unexport:
                unexport.write(str(self._io))
            print(f"GPIO{self._io} unexported")
        except Exception as e:
            print(f"Error while unexporting IO: {str(e)}")

    # Private methods
    def _init_io(self):
        try:
            with open(f"{self._gpio_path}/export", "w") as export:
                export.write(str(self._io))
            print(f"GPIO{self._io} exported")
        except Exception as e:
            print(f"Error while exporting IO: {str(e)}")
