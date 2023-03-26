class Piece:
    def __init__(self, rank, color):
        self.rank = rank
        self.color = color

class Flag(Piece):
    def __init__(self, color):
        super().__init__('F', color)

class Bomba(Piece):
    def __init__(self, color):
        super().__init__('B', color)

class Spy(Piece):
    def __init__(self, color):
        super().__init__('S', color)

class Marechal(Piece):
    def __init__(self, color):
        super().__init__('10', color)

class General(Piece):
    def __init__(self, color):
        super().__init__('9', color)

class Coronel(Piece):
    def __init__(self, color):
        super().__init__('8', color)

class Major(Piece):
    def __init__(self, color):
        super().__init__('7', color)

class Capitao(Piece):
    def __init__(self, color):
        super().__init__('6', color)

class Tenente(Piece):
    def __init__(self, color):
        super().__init__('5', color)

class Sargento(Piece):
    def __init__(self, color):
        super().__init__('4', color)

class Desarmador(Piece):
    def __init__(self, color):
        super().__init__('3', color)

class Soldado(Piece):
    def __init__(self, color):
        super().__init__('2', color)