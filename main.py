from src.Game import *


def main():
    play_again = True

    while play_again:
        player1_name = input("Player 1 , enter your name\n")
        player2_name = input("Player 2 , enter your name\n")
        Game = initGame(player1_name, player2_name)

        while Game.player1.points < 6 and Game.player2.points < 6:
            Game.initRound()

            while Game.endRound() and Game.deck:
                print(f"\n\nTime for {player1_name} ({Game.player1.gender}) to play!")
                Game.player1.playTurn(Game.deck)

                if Game.player2.isAlive and Game.deck:
                    print(f"Time for {player2_name}({Game.player2.gender}) to play!")
                    Game.player2.playTurn(Game.deck)

            if not Game.deck:
                if Game.player1.compare(Game.player2) == 0:
                    Game.player2.hasWon = True
                    print(f"{player2_name} wins")
                elif Game.player1.compare(Game.player2) == 1:
                    Game.player1.hasWon = True
                    print(f"{player1_name} wins")
                else:
                    Game.player1.hasWon = Game.player2.hasWon = True
                    print("Tie")

            computePoints(Game.player1)
            computePoints(Game.player2)

        if Game.player1.points == 6:
            print("GG a toi le couz")
            play_again = input("Do you want to play again ? (True/False)")

        elif Game.player2.points == 6:
            print("GG a toi l'autre couz")
            play_again = input("Do you want to play again ? (True/False)")



if __name__ == "__main__":
    main()
