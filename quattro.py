from tabulate import tabulate

JETONS = {'X', 'O'}

class Board:
    def __init__(self, rows=6, cols=7) -> None:
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

class Wilkinson:
    def __init__(self) -> None:
        self.board = Board()
        self.joueur1 = Player(1)
        self.joueur2 = Player(2)
        
        print(self.board)

    def prompt(self):
        
        pass

    def is_int(self, input):
        try:
            int(input)
            return True
        except ValueError:
            return False
    
    def read_intput(self, réponse):
        if not self.is_int(self, réponse):
            print("Ce n'est pas un nombre entier !")
            self.prompt() #re demander l'input
        elif not (0 < int(réponse) < 8):
            print(f"Ce n'est pas le numéro d'une colonne ! Veuillez entrer un nombre entre 1 et {self.board.cols}")
            self.prompt()
        else:
            self.colonne_input = int(réponse)
    
    def read_input(self, réponse):
        pass

    def drop_jeton(self, colonne_input :int, joueur :str):
        self.column_id = colonne_input - 1
        self.coin_type = joueur
        column_data = self.board.get_column(self.column_id)
        
        for row_id, cell in enumerate(column_data):
            # si la cellule n'est PAS vide
            if (cell != ''):
                # si on est sur la ligne la plus haute 
                if row_id == 0:
                    raise IndexError("La colonne est pleine !")
                # on change la cellule PRÉCÉDENTE
                self.board.data[row_id-1][self.column_id] = self.coin_type
                break

            # si on est sur la dernière ligne
            # on place le jeton sur CETTE ligne
            elif row_id == self.board.rows-1:
                self.board.data[row_id][self.column_id] = self.coin_type
            # else:
            #     raise InterruptedError("Unexpected !")
        print(self.board)
    
    def is_game_over(self):
        VECTEUR_A = [(0,0),(1,1),(2,2),(3,3)]
        VECTEUR_B = [(0,0),(0,1),(0,2),(0,3)]
        VECTEUR_C = [(0,0),(1,0),(2,0),(3,0)]
        VECTEUR_D = [(0,0),(1,-1),(2,-2),(3,-3)]
        for self.__i, row in enumerate(self.board.data):
            for self.__j, cell in enumerate(row):
                if (
                    self.check_direction(self.__i, self.__j, VECTEUR_A) or
                    self.check_direction(self.__i, self.__j, VECTEUR_B) or
                    self.check_direction(self.__i, self.__j, VECTEUR_C) or
                    self.check_direction(self.__i, self.__j, VECTEUR_D)
                ):
                    print("Habemous winner !")
                    return True

    def check_direction(self, row, col, vecteur):
        # JETONS = {'X', 'O'}
        jeton = self.board.data[self.__i][self.__j]
        if not jeton in JETONS:
            return False, []

        coins = [ 
            self.board.data[self.__i + i][self.__j+j] 
            for i, j in vecteur 
            if (self.__i+i < self.board.rows) and (self.__j+j < self.board.cols) 
        ]

        coinset = set(coins)

        if (
            (len(coinset) == 1) and # un seul type de jeton
            (coins[0]==jeton) and # le jeton appartient au joueur en cours (osef ?)
            (len(coins) == 4) # il y en a bien 4 à la suite
        ):
            return True
        else: return False

class Player:
    def __init__(self, id, jeton=None) -> None:
        self.name = f"Joueur {id}"
        if jeton not in JETONS:
            jeton = JETONS.pop()
        self.jeton = jeton

class Lci(Wilkinson):
    def __init__(self) -> None:
        super().__init__()
        print(self.board)

t = Wilkinson()

"""
t.game.drop_jeton(2, 'X')
t.game.drop_jeton(2, 'O')
t.game.drop_jeton(3, 'X')
t.game.drop_jeton(4, 'X')
t.game.drop_jeton(5, 'X')
t.game.is_game_over()
"""