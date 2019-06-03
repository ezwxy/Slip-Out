# -*- coding:utf-8 -*-

import pygame


class TextObject(object):
    def __init__(self, x, y, textFunc, colour, fontName, fontSize):
        self.pos = (x, y)
        self.textFunc = textFunc
        self.colour = colour
        self.font = pygame.font.SysFont(fontName, fontSize)
        self.bounds = self.getSurface(textFunc)

    def draw(self, surface, centralized=False):
        textSurface, self.bounds = self.getSurface(self.textFunc())
        if centralized:
            pos = (self.pos[0] - self.bounds.width // 2, self.pos[1])
        else:
            pos = self.pos
        surface.blit(textSurface, pos)

    def getSurface(self, text):
        textSurface = self.font.render(text, False, self.color)
        return textSurface, textSurface.get_rect()

    def update(self):
        pass
