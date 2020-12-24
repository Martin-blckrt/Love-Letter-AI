from src.Game import initGame, computePoints


def main():
    play_again = True

    print("\n*---------------- LOVE LETTER ----------------*")
    print("\t\t\tIA41 Project A20 semester\n")
    print("Created by Alexandre Desbos, Martin Blanckaert et Thomas Sirvent ")
    print("Check README.md to read game rules\n")
    print("Enjoy the game !")
    print("*---------------------------------------------*\n")

    while play_again:

        print("Let's conquer the princess' heart !\n")
        player1_name = input("Enter your name : \n")
        player2_name = input("Enter the bot's name : \n")

        game = initGame(player1_name, player2_name)

        while game.player1.points < 6 and game.player2.points < 6:
            game.initRound()

            while game.endRound() and game.deck:

                # afficher le deck seulement lorsqu'on a 4 cartes dans le deck.
                if len(game.deck) < 6:
                    print(f"\nThere are {len(game.deck)-1} card(s) left in the deck")

                print(f"\n\t--- Time for {player1_name} ({game.player1.gender}) to play! --- \n")

                # print isolated cards every turns :
                print("Isolated cards are : ")
                for a in range(len(game.isolatedCards)):
                    print(f"{game.isolatedCards[a].title}[{game.isolatedCards[a].value}] ", end="")

                if len(game.player1.playedCards) > 0:
                    # print played cards every turns
                    print("\n\nCards played during the round : ")

                    for pc in range(len(game.player1.playedCards)):
                        print(f"{game.player1.playedCards[pc].title} ", end="\n")

                print("\n")

                game.player1.playTurn(game.deck)

                if game.player2.isAlive and game.player1.isAlive and game.deck:

                    print(f"\n\t--- Time for {player2_name}({game.player2.gender}) to play! ---\n")
                    print(f"{player2_name} is thinking")

                    game.player2.playTurn(game.deck)

            if not game.deck and game.player2.isAlive and game.player1.isAlive:
                game.player1.showdown()
                computePoints(game.player1)
                computePoints(game.player2)

        if game.player1.points >= 6:

            print(f"{player1_name} WINS THE GAME !")

        elif game.player2.points >= 6:

            print(f"{player2_name} WINS THE GAME !")

        else:
            print('DRAW')

        startOver = input("\nDo you want to play again ? (Yes/No)\n")
        startOver.lower()

        while startOver != "yes" and startOver != "no":
            startOver = input("\nInvalid input ! Play again ? (Yes/No)\n")

        if startOver == "no":
            play_again = False

    print("Thanks for playing !")


if __name__ == "__main__":
    main()
