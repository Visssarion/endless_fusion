# Single Tonies
# Make great
# Makaronies!

class Time:
    delta_time: float = 0.0
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __del__(self):
        Time.__instance = None


