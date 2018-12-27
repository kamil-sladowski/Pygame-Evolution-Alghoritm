import sys
import pygame
from math import sin, cos
from consts import COLOR1, RADIUS, X_MAX, Y_MAX, FONT_COLOR


class Game:

    def __init__(self, drawing_manager, mark):
        self.drawing_manager = drawing_manager
        self.mark = mark
        self.drawed_points = []
        pygame.init()
        self.screen = pygame.display.set_mode((X_MAX, Y_MAX))
        pygame.font.init()
        self.myfont = pygame.font.SysFont('Comic Sans MS', 30)

    def __check_quit(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    @property
    def next_pivot(self):
        return self.drawing_manager.pivots

    def print_mark(self, text="some text"):
        self.screen.fill((0,0,0))
        textsurface = self.myfont.render(text, False, FONT_COLOR)
        self.screen.blit(textsurface, (50, 50))

    def play(self):
        circuit = ""
        self.drawing_manager.prepare_new_random_figure()

        while True:
            event = pygame.event.wait()
            self.__check_quit(event)

            if pygame.mouse.get_pressed()[0]:
                print("mouse button pressed")
                self.drawing_manager.prepare_new_random_figure()
            if pygame.mouse.get_pressed()[2]:
                circuit = self.mark.count_mark_of_structure()

            self.print_mark(text=circuit)
            for next_id in range(self.drawing_manager.elements_num):
                self.drawed_points.append(self.draw_next_ngon(next_id))
            pygame.display.update()
            pygame.event.clear()

    def draw_next_ngon(self, next_id):
        pi2 = 2 * 3.14
        pivot = self.next_pivot[next_id]
        vert_num = self.drawing_manager.figure_types[next_id]
        for i in range(0, vert_num):
            pygame.draw.line(self.screen, COLOR1, pivot,
                             (cos(i / vert_num * pi2) * RADIUS + pivot[0],
                              sin(i / vert_num * pi2) * RADIUS + pivot[1]))

        ngon_points = [(cos(i / vert_num * pi2) * RADIUS + pivot[0],
                       sin(i / vert_num * pi2) * RADIUS + pivot[1]) for i in range(0, vert_num)]
        pygame.draw.lines(self.screen, COLOR1, True, ngon_points)
        return ngon_points
