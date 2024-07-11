from tabulate import tabulate

ligne_vide = ['']*7
data = [ligne_vide.copy() for _ in range(6)]
# data[4][5] = 'X'
data_bk = [
    ['01', '02', '03', '04', '05', '06', '07'], 
    ['11', '12', '13', '14', '15', '16', '17'], 
    ['21', '22', '23', '24', '25', '26', '27'], 
    ['31', '32', '33', '34', '35', '36', '37'], 
    ['41', '42', '43', '44', '45', '46', '47'], 
    ['51', '52', '53', '54', '55', '56', '57']
]
def get_col(df, col_id):
    return [row[col_id] for row in df]

def insert_coin(df, col, coin):
    col_id = col - 1
    colonne = get_col(df, col_id)
    # print(colonne)
    for row_id, cell in enumerate(colonne):
        if (cell != '') :
            if row_id==0: raise IndexError("La colonne est pleine !")
            # print("test")
            df[row_id-1][col_id] = coin
            break
        elif (row_id == len(df)-1):
            df[row_id][col_id] = coin

    return df

insert_coin(data, 2, 'X')
insert_coin(data, 3, 'O')
insert_coin(data, 2, 'X')
insert_coin(data, 2, 'O')
insert_coin(data, 3, 'X')
insert_coin(data, 4, 'O')
insert_coin(data, 5, 'X')
insert_coin(data, 4, 'O')
insert_coin(data, 4, 'X')
insert_coin(data, 5, 'O')
insert_coin(data, 5, 'X')
insert_coin(data, 6, 'O')
insert_coin(data, 5, 'X')

print(get_col(data, 5-1))

print(data)

t = tabulate(data, headers=range(1,8), tablefmt='simple_grid', colalign=(['center']*7))
print(t)
# class Board:
#     def __init__(self):
#         empty_row = ['']*7
#         self.data = [empty_row]*6
#         self.board = tabulate(self.data, headers=range(1,8), tablefmt='simple_grid', colalign=(['center']*7))
#         print(self.board)

def voisins(df, row, col):
    """ renvoie une liste des 8 voisins d'un jeton 
    (avec des "-" pour les voisins hors limites)
    la liste est en sens horaire """
    circuit = [ (-1,0),(0,1),(1,0),(1,0),(0,-1),(0,-1),(-1,0),(-1,0) ]
    for i, j in circuit:
        ligne = row + i
        colonne = col + j
        print(df[ligne][colonne])

def champion(df):
    """ parcours toutes les cases du board à la recherche de 4 pions alignés """
    # 4 axes :
    VECTEUR_A = [(0,0),(1,1),(2,2),(3,3)]
    VECTEUR_B = [(0,0),(0,1),(0,2),(0,3)]
    VECTEUR_C = [(0,0),(1,0),(2,0),(3,0)]
    VECTEUR_D = [(0,0),(1,-1),(2,-2),(3,-3)]
    for i, row in enumerate(df):
        for j, cell in enumerate(row):
            if (
                check_dir(df, i, j, VECTEUR_A) or
                check_dir(df, i, j, VECTEUR_B) or
                check_dir(df, i, j, VECTEUR_C) or
                check_dir(df, i, j, VECTEUR_D)
            ):
                print("Gagnant gagnant buffet géant !", )
                return True

def check_dir(df, row, col, vecteur):
    jeton = df[row][col]

    if not jeton in JETONS:
        return False, []
    
    # print(f"coin à la case ({row}, {col}) : {jeton} | ", end='')

    coins = [df[row+i][col+j] for i, j in vecteur if (row+i < len(df)) and (col+j < len(df[0]))]
    coins_id = [(row+i, col+j) for i, j in vecteur if (row+i < len(df)) and (col+j < len(df[0]))]
    coins_set = set(coins)
    # print(coins, coins_set, sep=" | ", end=' ')

    if (len(coins_set) == 1) and (coins[0] == jeton) and (len(coins) == 4):
        # print("\n", coins, end=" - ")
        return True, coins_id
    # print()
    return False, []

JETONS = {'X', 'O'}
champion(data)