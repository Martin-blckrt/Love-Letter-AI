#CLASSES

## Player

### Variables
- type
    + IA ou humain
    
- deadpool
    + if True alors no die for next turn only
    
- isAlive
    + True ou False, permet de vérifier qu'un joueur est encore dans le jeu.
    
- playedCards[]
    + Cartes déjà jouées face visible sur la table.
    
- hand[]
    + Liste des cartes que le joueur a dans sa main.
    
- deck[]
    + Liste avec les cartes restantes dans la pioche
    + if deck[] == empty
        vérifier si player1 a gagné, player2 a gagné ou égalité
    
- extraPoint
    + Booleen relatif à l'espionne.

- hasWon
    + Booleen initialisé à 0
    + if player1.isAlive == 0
        player2.hasWon = 1

### Methods

- draw( _DrawCardChancellor_ )
    + prend pas d'argument sauf quand chancelier elle prend le nombre de cartes piochées
    + Si hand[0] est joué, faire `hand[0] = hand[1] `et dégager hand[1] : A la fin du tour, il ne faut que hand[0] dans les mains des gens.
    + Lors d'une pioche, on ajoute la carte piochée à la fin de la main du joueur (la liste hand)

- playCard()
    + fais jouer la carte
    
-endRound()

- power(target , _guessGuard_ )

    + prend en argument la cible du pouvoir de la carte jouée.
    + prend en argument _optionnel_ la carte que le joueur demande à la cible en jouant le garde.  

- discard( )
    + add `hand[0]` to playedCards[]
    + remove `hand[0]` from hand[]
    + draw( )
        
- endRound ()
    + Appelé lorsque deck est vide et dans les cartes princess, baron et guard.
    + points += isWin + (isAlive and extraPoints)
    + restartRound = 1
    + reload
    
## Card

### Variables

- title
    + nom en français de la carte
- id
    + Valeur et id de la carte.
- totalNumber
    + Nombre total de la carte en question.
- leftNumber
    + Nombre restant de la carte en question en jeu.
- description
    + Décrit le(s) effet(s) de la carte.
- assets
    + image et son liés au GUI
    
### Methods

- power(target, _guessGuard_)
    + Active la carte.

- reveal(target)
    + affiche le hand[0] de l'adversaire

- compare(other_card)
    +  compare les valeurs de self et other_card et renvoie un int à 3 valeurs

## Children de Card

- spy 
    + power(target) : player1.extraPoint = 1
    
- guard

    + power(target, guess())
    
    + guess() pour humain
        * print(Which card do you want to guess [0-9]\1)
        * retrieve input
        * return input
        
    + decide() pour IA
    
    + if guess.input (ou decide) == target.Hand[0].value
        target.isAlive = False
        player.hasWon = 1
        endRound()
    
- priest

    + power(target)
        reveal(target)

- baron

    + power(target)
        vérifier si player1 gagne (et donc lui donner hasWon = 1) ou le contraire ou si la game continue
        
- handmaid
    
    + power(target) avec target = player
        Deadpool = True

- prince
    
    + power(target)
        target.discard
        
- chancellor

    + power(target)   avec target = player
        pioche(2)
        append à la fin de la liste deck[] Hand[a] et Hand[b]
        remove Hand[a] et Hand[b]
        
- king

    + power(target)
        variable tampon pour switch target.Hand[0] et player.Hand[0]
        
- countess

    + if (king or prince) in Hand[]
        playCard countess
        
        
    Attention : mettre le check apres avoir pioché

- princess
    + if princess is in player.playedCards[]
        player.isAlive = False.
        otherplayer.hasWon = 1
        endRound()


#IA 

- NextState(game) : Prend en paramètre l'instance d'objet de la classe Game et que ca retoune l'updated game.

- Terminate(s) : Vérifie que l'état donné en paramètre est un état "final".

- eval(s) : Calcule/estime l'issu du round à chaque position p retourne. 

- Min(bestscore, eval(s))

- Max(bestscore, eval(s))


#Pour eval() 
Formule de proba d'une carte : 

21 - len(self.playedCards[]) + len(opponent.playercard[]) + len(isolatedcard[]) + len(self.hand) + chancellored()

chancelored() faire attention au cas ou il reste strict. moins de 4 cartes. 

# ATTENTION :
- carte cachée considérée comme "en jeu" alors que IRL not true
- code pensé de façon modulable pour fonctionner avec des tweak mineurs à plusieurs joueurs