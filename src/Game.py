import sys
import pygame
from consts import COLOR1, RADIUS, X_MAX, Y_MAX
import individual



class Game:

    def __init__(self, figures_mgr):
        self.figures_mgr = figures_mgr
        pygame.init()
        self.screen = pygame.display.set_mode((X_MAX, Y_MAX))
        pygame.font.init()
        self.myfont = pygame.font.SysFont('Comic Sans MS', 30)
        self.individuals = []
        self.used_pivots = figures_mgr.used_pivots_by_individuals

    def __check_quit(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    def evolution(self):
        individual.generate_population(self.individuals, self.figures_mgr)

    def play(self):
        self.individuals = individual.generate_initial_individuals(self.figures_mgr)

        while True:
            event = pygame.event.wait()
            self.__check_quit(event)

            if pygame.mouse.get_pressed()[0]:
                self.evolution()

            self.screen.fill((0,0,0))
            self.draw_circles(self.figures_mgr.shapes)
            pygame.display.update()
            pygame.event.clear()

    def draw_circles(self, shapes):

        for shape in shapes:
            x, y = shape.pivot
            color = shape.color
            x *= RADIUS * 2
            y *= RADIUS * 2
            pygame.draw.circle(self.screen,
                               color, (x, y), RADIUS, 0)


