from tower import Tower


class Engi(Tower):
    name = "engi"
    keybind = "l"
    range_radius = 215
    width = 75
    height = 65

    def __init__(self, placement=None):
        super(Engi, self).__init__(Engi, placement)
