from Matrix import Matrix
from consts import X_MAX, Y_MAX, RADIUS
from random import choice, shuffle


class IslandMatrix(Matrix):

    def __init__(self, idMatrix):
        super().__init__()
        self.idMatrix = idMatrix


        # A function to check if a given cell

    # (row, col) can be included in DFS
    def isSafe(self, i, j, visited):
        # row number is in range, column number
        # is in range and value is 1
        # and not yet visited
        return (i >= 0 and i < self.height and
                j >= 0 and j < self.width and
                not visited[i][j] and self.idMatrix[i, j])

        # A utility function to do DFS for a 2D

    # boolean matrix. It only considers
    # the 8 neighbours as adjacent vertices
    def DFS(self, i, j, visited, prev_figure):

        # These arrays are used to get row and
        # column numbers of 8 neighbours
        # of a given cell
        rowNbr = [-1, -1, -1, 0, 0, 1, 1, 1];
        colNbr = [-1, 0, 1, -1, 1, -1, 0, 1];

        # Mark this cell as visited

        visited[i][j] = True
        self.matrix[i][j] = prev_figure

        # Recur for all connected neighbours
        for k in range(8):
            if self.isSafe(i + rowNbr[k], j + colNbr[k], visited):
                self.DFS(i + rowNbr[k], j + colNbr[k], visited, prev_figure)

                # The main function that returns

    # count of islands in a given boolean
    # 2D matrix
    def countIslands(self):
        # Make a bool array to mark visited cells.
        # Initially all cells are unvisited
        visited = [[False for j in range(self.width)] for i in range(self.height)]

        # Initialize count as 0 and travese
        # through the all cells of
        # given matrix
        count = 0
        for x in range(self.width):
            for y in range(self.height):
                # If a cell with value 1 is not visited yet,
                # then new island found
                print(visited[0][0])
                if visited[y][x] == False and self.idMatrix[x, y] > 1: # num
                    # Visit all cells in this island
                    # and increment island count
                    self.DFS(x, y, visited, self.idMatrix[x, y])
                    count += 1
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
