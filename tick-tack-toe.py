from collections import defaultdict


class Game(object):

    def __init__(self, field='', name0='Player1', name1='Player2', field_size=3,
                 in_row_to_win=3):
        if not field:
            field = [[-1 for col in range(field_size)] for row in range(field_size)]
        self.field = field
        self.name0 = name0
        self.name1 = name1
        self.size = field_size
        self.abreast = in_row_to_win
        self.symbols = {0: 'x', 1: 'o', -1: '-'}

    def player2name(self, player):
        if player == 0:
            return self.name0
        else:
            return self.name1

    def next_move(self):
        count = defaultdict(int)
        for i in self.field:
            for j in i:
                count[j] += 1
        return int(count[0] > count[1])

    def whose_move(self):
        return self.player2name(self.next_move())

    def whose_win(self):
        return -1

    def move(self, x, y):
        x -= 1
        y -= 1
        next_symbol = self.next_move()
        if self.field[x][y] == -1:
            self.field[x][y] = next_symbol
        else:
            print(f"Error: place {x+1}-{y+1} is taken")
            return
        if self.whose_win() != -1:
            print(self.player2name(self.whose_win()))

    def __str__(self):
        return '\n'.join([' '.join(map(lambda element: self.symbols[element], row)) for row in self.field])


if __name__ == '__main__':
    a = Game(field_size=4, name0='Alex', name1='God')
    print(a)
    print(a.whose_move())
    a.move(1, 2)
    print(a)
    print(a.whose_move())
    a.move(2, 1)
    print(a)
    print(a.whose_move())
    a.move(2, 1)
    print(a)
