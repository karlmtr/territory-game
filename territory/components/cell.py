from enum import Enum
import pygame as pg


class CellState(Enum):
    BLANK = 0
    OCCUPIED = 1


class Cell:
    def __init__(
        self,
        left: int,
        top: int,
        width: float,
        height: float,
        state: CellState,
        team: int = 0,
    ):
        self.rect = pg.Rect(left, top, width, height)
        self.state = state
        self.team = team

    def draw(self, screen: pg.Surface):
        if self.state == CellState.BLANK:
            pg.draw.rect(screen, (255, 255, 255), self.rect)
        else:
            pg.draw.rect(screen, (255, 0, 0), self.rect)
