from tower import Tower
from pyautogui import click


class Mortar(Tower):
    name = "mortar"
    keybind = "n"
    range_radius = 161
    width = 119
    height = 103

    def __init__(self, placement=None, aim=None):
        super(Mortar, self).__init__(Mortar, placement)

