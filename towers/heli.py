from tower import Tower


class Heli(Tower):
    name = "heli"
    keybind = "b"
    range_radius = 118
    width = 145
    height = 125

    def __init__(self, placement=None):
        super(Heli, self).__init__(Heli, placement)
