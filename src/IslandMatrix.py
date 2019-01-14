from Matrix import Matrix
from consts import X_MAX, Y_MAX, RADIUS
from random import choice, shuffle


class IslandMatrix(Matrix):

    def __init__(self, idMatrix, figure_matrix):
        super().__init__()
        self.idMatrix = idMatrix
        self.figure_matrix = figure_matrix

    def isSafe(self, i, j, visited):
        return (0 <= i < self.height and
                0 <= j < self.width and
                not visited[i][j] and self.idMatrix[i, j])

    def is_the_same_figure(self, i, j, prev_figure):
        return prev_figure == self.figure_matrix[i, j]

    def DFS(self, i, j, visited, prev_figure, prev_num):

        rowNbr = [-1, -1, -1, 0, 0, 1, 1, 1]
        colNbr = [-1, 0, 1, -1, 1, -1, 0, 1]

        # Mark this cell as visited

        visited[i][j] = True
        self.matrix[i][j] = prev_num

        # Recur for all connected neighbours
        for k in range(8):
            if self.isSafe(i + rowNbr[k], j + colNbr[k], visited):
                if self.is_the_same_figure(i + rowNbr[k], j + colNbr[k], prev_figure):
                    self.DFS(i + rowNbr[k], j + colNbr[k], visited, prev_figure, prev_num)
                else:
                    prev_figure = self.figure_matrix[i, j]
                    self.DFS(i + rowNbr[k], j + colNbr[k], visited, prev_figure, prev_num + 1)

                    # The main function that returns

    # count of islands in a given boolean
    # 2D matrix
    def count_islands(self):
        # Make a bool array to mark visited cells.
        # Initially all cells are unvisited
        prev_figure = 0
        prev_num = 0
        visited = [[False for j in range(self.width)] for i in range(self.height)]

        # Initialize count as 0 and travese
        # through the all cells of
        # given matrix
        count = 0
        for x in range(self.width):
            for y in range(self.height):
                # If a cell with value 1 is not visited yet,
                # then new island found
                if visited[y][x] == False and self.idMatrix[x, y] > 1:  # num

                    # if prev_figure == self.figure_matrix[x, y]:
                    self.DFS(x, y, visited, prev_figure, prev_num)
                    # else:
                    #     self.DFS(x, y, visited, prev_figure, prev_num + 1)
                    count += 1
        print("count")
        print(count)
        return count

# g = IslandMatrix()
# g.countIslands()
# g.print_matrix()

# This code is contributed by Neelam Yadav


# def get_free_space(self, first_parent_pivot,  size=3):
#     new_free_space = []
#     f_x, f_y = first_parent_pivot
#     x_possibility = [f_x, f_x +1, f_x -1, f_x +2, f_x-2]
#     y_possibility = [f_y, f_y +1, f_y -1, f_y +2, f_y-2]
#     shuffle(x_possibility)
#     shuffle(y_possibility)
#     for new_x in x_possibility:
#         for new_y in y_possibility:
#             if self.id_matrix[new_y][new_x] == 0:
#                 space_size = 1
#                 x_opt = [-1, 0, 1]
#                 y_opt = [-1, 0, 1]
#                 for n_x in x_opt:
#                     for n_y in y_opt:
#                         if space_size < size and n_x != n_y and n_x !=0:
#                             if self.id_matrix[n_y][n_x] == 0:
#                                 new_free_space.append((n_x, n_y))
#                                 space_size +=1
#                 new_free_space.append((new_x, new_y))
#     return new_free_space
