# -*- coding:utf-8 -*-

from gameObject import GameObject
from textObject import TextObject
import config as c


class Button(GameObject):
    def __init__(self, x, y, w, h, text, onClick=lambda x: None, padding=0):
        super().__init__(x, y, w, h)
        self.state = 'normal'
        self.onClick = onClick
        self.text = TextObject(x + padding, y + padding, lambda: text, c)
