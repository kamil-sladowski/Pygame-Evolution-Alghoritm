from Matrix import Matrix
from consts import X_MAX, Y_MAX, RADIUS
from random import choice, shuffle, random
from recordtype import recordtype

# = ([list of id], type, amount, fittness)
Island = recordtype('Island', 'ids type amount fitness')


class IslandMatrix(Matrix):

    def __init__(self, idMatrix, figure_matrix):
        super().__init__()
        self.idMatrix = idMatrix
        self.figure_matrix = figure_matrix
        self.islands_num = 1

    def isSafe(self, x, y, visited):
        return (0 <= y < self.height and
                0 <= x < self.width and
                not visited[y][x] and self.idMatrix[x, y])

    def is_the_same_figure(self, x, y, prev_figure):
        return prev_figure == self.figure_matrix[x, y]

    def DFS(self, x, y, visited, prev_figure, prev_num):

        rowNbr = [-1, -1, -1, 0, 0, 1, 1, 1]
        colNbr = [-1, 0, 1, -1, 1, -1, 0, 1]
        visited[y][x] = True
        self.matrix[y][x] = prev_num

        for k in range(8):
            if self.isSafe(x + rowNbr[k], y + colNbr[k], visited):
                if self.is_the_same_figure(x + rowNbr[k], y + colNbr[k], prev_figure):
                    prev_num = self.DFS(x + rowNbr[k], y + colNbr[k], visited, prev_figure, prev_num)
                else:
                    prev_figure = self.figure_matrix[x + rowNbr[k], y + colNbr[k]]
                    prev_num = self.DFS(x + rowNbr[k], y + colNbr[k], visited, prev_figure, prev_num + 1)

        return prev_num

    def detect_islands(self):

        prev_num = 1
        visited = [[False for j in range(self.width)] for i in range(self.height)]
        self.matrix = [[0 for j in range(self.width)] for i in range(self.height)]

        for x in range(self.width):
            for y in range(self.height):
                if visited[y][x] is False and self.idMatrix[x, y] > 1:
                    prev_figure = self.figure_matrix[x, y]
                    prev_num = self.DFS(x, y, visited, prev_figure, prev_num)
                    self.islands_num = prev_num

    def calc_island_statistics(self):
        self.islands = {}
        for i in range(self.islands_num):
            # = ([list of id], type, amount, fittness)
            self.islands[i + 1] = Island(ids=[], type=3, amount=0, fitness=0)

        for x in range(self.width):
            for y in range(self.height):
                num = self.matrix[y][x]
                type = self.figure_matrix[x, y]
                if num is not 0 and type !=0:
                    self.islands[num].ids.append(num)
                    self.islands[num].type = type
                    self.islands[num].amount += 1
                    self.islands[num].fitness += type * self.islands[num].amount

    def deduce_child_type(self, id_1, id_2):
        return choice([self.islands[id_1].type, self.islands[id_2].type])

    def delete_island(self, island):
        pass

    def get_number_of_islands(self):
        return self.islands_num

    def fitness_wheel(self):
        f_max = 0
        wheel = []
        print("self.islands_num")
        print(self.islands_num)
        for num in range(self.islands_num):
            f_max += self.islands[num +1].fitness
        previous = 0
        for num in range(1, self.islands_num):
            wheel.append((self.islands[num +1].ids, previous, previous + self.islands[num +1].fitness/f_max))
            previous = previous + self.islands[num +1].fitness / f_max

        return wheel, f_max

    def get_islands_to_kill(self):
        how_much_kill = choice(range(0, int(self.islands_num/2)))
        print("how_much_kill")
        print(how_much_kill)
        islands_to_delete = set()
        wheel, f_max = self.fitness_wheel()
        for _ in range(how_much_kill):
            t = random()/f_max
            for w_record in wheel:
                if t < w_record[2]:
                    for id in w_record[0]:
                        islands_to_delete.add(id)
                    break
        return islands_to_delete

