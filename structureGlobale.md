#CLASSES

### Joueur

- pioche
- joue
- defausse
- nb_points
- still_alive

### Carte

- valeur
- nb exemplaire total
- nb exemplaire en jeu
- description
- visu


- espionne (prend +1 puntos at the end)
- garde (guess card if guess=True then dead)
- pretre (check hand)
- baron (check hand with other hand then lowest dies)
- servante (protect for 1 round)
- prince (defausse then pioche)
- chancellier (remise de carte en dessous)
- roi (switch hands)
- comtesse (if roi or prince then joue comtesse --> mettre check apres avoir pioché)
- princess (if apparition alors dead)



## ATTENTION :
- carte cachée considérée comme "en jeu" alors que IRL not true