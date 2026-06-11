from src.utils import *
from .creature import Creature


class Tileopodium(Creature):
    def __init__(self, surf, pos, groups):
        super().__init__(surf, pos, groups)
        