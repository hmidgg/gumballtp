"""Equipe, Journal et Simulation."""


class Equipe:
    def __init__(self, membres=None):

        self._membres = list(membres) if membres else []

    def ajouter(self, personnage):
        self._membres.append(personnage)

    def retirer(self, personnage):
        self._membres.remove(personnage)     

    @property
    def membres(self):
        return list(self._membres)           

    def __str__(self):
        return ", ".join(m.nom for m in self._membres)
    def __add__(self, autre):
        if isinstance(autre, Equipe):
            return Equipe(self._membres + autre.membres)
        if hasattr(autre, "agir"):
            return Equipe(self._membres + [autre])
        return NotImplemented
       


class Journal:
    def __init__(self):
        self._entrees = []

    def enregistrer(self, nom, chaos):
        self._entrees.append((nom, chaos))

    def entrees(self):
        return list(self._entrees)

    def total(self):
        return sum(chaos for _, chaos in self._entrees)


class Simulation:
    SEUIL_CHAOS = 100

    def __init__(self, equipe):
        self._equipe = equipe                
        self._journal = Journal()           

    @property
    def chaos(self):
        return self._journal.total()

    @property
    def historique(self):
        return self._journal.entrees()

    def est_perdue(self):
        return self.chaos >= Simulation.SEUIL_CHAOS

    def jouer_tour(self, situation):
        somme = sum(m.agir(situation) for m in self._equipe.membres)
        chaos_tour = max(0, situation.chaos_de_base() + somme)
        self._journal.enregistrer(situation.nom, chaos_tour)
        return chaos_tour

    def lancer(self, situations):
        for situation in situations:
            if self.est_perdue():
                break
            self.jouer_tour(situation)
        if self.est_perdue():
            return "DÉFAITE : trop de chaos"
        return "VICTOIRE : Elmore est sauvée"

    def lancer(self, *situations):
        if  len(situations) == 1 and isinstance(situations[0],(list,tuple)):
            situations = situations[0]
        for situation in situations:
            if self.est_perdue():
                break
            self.jouer_tour(situation)
            if self.est_perdue():
                return "DÉFAITE : trop de chaos"
        return "VICTOIRE : Elmore est sauvée"
