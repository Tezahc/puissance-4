from tabulate import tabulate

class Jeton:
    def __init__(self) -> None:
        self.set = {'X', 'O'}
        self.list = list(self.set)

class Board:
    def __init__(self, rows=6, cols=7) -> None:
        # définition du jeu de jetons
        self.jetons = Jeton()

        # personnalisation taille du board
        self.rows = rows
        self.cols = cols
        # on crée une ligne vide modèle
        # pas self car on veut pas l'utiliser nulle part ailleurs
        empty_row = ['']*self.cols
        
        # on crée un tableau vide à partir de la ligne modèle
        self.data = [empty_row.copy() for _ in range(self.rows)]

    def __str__(self) -> str:
        # rappel : doit retourner un str
        t = tabulate(
            self.data, 
            headers=range(1, self.cols+1), 
            tablefmt='simple_grid', 
            colalign=(['center']*self.cols)
        )
        return t
    
    def get_column(self, col_id):
        self.__col_id = col_id
        return [ row[self.__col_id] for row in self.data ]