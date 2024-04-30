class Node:
    def __init__(self, data, level, fval):
        self.data = data
        self.level = level
        self.fval = fval

    def generate_child(self):
        # Generate next states by moving blank space in 4 directions {up,down,left,right}
        x, y = self.find(self.data, "_")
        # direction_list has 4 directions [up, down, left, right]
        direction_list = [[x, y - 1], [x, y + 1], [x - 1, y], [x + 1, y]]
        children = []
        for direction in direction_list:
            child = self.shuffle(self.data, x, y, direction[0], direction[1])
            if child is not None:
                child_node = Node(child, self.level + 1, 0)
                children.append(child_node)
        return children

    def shuffle(self, puz, x1, y1, x2, y2):
        # Swap the cells x1, y1 and x2, y2
        if x2 >= 0 and x2 < len(self.data) and y2 >= 0 and y2 < len(self.data):
            temp_puz = []
            temp_puz = self.copy(puz)
            temp = temp_puz[x2][y2]
            temp_puz[x2][y2] = temp_puz[x1][y1]
            temp_puz[x1][y1] = temp
            return temp_puz
        else:
            return None

    def copy(self, matrix):
        temp = []
        for row in matrix:
            t = row[:] # Creates copy of the row
            temp.append(t)
        return temp

    def find(self, puz, x):
        for i in range(0, len(self.data)):
            for j in range(0, len(self.data)):
                if puz[i][j] == x:
                    return i, j


class Puzzle:
    def __init__(self, size):
        self.n = size
        self.open = []  # List of Nodes (puzzle matrix, level, fval)
        self.closed = []  # List of Nodes

    def accept(self):
        # Accepts the puzzle from the user
        puz = []
        for i in range(0, self.n):
            temp = input().split(" ")
            puz.append(temp)
        return puz

    def calculate_f_val(self, start, goal):
        # Heuristic Function to calculate hueristic value f(x) = h(x) + g(x)
        return self.calculate_h_val(start.data, goal) + start.level

    def calculate_h_val(self, start, goal):
        # Calculates the total mismatches
        temp = 0
        for i in range(0, self.n):
            for j in range(0, self.n):
                if start[i][j] != goal[i][j] and start[i][j] != "_":
                    temp += 1
        return temp

    def print_arrow(self):
        print("")
        print("  | ")
        print(" \\'/ \n")

    def print_state(self, matrix):
      for row in matrix:
          for cell in row:
              print(cell, end=" ")
          print("")

    def process(self):
        # Accept Start and Goal Puzzle state
        print("Enter the start state matrix")
        start = self.accept()
        print("Enter the goal state matrix")
        goal = self.accept()

        start = Node(start, 0, 0)
        start.fval = self.calculate_f_val(start, goal)
        # Put the start node in the open list
        self.open.append(start)
        print("Sovling")
        while True:
            cur = self.open[0]
            self.print_arrow()
            self.print_state(cur.data)
            # If no diff betw curr and goal state, we reached goal state
            if self.calculate_h_val(cur.data, goal) == 0:
                break
            for child in cur.generate_child():
                child.fval = self.calculate_f_val(child, goal)
                self.open.append(child)
            self.closed.append(cur)
            del self.open[0]

            # sort the opne list based on f value
            self.open.sort(key=lambda x: x.fval, reverse=False)


puz = Puzzle(3)
puz.process()
