from towers.dart import Dart
from towers.boomer import Boomer
from towers.bomb import Bomb
from towers.tack import Tack
from towers.ice import Ice
from towers.glue import Glue
from towers.sniper import Sniper
from towers.sub import Sub
from towers.bucc import Bucc
from towers.ace import Ace
from towers.heli import Heli
from towers.mortar import Mortar
from towers.wizard import Wizard
from towers.souper import Souper
from towers.ninja import Ninja
from towers.alch import Alch
from towers.druid import Druid
from towers.farm import Farm
from towers.spact import Spact
from towers.village import Village
from towers.engi import Engi

import time
from tower import Tower
import win32ui
import keyboard

types = [
    Dart,
    Boomer,
    Bomb,
    Tack,
    Ice,
    Glue,
    Sniper,
    Sub,
    Bucc,
    Ace,
    Heli,
    Mortar,
    Wizard,
    Souper,
    Ninja,
    Alch,
    Druid,
    Farm,
    Spact,
    Village,
    Engi
]


def is_btd6():
    foreground = win32ui.GetForegroundWindow()
    window_name = foreground.GetWindowText()
    return window_name == 'BloonsTD6'


def main():
    while not keyboard.is_pressed(']'):
        pass
    time.sleep(1)
    darts = Dart.box(3, 3, upgrades=[2, 4, 0])
    time.sleep(2)
    del darts


if __name__ == '__main__':
    main()
