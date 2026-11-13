import pytest


def test_borner_statique():
    from personnages import Personnage
    assert Personnage.borner(150) == 100
    assert Personnage.borner(-5) == 0

def test_attribut_de_classe():
    from personnages import Personnage
    avant = Personnage.nombre_total()
    Personnage("Test")
    assert Personnage.nombre_total() == avant + 1

def test_reagir_agir():
    from personnages import Personnage
    from situations import Situation
    p = Personnage("Test")
    assert p.agir(Situation.incendie(4)) == -6
    assert p.energie == 88


def test_tour_simple():
    from personnages import Personnage
    from situations import Situation
    from simulation import Equipe, Simulation
    sim = Simulation(Equipe([Personnage("A"), Personnage("B")]))
    assert sim.jouer_tour(Situation.incendie(3)) == 20


def test_setter_borne():
    from personnages import Personnage
    p = Personnage("Test")
    p.energie = 500
    assert p.energie == 100

def test_prive():
    from personnages import Personnage
    p = Personnage("Test")
    with pytest.raises(AttributeError):
        p.__energie

def test_eq_et_repr():
    from personnages import Personnage
    assert Personnage("A") == Personnage("A", 10)
    assert repr(Personnage("A")) == "Personnage('A', energie=100)"


def test_reactions_incendie():
    from personnages import Gumball, Darwin, Anais, Nicole, Richard
    from situations import Situation
    s = Situation.incendie(4)
    equipe = (Gumball(), Darwin(), Anais(), Nicole(), Richard())
    assert [p.reagir(s) for p in equipe] == [-5, -6, -20, -10, 10]

def test_nicole_explose():
    from personnages import Nicole
    from situations import Situation
    n, s = Nicole(), Situation.betise(3)
    for attendu in (24, 48, 72, 96):
        n.reagir(s)
        assert n.colere == attendu
    assert n.reagir(s) == 15
    assert n.colere == 0

def test_heritage_multiple():
    from personnages import Gumball, Enfant, Farceur
    g = Gumball()
    assert isinstance(g, Enfant) and isinstance(g, Farceur)
    assert g.blague() == "Gumball fait une blague !"

def test_simulation_complete():
    from personnages import Gumball, Darwin, Anais, Nicole, Richard
    from situations import Situation
    from simulation import Equipe, Simulation
    equipe = Equipe([Gumball(), Darwin(), Anais(), Nicole(), Richard()])
    sim = Simulation(equipe)
    msg = sim.lancer([Situation.incendie(3), Situation.inondation(4),
                      Situation.betise(2)])
    assert sim.chaos == 33
    assert msg == "VICTOIRE : Elmore est sauvée"
