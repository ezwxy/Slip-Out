# -*- coding:utf-8 -*-

import pygame
import sys
from gameObject import GameObject


class Person(GameObject):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)
