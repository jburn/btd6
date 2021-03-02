from tower import Tower


class Boomer(Tower):
    name = "boomer"
    keybind = "w"
    range_radius = 231
    width = 75
    height = 65

    def __init__(self, placement=None):
        super(Boomer, self).__init__(Boomer, placement)
