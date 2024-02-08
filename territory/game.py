import pygame as pg

from territory.components.grid import Grid


class Game:
    MAX_TEAMS = 4
    
    def __init__(self, width:int, height:int, rows:int, cols:int, nbTeams:int):
        self.nbTeams = nbTeams

        self.grid = Grid(width, height, rows, cols, nbTeams)

    def draw(self, screen:pg.Surface):
        self.grid.draw(screen)

    