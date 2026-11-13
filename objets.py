class Extincteur:
    def __init__(self, charges=2):
        self.nom = "Extincteur"
        self.charges = charges

    def agir(self, situation):
        if self.charges > 0 and situation.type_danger == "feu":
            self.charges -= 1
            return -(situation.chaos_de_base() // 2)
            
        return 0
class Serpilliere:
    def __init__(self):
        self.nom = "Serpillière"
        s
    def agir(self, situation):
        if situation.type_danger == "eau":
            return -(situation.chaos_de_base() // 3)
            
        return 0
    def __str__(self):
        return "Serpillière"
