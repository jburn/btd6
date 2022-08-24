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
import pyautogui as pag
from constants import *

pag.PAUSE = 0.5

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



def set_fast():
    """
    Check if playing in slowmode and change to fast mode if we are
    """
    if pag.pixel(1852, 998) == (98, 202, 0):
        pag.leftClick(1852, 998)

def is_btd6():
    foreground = win32ui.GetForegroundWindow()
    window_name = foreground.GetWindowText()
    return window_name == 'BloonsTD6'

def nav_deflation_infernal():
    pag.leftClick(MAINMENUPLAY)
    pag.leftClick(MAPMENU_NAVLEFT)
    pag.leftClick(MAPMENU_NAVLEFT)
    pag.leftClick(MAPMENU_DOWNLEFT)
    pag.leftClick(EASY_DIFFICULTY)
    pag.leftClick(DEFLATION)
    time.sleep(5)
    pag.leftClick(DEFLATION)
    time.sleep(2)


def deflation_infernal():
    levelup = 0
    print("Navigating to game")
    nav_deflation_infernal()

    village_pos = Point(x=1582, y=637)
    sniper_pos = Point(x=1534, y=559)
    alc_pos = Point(x=1594, y=518)

    print("Placing towers")
    sniper = Sniper(placement=sniper_pos, upgrades=[0,2,4])
    village = Village(placement=village_pos, upgrades=[2,0,0])
    alch = Alch(placement=alc_pos, upgrades=[4,0,1])

    print("Start game")
    keyboard.press_and_release("space")
    time.sleep(0.4)
    set_fast()

    print("Waiting for completion")
    while pag.pixel(GAMEWIN.x, GAMEWIN.y) != GAMEWINBGCOLOR:
        if pag.pixel(LEVELUP.x, LEVELUP.y) == LEVELUPCOLOR:
            print("Leveled up!")
            levelup += 1
            pag.leftClick(LEVELUP.x, LEVELUP.y)
            pag.leftClick(LEVELUP.x, LEVELUP.y)
        pass
    
    print("Game won")
    time.sleep(0.5)
    print("Press next")
    pag.leftClick(GAMEWINNEXTBUTTON) # press next
    time.sleep(0.5)
    print("Returning to main menu")
    pag.leftClick(GAMEWINHOMEBUTTON) # press home
    time.sleep(2)
    return levelup


if __name__ == '__main__':
    while not keyboard.is_pressed('+'):
        pass
    num_games = 0
    num_levels = 0
    while True:
        levels_gained = deflation_infernal()
        num_levels += levels_gained
        num_games += 1
        print(f"Finished game number {num_games} successfully! Levels gained: {levels_gained}, Total: {num_levels}")
