"""Jeu Quixo

Ce programme permet de joueur au jeu Quixo.
"""

from api import initialiser_partie, jouer_un_coup
from quixo import Quixo, interpréter_la_commande
SECRET = ""


if __name__ == "__main__":
    args = interpréter_la_commande()
    id_partie, joueurs, plateau = initialiser_partie(args.idul, SECRET)
    while True:
        quixo = Quixo(joueurs, plateau)
        print(quixo)
        origine, direction = quixo.choisir_un_coup()
        id_partie, joueurs, plateau = jouer_un_coup(
            id_partie,
            origine,
            direction,
            args.idul,
            SECRET,
        )
