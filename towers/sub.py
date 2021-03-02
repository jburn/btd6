from tower import Tower


class Sub(Tower):
    name = "sub"
    keybind = "x"
    range_radius = 226
    aquatic = True
    width = 75
    height = 65

    def __init__(self, placement=None):
        super(Sub, self).__init__(Sub, placement)
