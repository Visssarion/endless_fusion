# Single Tonies
# Make great
# Makaronies!
from scripts.singleton import Singleton


class Time(metaclass=Singleton):
    delta_time: float = 0.0
    __instance = None

