# Simulation de Gumball

Un jeu de simulation en Python où Gumball et sa famille tentent de sauver
Elmore de situations chaotiques. Chaque personnage réagit différemment aux
événements et dépense de l’énergie pour agir.

## Prérequis

- Python 3
- `pytest` pour lancer les tests

## Lancer la simulation

À la racine du projet, exécutez :

```bash
python3 main.py
```

Le programme affiche l’historique des situations, le chaos total, l’état des
personnages et le résultat de la partie.

## Règles principales

- Une situation possède une gravité comprise entre 1 et 10.
- Le chaos de base d’une situation est égal à sa gravité multipliée par 10.
- Les personnages réduisent ou augmentent le chaos selon leur personnalité.
- Agir consomme de l’énergie ; un personnage épuisé ne peut plus agir.
- La simulation s’arrête lorsque le chaos atteint le seuil de 100.

Les situations prédéfinies sont un incendie, une inondation et une bêtise de
Gumball. Elles peuvent être créées avec `Situation.incendie(gravite)`,
`Situation.inondation(gravite)` et `Situation.betise(gravite)`.

## Nicole et Penny

La classe Penny a été ajoutée comme personnage enfant. Elle réduit davantage
le chaos des situations liées à l’eau, car elle y est à l’aise, et réagit
différemment aux autres dangers.

Nicole affiche désormais aussi son niveau de colère. Son affichage réutilise
celui de la classe mère afin de conserver les informations communes du
personnage sans en recopier le format, puis d’ajouter son état propre.

## Tests

Installez `pytest` si nécessaire, puis lancez :

```bash
python3 -m pytest -q
```

## Organisation du projet

- `main.py` : point d’entrée et exemple de simulation.
- `personnages.py` : personnages, comportements et héritage.
- `situations.py` : situations, gravité et coûts en énergie.
- `simulation.py` : équipe, journal et déroulement de la partie.
- `test_tp.py` : tests automatisés avec `pytest`.
