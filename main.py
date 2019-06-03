# -*- coding:utf-8 -*-

import random
from datetime import datetime, timedelta
import os
import time
import pygame
from pygame.rect import Rect
import config as c
from game import Game
from mainMenu import MainMenu
from settings import Settings
from person import Person
from background import Background


class SlipOut(Game):
    def __init__(self):
        Game.__init__(self, 'Slip Out', 1280, 720, 30)


def main():
    SlipOut().run()


if __name__ == '__main__':
    main()
