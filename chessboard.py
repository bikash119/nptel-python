class Board:
    def __init__(self,size) -> None:
        self.board = [[0 for i in range (size)] for i in range(size)]

    def __str__(self) -> str:

        return "|\n\n".join(
            "".join(
                [ "|__|\N{snake}" for i in range(len(self.board[i])//2)]
                ) for i in range(len(self.board)))+ "|"


