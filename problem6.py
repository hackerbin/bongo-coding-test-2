import copy


class Maze(object):
    def __init__(self, x, y, maze):
        self.start_x = x
        self.start_y = y
        self.num_of_row = len(maze)
        self.num_of_col = len(maze[0])  # assuming a proper maze; that means all row has same number of column
        self.arr = copy.deepcopy(maze)  # deepcopy to keep original array as it is
        self.found = False
        self.visited = []  # to keep visited paths

    def traverse(self, x, y):
        if self.arr[x][y] == 2:  # Found at x,y
            self.found = True
            self.visited.append((x, y))
            return True
        elif self.arr[x][y] == 1:  # Wall at x,y
            return False
        elif self.arr[x][y] == 3:  # Already visited ar x,y
            return False

        # marking visited point
        self.arr[x][y] = 3
        self.visited.append((x, y))

        # Clockwise traverse neighbours
        if ((x < self.num_of_row - 1 and self.traverse(x + 1, y))
                or (y > 0 and self.traverse(x, y - 1))
                or (x > 0 and self.traverse(x - 1, y))
                or (y < self.num_of_col - 1 and self.traverse(x, y + 1))):
            return True

    def find_path(self):
        self.traverse(self.start_x, self.start_y)
        print('Visited paths are = {}'.format(self.visited))
        if self.found:
            print('Found at ({},{})'.format(self.visited[-1][0], self.visited[-1][1]))
        return {'found': self.found, 'destination': self.visited[-1] if self.found else None}


if __name__ == '__main__':
    print('Running a sample maze :: for demonstration purpose only')
    arr = [
        [0, 0, 0, 0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 2],
        [0, 0, 0, 0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
    ]
    Maze(0, 0, maze=arr).find_path()
