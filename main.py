"""
Script principal avec la boucle de jeu & re-jeu
"""

import src.gui as gui


def gameloop():
    """
    Main game loop: sépare le while pour restart et celui qui gère le jeu,
    améliore la lecture si bien ficellé
    """


if __name__ == '__main__':
    over = False

    while not over:
        gui.initializeWindow()

        user_input = input('Rejouer ?[yes/no]\n')
        user_input.casefold()

        if user_input == 'no':
            over = True

    print('Fini !')
