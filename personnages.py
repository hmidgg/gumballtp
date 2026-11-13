class Personnage:
    nb_personnages = 0                       

    def __init__(self, nom, energie=100):
        self._nom = nom                      
        self.__energie = Personnage.borner(energie)   # privé
        self._humeur = 50                    # protégé
        Personnage.nb_personnages += 1

    
    @staticmethod
    def borner(valeur, mini=0, maxi=100):
        return max(mini, min(maxi, valeur))

    @classmethod
    def nombre_total(cls):
        return cls.nb_personnages

   
    @property
    def nom(self):
        return self._nom

    @property
    def humeur(self):
        return self._humeur

    @property
    def energie(self):
        return self.__energie

    @energie.setter
    def energie(self, valeur):
        self.__energie = Personnage.borner(valeur)

   
    def modifier_energie(self, delta):
        self.energie = self.energie + delta

    def est_epuise(self):
        return self.energie == 0

    def reagir(self, situation):
        return -(situation.chaos_de_base() // 6)

    def agir(self, situation):
        if self.est_epuise():
            return 0
        self.modifier_energie(-situation.cout_energie())
        return self.reagir(situation)

    
    def __str__(self):
        return f"{self._nom} (énergie={self.energie}, humeur={self._humeur})"

    def __repr__(self):
        return f"Personnage({self._nom!r}, energie={self.energie})"

    def __eq__(self, autre):
        return isinstance(autre, Personnage) and self._nom == autre._nom

    def __hash__(self):
        return hash(self._nom)



class Colerique:
    LIMITE_COLERE = 100
    _colere = 0

    @property
    def colere(self):
        return self._colere

    def augmenter_colere(self, valeur):
        self._colere = self._colere + valeur

    def est_explosif(self):
        return self._colere >= Colerique.LIMITE_COLERE

    def calmer(self):
        self._colere = 0


class Farceur:
    def blague(self):
        return f"{self.nom} fait une blague !"



class Enfant(Personnage):
    def etre_puni(self):
        self.modifier_energie(-20)


class Adulte(Personnage):
    def punir(self, enfant):
        enfant.etre_puni()


class Gumball(Enfant, Farceur):
    def __init__(self, energie=100):
        super().__init__("Gumball", energie)

    def reagir(self, situation):
        base = situation.chaos_de_base()
        if situation.type_danger == "betise" or self._humeur > 60:
            return base // 2
        return -(base // 8)

    def agir(self, situation):
        chaos = super().agir(situation)
        if chaos > 0:
            self._humeur = Personnage.borner(self._humeur + 15)
        else:
            self._humeur = Personnage.borner(self._humeur - 5)
        return chaos


class Darwin(Enfant):
    def __init__(self, energie=100):
        super().__init__("Darwin", energie)


class Anais(Enfant):
    def __init__(self, energie=100):
        super().__init__("Anaïs", energie)

    def reagir(self, situation):
        return -(situation.chaos_de_base() // 2)


class Nicole(Adulte, Colerique):
    def __init__(self, energie=100):
        super().__init__("Nicole", energie)

    def reagir(self, situation):
        base = situation.chaos_de_base()
        montee = situation.gravite * 4
        if situation.type_danger == "betise":
            montee *= 2
        self.augmenter_colere(montee)
        if self.est_explosif():
            self.calmer()
            return base // 2
        return -(base // 4)


class Richard(Adulte, Farceur):
    def __init__(self, energie=100):
        super().__init__("Richard", energie)

    def reagir(self, situation):
        return situation.chaos_de_base() // 4
