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

    def player2name(self, player):
        if player == 0:
            return self.name0
        else:
            return self.name1

    def whose_move(self):
        return self.player2name(self.field.count(1) > self.field.count(2))

    def finish_check(self):
        return 0

    def __str__(self):
        d = {0: 'x', 1: 'o', -1: '-'}
        return '\n'.join([' '.join(map(lambda element: d[element], row)) for row in self.field])


if __name__ == '__main__':
    a = Game(field_size=4, name0='Alex', name1='God')
    print(a)
    print(a.whose_move())