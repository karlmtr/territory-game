import pygame as pg


class Ball:
    def __init__(self, x:int, y:int, radius:int, color:int, speed:int):
        rect = pg.Rect(x, y, radius, radius)
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed = 0

    def draw(self, screen: pg.Surface):
        ...
