from math import sin, cos

import pygame
import sys
from random import randint, getrandbits
from consts import *

pygame.init()

screen = pygame.display.set_mode((X_MAX, Y_MAX))
points = [(100, 100), (150, 200), (200, 100)]
pivots = {}
drawedPoints = {}
figureType = {}
pivots["0"] = (50, 50)
figureType["0"] = 6
i = 0


# figureType["0"] = randint(3, 6)



def draw_ngon(Surface, color, n, radius, position, id):
    pi2 = 2 * 3.14
    for i in range(0, n):
        pygame.draw.line(Surface, color, position,
                         (cos(i / n * pi2) * radius + position[0], sin(i / n * pi2) * radius + position[1]))

    ngonPoints = [(cos(i / n * pi2) * radius + position[0], sin(i / n * pi2) * radius + position[1]) for i in
                  range(0, n)]
    pygame.draw.lines(Surface, color, True, ngonPoints)
    return ngonPoints


def checkQuit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

def arePointsInRange( x, y):
    if x > X_MAX or x < 0 or y > Y_MAX or y < 0:
        return False
    return True


def getNextPivot():
    while True:
        existing_point = randint(0, len(pivots) - 1)
        x, y = pivots[str(existing_point)]
        new_x = x + 2 * RADIUS * getrandbits(1)  # (-1 * getrandbits(1)) *
        new_y = y + 2 * RADIUS * getrandbits(1)  # (-1 * getrandbits(1)) *
        print(pivots.values())
        if arePointsInRange(new_x, new_y) and (not (new_x, new_y) in pivots.values()):
            print("aaaaaaa")
            return new_x, new_y
        # else:
        #     return 0,0


def prepare_new_figure(i):
    figureType[str(i)] = randint(4, 6)
    pivots[str(i)] = getNextPivot()
    print("len")
    print(len(pivots))


def count_mark_of_structure():
    print("pivots")
    print(pivots)


for i in range(3):
    i = prepare_new_figure(i)

i = 3
while True:
    checkQuit()

    if pygame.mouse.get_pressed()[0]:
        print("mouse button pressed")
        i = prepare_new_figure(i)
        count_mark_of_structure()

    for i in range(3):
        drawedPoints[str(i)] = draw_ngon(screen, COLOR1, figureType[str(i)], RADIUS, pivots[str(i)], 0)
    pygame.display.update()
    pygame.time.delay(200)

# def animatePolygon():
#     while True:
#
#         # check for quit events
#         checkQuit()
#
#         # erase the screen
#         screen.fill(white)
#
#         # draw the updated picture
#
#         points = updatePoints(points, xMax, yMax)  # changes the location of the points
#         pygame.draw.polygon(screen, (0, 100, 100), points, 10)
#         pygame.draw.lines(screen, black, False, points, 1)  # redraw the points
#
#         # update the screen
#         pygame.display.update()
#         pygame.time.delay(200)
