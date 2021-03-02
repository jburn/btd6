from tower import Tower


class Wizard(Tower):
    name = "wizard"
    keybind = "a"
    range_radius = 215
    width = 75
    height = 65

    def __init__(self, placement=None):
        super(Wizard, self).__init__(Wizard, placement)
