from src.Game import *

# TODO: why not mettre le if not game.deck et les computepoints() dans endround() ?
# Tout à l'air de pouvoir s'écrir dans Game.py voir Player.py


def main():
    play_again = True

    while play_again:

        player1_name = input("Player 1 , enter your name\n")
        player2_name = input("Player 2 , enter your name\n")
        game = initGame(player1_name, player2_name)

        while game.player1.points < 6 and game.player2.points < 6:
            game.initRound()

            while game.endRound() and game.deck:
                print(f"{len(game.deck)-1}")
                print(f"\n\nTime for {player1_name} ({game.player1.gender}) to play!")
                game.player1.playTurn(game.deck)

                if game.player2.isAlive and game.player1.isAlive and game.deck:
                    print(f"\n\nTime for {player2_name}({game.player2.gender}) to play!")
                    game.player2.playTurn(game.deck)

            if not game.deck:
                game.player1.deckEmpty()

            computePoints(game.player1)
            computePoints(game.player2)

        if game.player1.points >= 6:
            print(f"{player1_name} WINS THE GAME !")
            play_again = input("\nDo you want to play again ? (True/False)\n")
        elif game.player2.points >= 6:
            print(f"{player2_name} WINS THE GAME !")
            play_again = input("\nDo you want to play again ? (True/False)\n")


if __name__ == "__main__":
    main()
