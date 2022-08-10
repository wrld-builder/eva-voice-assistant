import pygame
import numpy as np
from math import *
from win32gui import SetWindowLong
from win32con import GWL_EXSTYLE
from win32gui import GetWindowLong
from win32con import WS_EX_LAYERED
from win32gui import SetLayeredWindowAttributes
from win32api import RGB
from win32con import LWA_COLORKEY

class EvaMagicCube:
    def __init__(self):
        pygame.init()

        self.FUCHSIA = (255, 0, 128)
        self.WHITE = (255, 255, 255)
        self.RED = (255, 0, 0)
        self.BLACK = (0, 0, 0)

        self.WIDTH = 800
        self.HEIGHT = 600

        self.__screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT), pygame.NOFRAME)

        self.__hwnd = pygame.display.get_wm_info()["window"]
        SetWindowLong(self.__hwnd, GWL_EXSTYLE, GetWindowLong(self.__hwnd, GWL_EXSTYLE) | WS_EX_LAYERED)
        SetLayeredWindowAttributes(self.__hwnd, RGB(*self.FUCHSIA), 0, LWA_COLORKEY)

        self.__scale = 100
        self.__circle_pos = [self.WIDTH/2, self.HEIGHT/2]
        self.__angle = 0

        self.__points = []
        self.__rotation_z = []
        self.__rotation_y = []
        self.__rotation_x = []

        self.__projection_matrix = []
        self.__projected_points = []

    def set_cube_vertices(self):
        self.__points.append(np.matrix([-1, -1, 1]))
        self.__points.append(np.matrix([1, -1, 1]))
        self.__points.append(np.matrix([1,  1, 1]))
        self.__points.append(np.matrix([-1, 1, 1]))
        self.__points.append(np.matrix([-1, -1, -1]))
        self.__points.append(np.matrix([1, -1, -1]))
        self.__points.append(np.matrix([1, 1, -1]))
        self.__points.append(np.matrix([-1, 1, -1]))

        self.__projection_matrix = np.matrix([
            [1, 0, 0],
            [0, 1, 0]
        ])

        self.__projected_points = [
            [n, n] for n in range(len(self.__points))
        ]

    def connect_points(self, i, j, points):
        pygame.draw.line(self.__screen, self.BLACK, (points[i][0], points[i][1]),
                         (points[j][0], points[j][1]))

    def update_stuff(self):
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        exit()

            rotation_z = np.matrix([
                [cos(self.__angle), -sin(self.__angle), 0],
                [sin(self.__angle), cos(self.__angle), 0],
                [0, 0, 1],
            ])

            rotation_y = np.matrix([
                [cos(self.__angle), 0, sin(self.__angle)],
                [0, 1, 0],
                [-sin(self.__angle), 0, cos(self.__angle)],
            ])

            rotation_x = np.matrix([
                [1, 0, 0],
                [0, cos(self.__angle), -sin(self.__angle)],
                [0, sin(self.__angle), cos(self.__angle)],
            ])
            self.__angle += 0.01

            self.__screen.fill(self.FUCHSIA)

            i = 0
            for point in self.__points:
                rotated2d = np.dot(rotation_z, point.reshape((3, 1)))
                rotated2d = np.dot(rotation_y, rotated2d)
                rotated2d = np.dot(rotation_x, rotated2d)

                projected2d = np.dot(self.__projection_matrix, rotated2d)

                x = int(projected2d[0][0] * self.__scale) + self.__circle_pos[0]
                y = int(projected2d[1][0] * self.__scale) + self.__circle_pos[1]

                self.__projected_points[i] = [x, y]
                pygame.draw.circle(self.__screen, self.RED, (x, y), 5)
                i += 1

            for p in range(4):
                self.connect_points(p, (p + 1) % 4, self.__projected_points)
                self.connect_points(p + 4, ((p + 1) % 4) + 4, self.__projected_points)
                self.connect_points(p, (p + 4), self.__projected_points)

            pygame.display.update()

    def destroy_magic_cube(self):
        pygame.display.quit()