
from pyautogui import *
from util import *


class Tower:
    """A tower in btd6"""
    towers = []
    name = None
    keybind = None
    range_radius = None
    width = None
    height = None
    aquatic = False
    hitbox = None

    def __init__(self, tower_type, placement=None, upgrades=None, **kwargs):
        self.placement = None
        self.name = tower_type.name
        self.range_radius = tower_type.range_radius
        self.keybind = tower_type.keybind
        self.width = tower_type.width
        self.height = tower_type.height
        self.aquatic = tower_type.aquatic
        if placement:
            if self.place(placement):
                self.placement = placement
                self.upgrade(upgrades)


    @classmethod
    def row(cls, length, start=None, inverse=None, upgrades=None, **kwargs):
        if not start:
            start = position()
        row = []
        for i in range(length):
            change = i * cls.width
            if inverse:
                change = change*-1
            row.append(Tower(cls, Point(start.x + change, start.y), upgrades=upgrades, **kwargs))
        return row

    @classmethod
    def column(cls, length, start=None, inverse=None, upgrades=None, **kwargs):
        if not start:
            start = position()
        column = []
        for i in range(length):
            change = i * cls.height
            if inverse:
                change = change*-1
            column.append(Tower(cls, Point(start.x, start.y + change), upgrades=upgrades, **kwargs))
        return column

    @classmethod
    def box(cls, width, height, start=None, inverse=None, upgrades=None, **kwargs):
        if not start:
            start = position()

        box = []
        for i in range(height):
            change = i * cls.height
            if inverse:
                change = change*-1
            box.append(cls.row(width, Point(start.x, start.y + change), upgrades=upgrades, **kwargs))
        return box

    @classmethod
    def placeable(cls, placement):
        if placement.x < 1100:
            measuring_point = Point(placement.x - 90, placement.y)
        else:
            measuring_point = Point(placement.x + 90, placement.y)

        before = pixel(measuring_point.x, measuring_point.y)
        moveTo(placement)
        after = pixel(measuring_point.x, measuring_point.y)
        if (after[0] - before[0]) >= 8:
            return False
        else:
            return True

    def can_be_placed(self, placement):
        moveTo(placement.x, placement.y)
        if placement.x > 1100:
            measuring_point = Point(placement.x - (self.range_radius - 2), placement.y)
        else:
            measuring_point = Point(placement.x + (self.range_radius - 2), placement.y)

        before = pixel(measuring_point.x, measuring_point.y)
        press(self.keybind)
        after = pixel(measuring_point.x, measuring_point.y)
        if (after[0] - before[0]) >= 8:
            return False
        else:
            return True

    def place(self, placement, attempts=0):
        if self.can_be_placed(placement):
            click(placement.x, placement.y, duration=.05)
        else:
            if attempts > 4:
                return False
            return self.place(placement, attempts + 1)
        return placement

    def upgrade(self, upgrades):
        click(self.placement)
        try:
            for i in range(upgrades[0]):
                press(',')
            for i in range(upgrades[1]):
                press('.')
            for i in range(upgrades[2]):
                press('/')
        except:
            pass
        press('escape')

    def __del__(self):
        click(self.placement)
        press('backspace')
