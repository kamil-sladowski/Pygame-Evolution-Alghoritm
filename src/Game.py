import sys
import pygame
from math import sin, cos
from consts import COLOR1, RADIUS, X_MAX, Y_MAX, FONT_COLOR, NEW_POPULATION_SIZE_MIN, NEW_POPULATION_SIZE_MAX
from random import choice


class Game:

    def __init__(self, drawing_manager, mark):
        self.drawing_manager = drawing_manager
        self.mark = mark
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
        text_surface = self.myfont.render(text, False, FONT_COLOR)
        self.screen.blit(text_surface, (50, 50))

    def evolution(self):
        new_population_size = choice(range(NEW_POPULATION_SIZE_MIN, NEW_POPULATION_SIZE_MAX))
        for _ in range(new_population_size):
            self.drawing_manager.create_new_object()
        # self.drawing_manager.kill_series()


    def play(self):
        circuit = ""

        while True:
            event = pygame.event.wait()
            self.__check_quit(event)

            if pygame.mouse.get_pressed()[0]:
                self.evolution()
            if pygame.mouse.get_pressed()[2]:
                circuit = self.mark.count_mark_of_structure()

            self.print_mark(text=circuit)
            for next_id in range(self.drawing_manager.elements_num):
                self.draw_next_ngon(next_id)
            pygame.display.update()
            pygame.event.clear()

    def draw_next_ngon(self, next_id):
        pi2 = 2 * 3.14
        x, y = self.next_pivot[next_id]
        x *= RADIUS * 2
        y *= RADIUS * 2
        vert_num = self.drawing_manager.figure_types[next_id]
        for i in range(0, vert_num):
            pygame.draw.line(self.screen, COLOR1, (x,y),
                             (cos(i / vert_num * pi2) * RADIUS + x,
                              sin(i / vert_num * pi2) * RADIUS + y))

        ngon_points = [(cos(i / vert_num * pi2) * RADIUS + x,
                       sin(i / vert_num * pi2) * RADIUS + y) for i in range(0, vert_num)]
        pygame.draw.lines(self.screen, COLOR1, True, ngon_points)
        return ngon_points
