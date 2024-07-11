from prettytable import PrettyTable, HEADER

# table = PrettyTable()
# table.field_names = range(1,8)
# for i in range(6):
#     table.add_row([' ']*7, divider=True)

# table.header
# print(table)
        
class Board(PrettyTable):
    def __init__(self, field_names=None, **kwargs) -> None:
        super().__init__(field_names, **kwargs)
        self.field_names = range(1,8)

        empty_row = ['']*7
        self.data = [empty_row]*6
        for row in self.data:
            self.add_row(row, divider=True)
        
        print(self.data)

    def add_piece(self, player :str, column :int):
        # self.get_string
        pass



plateau = Board()
print(plateau)
print(plateau.get_string(fields=['4']))
plateau.add_piece('X', 4)
print(plateau.get_csv_string())