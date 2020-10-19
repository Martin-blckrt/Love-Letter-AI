class Card:
    def __init__(self, title, value, totalNumber, description):
        self.title = title
        self.value = value
        self.totalNumber = totalNumber
        self.leftNumber = totalNumber
        self.description = description
        # self.assets = assets 

    # TODO. Ecrire les methodes de la class Card


class Spy(Card):

Spy_Card = Spy("Spy", 0, 2, "Gardez un pion Faveur si personne ne joue ou défausse une carte Espionne.")  # on devrait utiliser les constructeurs dans un fichier init, pas dans le fichier Card

# TODO. Creer un fichier initialisation qui contient une fonction appelant tous les constructeurs pour "creer" et
#  remplir le deck... etc


class Guard(Card):

Guard_Card = Guard("Guard", 1, 6, "Devinez la main d'un autre joueur.")


class Priest(Card):

Priest_Card = Priest("Priest", 2, 2, "Regardez la main d'un autre jouer.")


class Baron(Card):


Baron_Card = Baron("Baron", 3, 2, "Comparez votre main avec celle d'un autre joueur.")


class Handmaid(Card):


Handmaid_Card = Handmaid("Handmaid", 4, 2, "Les autres cartes n'ont pas d'effet sur vous jusqu'au prochain tour.")


class Prince(Card):


Prince_Card = Prince("Prince", 5, 2, "Défaussez votre main et piochez à nouveau.")


class Chancellor(Card):


Chancellor_Card = Chancellor("Chancellor", 6, 2, "Piochez et remettez deux cartes sous le paquet.")


class King(Card):


King_Card = King("King", 7, 1, "Échangez votre main contre celle d'un autre joueur.")


class Countess(Card):


Countess_Card = Countess("Countess", 8, 1, "Vous devez impérativement la jouer si vous avez le Roi ou un Prince.")


class Princess(Card):


Princess_Card = Princess("Princess", 9, 1, "Quittez la manche si vous devez la jouer.")
