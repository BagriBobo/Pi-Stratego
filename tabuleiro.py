class Board:
    def __init__(self):
        self.grid = [[' ' for _ in range(10)] for _ in range(10)]
        
        self.lagos = [(4, 2), (4, 3), (5, 2), (5, 3),
                      (4, 6), (4, 7), (5, 6), (5, 7)]      
    
    def print_board(self):
        for row in self.grid:
            print(' '.join(row))

    def position_piece(self, piece, x, y):
        if self.grid[x][y] != ' ':
            print("Essa posição já está ocupada.")
            return False
        
        if (x, y) in self.lagos:
            print("Essa posição é um lago e não pode ser ocupada.")
            return False
        
        self.grid[x][y] = piece.rank
        return True


