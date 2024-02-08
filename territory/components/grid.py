import pygame as pg
import random
from territory.components.cell import Cell, CellState


class Grid:
    def __init__(
        self, width: int, height: int, rows: int, cols: int, nbTeams: int
    ) -> None:
        self.width = width
        self.height = height
        self.rows = rows
        self.cols = cols
        self.cell_width = width // cols
        self.cell_height = height // rows
        self.cells = [
            [
                Cell(
                    i * self.cell_width,
                    j * self.cell_height,
                    width=self.cell_width,
                    height=self.cell_height,
                    state=random.choice(list(CellState)),
                )
                for i in range(cols)
            ]
            for j in range(rows)
        ]

    def draw(self, screen: pg.Surface) -> None:
        for i in range(self.rows):
            for j in range(self.cols):
                self.cells[i][j].draw(screen)

    def __set_teams(self, nbTeams: int) -> None:
        self.teams_coord: list[tuple[int, int]] = []

        match nbTeams: 
            case 2 : 
                for i in range(2):
                    xcoord: int = self.width // 2
                    ycoord: int = self.height // 4 * (i+1)
                    self.teams_coord.append((xcoord, ycoord))

            case _ : 
                raise NotImplementedError(f"nbTeams = {nbTeams} is not implemented") 
         
            
            
