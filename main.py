import numpy as np
import copy
from pecas import Piece
from tabuleiro import Board


class Jogador:
    def _init_(self, nome, color):
        self.nome = nome
        self.color = color
        self.pieces = []

board = Board()
board.print_board()

for piece_rank, piece_count in [('10', 1),('9', 1), ('8', 2), ('7', 3), ('6', 4), ('5', 4), ('4', 4), ('3', 5), ('2', 8), ('S', 1),('B', 6),('F', 1)]:
    for i in range(piece_count):
        while True:
            x = int(input(f"Digite a linha para a peça {piece_rank}: "))
            y = int(input(f"Digite a coluna para a peça {piece_rank}: "))
            piece = Piece(piece_rank, 'red')
            if board.position_piece(piece, x, y):
                break

board.print_board()