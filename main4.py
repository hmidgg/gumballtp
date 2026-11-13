from personnages import Personnage, Gumball, Darwin, Anais, Nicole, Richard
from situations import Situation
from simulation import Equipe, Simulation


def main():
    equipe = Equipe([Gumball(), Darwin(), Anais(), Nicole(), Richard()])
    sim = Simulation(equipe)

    message = sim.lancer([
        Situation.incendie(3),
        Situation.inondation(4),
        Situation.betise(2),
    ])

    print("=== Historique ===")
    for nom, chaos in sim.historique:
        print(f"{nom} {chaos:+d}")

    print(f"\nChaos total : {sim.chaos}/{Simulation.SEUIL_CHAOS}\n")

    for perso in equipe.membres:
        print(perso)

    print(f"\n{message}")
    print(f"Personnages créés : {Personnage.nombre_total()}")
    print("MRO de Nicole :", " -> ".join(c.__name__ for c in Nicole.__mro__))


if __name__ == "__main__":
    main()
