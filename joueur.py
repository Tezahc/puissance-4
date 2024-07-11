from bread import Jeton

class Player:
    # def __init__(self, id, jeton_input=None) -> None:
        # super().__init__()
    def __init__(self, id, jetons :Jeton, jeton_input=None) -> None:
        self.name = f"Joueur {id}"
        if jeton_input not in jetons.set:
            jeton_input = jetons.list.pop()
        self.jeton = jeton_input