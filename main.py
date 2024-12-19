from api import initialiser_partie, jouer_un_coup, récupérer_une_partie
from quixo import Quixo, interpréter_la_commande
from quixo_ia import QuixoIA, Plateau

SECRET = ""

if __name__ == "__main__":
    args = interpréter_la_commande()

    id_partie, joueurs, plateau = initialiser_partie(args.idul, SECRET)

    if args.autonome:
        ia = QuixoIA(joueurs, plateau)

        while True:
            print("\nÉtat du plateau :")
            print(ia)

            print("\nL'IA réfléchit à son coup...")
            try:
                coup = ia.jouer_un_coup('X')
                print(f"IA joue : {coup}")

                id_partie, joueurs, plateau = jouer_un_coup(
                    id_partie,
                    coup['origine'],
                    coup['direction'],
                    args.idul,
                    SECRET
                )

                ia.plateau = Plateau(plateau)

                id_partie, joueurs, plateau, vainqueur = récupérer_une_partie(id_partie, args.idul, SECRET)
                if vainqueur:
                    print(f"\nPartie terminée ! Le gagnant est : {vainqueur}")
                    break
            except Exception as e:
                print(f"Erreur pendant le coup de l'IA : {e}")
                break
    else:
        print("Mode interactif activé : Joueur humain contre le serveur.")
        while True:
            quixo = Quixo(joueurs, plateau)

            print("\nÉtat du plateau :")
            print(quixo)

            try:
                origine, direction = quixo.choisir_un_coup()

                id_partie, joueurs, plateau = jouer_un_coup(
                    id_partie,
                    origine,
                    direction,
                    args.idul,
                    SECRET
                )

                id_partie, joueurs, plateau, vainqueur = récupérer_une_partie(id_partie, args.idul, SECRET)
                if vainqueur:
                    print(f"\nPartie terminée ! Le gagnant est : {vainqueur}")
                    break
            except Exception as e:
                print(f"Erreur pendant le tour du joueur : {e}")
                break
