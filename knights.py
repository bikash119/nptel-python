def attack_possible(knight_pos,target_pos):
    queue = []
    marked = {}
    knight = Knight(knight_pos)
    queue.insert(0,knight_pos)
    marked[knight_pos] = 1
    while len(queue) > 0:
        pseudo_knight = Knight(queue.pop())
        neighbours = pseudo_knight.find_neighbours()
        for elem in neighbours:
            if elem not in marked.keys():
                marked[elem] =1
                queue.insert(0,elem)
        if target_pos in marked.keys():
            print("target attacked")
            return True
    else:
        print("target cannot be attacked")
        return False
    
class Board:
    def __init__(self,board_size):
        board = [[0 for i in range(board_size)] for i in range(board_size)]
        knight = Knight((0,2))


class Knight:
    def __init__(self, point) -> ():
        self.x = point[0]
        self.y = point[1]
    
    def __str__(self):
        return f"knight position: ({self.x},{self.y})"
    
    def find_neighbours(self) -> []:
        neighbours = []
        neighbours.append(self.get_north_west()) if self.move_possible(self.get_north_west(),3) else None
        neighbours.append(self.get_north_east()) if self.move_possible(self.get_north_east(),3) else None
        neighbours.append(self.get_south_west()) if self.move_possible(self.get_south_west(),3) else None
        neighbours.append(self.get_south_east()) if self.move_possible(self.get_south_east(),3) else None
        neighbours.append(self.get_east_north()) if self.move_possible(self.get_east_north(),3) else None
        neighbours.append(self.get_east_south()) if self.move_possible(self.get_east_south(),3) else None
        neighbours.append(self.get_west_north()) if self.move_possible(self.get_west_north(),3) else None
        neighbours.append(self.get_west_south()) if self.move_possible(self.get_west_south(),3) else None
        return neighbours
    def get_north_west(self):
        x = self.x + 2
        y = self.y - 1
        return (x,y)
    def get_north_east(self):
        x = self.x +2
        y = self.y +1
        return (x,y)
    def get_south_west(self):
        x = self.x -2
        y = self.y -1
        return (x,y)
    def get_south_east(self):
        x = self.x -2
        y = self.y +1
        return (x,y)
    def get_west_north(self):
        x = self.x +1
        y = self.y -2
        return (x,y)
    def get_west_south(self):
        x = self.x -1
        y = self.y -2
        return (x,y)
    def get_east_north(self):
        x = self.x +1
        y = self.y +2
        return (x,y)
    def get_east_south(self):
        x = self.x -1
        y = self.y +2
        return (x,y)
    
    def move_possible(self,attack_candidate,board_size)-> bool:
        return attack_candidate[0] >= 0 and attack_candidate[1] >= 0 and attack_candidate[0] < board_size and attack_candidate[1] < board_size

# knight = Knight((7,7))
# neighbours = knight.find_neighbours((8,8))
is_attack_possible= attack_possible((0,0),(1,1))
print(is_attack_possible)
# print(neighbours)