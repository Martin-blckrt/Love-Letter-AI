class Card:
    def __init__(self, title, value, totalNumber, leftNumber, description, assets):
        self.title = title
        self.value = value
        self.totalNumber = totalNumber
        self.leftNumber = leftNumber
        self.description = description
        self.assets = assets

    # TODO. Ecrire les methodes de la class Card


class Spy(Card):


Spy_Card = Spy()  # on devrait utiliser les constructeurs dans un fichier init, pas dans le fichier Card

# TODO. Creer un fichier initialisation qui contient une fonction appelant tous les constructeurs pour "creer" et
#  remplir le deck... etc


class Guard(Card):
    def __init__(self):
        self.title = "Guard"
        self.value = 1
        self.totalNumber = 6
        self.description = "Devinez la main d'un autre joueur."


Guard_Card = Guard()


class Priest(Card):
    def __init__(self):
        self.title = "Priest"
        self.value = 2
        self.totalNumber = 2
        self.description = "Regardez la main d'un autre joueur."


Priest_Card = Priest()


class Baron(Card):
    def __init__(self):
        self.title = "Baron"
        self.value = 3
        self.totalNumber = 2
        self.description = "Comparez votre main avec celle d'un autre joueur."


Baron_Card = Baron()


class Handmaid(Card):
    def __init__(self):
        self.title = "Handmaid"
        self.value = 4
        self.totalNumber = 2
        self.description = "Les autres cartes n'ont pas d'effet sur vous jusqu'au prochain tour."


Handmaid_Card = Handmaid()


class Prince(Card):
    def __init__(self):
        self.title = "Prince"
        self.value = 5
        self.totalNumber = 2
        self.description = "Défaussez votre main et piochez à nouveau."


Prince_Card = Prince()


class Chancellor(Card):
    def __init__(self):
        self.title = "Chancellor"
        self.value = 6
        self.totalNumber = 2
        self.description = "Piochez et remettez deux cartes sous le paquet."


Chancellor_Card = Chancellor()


class King(Card):
    def __init__(self):
        self.title = "King"
        self.value = 7
        self.totalNumber = 1
        self.description = "Échangez votre main contre celle d'un autre joueur."


King_Card = King()


class Countess(Card):
    def __init__(self):
        self.title = "Countess"
        self.value = 8
        self.totalNumber = 1
        self.description = "Vous devez impérativement la jouer si vous avez le Roi ou un Prince."


Countess_Card = Countess()


class Princess(Card):
    def __init__(self):
        self.title = "Princess"
        self.value = 9
        self.totalNumber = 1
        self.description = "Quittez le tour si vous devez la jouer."


Princess_Card = Princess()
