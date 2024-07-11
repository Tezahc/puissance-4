from bread import Board
from joueur import Player

class Wilkinson:
    def __init__(self) -> None:
        self.board = Board()
        self.game_over = False
        
        # accessible dans self.board.jetons.list/set
        # self.jetons_set={'X', 'O'}
        # self.jetons_list=list(self.jetons_set)

        # définition des joueurs
        self.joueur1 = Player(1, self.board.jetons)
        self.joueur2 = Player(2, self.board.jetons)
        self.active_player = None

        print(self.board)
        self.prompt()

    def prompt(self):
        while not self.game_over:
            self.next_player()
            print("joueur actif : ", self.active_player.name, self.active_player.jeton)
            rep = input(f"{self.active_player.name}, veuillez entrer un numéro de colonne : ")
            self.read_intput(rep)
            self.drop_jeton(self.active_player)
            
            self.is_game_over()
        print(f"Habemous winner ! Bravo à {self.active_player.name}")
    
    def next_player(self):
        if self.active_player == self.joueur1:
            self.active_player = self.joueur2
        else: # l'autre OU not defined trop smartass
            self.active_player = self.joueur1
    
    def is_int(self, input):
        try:
            int(input)
            return True
        except ValueError:
            return False
    
    def read_intput(self, réponse):

        if not self.is_int(réponse):
            raise ValueError("Ce n'est pas un nombre entier !")
    #TODO : reproposer un prompt
            print("Ce n'est pas un nombre entier !")
            self.prompt()
        elif not (0 < int(réponse) < 8):
            raise ValueError(f"Ce n'est pas le numéro d'une colonne ! Veuillez entrer un nombre entre 1 et {self.board.cols}")
    #TODO : reproposer un prompt
            print(f"Ce n'est pas le numéro d'une colonne ! Veuillez entrer un nombre entre 1 et {self.board.cols}")
            self.prompt()
        else:
            self.colonne_input = int(réponse)
            return int(réponse)
    
    def read_input(self, réponse):
        pass

    def drop_jeton(self, joueur):
        self.column_id = self.colonne_input - 1
        self.coin_type = joueur.jeton
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
                    self.game_over = True
                    return True

    def check_direction(self, row, col, vecteur):
        # JETONS = {'X', 'O'}
        # jeton = self.board.data[self.__i][self.__j]
        jeton = self.active_player.jeton
        if not jeton in self.board.jetons.set:
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

if __name__ == "__main__":
    t = Wilkinson()