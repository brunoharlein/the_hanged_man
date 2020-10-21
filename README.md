# Jouer au pendu

Le pendu se joue à deux. Le premier joueur pense à un motque le second joueur doit deviner
et, sur une feuille de papier, trace un tiret pour chacune des lettres du mot.

Le second joueur propose une lettre. Si elle existe dans le mot, le premier joueur l'écrit à sa place sur les traits ;
sinon, il dessine une partie du corps du pendu. Pour gagner, le deuxieme joueur doit deviner le mot avant que le dessin du pendu soit terminé.

## Sujet traités dans ce projet :
    - Art ASCII
    - Concevoir un programme avec un organigramme
    - Listes et index
    - L'opérateur IN
    - Les méthodes
    - Les méthodes de chaîne de caracteres SPLIT(), LOWER(), UPPER(), STARTSWITH() et ENDSWITH()
    - L'instruction ELIF
    
## Organigramme

![Screenshot](IMG_2426.png)

Pensez à ce qui se produit quand vous jouez au pendu. D'abord, l'ordinateur choisit un mot. Ensuite, le joueur propose des lettres.
Le jeu ne s'arrête pas une fois que le joueur a proposé une lettre. Le programme doit vérifier si cette dernière se trouve dans le mot à deviner.
Il existe deux possibilités : La lettre se trouve dans le mot ou elle ne s'y trouve pas.
Lorsque la lettre est dans le mot, il faut vérifier si le joueur a trouvé toutes les lettres et gagne la partie.
Lorsque la lettre n'est pas dans le mot, il faut vérifier si le pendu est complet et si le joueur a perdu.
Il n'est pas nécessaire de mettre une flèche de la case "la lettre est dans le mot" vers "le joueur n'a plus de coup à jouer et perd"
parce qu'il est impossible pour le joueur de perdre s'il vient de trouver une lettre.
De la même facon, il est impossible au joueur de gagner si sa proposition est fausse.
Que le joueur ait gagné ou perdu, on lui propose de rejouer. S'il ne le souhaite pas, le programme s'arrête ; sinon, il continue et choisit un nouveau mot.

Le joueur ne propose pas qu'une seule lettre ; il joue jusqu'à ce qu'il gagne ou qu'il perde. 
Que se passe t'il quand le joueur propose une lettre déjà choisie ? Plutôt que de compter la lettre, on lui offre d'en saisir une nouvelle.

Le joueur a besoin de savoir ce qui se passe dans le jeu. Le programme doit afficher le pendu et le mot choisi ( avec des tirets pour les lettres n'ayant pas encore été trouvées).
Cela indique au joueur s'il est sur le point de gagner ou de perdre.
Les informations sont mises à jour chaque fois que le joueur propose une lettre.

#### L'organigramme met en évidence tout ce qui peut se produire dans le jeu du pendu. Lorsque vous concevrez vos propres jeux, un organigramme vous indiquera tout ce que vous devez placer dans le code

Merci à Al Sweigart pour l'exemple du code d'origine 