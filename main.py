from src.Game import *


def main():
    play_again = True

    while play_again:
        player1_name = input("Ayyy yo dafuk is yo name\n")
        player2_name = input("Ayyy yo dafuk is yo opponents name\n")
        Game = initGame(player1_name, player2_name)

        while Game.player1.points < 6 and Game.player2.points < 6:
            Game.initRound()

            while Game.endRound():
                Game.player1.playTurn(Game.deck, Game.player2)

                if Game.player2.isAlive:

                    Game.player2.playTurn(Game.deck, Game.player1)

            if not Game.deck:
                if Game.player1.compare(Game.player2) == 0:
                    Game.player2.hasWon = True
                elif Game.player1.compare(Game.player2) == 1:
                    Game.player1.hasWon = True
                else:
                    Game.player1.hasWon = Game.player2.hasWon = True

            Game.player1.computePoints()
            Game.player2.computePoints()

        if Game.player1.points == 6:
            print("GG a toi le couz")
        else:
            print("GG a toi l'autre couz")

        play_again = input("Do you want to play again ? (True/False)")


if __name__ == "__main__":
    main()
