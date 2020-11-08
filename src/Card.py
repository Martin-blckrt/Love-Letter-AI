
class Card:
    def __init__(self, title, value, totalNumber, description, player1, player2):
        self.title = title
        self.value = value
        self.totalNumber = totalNumber
        self.leftNumber = totalNumber
        self.description = description
        self.player1 = player1
        self.player2 = player2
        # self.assets = assets 

    def reveal(self):
        print(self.title)


#TODO: Find a way to act on players in order to activate powers. Error "Player is not an object" with Guard

class Spy(Card):
    def power(self, activePLayer):

        activePLayer.extraPoints += 1


class Guard(Card):
    def power(self, activePlayer):

        opponent = activePlayer.opponent

        if activePlayer.gender == "Human":
            cardGuessed = activePlayer.guess()
        else:
            cardGuessed = activePlayer.decide()

        if cardGuessed == opponent.hand[0]:
            opponent.isAlive = False


class Priest(Card):
    def power(self, activePlayer):

        activePlayer.opponent.hand[0].reveal()


class Baron(Card):
    def power(self, activePlayer):

        opponent = activePlayer.opponent

        if activePlayer.compare(opponent) == 0:
            activePlayer.isAlive = False
        elif activePlayer.compare(opponent) == 1:
           opponent.isAlive = False


class Handmaid(Card):
    def power(self, activePlayer):

        activePlayer.deadpool = True



class Prince(Card):
    def power(self, activePlayer):

        choice = input("who do you want to target ? [You/Opponent]\n")

        if choice == "You":
            target = activePlayer
        else:
            target = activePlayer.opponent

        target.discard()
        target.draw()


class Chancellor(Card):
    def power(self, activePlayer, deck):

        for i in range(3):

            activePlayer.draw(deck)


class King(Card):
    def power(self, activePlayer):

        opponent = activePlayer.opponent
        temp = activePlayer.hand[0]

        activePlayer.hand[0] = opponent.hand[1]
        opponent.hand[1] = temp


class Countess(Card):
    def power(self, activePlayer):
        print('BOOM Countess')

    pass


class Princess(Card):
    def power(self, activePlayer):
        print('BOOM Princess')
    pass
