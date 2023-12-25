def attack_possible(knight_pos,target_pos):
    queue = []
    marked = set()
    knight = Knight(knight_pos)
    queue.insert(0,knight_pos)
    marked[knight_pos] = 1
    while not queue.isemtpy():
        neighbours = knight.find_neighbours(queue.pop())
        marked_neighbours = marked+neighbours
        if target_pos in marked_neighbours:
            print("target attacked")
            return True
        else:
            for elem in marked_neighbours:
                queue.insert(0,elem)
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
    
    def find_neighbours(self,current_pos) -> set():
        neighbours = []
        neighbours.append(self.get_north_east()) if self.move_possible(self.get_north_east(),8) else None
        neighbours.append(self.get_north_east()) if self.move_possible(self.get_north_east(),8) else None
        neighbours.append(self.get_north_west()) if self.move_possible(self.get_north_west(),8) else None
        neighbours.append(self.get_south_east()) if self.move_possible(self.get_south_east(),8) else None
        neighbours.append(self.get_south_west()) if self.move_possible(self.get_south_west(),8) else None
        neighbours.append(self.get_east_north()) if self.move_possible(self.get_east_north(),8) else None
        neighbours.append(self.get_east_south()) if self.move_possible(self.get_east_south(),8) else None
        neighbours.append(self.get_west_north()) if self.move_possible(self.get_west_north(),8) else None
        neighbours.append(self.get_west_south()) if self.move_possible(self.get_west_south(),8) else None
        return set(neighbours)
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
        return attack_candidate[0] > 0 and attack_candidate[1] > 0 and attack_candidate[0] <= board_size and attack_candidate[1] <= board_size

knight = Knight((0,0))
neighbours = knight.find_neighbours((0,0))
print(neighbours)